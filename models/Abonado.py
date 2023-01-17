from models.Cliente import Cliente


class Abonado(Cliente):
    def __init__(self, vehiculo, plaza, dni, nombre, apellidos, abono, n_tarjeta):
        super().__init__(vehiculo)
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.abono = abono
        self.n_tarjeta = n_tarjeta
        self.plaza = plaza
