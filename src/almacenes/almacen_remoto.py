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

        self.connection = TAPNet(self.ip, self.port, self.buffer_size, self.timeout, self.max_tries)

        self.lista_paquetes = []



        # self.__almacenGrande = Big_almacen()


    def guardar_paquete(self,  data):

        print(data)
        ack = self.connection.ack_message(data)
        self.connection.UDP_connection.sendto(ack, ('0.0.0.0', 9877))


        hash_chunks = data['hash_chunks']
        len_chunks = data['len_chunks']
        id_paquete = data['paquete_id']
        cliente = data['cliente']


        # falta comprobar el numero de subpaquetes que nos van a enviar
        #


        while 1:
            data, address = self.connection.UDP_connection.recvfrom(self.buffer_size)
            print(data)
            data = self.connection.translate_package_to_data(data)


            print(data)

            pacakge_id = data['paquete_id']
            subpackage_id = data['subpackage_id']
            subpackage_num = data['subpackage_num']
            subpackage_hash = data['subpackage_hash']
            subpackage = data['subpackage']


            # verificar mediante SHA256 que los datos recibidos son los que nos han enviado
            self.__hasheador.update(subpackage)
            check_subpackage = self.__hasheador.digest()
            if subpackage_hash == check_subpackage:
                # enviamos ack de vuelta OK
                pass
            else:
                # enviamos ack de vuelta NOT OK
                pass


    def recoger_paquete(self, package, cliente):
        pass


    def run(self):

        while 1:
            print("while 1")
            # recibimos un paquete del cliente
            data, address = self.connection.UDP_connection.recvfrom(self.buffer_size)

            print(data)

            # hay que comprobar que es lo que queremos hacer. Guardar o Recoger un paquete.
            data_translated = self.connection.translate_package_to_data(data)

            print(data_translated)

            if data_translated['primer_mensaje'] == 24:
                print("primer mensaje 24")
                self.guardar_paquete(data_translated)


            if data_translated['primer_mensaje'] == 42:
                self.recoger_paquete()

                # devolvemos okay, buscamos el paquete y lo devolvemos



    def insert_package(self, data):

        pass






if __name__ == '__main__':

    ip = '0.0.0.0'
    port = 9876
    almacen_remoto = Remote_almacen(ip, port, 2048, 1, 3)
    almacen_remoto.run()


