class Plaza:
    def __init__(self, id_plaza, tipo, ocupada, abonado):
        self._id_plaza = id_plaza
        self._tipo = tipo
        if tipo == 'turismo':
            self._tarifa = 0.12
        elif tipo == 'motocicleta':
            self._tarifa = 0.08
        elif tipo == 'm_reducida':
            self._tarifa = 0.10
        self._ocupada = ocupada
        self._abonado = abonado

    # GETTERS Y SETTERS
    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def id_plaza(self):
        return self._id_plaza

    @id_plaza.setter
    def id_plaza(self, id_plaza):
        self._id_plaza = id_plaza

    @property
    def tarifa(self):
        return self._tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        self._tarifa = tarifa

    @property
    def ocupada(self):
        return self._ocupada

    @ocupada.setter
    def ocupada(self, ocupada):
        self._ocupada = ocupada

    @property
    def abonado(self):
        return self._abonado

    @abonado.setter
    def abonado(self, abonado):
        self._abonado = abonado
