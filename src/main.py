from src.empresa.cliente import Cliente
from src.empresa.empresa import Empresa
from uuid import uuid4
from uuid import uuid1

import sys

# TODO: revisar documentacion de las funciones
# TODO: añadir robots
# TODO: añadir almacen remoto

if __name__ == "__main__":


    empresa = Empresa()

    cliente1 = Cliente('Claudia')
    cliente2 = Cliente('Raul')
    cliente3 = Cliente('Juan')

    empresa.alta_cliente(cliente1)
    empresa.alta_cliente(cliente2)

    objeto1 = 4
    objeto2 = "objeto2"

    # empresa.guardar_objeto(objeto1, cliente1)
    # empresa.estado_almacenamiento("small")

    empresa.guardar_objeto(objeto2, cliente2)
    # empresa.estado_almacenamiento("small")

    # lol = empresa.recuperar_objeto(objeto1, cliente1)
    # empresa.estado_almacenamiento("small")
    # empresa.estado_almacenamiento("big")

    '''

    uno = uuid1()
    dos =  uuid4()
    tres =  uuid4()
    cuatro =  uuid4()
    cinco =  uuid4()

    print(type(uno))
    print(dos)
    print(tres)
    print(cuatro)
    print(cinco)

    print(len(str.encode(str(uno))))
    
    '''

