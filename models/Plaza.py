class Plaza:
    def __init__(self, id_plaza, tipo, ocupada, abonado):
        self.id_plaza = id_plaza
        self.tipo = tipo
        if tipo == 'turismo':
            self.tarifa = 0.12
        elif tipo == 'motocicleta':
            self.tarifa = 0.08
        elif tipo == 'm_reducida':
            self.tarifa = 0.10
        self.ocupada = ocupada
        self.abonado = abonado

