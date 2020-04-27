import sys


class Block:

    __size = 0
    __data = None
    __hash_key = None
    __cliente = []

    def __init__(self):
        pass

    def set_data(self, data, cliente):
        """
        establecemos los datos que va a contener el paquete.
        :param data: pueden ser varios tipos. Datos que vamos a guardar en el paquete.
        :param cliente: cliente al que pertenece este paquete.
        :return: hash_key de 8 digitos enteros con el que podemos identificar el paquete más adelante.
        """
        self.__size = sys.getsizeof(data)
        self.__data = data
        self.__cliente.append(cliente)
        # establecemos una hash key de 8 digitos enteros como clave unica del paquete.
        self.__hash_key = abs(hash(data)) % (10 ** 8)

        return self.__hash_key

    def add_client(self, client):

        print(self.__cliente)
        self.__cliente.append(client)
        print(self.__cliente)
        return "please work"

    def get_data(self):
        """
        :return: pueden ser varios tipos. Devuelve contenido del paquete.
        """
        return self.__data

    def get_size(self):
        """
        :return: tamaño del paquete. Este tamaño van a ser los bytes que ocupe el tipo de dato que contenga.
        """
        return self.__size

    def get_client(self):
        """
        :return: cliente al que pertenece el paquete.
        """
        return self.__cliente

    def get_hash_key(self):
        """
        :return: hash key de 8 digitos enteros. Identifica el paquete.
        """
        return self.__hash_key