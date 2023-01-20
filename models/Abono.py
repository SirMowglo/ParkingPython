import datetime
import random

from models.Cobro import Cobro


class Abono:
    def __init__(self, tipo):
        self.__f_activacion = datetime.datetime.now()
        self.__tipo = tipo
        if tipo == 'mensual':
            self.__f_cancelacion = (self.__f_activacion + datetime.timedelta(days=30))
            self.__precio = 25.0
        elif tipo == 'trimestral':
            self.__f_cancelacion = (self.__f_activacion + datetime.timedelta(days=90))
            self.__precio = 70.0
        elif tipo == 'semestral':
            self.__f_cancelacion = (self.__f_activacion + datetime.timedelta(days=180))
            self.__precio = 130.0
        elif tipo == 'anual':
            self.__f_cancelacion = (self.__f_activacion + datetime.timedelta(days=360))
            self.__precio = 200.0
        self.__cobro = Cobro(self.__precio)
        self.__pin = random.randint(100000, 999999)

    # GETTERS Y SETTERS
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def cobro(self):
        return self.__cobro

    @cobro.setter
    def cobro(self, cobro):
        self.__cobro = cobro
    @property
    def f_activacion(self):
        return self.__f_activacion

    @f_activacion.setter
    def f_activacion(self, f_activacion):
        self.__f_activacion = f_activacion

    @property
    def f_cancelacion(self):
        return self.__f_cancelacion

    @f_cancelacion.setter
    def f_cancelacion(self, f_cancelacion):
        self.__f_cancelacion = f_cancelacion

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    def __str__(self):
        return '==================================================\n' \
               f'TIPO: {self.tipo}\n' \
               f'ACTIVACION: {self.f_activacion.strftime("%Y-%m-%d")}\n' \
               f'CANCELACION: {self.f_cancelacion.strftime("%Y-%m-%d")}\n' \
               f'PRECIO: {self.precio}\n' \
               f'PIN: {self.pin}\n' \
               f'==================================================\n'
