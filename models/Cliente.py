class Cliente:
    def __init__(self, vehiculo):
        self._vehiculo = vehiculo

    @property
    def vehiculo(self):
        return self._vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self._vehiculo = vehiculo