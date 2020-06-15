import sys
from src.empresa import cliente as Cliente


class Block:

    def __init__(self):
        self.__size = 0
        self.__data = None
        self.__clientes = {}
        self.__value_to_cast = None

    def set_data(self, data, cliente):
        """
        establecemos los datos que va a contener el paquete. Casteamos a str el contenido para guardar todos los datos
        como string. self.__value_to_cast contiene el tipo de dato que era :param data: antes de castearlo a string.
        :param data: pueden ser varios tipos. Datos que vamos a guardar en el paquete.
        :param cliente: cliente al que pertenece este paquete.
        :return: hash_key de 8 digitos enteros con el que podemos identificar el paquete más adelante.
        """
        self.__size = sys.getsizeof(data)
        self.__data = str(data)
        self.__value_to_cast = type(data)
        self.__add_client(cliente)

    def __add_client(self, cliente):

        clients_id = self.get_clients_id()

        if isinstance(cliente, int):
            if cliente not in clients_id:
                self.__clientes[cliente] = "placeholder"

        elif cliente.get_id() not in clients_id:
            self.__clientes[cliente.get_id()] = cliente.get_name()

    def get_data(self):
        """
        :return: Devuelve el contenido(data) del paquete de la clase que previamente era (antes del casta a str)
        """
        return self.__value_to_cast(self.__data)

    def get_size(self):
        """
        :return: tamaño del paquete. Este tamaño van a ser los bytes que ocupe el tipo de dato que contenga.
        """
        return self.__size

    def get_clients(self):
        """
        :return: nombre de los clientes que poseen este paquete.
        """

        list_name_clientes = []
        for i in self.__clientes.keys():
            # esto añade los nombres a list_name_clientes
            list_name_clientes.append(self.__clientes[i])

        return list_name_clientes

    def get_clients_id(self):
        """

        :return:
        """

        list_id_clientes = []
        for i in self.__clientes.keys():
            # esto añade a list_id_clientes las keys
            list_id_clientes.append(i)

        return list_id_clientes

    def delete_owners(self):
        """

        :return:
        """
        self.__clientes = []
