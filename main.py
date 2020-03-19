import arena as almacen
import sys

small_warehouse = almacen.Arena([8, 16, 24, 32])
big_warehouse = almacen.Arena([40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120, 128, 136, 144, 152, 160])
list_clients = []


def guardar_objeto(objeto, client):
    """
    Guardamos el objeto en el lugar adecuado. Devuelve un identificador para poder recuperarlo.
    :param objeto: objeto que vamos a guardar.
    :param cliente: cliente al que pertenece el objeto.
    :return: str. identificador unico del objeto.
    """
    if client not in list_clients:
        return "el cliente no existe en el sistema."

    size_object = sys.getsizeof(objeto)

    if size_object <= 32:
        return small_warehouse.add_package(objeto, client)
    else:
        return big_warehouse.add_package(objeto, client)


def recuperar_objeto(id_paquete, client):
    """
    Buscamos el objeto en el almacen pequenioo, si no existe lo buscamos en el grande.
    :param id_paquete: identificador del objeto que estamos buscando.
    :param client: cliente al que pertenece el objeto que estamos buscando.
    :return: el objeto que hemos encontrado. Si no devolvemos "no es este warehouse".
    """

    object_to_return = small_warehouse.get_package(id_paquete, client)
    if object_to_return is "no es este warehouse":
        object_to_return = big_warehouse.get_package(id_paquete, client)
    return object_to_return


def alta_cliente(client):
    """
    Da de alta a un cliente en el negocio.
    :param client: cliente al que vamos a dar de alta.
    :return: nada
    """

    list_clients.append(client)

    return "se ha dado de alta al cliente."


def baja_cliente(client):
    """
    Da de baja a un cliente en el negocio, si existe.
    :param cliente: cliente al que vamos a dar de baja.
    :return: nada
    """

    list_clients.remove(client)

    return "hemos eliminado al cliente."


def estado_almacenamiento():
    """
    Imprime por pantalla el estado de los almacenes.
        para el almacen de objetos pequeños imprimmos, la informacion completa de los contenedores, pales y paquetes.
        para el almacen de objetos grandes, el numero de objetos, tamaño, contenido y cliente de cada uno.
    :return: nada
    """

    # small_warehouse.status()
    big_warehouse.status()


def objetos_de(cliente):
    """
    Imprime por pantalla el listado de objetos que pertenecen a un cliente.

    :param cliente: cliente que posee los objetos.
    :return: nada.
    """

    pass


if __name__ == "__main__":
    client1 = 'Claudia'
    paquete1 = 'paquete1'
    paquete2 = 'paquete2'
    paquete11 = 4
    paquete22 = 4.4



    alta_cliente(client1)
    key_paquete1 = guardar_objeto(paquete1, client1)
    key_paquete2 = guardar_objeto(paquete2, client1)

    key_paquete11 = guardar_objeto(paquete11, client1)
    key_paquete22 = guardar_objeto(paquete22, client1)

    estado_almacenamiento()