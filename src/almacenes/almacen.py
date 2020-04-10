from uuid import UUID

# from tapnet import TAPNet
from ..contenedor.paquete import Paquete


class Almacen:
    """
    Clase padre de todos los almacenes
    """

    def __init__(self):
        pass

    def guardar_paquete(self, paquete: Paquete) -> UUID:
        """
        Hace las gestiones pertinentes para almacenar el paquete
        :param paquete: Paquete a almacenar
        :return: ID del paquete guardado
        """
        return paquete.id

    def recuperar_paquete(self, id_paquete: UUID) -> Paquete:
        """
        Busca el paquete con el id especificado y lo saca del almacén
        :param id_paquete: identificador del paquete a buscar
        :return: Paquete encontrado
        """
        pass


class AlmacenLocal(Almacen):
    """
    Clase padre de los almacenes locales
    """
    pass


class AlmacenObjetosGrandes(AlmacenLocal):
    """
    Almacén para objetos grandes (de más de 32 unidades)
    """

    def __init__(self):
        super().__init__()
        self.paquetes = {}


class AlmacenObjetosPequenos(AlmacenLocal):
    """
    Almacén para objetos pequeños (≤ 32 unidades)
    """

    def __init__(self):
        super().__init__()
        self.contenedores = []


'''
class AlmacenRemoto(Almacen):
    """
    Almacén remoto
    """
    def __init__(self, ip, port):
        self.tapnet = TAPNet(ip, port)
        super().__init__()        
'''
