import sys
from ..almacenes.almacen import AlmacenObjetosGrandes, AlmacenObjetosPequenos
from ..contenedor.paquete import Block
from .cliente import Cliente



class Empresa:

    __almacenGrande = None
    __almacenPequeno = None

    __clientes = []



    def __init__(self):
        self.__almacenGrande = AlmacenObjetosGrandes()
        self.__almacenPequeno = AlmacenObjetosPequenos()

    def guardar_objeto(self, objeto, client: Cliente):
        """
        Guardamos el objeto en el lugar adecuado. Devuelve un identificador para poder recuperarlo.
        :param objeto: objeto que vamos a guardar.
        :param cliente: cliente al que pertenece el objeto.
        :return: str. identificador unico del objeto.
        """
        list_of_ids = []
        for c in range(0, len(self.__clientes)):
            list_of_ids.append(self.__clientes[c].get_id())

        if client.get_id() not in list_of_ids:
            return "el cliente no existe en el sistema."
        else:
            return client.get_id()

        #size_object = sys.getsizeof(objeto)

        #if size_object <= 32:
          #  return small_warehouse.guardar_paquete(objeto, client)
        #else:
         #   return big_warehouse.guardar_paquete(objeto, client)


    def recuperar_objeto(id_paquete, client):
        """
        Buscamos el objeto en el almacen pequenioo, si no existe lo buscamos en el grande.
        :param id_paquete: identificador del objeto que estamos buscando.
        :param client: cliente al que pertenece el objeto que estamos buscando.
        :return: el objeto que hemos encontrado. Si no devolvemos "no es este warehouse".
        """
        pass

        object_to_return = small_warehouse.get_package(id_paquete, client)
        if object_to_return is "no es este warehouse":
            object_to_return = big_warehouse.get_package(id_paquete, client)
        return object_to_return


    def alta_cliente(self, client):
        """
        Da de alta a un cliente en el negocio.
        :param client: cliente al que vamos a dar de alta.
        :return: nada
        """
        self.__clientes.append(client)

    def baja_cliente(client):
        """
        Da de baja a un cliente en el negocio, si existe.
        :param cliente: cliente al que vamos a dar de baja.
        :return: nada
        """
        pass

        list_clients.remove(client)

        return "hemos eliminado al cliente."


    def estado_almacenamiento():
        """
        Imprime por pantalla el estado de los almacenes.
            para el almacen de objetos pequeños imprimmos, la informacion completa de los contenedores, pales y paquetes.
            para el almacen de objetos grandes, el numero de objetos, tamaño, contenido y cliente de cada uno.
        :return: nada
        """

        pass
        # small_warehouse.status()
        big_warehouse.status()


    def objetos_de(cliente):
        """
        Imprime por pantalla el listado de objetos que pertenecen a un cliente.

        :param cliente: cliente que posee los objetos.
        :return: nada.
        """

        pass
