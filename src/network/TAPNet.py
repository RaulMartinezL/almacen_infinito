from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
from time import sleep
import hashlib

''' 
data = {"package_id": 0,
                "subpackage_id": 0,
                "subpackage_num": 0,
                "subpackage_hash": self.__hasheador,
                "datos_en_si": null
                }
'''


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

    def make_chunks(self, package):
        package_data = str(package.get_data())
        package_data = str.encode(package_data)
        self.__hasheador.update(package_data)

        chunks = [package_data[i:i + self.buffer_size] for i in range(0, len(package_data), self.buffer_size)]

        return chunks

    def send_package(self, message_type, data):

        tipo_mensaje_enviamos = self.__message_types.get(message_type)
        message = tipo_mensaje_enviamos(data)

        self.UDP_connection.sendto(message, (self.ip, self.port))

    def normal_message(self, data):
        message = int(1).to_bytes(4, 'little') + data["package_id"].to_bytes(4, 'little') + \
                  data["subpackage_hash"] + data["subpackage_num"].to_bytes(4, 'little') + \
                  data["subpackage_id"].to_bytes(4, 'little')

        return message

    def ack_message(self, data):
        message = int(0).to_bytes(4, 'little') + data["package_id"].to_bytes(4, 'little') + \
                  data["subpackage_id"].to_bytes(4, 'little')

        return message

    def translate_package_to_data(self, data):
        message_type = int.from_bytes(data[0:3], ' little')
        paquete_id = int.from_bytes(data[4:7], ' little')

        if message_type == 0:
            pass
            # hacemos la conversion del mensaje ack

        elif message_type == 1:
            pass
            # este mensaje tiene datos y vamos a ver cuales son.

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