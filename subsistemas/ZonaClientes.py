import math
import pickle
import random
from datetime import datetime

from models.Cliente import Cliente
from models.Cobro import Cobro
from models.Parking import Parking
from models.Ticket import Ticket
from models.Vehiculo import Vehiculo


def depositar_vehiculo():
    parking_file = open("data/parking.pickle", "rb")
    parking = pickle.load(parking_file)
    parking_file.close()

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
        ticket = Ticket(cl1.vehiculo.matricula,
                        plazasDisp[0].id_plaza,
                        random.randint(100000, 999999))
        cl1.ticket = ticket

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


def retirar_vehiculo():
    parking_file = open("data/parking.pickle", "rb")
    parking = pickle.load(parking_file)
    parking_file.close()

    matr = input('Introduce la matricula del vehiculo: ')
    n_plaza = input('Introduce el identificador de la plaza donde se encuentra tu vehiculo: ')
    pin = str(input('Introduce el pin asociado a la plaza: '))

    cliente_file = open("data/cliente.pickle", "rb")
    clientes = pickle.load(cliente_file)
    cliente_file.close()
    clientes_encontrados = [cliente for cliente in clientes
                            if n_plaza == str(cliente.ticket.id_plaza) and
                            matr == cliente.ticket.matricula and
                            pin == cliente.ticket.pin]
    if len(clientes_encontrados) > 0:

        plaza = parking.lista_plazas[
            clientes_encontrados[0].ticket.id_plaza - 1
        ]

        pago = math.trunc((datetime.now() - clientes_encontrados[0].ticket.f_deposito)
                          .total_seconds()/60) * plaza.tarifa
        print('==================================================\n')
        print(f'El pago a realizar es de: {pago} euros ')
        c_cobro = float(input(f'Introduce la cantidad solicitada: '))

        if c_cobro >= pago:
            resto = c_cobro - pago
            print(f'==================================================\n'
                  f'El tramite ha sido un exito, este es el importe restante: {resto}')

            cobro = Cobro(pago)
            parking.lista_plazas[parking.lista_plazas.index(plaza)].ocupada = False
            clientes.remove(clientes_encontrados[0])

            cobros_file = open("data/cobros.pickle", "rb")
            cobros = pickle.load(cobros_file)
            cobros.append(cobro)
            cobros_file = open("data/cobros.pickle", "wb")
            pickle.dump(cobros, cobros_file)
            cobros_file.close()

            cliente_file = open("data/cliente.pickle", "wb")
            pickle.dump(clientes, cliente_file)
            cliente_file.close()

            parking_file = open("data/parking.pickle", "wb")
            pickle.dump(parking, parking_file)
            parking_file.close()
        else:
            print('El importe no llega al minimo solicitado')
    else:
        print('No se ha encontrado cliente')
