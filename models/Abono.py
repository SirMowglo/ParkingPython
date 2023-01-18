import datetime


class Abono:
    def __init__(self, tipo):
        self.__f_activacion = datetime.datetime.now()\
            .strftime("%Y-%m-%d")
        self.__tipo = tipo
        if tipo == 'mensual':
            self._f_cancelacion = (self.__f_activacion + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
            self.__precio = 25.0
        elif tipo == 'trimestral':
            self._f_cancelacion = (self.__f_activacion + datetime.timedelta(days=90)).strftime("%Y-%m-%d")
            self.__precio = 70.0
        elif tipo == 'semestral':
            self._f_cancelacion = (self.__f_activacion + datetime.timedelta(days=180)).strftime("%Y-%m-%d")
            self.__precio = 130.0
        elif tipo == 'anual':
            self._f_cancelacion = (self.__f_activacion + datetime.timedelta(days=360)).strftime("%Y-%m-%d")
            self.__precio = 200.0

    # GETTERS Y SETTERS
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def f_activacion(self):
        return self.__f_activacion

    @f_activacion.setter
    def f_activacion(self, f_activacion):
        self.__f_activacion = f_activacion

    @property
    def f_cancelacion(self):
        return self._f_cancelacion

    @f_cancelacion.setter
    def f_cancelacion(self, f_cancelacion):
        self._f_cancelacion = f_cancelacion
