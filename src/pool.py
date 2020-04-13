from src import paquete as paquete


class Pool:
    __pool_size = None
    __block_size = None
    __class_idx = None

    allocated_blocks = []
    __free_blocks = []
    __untouched_blocks = []

    def __init__(self, pool_size):
        self.__pool_size = pool_size

    def get_block_size(self):
        return self.__block_size

    def is_not_full(self):
        """
        suma la longitud de free_blocks y untouched_blocks. Si es mayor qué 0, quiere decir que hay bloques en los
        que podemos insertar el paquete.

        :return: True si hay bloques libre. False si no hay bloques libres.
        """

        print(len(self.__untouched_blocks))
        print(len(self.__free_blocks))
        # revisar este if si el check full no funciona.
        if len(self.__untouched_blocks) + len(self.__free_blocks) > 0:
            return True
        else:
            return False

    def define_block_size(self, class_idx, list_blocks_size):
        """
        definimos el numero total de bloques que el pool va a tener.
        de esta forma se desperdicia algo de memoria.

        :param class_idx: class_idx correpondiente al pool.
        :param list_blocks_size: lista con la correspondencia del class_idx, que hace de index a numero máximo
        de memoria que admite cada bloque. Ejemplo de esta lista -> [8,16,24]
        :return: nothing.
        """
        self.__class_idx = class_idx
        self.__block_size = list_blocks_size[class_idx]

        num_total_blocks = self.__pool_size / self.__block_size

        for i in range(0, int(num_total_blocks)):
            self.__untouched_blocks.append(paquete.Block())

    def get_pool_class_idx(self):
        """
        devolvemos el class_idx del pool.
        :return: int.
        """
        return self.__class_idx

    def insert_block(self, block_to_insert, client):
        """
        insertamos un paquete en el pool. en este todas las comprobacions del size del paquete y class_idx están hechas.

        :param client: cliente al que pertenece el paquete que estamos insertando.
        :param block_to_insert: puede ser varios tipos. Datos que vamos a insertar en el paquete.
        :return: string con informacion.
        """

        if self.is_not_full() is False:
            return 'el paquete no se puede almacenar porque no hay espacio en el pool seleccionado.'

        if len(self.__free_blocks) > 0:
            block24 = self.__free_blocks.pop()
            hash_key = block24.set_data(block_to_insert, client)
            self.allocated_blocks.append(block24)
            return hash_key
        else:
            block24 = self.__untouched_blocks.pop()
            hash_key = block24.set_data(block_to_insert, client)
            self.allocated_blocks.append(block24)
            return hash_key

    def get_package(self, hash_key_object, client_who_own):
        """
        buscamos en los bloques que están allocated (es decir, que tienen informacion) un paquete con
        el contenido indicado en param package. Devuelve None si no existe.

        :param package: puede ser varios tipos. Contenido del paquete que estamos buscando.
        :return: Pueden ser varios tipos. Devuelve el contenido del paquete o None si no existe.
        """

        for i in range(0, len(self.allocated_blocks)):
            hash_key = self.allocated_blocks[i].get_hash_key()
            client = self.allocated_blocks[i].get_client()
            if hash_key == hash_key_object and client == client_who_own:
                package_to_return = self.allocated_blocks.pop(i)
                self.__free_blocks.append(package_to_return)
                return package_to_return.get_data()

        return None

    def check_same_package(self, package, client):

        print("check same package")

        for i in range(0, len(self.allocated_blocks)):
            hash_key = self.allocated_blocks[i].get_hash_key()
            if hash_key == package:
                self.allocated_blocks[i].add_client(client)
                return hash_key

