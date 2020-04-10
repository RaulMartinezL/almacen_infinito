from uuid import uuid4


class Cliente:
    """
    Cliente de la empresa de almacenamiento
    """
    __id = None
    __name = None

    def __init__(self, name: str):
        self.__name = name
        self.__id = uuid4()

    def get_id(self):
        """
        Obtiene el identificador del Cliente
        :return: Identificador único del Cliente
        """
        return self.__id

