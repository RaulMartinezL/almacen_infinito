from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
from time import sleep
import hashlib


class TAPNet:

    def __init__(self, ip, port, buffer_size, timeout, max_tries):
        self.ip = ip
        self.port = port
        self.buffer_size = buffer_size
        self.timeout = timeout
        self.max_tries = max_tries

        self.__message_types = {0: self.ack_message, 1: self.normal_message}
        self.__hasheador = hashlib.sha256()

        self.UDP_connection = socket(AF_INET, SOCK_DGRAM)
        self.UDP_connection.bind((self.ip, self.port))

    def digest(self):
        return self.__hasheador.digest()

    def make_chunks(self, datos):
        package_data = str.encode(datos)
        self.__hasheador.update(package_data)

        chunks = [package_data[i:i + self.buffer_size] for i in range(0, len(package_data), self.buffer_size)]

        return chunks

    def send_package(self, message_type, paquete, ip, puerto):

        tipo_mensaje_enviamos = self.__message_types.get(message_type)
        message = tipo_mensaje_enviamos(paquete)

        self.UDP_connection.sendto(message, (ip, puerto))

    def normal_message(self, data):
        for key, value in data.items():
            print(key, value)

        if data['primer_mensaje'] is not None:
            # creamos el primer mensaje
            message = int(1).to_bytes(4, 'little') + data['paquete_id'].to_bytes(4, 'little') + \
                      data['primer_mensaje'].to_bytes(4, 'little')

            # si existe esta key en el diccionario quiere decir que vamos a guardar el paquete si no existe es que
            # vamos a sacar el paquete
            if data['hash_chunks']:
                message = message + data['len_chunks'].to_bytes(4, 'little') + data['cliente'].to_bytes(4, 'little') + \
                          data['hash_chunks']  # hash_chunks son bytes. Mide 32

            return message

        message = int(1).to_bytes(4, 'little') + data["paquete_id"].to_bytes(4, 'little') + \
                  data["subpackage_id"].to_bytes(4, "little") + data["subpackage_num"].to_bytes(4, 'little') + \
                  data["subpackage_hash"]# subpackage_hash tambien van a ser bytes. Mide 32

        message = message + data['subpackage']

        return message

    def ack_message(self, data):
        message = int(0).to_bytes(4, 'little') + data["paquete_id"].to_bytes(4, 'little')

        if "subpackage_id" in data:
            message = message + data["subpackage_id"].to_bytes(4, 'little')

        return message

    def translate_package_to_data(self, data):
        dict_to_return = {}

        message_type = int.from_bytes(data[0:3], 'little')
        paquete_id = int.from_bytes(data[4:7], 'little')

        # subpackage_id = int.from_bytes(data[8:11], 'little')

        if message_type == 1:
            primer_mensaje = int.from_bytes(data[8:11], 'little')

            # queremos guardar el paquete y este es el primer mensaje
            if primer_mensaje == 24:
                len_chunks = int.from_bytes(data[12:15], 'little')
                cliente = int.from_bytes(data[16:19], 'little')
                # hash_chunks = int.from_bytes(data[20:], 'little')
                hash_chunks = data[20:]

                dict_to_return['message_type'] = message_type
                dict_to_return['paquete_id'] = paquete_id
                dict_to_return['primer_mensaje'] = primer_mensaje
                dict_to_return['hash_chunks'] = hash_chunks
                dict_to_return['len_chunks'] = len_chunks
                dict_to_return['cliente'] = cliente

            # queremos sacar el paquete y este es el primer mensaje
            elif primer_mensaje == 42:
                dict_to_return['message_type'] = message_type
                dict_to_return['paquete_id'] = paquete_id

            # comportamiento normal a partir del primer mensaje
            else:
                subpackage_id = int.from_bytes(data[8:11], 'little')
                subpackage_num = int.from_bytes(data[12:15], 'little')
                # subpackage_hash = int.from_bytes(data[21:52], 'little')
                subpackage_hash = data[16:48]

                print(data)
                subpackage = data[48:]

                dict_to_return['message_type'] = message_type
                dict_to_return['paquete_id'] = paquete_id
                dict_to_return['subpackage_id'] = subpackage_id
                dict_to_return['subpackage_num'] = subpackage_num
                dict_to_return['subpackage_hash'] = subpackage_hash
                dict_to_return['subpackage'] = subpackage

        elif message_type == 0:

            dict_to_return['message_type'] = message_type
            dict_to_return['paquete_id'] = paquete_id

        return dict_to_return

    def guardar_objeto(self, paquete):

        pass

    def recuperar_objet(self):
        pass

    '''
    def guardar_paquete(self, paquete, cliente):
        pass

        # dividir los datos del paquete en un tamaño de maximo 2048 bits

        data = [paquete.get_data()]
        hasher = hashlib.sha256()
        hasher.update(data)
        chunks = [data[i:i + BUFFER_SIZE] for i in range(0, len(data), BUFFER_SIZE)]
        client = socket(AF_INET, SOCK_DGRAM)
        client.sendto(len(chunks).to_bytes(4, 'big'), (ip, port))

        for c in chunks:
            client.sendto(c, (ip, port))

        # poder enviar paquetes garantizando que lleguen de forma integra, recepcionando un ACK

    '''
