import datetime
class Ticket:
    def __init__(self, matricula, id_plaza, pin):
        self._matricula = matricula
        self._f_deposito = datetime.datetime.now()\
            .strftime("%Y-%m-%d / %H:%M:%S")
        self._id_plaza = id_plaza
        self._pin = pin

# GETTERS Y SETTERS
    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @property
    def id_plaza(self):
        return self._id_plaza

    @id_plaza.setter
    def id_plaza(self, id_plaza):
        self._id_plaza = id_plaza

    @property
    def pin(self):
        return self._pin

    @pin.setter
    def pin(self, pin):
        self._pin = pin

    @property
    def f_deposito(self):
        return self._f_deposito

    @f_deposito.setter
    def f_deposito(self, f_deposito):
        self._f_deposito = f_deposito

# METODOS
    def __str__(self):
        return '==================================================\n' \
               f'FECHA = {self.f_deposito}\n' \
               f'MATRICULA = {self.matricula}\n' \
               f'PLAZA = {self.id_plaza}\n' \
               f'PIN = {self.pin}\n' \
               '==================================================\n'
