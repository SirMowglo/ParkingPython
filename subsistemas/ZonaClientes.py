import math
import pickle
import random
from datetime import datetime

from models.Cliente import Cliente
from models.Cobro import Cobro
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
                  if not plaza.ocupada and
                  tip == plaza.tipo and
                  plaza.abonado is None]
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
                          .total_seconds() / 60) * plaza.tarifa
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


def depositar_abonado():
    parking_file = open("data/parking.pickle", "rb")
    parking = pickle.load(parking_file)
    parking_file.close()
    abonados_file = open("data/abonado.pickle", "rb")
    abonados = pickle.load(abonados_file)
    abonados_file.close()

    matr = input("Introduce la matricula del vehiculo: ")
    dni = input("Introduce tu DNI: ")
    try:
        abonado_actual = next(abonado for abonado in abonados if dni == abonado.dni)

        if abonado_actual.dni == dni and matr == abonado_actual.vehiculo.matricula:
            plazas = [plaza for plaza in parking.lista_plazas if plaza.abonado is not None]
            if len(plazas) > 0:
                plaza = next(plaza for plaza in plazas if plaza.abonado.dni == dni)
                plaza.ocupada = True

                parking_file = open("data/parking.pickle", "wb")
                pickle.dump(parking, parking_file)
                parking_file.close()
                print('Se ha ocupado la plaza con exito')
                print(abonado_actual)
            else:
                print('Ha habido un problema con los datos proporcionados')
    except:
        print('Se ha detectado un error con el dni')


def retirar_abonado():
    parking_file = open("data/parking.pickle", "rb")
    parking = pickle.load(parking_file)
    parking_file.close()

    matr = input("Introduce la matricula del vehiculo: ")
    id_plaza = input('Introduce el identificador de la plaza asignada: ')
    pin = input('Introduce el pin correspondiente: ')

    plazas = [plaza for plaza in parking.lista_plazas if plaza.abonado is not None]
    print(plazas)
    if len(plazas) > 0:
        plaza = next(plaza for plaza in plazas
                     if plaza.abonado.vehiculo.matricula == matr
                     and str(plaza.id_plaza) == id_plaza
                     )
        if str(plaza.abonado.abono.pin) == pin:
            plaza.ocupada = False

            parking_file = open("data/parking.pickle", "wb")
            pickle.dump(parking, parking_file)
            parking_file.close()
            print('Se ha salido de la plaza con exito')
        else:
            print('PIN erroneo')
