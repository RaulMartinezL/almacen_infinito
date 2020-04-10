from src.empresa.cliente import Cliente
from src.empresa.empresa import Empresa

import sys

if __name__ == "__main__":

    empresa1 = Empresa()
    cliente = Cliente('Claudia')
    empresa1.alta_cliente(cliente)

    paquete = "hello"
    paquete2 = 92

    print(sys.getsizeof(paquete))
    print(sys.getsizeof(paquete2))

    aa = empresa1.guardar_objeto(paquete, cliente)
