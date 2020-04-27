from src.empresa.cliente import Cliente
from src.empresa.empresa import Empresa

import sys

if __name__ == "__main__":
<<<<<<< HEAD
=======
    client1 = 'Claudia'
    client2 = 'Raul'
    paquete1 = 'paquete1'
    paquete2 = 'paquete2'
>>>>>>> master

    empresa1 = Empresa()

    cliente1 = Cliente('Claudia')
    cliente2 = Cliente('Roberto')
    cliente3 = Cliente('Raul')

    paquete1 = 1
    paquete2 = 2

<<<<<<< HEAD
    empresa1.alta_cliente(cliente1)
    empresa1.alta_cliente(cliente2)
    empresa1.alta_cliente(cliente3)

    empresa1.guardar_objeto(paquete1, cliente1)
    empresa1.guardar_objeto(paquete1, cliente2)
    empresa1.guardar_objeto(paquete2, cliente1)
=======
    alta_cliente(client1)
    alta_cliente(client2)

    key_paquete1 = guardar_objeto(paquete1, client1)
    key_paquete2 = guardar_objeto(paquete1, client2)

    print(key_paquete1)
    print("dd")
    print(key_paquete2)
>>>>>>> master

    empresa1.recuperar_objeto(paquete1, cliente3)

    empresa1.estado_almacenamiento("small")
