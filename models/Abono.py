import datetime


class Abono:
    def __init__(self, tipo):
        self.f_activacion = datetime.datetime.now()
        self.tipo = tipo
        if(tipo == 'mensual'):
            self.f_cancelacion = self.f_activacion + datetime.timedelta(days=30)
        elif (tipo == 'trimestral'):
            self.f_cancelacion = self.f_activacion + datetime.timedelta(days=90)
        elif (tipo == 'semestral'):
            self.f_cancelacion = self.f_activacion + datetime.timedelta(days=180)
        elif (tipo == 'anual'):
            self.f_cancelacion = self.f_activacion + datetime.timedelta(days=360)
