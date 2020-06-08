# server
import hashlib
import sys

from socket import socket, AF_INET, SOCK_DGRAM
from src.network.TAPNet import TAPNet


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

        self.connection = TAPNet(ip, port, buffer_size, timeout, max_tries)

        self.lista_paquetes = []



        # self.__almacenGrande = Big_almacen()


    def guardar_paquete(self,  data):
        ack = self.connection.ack_message(data)
        self.connection.UDP_connection.sendto(ack, (self.ip, self.port))


        hash_chunks = data['hash_chunks']
        len_chunks = data['len_chunk']
        id_paquete = data['id_paquete']
        cliente = data['cliente']


        while 1:

            # si han llegado bien enviamos el ack de vuelta al remitente.
            # los datos llegan mal, no enviaremos el ack correspopniente de manera que el remitente lo vuelva a enviar



            data, address = self.connection.UDP_connection.recvfrom(self.buffer_size)

            # verificar mediante SHA256 que los datos recibidos son los que nos han enviado
            data = self.connection.translate_package_to_data(data)

            pacakge_id = self.data['package_id']
            subpackage_id = self.data['subpackage_id']
            subpackage_num = self.data['subpackage_num']
            chunk = self.data['chunk']
            subpackage_hash = self.data['subpackage_hash']


    def recoger_paquete(self, package, cliente):
        pass


    def run(self):

        while 1:
            # recibimos un paquete del cliente
            data, address = self.connection.UDP_connection.recvfrom(self.buffer_size)

            # hay que comprobar que es lo que queremos hacer. Guardar o Recoger un paquete.
            data = self.connection.translate_package_to_data(data)

            if data['primer_mensaje'] == 24:
                self.guardar_paquete(data)


            if data['primer_mensaje'] == 42:
                self.recoger_paquete()

                # devolvemos okay, buscamos el paquete y lo devolvemos



    def insert_package(self, data):

        pass






if __name__ == '__main__':

    ip = '0.0.0.0'
    port = 9876
    almacen_remoto = Remote_almacen(ip, port, 2048, 1, 3)
    almacen_remoto.run()


