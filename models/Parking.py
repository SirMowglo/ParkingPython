from models.Plaza import Plaza
import math

class Parking:
    def __init__(self, n_plazas):
        self.lista_plazas = []
        for i in range(0, math.trunc(n_plazas*0.7)):
            self.lista_plazas.append(Plaza(i, 'turismo', False, None))
        for i in range(0, math.trunc(n_plazas*0.15)):
            self.lista_plazas.append(Plaza(i, 'motocicleta', False, None))
        for i in range(0, math.trunc(n_plazas*0.15)):
            self.lista_plazas.append(Plaza(i, 'm_reducida', False, None))
