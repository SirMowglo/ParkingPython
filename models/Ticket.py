import datetime
import random


class Ticket:
    def __init__(self, matricula, id_plaza, pin):
        self.__matricula = matricula
        self.__f_deposito = datetime.datetime.now()
        self.__id_plaza = id_plaza
        self.__pin = str(pin)

# GETTERS Y SETTERS
    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def id_plaza(self):
        return self.__id_plaza

    @id_plaza.setter
    def id_plaza(self, id_plaza):
        self.__id_plaza = id_plaza

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def f_deposito(self):
        return self.__f_deposito

    @f_deposito.setter
    def f_deposito(self, f_deposito):
        self.__f_deposito = f_deposito

# METODOS
    def __str__(self):
        return '==================================================\n' \
               f'FECHA = {self.f_deposito.strftime("%Y-%m-%d / %H:%M:%S")}\n' \
               f'MATRICULA = {self.matricula}\n' \
               f'PLAZA = {self.id_plaza}\n' \
               f'PIN = {self.pin}\n' \
               '==================================================\n'
