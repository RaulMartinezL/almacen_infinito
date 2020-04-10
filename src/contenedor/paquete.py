import sys
from uuid import uuid4


class Block:

    __size = 0
    __data = None
    __hash_key = None
    __cliente = None
    __value_to_cast = None
    __id = None

    def __init__(self):
        self._id = uuid4()

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
        self.__cliente = cliente

        # establecemos una hash key de 8 digitos enteros como clave unica del paquete.
        #self.__hash_key = abs(hash(data)) % (10 ** 8)

        return self.__hash_key

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

    def get_id(self):
        """
        :return:
        """
        return self.__id