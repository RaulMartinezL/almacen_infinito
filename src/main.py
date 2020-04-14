from src.empresa.cliente import Cliente
from src.empresa.empresa import Empresa

import sys

if __name__ == "__main__":

    empresa1 = Empresa()

    cliente1 = Cliente('Claudia')
    cliente2 = Cliente('Roberto')
    cliente3 = Cliente('Raul')

    paquete1 = 1
    paquete2 = 2

    empresa1.alta_cliente(cliente1)
    empresa1.alta_cliente(cliente2)
    empresa1.alta_cliente(cliente3)

    empresa1.guardar_objeto(paquete1, cliente1)
    empresa1.guardar_objeto(paquete1, cliente2)
    empresa1.guardar_objeto(paquete2, cliente1)

    empresa1.recuperar_objeto(paquete1, cliente3)

    empresa1.estado_almacenamiento("small")
