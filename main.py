from models.Parking import Parking
import pickle

from subsistemas import ZonaClientes


def reset():
    open("data/parking.pickle", "w").close()
    open("data/cliente.pickle", "w").close()
    open("data/abono.pickle", "w").close()
    open("data/abonado.pickle", "w").close()

    p = Parking(20)
    clientes = []
    abonos = []
    abonados = []

    parking_file = open("data/parking.pickle", "wb")
    pickle.dump(p, parking_file)
    parking_file.close()

    clientes_file = open("data/cliente.pickle", "wb")
    pickle.dump(clientes, clientes_file)
    clientes_file.close()

    abonos_file = open("data/abono.pickle", "wb")
    pickle.dump(abonos, abonos_file)
    abonos_file.close()

    abonados_file = open("data/abonado.pickle", "wb")
    pickle.dump(abonados, abonados_file)
    abonados_file.close()

def mainMethod():
    salir = False

    while not salir:
        entradaZona = input('==================================================\n'
                            'Donde quieres acceder?:\n'
                            '1. Zona de Clientes\n'
                            '2. Zona de Administrador\n'
                            '3. Reset del parking\n'
                            'Otro. Salir del sistema\n')
        if entradaZona == '1':
            print('Estas en zona de clientes')
            opCliente = input('==================================================\n'
                              'Que operacion quieres realizar?:\n'
                              '1. Depositar vehiculo\n'
                              '2. Retirar vehiculo\n'
                              '3. Depositar vehiculo abonado\n'
                              '4. Retirar vehiculo de abonado\n')
            if opCliente == '1':
                parking_file = open("data/parking.pickle", "rb")
                parking = pickle.load(parking_file)
                parking_file.close()

                ZonaClientes.depositar_vehiculo(parking)

        elif entradaZona == '2':
            if entradaZona == '1':
                print('Estas en zona de clientes')
                opAdmin = input('==================================================\n'
                                'Que operacion quieres realizar?:\n'
                                '1. Ver estado parking\n'
                                '2. Ver facturacion entre fechas\n'
                                '3. Consulta de abonados\n'
                                '4. Gestionar abonos\n'
                                '5.Ver caducidad abonos')
                if opAdmin == '1':
                    parking_file = open("data/parking.pickle", "rb")
                    parking = pickle.load(parking_file)
                    parking_file.close()
                    print(parking)

        elif entradaZona == '3':
            reset()
        else:
            print("Saliste del sistema")
            salir = True


mainMethod()
