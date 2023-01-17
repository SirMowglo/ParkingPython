from models.Cliente import Cliente


class Abonado(Cliente):
    def __init__(self, vehiculo, plaza, dni, nombre, apellidos, abono, n_tarjeta):
        super().__init__(vehiculo)
        self._dni = dni
        self._nombre = nombre
        self._apellidos = apellidos
        self._abono = abono
        self._n_tarjeta = n_tarjeta
        self._plaza = plaza


# GETTERS Y SETTERS
    @property
    def plaza(self):
        return self._plaza
    @plaza.setter
    def plaza(self, plaza):
        self.plaza = plaza

    @property
    def dni(self):
        return self._dni
    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellidos(self):
        return self._apellidos
    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    @property
    def abono(self):
        return self._abono

    @abono.setter
    def abono(self, abono):
        self._abono = abono

    @property
    def n_tarjeta(self):
        return self._n_tarjeta
    @n_tarjeta.setter
    def n_tarjeta(self, n_tarjeta):
        self._n_tarjeta = n_tarjeta