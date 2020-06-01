# server
import hashlib
from socket import socket, AF_INET, SOCK_DGRAM
import sys

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


    def guardar_paquete(self, package, cliente):
        pass

        # verificar mediante SHA256 que los datos recibidos son los que nos han enviado
        # si han llegado bien enviamos el ack de vuelta al remitente.
        # los datos llegan mal, no enviaremos el ack correspopniente de manera que el remitente lo vuelva a enviar


    def run(self):

        while 1:
            #recibimos un paquete del cliente
            data, address = self.connection.UDP_connection.recvfrom(self.buffer_size)

            data = self.connection.translate_package_to_data(data)

            #verificamos que los datos recibidos son correctos


            #si son correctos enviamos un ack correspondiente al subpaquete

            #si no son correctos no enviamos el ack correspondiente

    def insert_package(self, data):

        pass








if __name__ == '__main__':

    ip = '0.0.0.0'
    port = 9876
    almacen_remoto = Remote_almacen(ip, port, 2048, 1, 3)
    almacen_remoto.run()









