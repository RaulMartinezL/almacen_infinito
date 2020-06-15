import random


class Cliente:
    """
    Cliente de la empresa de almacenamiento
    """
    dict_data = {}

    def __init__(self, name: str):
        self.__name = name
        self.__id = random.getrandbits(32)
        self.dict_data[self.__id] = self.__name

    def get_id(self):
        """
        Obtiene el identificador del Cliente
        :return: Identificador único del Cliente
        """
        return self.__id

    def get_name(self):
        """

        :return:
        """
        return self.__name