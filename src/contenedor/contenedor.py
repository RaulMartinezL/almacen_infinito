from src.contenedor import pale as pale
import sys


class Arena:
    """
    Contenedor es la clase equivalente a la Arena de python
    """
    __blocks_size = []

    __free_pools = []
    __used_pools = []


    def get_pools(self):
        return self.__used_pools

    def __init__(self, blocks_size):

        for i in range(0, 4):
            self.__create_free_pool()
        self.__blocks_size = blocks_size

    def __create_free_pool(self):
        """
        crea un pool nuevo vacio y lo inserta a self.__free_pools .
        :return: nothing.
        """
        self.__free_pools.append(pale.Pool())

    def __get_class_idx(self, size):
        """
        devuelve el size class idx correpondiente a size.

        :param size: entero que indica el size de un block, en bytes.
        :return: entero (0,1,2 o 3 ...) que corresponde al size class idx.
        """
        for i in range(0, len(self.__blocks_size)):
            if size / self.__blocks_size[i] <= 1:
                return i

        # si llegamos aqui, quiere decir que no tenemos contemplado el class idx para el size del paquete
        # no deberiamos de llegar nunca
        return -1

    def __get_pool_idx(self, class_idx):
        """
        devuelve un pool donde los bloques son del size class_idx y donde hay bloques libres.
        si no existe un pool asi, comprueba que haya alguno free.

        :param class_idx: entero (0,1,2 o 3 ...) que corresponde al size class idx del pool que queremos buscar.
        :return: un pool.
        """
        if class_idx == -1:
            # chequear get_class_idx.
            sys.exit('no existe class idx para el size del paquete')

        # buscamos un pool usado, donde el size del bloque es suficiente para meter nuestro paquete
        # y que tenga bloques libres.
        for i in range(0, len(self.__used_pools)):
            if self.__used_pools[i].get_pool_class_idx() == class_idx:
                if self.__used_pools[i].is_not_full:
                    return self.__used_pools[i]

        # si no existe, buscamos un pool free, donde haremos que el size de los bloques sea suficiente para
        # meter nuestro paquete.
        if len(self.__free_pools) > 0:
            aux_pool = self.__free_pools.pop()
            aux_pool.define_block_size(class_idx, self.__blocks_size)
            self.__used_pools.append(aux_pool)
            return aux_pool

        return False

    def __fetch_package(self, data_package, client):
        """
        recorre la lista de pool los cuales tienen blocks (esta lista es self.__used_pools) hasta encontrar un pool
        donde class_idx sea la que estamos buscando.
        si no es asi quiere decir que no existe el paquete que estamos buscando.

        :param package: data del paquete que estamos buscando.
        :param pool_idx: class_pool_idx de los pools donde estamos buscando el paquete.
        :return: contenido del paquete que hemos encontrado que coincide con param package.
        """

        if len(self.__used_pools) == 0:
            sys.exit("para buscar paquetes primero tienes que meter al menos uno")

        for i in range(0, len(self.__used_pools)):
            package_to_return = self.__used_pools[i].get_package(data_package, client)
            if package_to_return is not None:
                return package_to_return

        return None

    def is_not_full(self):
        """
        comprobamos que hay espacio disponible en los palés que contiene este contenedor.
        :return: True si existe espacio disponible. False si no existe espacio disponible.
        """

        if len(self.__free_pools) > 0:
            return True

        for i in range(0, len(self.__used_pools)):
            if self.__used_pools[i].is_not_full() is True:
                return True

        return False

    def __check_size(self, size):
        """
        Esto es una tonteria, ya se compreuba en get_pool_idx Y en get_class_idx
        :param size:
        :return:
        """
        can_insert = False
        for i in range(0, len(self.__blocks_size)):
            division = size/self.__blocks_size[i]
            if division < 1:
                can_insert = True

        return can_insert

    def add_package(self, package, client):
        """
        inserta un paquete en un block de un pool.

        :param client: cliente al que pertenece el paquete que estamos insertando
        :param package: datos que queremos insertar como paquete.
        :return: string con informacion.
        """

        # chequeamos el tamaño del paquete que nos pasan
        size = sys.getsizeof(package)

        # obtenemos el pool, dónde los tamaños de los blocks son suficientes para nuestro paquete
        pool_where_insert = self.__get_pool_idx(self.__get_class_idx(size))

        if pool_where_insert is False:
            return False

        # insertamos el paquete en el pool correspondiente
        pool_where_insert.insert_block(package, client)
        return True

    def get_package(self, data_package, client):
        """

        :param data_package:
        :param client:
        :return:
        """

        return self.__fetch_package(data_package, client)



    def status_small_warehouse(self):
        """
        imprimimos el estado del almacen small
        :return: nada.
        """
        print(self.__blocks_size)

        print(f"tenemos {len(self.__used_pools)} palés usados.")
        for i in range(0, len(self.__used_pools)):
            for j in range(0, len(self.__used_pools[i].allocated_blocks)):
                print(self.__used_pools[i].allocated_blocks[j].get_size())

    def status_big_warehouse(self):
        """
        imprimimos el estado del almacen grande
        :return: nada.
        """

        num_objects = 0
        # para cada pool que existe en esta arena
        for i in range(0, len(self.__used_pools)):
            # miramos todos los blocks allocated que tiene este pool
            for j in range(0, len(self.__used_pools[i].allocated_blocks)):
                size_object = self.__used_pools[i].allocated_blocks[j].get_size()
                content_object = self.__used_pools[i].allocated_blocks[j].get_data()
                client_object = self.__used_pools[i].allocated_blocks[j].get_clients()
                print(f"Este objeto contiene '{content_object}', pertenece a {client_object} y ocupa {size_object}")
                num_objects += 1

        print(f"\nEl numero de palés que existen en el almacen grande son: {len(self.__used_pools)}")
        print(f"El numero de objetos que existen en todos los palés del almacen grande son: {num_objects}")

        for i in range(0, len(self.__used_pools)):
            if len(self.__used_pools[i].allocated_blocks) <= 0:
                print(f"El almacen grande ha enviado todos los paquetes del palé {i + 1}")
