from threading import Thread


class Robot(Thread):
    """
    Robot que hace el trabajo de transportar los paquetes entre el mostrador y su ubicación en un almacén local
    """
    def run(self) -> None:
        """
        Método que permanece a la escucha de instrucciones por parte de la Empresa
        """
        pass