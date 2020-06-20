# server
import hashlib
import sys

from socket import socket, AF_INET, SOCK_DGRAM
from src.network.TAPNet import TAPNet

from big_almacen import Big_almacen

ACK = 0
NORMAL = 1


class Remote_almacen:

    def __init__(self, ip, port, buffer_size, timeout, max_tries):

        self.ip = ip
        self.port = port
        self.buffer_size = buffer_size
        self.timeout = timeout
        self.max_tries = max_tries
        self.__hasheador = hashlib.sha256()

        self.connection = TAPNet(self.ip, self.port, self.buffer_size, self.timeout, self.max_tries)

        self.lista_paquetes = []
        self.lista_paquetes_hash = []

        self.__almacenGrande = Big_almacen()

    def guardar_paquete(self, data):

        hash_chunks = data['hash_chunks']
        len_chunks = data['len_chunks']
        id_paquete = data['paquete_id']
        cliente = data['cliente']

        self.connection.send_package(ACK, data, '0.0.0.0', 9877)

        # falta comprobar el numero de subpaquetes que nos van a enviar


        for i in range(0, len_chunks):

            data, address = self.connection.UDP_connection.recvfrom(self.buffer_size)
            data_translated = self.connection.translate_package_to_data(data)

            package_id = data_translated['paquete_id']
            subpackage_id = data_translated['subpackage_id']
            subpackage_num = data_translated['subpackage_num']
            subpackage_hash = data_translated['subpackage_hash']
            subpackage = data_translated['subpackage']

            # verificar mediante SHA256 que los datos recibidos son los que nos han enviado
            hasheador_chido = hashlib.sha256()
            hasheador_chido.update(subpackage)
            check_subpackage = hasheador_chido.digest()

            if subpackage_hash == check_subpackage:
                # si hemos recibido bien el subpackage
                self.lista_paquetes.append(subpackage)
                self.lista_paquetes_hash.append(subpackage_hash)
                #actualizamos el hash de todos los paquetes con el nuevo que nos acaba de llegar
                hash_entero = b''.join(self.lista_paquetes_hash)
                if hash_chunks == hash_entero:
                    # guardamos el paquete
                    paquete_in_bytes = b''.join(self.lista_paquetes)
                    paquete = paquete_in_bytes.decode("utf-8")
                    return self.__almacenGrande.guardar_paquete(paquete, cliente, package_id)

    def recoger_paquete(self, data_translated):
        id_paquete = data_translated['paquete_id']
        cliente = data_translated['cliente']

        object_to_return = self.__almacenGrande.recuperar_paquete(id_paquete, cliente)

        # dividimos en chunks de 2048 bits
        chunks_to_return = self.connection.make_chunks(object_to_return)

        data = {'primer_mensaje': 24,
                'hash_chunks': self.connection.digest(),
                'len_chunks': len(chunks_to_return),
                'paquete_id': id_paquete,
                'cliente': cliente}


        self.connection.send_package(NORMAL, data, '0.0.0.0', 9877)
        ack = self.connection.UDP_connection.recvfrom(self.buffer_size)

        primer_mensaje_vuelta = self.connection.translate_package_to_data(ack[0])

        if primer_mensaje_vuelta['message_type'] == 0:
            # envio mensaje
            data_to_return = {}
            for i in range(0, len(chunks_to_return)):
                chunk_a_enviar = chunks_to_return[i]
                self.__hasheador.update(chunk_a_enviar)

                data_to_return['paquete_id'] = id_paquete
                data_to_return['subpackage_id'] = i
                data_to_return['subpackage_num'] = len(chunks_to_return)
                data_to_return['subpackage'] = chunk_a_enviar
                data_to_return['subpackage_hash'] = self.__hasheador.digest()

                self.connection.send_package(NORMAL, data_to_return, '0.0.0.0', 9877)



    def run(self):

        while 1:
            print("esperando un mensaje")
            # recibimos un paquete del cliente
            data, address = self.connection.UDP_connection.recvfrom(self.buffer_size)

            # hay que comprobar que es lo que queremos hacer. Guardar o Recoger un paquete.
            data_translated = self.connection.translate_package_to_data(data)


            if data_translated['primer_mensaje'] == 24:
                print("primer mensaje 24")
                self.guardar_paquete(data_translated)


            if data_translated['primer_mensaje'] == 42:
                print("primer mensaje 42")
                self.recoger_paquete(data_translated)





if __name__ == '__main__':
    ip = '0.0.0.0'
    port = 9876
    almacen_remoto = Remote_almacen(ip, port, 2048, 1, 3)
    almacen_remoto.run()
