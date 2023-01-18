class Plaza:
    def __init__(self, id_plaza, tipo, ocupada, abonado):
        self.__id_plaza = id_plaza
        self.__tipo = tipo
        if tipo == 'turismo':
            self.__tarifa = 0.12
        elif tipo == 'motocicleta':
            self.__tarifa = 0.08
        elif tipo == 'm_reducida':
            self.__tarifa = 0.10
        self.__ocupada = ocupada
        self.__abonado = abonado

    # GETTERS Y SETTERS
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def id_plaza(self):
        return self.__id_plaza

    @id_plaza.setter
    def id_plaza(self, id_plaza):
        self.__id_plaza = id_plaza

    @property
    def tarifa(self):
        return self.__tarifa

    @tarifa.setter
    def tarifa(self, tarifa):
        self.__tarifa = tarifa

    @property
    def ocupada(self):
        return self.__ocupada

    @ocupada.setter
    def ocupada(self, ocupada):
        self.__ocupada = ocupada

    @property
    def abonado(self):
        return self.__abonado

    @abonado.setter
    def abonado(self, abonado):
        self.__abonado = abonado

    def __str__(self):
        tipo = ''
        oc = '#'
        abonado = 'Nadie'

        if self.__tipo == 'turismo':
            tipo = 'T'
        elif self.__tipo == 'motocicleta':
            tipo = 'M'
        elif self.__tipo == 'm_reducida':
            tipo = 'R'
        if self.__ocupada:
            oc = 'O'
        if self.__abonado is not None:
            abonado = self.__abonado.nombre

        return f'{self.__id_plaza}{tipo}{oc} --> {abonado}'
