import datetime


class Abono:
    def __init__(self, tipo):
        self._f_activacion = datetime.datetime.now()\
            .strftime("%Y-%m-%d")
        self._tipo = tipo
        if tipo == 'mensual':
            self._f_cancelacion = (self._f_activacion + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
        elif tipo == 'trimestral':
            self._f_cancelacion = (self._f_activacion + datetime.timedelta(days=90)).strftime("%Y-%m-%d")
        elif tipo == 'semestral':
            self._f_cancelacion = (self._f_activacion + datetime.timedelta(days=180)).strftime("%Y-%m-%d")
        elif tipo == 'anual':
            self._f_cancelacion = (self._f_activacion + datetime.timedelta(days=360)).strftime("%Y-%m-%d")

    # GETTERS Y SETTERS
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def f_activacion(self):
        return self._f_activacion

    @f_activacion.setter
    def f_activacion(self, f_activacion):
        self._f_activacion = f_activacion

    @property
    def f_cancelacion(self):
        return self._f_cancelacion

    @f_cancelacion.setter
    def f_cancelacion(self, f_cancelacion):
        self._f_cancelacion = f_cancelacion
