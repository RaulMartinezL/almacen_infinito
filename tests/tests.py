import unittest

from src.empresa.empresa import Empresa
from src.empresa.cliente import Cliente


class BaseTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.empresa = Empresa()
        self.clients = [
            Cliente('Alberto'),
            Cliente('Antonio'),
            Cliente('Jose'),
            Cliente('Pablo')
        ]

    def basic_test(self):
        for c in self.clients:
            p_id = self.empresa.guardar_objeto('Hola', c)


if __name__ == '__main__':
    unittest.main()
