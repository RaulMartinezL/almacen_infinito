from src.contenedor import contenedor as contenedor
import sys


class Small_almacen:

    __blocks_size = [8, 16, 24, 32]
    __used_containers = []


    def __init__(self):
        self.__create__container()

    def __create__container(self):
        """
        crea un container nuevo y lo inserta en self.__used_containers.
        :return: nothing.
        """
        self.__used_containers.append(contenedor.Arena(self.__blocks_size))


    def guardar_paquete(self, package, cliente):
        """

        :param package:
        :param cliente:
        :return:
        """
        # buscamos si existe un pool del tamaño adecuado en los contenedores que hay actualmente creados.
        for i in range(0, len(self.__used_containers)):
            # si existe espacio en el contenedor, insertamos el paquete.
            if self.__used_containers[i].is_not_full():
                return self.__used_containers[i].add_package(package, cliente)

        # si llegamos a este punto, quiere decir que no existe un pale del tamaño de paquete necesario para meter
        # nuestro paquete, asique creamos un contenedor nuevo y volvemos a llamar a esta misma funcion.
        self.__create__container()
        return self.guardar_paquete(package, cliente)

    def recuperar_paquete(self, id_paquete, cliente):
        """

        :return:
        """
        pass

    def status(self):
        """

        :return:
        """

        pools = self.__used_containers[0].get_pools()


        for i in range(0, len(pools)):
            print(pools[i].allocated_blocks[0].get_data())


        print("Informacion del almacen pequeño: ")
        print(f"En el almacen pequeño tenemos {len(self.__used_containers)} contenedores usados: ")
        for i in range(0, len(self.__used_containers)):
            print(f"En el contenedor {i+1}:")
            self.__used_containers[i].status_small_warehouse()











