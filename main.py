from models.Parking import Parking
import pickle

from subsistemas import ZonaClientes, ZonaAdmin


def reset():
    open("data/parking.pickle", "w").close()
    open("data/cliente.pickle", "w").close()
    open("data/abono.pickle", "w").close()
    open("data/abonado.pickle", "w").close()
    open("data/cobros.pickle", "w").close()

    p = Parking(20)
    clientes = []
    abonos = []
    abonados = []
    cobros = []

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

    cobros_file = open("data/cobros.pickle", "wb")
    pickle.dump(cobros, cobros_file)
    cobros_file.close()


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
                              '4. Retirar vehiculo de abonado\n'
                              'Otro. Salir\n')
            if opCliente == '1':
                ZonaClientes.depositar_vehiculo()
            if opCliente == '2':
                ZonaClientes.retirar_vehiculo()
            if opCliente == '3':
                ZonaClientes.depositar_abonado()
            if opCliente == '4':
                ZonaClientes.retirar_abonado()

        elif entradaZona == '2':
            print('Estas en zona de clientes')
            opAdmin = input('==================================================\n'
                            'Que operacion quieres realizar?:\n'
                            '1. Ver estado parking\n'
                            '2. Ver facturacion entre fechas\n'
                            '3. Consulta de abonados\n'
                            '4. Gestionar abonos\n'
                            '5.Ver caducidad abonos\n'
                            'Otro. Salir\n')
            if opAdmin == '1':
                ZonaAdmin.consultar_estado_parking()
            if opAdmin == '2':
                ZonaAdmin.facturacion_entre_fechas()
            if opAdmin == '3':
                ZonaAdmin.consultar_abonos()
            if opAdmin == '4':
                ZonaAdmin.gestionar_abonos()

        elif entradaZona == '3':
            reset()
        else:
            print("Saliste del sistema")
            salir = True


# TODO Metodo que añada contenido para probar a los pickle
mainMethod()
