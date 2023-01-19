import pickle

from models.Cliente import Cliente
from models.Parking import Parking
from models.Ticket import Ticket
from models.Vehiculo import Vehiculo


def depositar_vehiculo(parking: Parking):
    nplaza_libre = 0
    for plaza in parking.lista_plazas:
        if not plaza.ocupada:
            nplaza_libre += 1
    print(f'Numero de Plazas libres: {nplaza_libre}')

    mat = input('Introduce la matricula del vehiculo: ')
    tip = input('Introduce el tipo del vehiculo (turismo, motocicleta o de movilidad reducida): ')

    cl1 = Cliente(Vehiculo(mat, tip))
    plazasDisp = [plaza for plaza in parking.lista_plazas
                  if not plaza.ocupada and tip == plaza.tipo]
    if len(plazasDisp) > 0:
        plazasDisp[0].ocupada = True
        ticket = Ticket(cl1.vehiculo.matricula, plazasDisp[0].id_plaza)

        cliente_file = open("data/cliente.pickle", "rb")
        clientes = pickle.load(cliente_file)

        clientes.append(cl1)
        cliente_file = open("data/cliente.pickle", "wb")
        pickle.dump(clientes, cliente_file)
        cliente_file.close()

        parking_file = open("data/parking.pickle", "wb")
        pickle.dump(parking, parking_file)
        parking_file.close()

        print(ticket)
    else:
        print('==================================================\n'
              'No hay plazas disponibles')
