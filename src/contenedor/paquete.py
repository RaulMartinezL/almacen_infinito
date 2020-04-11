import sys


class Block:

    __size = 0
    __data = None
    __clientes = []
    __value_to_cast = None

    def __init__(self):
        pass
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
        self.__clientes.append(cliente)
        print(self.__clientes)


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
        for i in range(0, len(self.__clientes)):
            list_name_clientes.append(self.__clientes[i].get_name())

        return list_name_clientes

    def get_clients_id(self):
        """

        :return:
        """

        list_id_clientes = []
        for i in range(0, len(self.__clientes)):
            list_id_clientes.append(self.__clientes[i].get_id())

        return list_id_clientes

    def delete_ownership(self, client):
        """

        :param client:
        :return:
        """
        for i in range(0, len(self.__clientes)):
            if self.__clientes[i].get_id() == client.get_id():
                self.__clientes.pop(i)
        print(self.__clientes)

