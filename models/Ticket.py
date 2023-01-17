import datetime
class Ticket:
    def __init__(self, matricula, id_plaza, pin):
        self.matricula = matricula
        self.f_deposito = datetime.datetime.now()
        self.id_plaza = id_plaza
        self.pin = pin
