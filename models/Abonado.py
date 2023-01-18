from models.Cliente import Cliente


class Abonado(Cliente):
    def __init__(self, vehiculo, plaza, dni, nombre, apellidos, abono, n_tarjeta):
        super().__init__(vehiculo)
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__abono = abono
        self.__n_tarjeta = n_tarjeta
        self.__plaza = plaza


# GETTERS Y SETTERS
    @property
    def plaza(self):
        return self.__plaza
    @plaza.setter
    def plaza(self, plaza):
        self.plaza = plaza

    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos
    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, abono):
        self.__abono = abono

    @property
    def n_tarjeta(self):
        return self.__n_tarjeta
    @n_tarjeta.setter
    def n_tarjeta(self, n_tarjeta):
        self.__n_tarjeta = n_tarjeta