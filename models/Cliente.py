class Cliente:
    def __init__(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo