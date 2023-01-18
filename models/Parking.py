from models.Plaza import Plaza
import math


class Parking:
    def __init__(self, n_plazas):
        self.lista_plazas = []
        for i in range(0, math.trunc(n_plazas * 0.7)):
            self.__lista_plazas.append(Plaza(len(self.__lista_plazas) + 1, 'turismo', False, None))
        for i in range(0, math.trunc(n_plazas * 0.15)):
            self.__lista_plazas.append(Plaza(len(self.__lista_plazas) + 1, 'motocicleta', False, None))
        for i in range(0, math.trunc(n_plazas * 0.15)):
            self.__lista_plazas.append(Plaza(len(self.__lista_plazas) + 1, 'm_reducida', False, None))

    # GETTERS Y SETTERS
    @property
    def lista_plazas(self):
        return self.__lista_plazas

    @lista_plazas.setter
    def lista_plazas(self, lista_plazas):
        self.__lista_plazas = lista_plazas

# METODOS
    def __str__(self):
        plazas = ''

        for plaza in self.__lista_plazas:
            if plaza.id_plaza % 4 == 0:
                plazas += str(plaza) + '\n'
            else: plazas += str(plaza) + ' || '

        return plazas