import datetime


class Cobro:
    def __init__(self, cobro):
        self.__cobro = cobro
        self.__f_cobro = datetime.datetime.now()

    @property
    def cobro(self):
        return self.__cobro

    @cobro.setter
    def cobro(self, cobro):
        self.__cobro = cobro

    @property
    def f_cobro(self):
        return self.__f_cobro

    @f_cobro.setter
    def f_cobro(self, f_cobro):
        self.__f_cobro = f_cobro

    def __str__(self):
        return '==================================================\n' \
               f'Cantidad del cobro: {self.cobro}\n' \
               f'Fecha del cobro: {self.f_cobro.strftime("%Y-%m-%d / %H:%M:%S")}\n' \
               f'==================================================\n'
