class Cliente:
    def __init__(self, vehiculo):
        self.__vehiculo = vehiculo
        self.__ticket = None

    @property
    def ticket(self):
        return self.__ticket

    @ticket.setter
    def ticket(self, ticket):
        self.__ticket = ticket

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    def __str__(self):
        return f'Vehiculo del cliente: {self.__vehiculo.matricula}, Tipo: {self.__vehiculo.tipo}'
