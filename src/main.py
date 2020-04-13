from src.empresa.cliente import Cliente
from src.empresa.empresa import Empresa

import sys

if __name__ == "__main__":

    empresa1 = Empresa()
    cliente = Cliente('Claudia')
    cliente2 = Cliente('Roberto')
    empresa1.alta_cliente(cliente)
    empresa1.alta_cliente(cliente2)

    paquete = "hello"
    paquete2 = "hello"

    print(sys.getsizeof(paquete))

    print("añadimos paquete 1")
    aa = empresa1.guardar_objeto(paquete2, cliente2)
    print("añadimos paquete 2")
    a = empresa1.guardar_objeto(paquete, cliente)
    print("mis muertow")

    fff = empresa1.recuperar_objeto(paquete, cliente)
    fffd = empresa1.recuperar_objeto(paquete, cliente2)

    print(fff)
    print(fffd)


    # empresa1.estado_almacenamiento()
