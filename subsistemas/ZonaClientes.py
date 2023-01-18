import random

from models.Cliente import Cliente
from models.Parking import Parking
from models.Ticket import Ticket
from models.Vehiculo import Vehiculo


class ZonaClientes:
    def depositar_vehiculo(self, parking: Parking):
        nplaza_libre = 0
        for plaza in parking.lista_plazas:
            if not plaza.ocupada:
                nplaza_libre += 1
        print(f'Numero de Plazas libres: {nplaza_libre}')

        mat = input('Introduce la matricula del vehiculo')
        tip = input('Introduce el tipo del vehiculo (turismo, motocicleta o de movilidad reducida')

        cl1 = Cliente(Vehiculo(mat, tip))
        ticket = None

        for plaza in parking.lista_plazas:
            first = True
            if not plaza.ocupada and tip == plaza.tipo and first:
                plaza.ocupada = True
                first = False
                ticket = Ticket(cl1.vehiculo.matricula, plaza.id_plaza)

        print(ticket)

