import sys
from ..almacenes.big_almacen import Big_almacen
from ..almacenes.small_almacen import Small_almacen
from ..network.TAPNet import TAPNet
from ..contenedor.paquete import Block
from .cliente import Cliente
from uuid import uuid4
import hashlib


ACK = 0
NORMAL = 1


class Empresa:
    __almacenGrande = None
    __almacenPequeno = None

    __clientes = []

    def __init__(self):
        self.ip = '0.0.0.0'
        self.port = 9877
        self.buffer_size = 2048
        self.time_out = 1
        self.max_tries = 3
        self.__comunicacion_TAPNET = TAPNet(self.ip, self.port, self.buffer_size, self.time_out, self.max_tries)

        self.__almacenGrande = Big_almacen()
        self.__almacenPequeno = Small_almacen()
        self.data = {"paquete_id": None,
                     "subpackage_id": None,
                     "subpackage_num": None,
                     "subpackage_hash": None,
                     "subpackage": None,
                     "primer_mensaje": None  # 24 para guardar paquete, 42 para recoger paquete
                     }

        self.__hasheador = hashlib.sha256()

    def guardar_objeto(self, objeto, client):
        """

        """
        list_of_ids = []
        for c in range(0, len(self.__clientes)):
            list_of_ids.append(self.__clientes[c].get_id())

        if client.get_id() not in list_of_ids:
            return "el cliente no existe en el sistema."

        size_object = sys.getsizeof(objeto)

        if size_object <= 32:
            return self.__almacenPequeno.guardar_paquete(objeto, client)
        else:

            # miramos los datos
            print(objeto)
            datos_objeto = objeto
            cliente = client.get_id()
            print(cliente)
            # id_objeto = objeto.get_id()

            # lo divido en chunks
            chunks = self.__comunicacion_TAPNET.make_chunks(datos_objeto)

            print(chunks)

            data = {'primer_mensaje': 24,
                    'hash_chunks': self.__comunicacion_TAPNET.digest(),
                    'len_chunks': len(chunks),
                    'paquete_id': 6,
                    'cliente': 33}

            # crear el primer mensaje
            self.__comunicacion_TAPNET.send_package(NORMAL, data, '0.0.0.0', 9876)
            ack = self.__comunicacion_TAPNET.UDP_connection.recvfrom(self.buffer_size)

            print("hemos recibido de vuelta el ack")
            print(ack[0])

            primer_mensaje_vuelta = self.__comunicacion_TAPNET.translate_package_to_data([0])

            print(primer_mensaje_vuelta)

            if primer_mensaje_vuelta['message_type'] == 0:
                # envio mensaje
                for i in range(0, len(chunks)):
                    chunk_a_enviar = chunks[i]
                    print("chunk A ENVIAR")
                    print(chunk_a_enviar)
                    self.__hasheador.update(chunk_a_enviar)

                    self.data['paquete_id'] = 1
                    self.data['subpackage_id'] = i
                    self.data['subpackage_num'] = len(chunks)
                    self.data['subpackage'] = chunk_a_enviar
                    self.data['subpackage_hash'] = self.__hasheador.digest()

                    print("aqui estoy compraobando el subpackage id")
                    print(self.data)
                    self.__comunicacion_TAPNET.send_package(NORMAL, self.data, '0.0.0.0', 9876)

            # return self.__almacenGrande.guardar_paquete(objeto, client)

    def recuperar_objeto(self, id_paquete, client):
        """

        """
        list_id_clientes = []
        for i in range(0, len(self.__clientes)):
            list_id_clientes.append(self.__clientes[i].get_id())

        object_to_return = self.__almacenPequeno.recuperar_paquete(id_paquete, client)
        if object_to_return is "no es este warehouse":
            object_to_return = self.__almacenGrande.recuperar_paquete(id_paquete, client)
        print(object_to_return)
        return object_to_return

    def alta_cliente(self, client):
        """
        Da de alta a un cliente en el negocio.
        :param client: cliente al que vamos a dar de alta.
        :return: nada
        """
        self.__clientes.append(client)

    def baja_cliente(self, client):
        """
        Da de baja a un cliente en el negocio, si existe.
        :param cliente: cliente al que vamos a dar de baja.
        :return: nada
        """
        pass

        for i in range(0, len(self.__clientes)):
            if client.get_id() is self.__clientes[i].get_id():
                self.__clientes.pop(i)

        return "hemos eliminado al cliente."

    def estado_almacenamiento(self, almacen) -> None:
        """
        Imprime por pantalla el estado de los almacenes.
            para el almacen de objetos pequeños imprimmos, la informacion completa de los contenedores, pales y paquetes.
            para el almacen de objetos grandes, el numero de objetos, tamaño, contenido y cliente de cada uno.
        :param almacen: string que indica de que almacen queremos la informacion. 'small' para el pequeño 'big' para el grande.
        :return: None
        """

        if almacen is "small":
            self.__almacenPequeno.status()
        if almacen is "big":
            self.__almacenGrande.status()

    def objetos_de(self, cliente):
        """
        Imprime por pantalla el listado de objetos que pertenecen a un cliente.

        :param cliente: cliente que posee los objetos.
        :return: nada.
        """

        pass
