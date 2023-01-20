import pickle
import datetime

from models.Abonado import Abonado
from models.Abono import Abono
from models.Cobro import Cobro
from models.Parking import Parking
from models.Vehiculo import Vehiculo


def consultar_estado_parking():
    parking_file = open("data/parking.pickle", "rb")
    parking = pickle.load(parking_file)
    parking_file.close()
    print('==================================================\n'
          'PLAZA = ID + Tipo + Estado --> Dueño abono\n'
          '==================================================\n')
    print(parking)


def facturacion_entre_fechas():
    cobros_file = open("data/cobros.pickle", "rb")
    cobros = pickle.load(cobros_file)
    cobros_file.close()

    fecha_fst = input('Introduce la primera fecha y hora para consultar (Y-M-D / H:M:S): ')
    fecha_lst = input('Introduce la segunda fecha para consultar (Y-M-D / H:M:S): ')

    cobros_realizados = [cobro for cobro in cobros
                         if cobro.f_cobro.strftime("%Y-%m-%d / %H:%M:%S") >= fecha_fst or
                         cobro.f_cobro.strftime("%Y-%m-%d / %H:%M:%S") <= fecha_lst]
    for cobro in cobros_realizados:
        print(cobro)


# TODO Comprobacion del metodo
def consultar_abonos():
    abonos_file = open("data/abono.pickle", "rb")
    abonos = pickle.load(abonos_file)
    abonos_file.close()

    for abono in abonos:
        print(abono)
        print('COBRO DEL ABONO: \n'
              f'{abono.cobro}')


def gestionar_abonos():
    parking_file = open("data/parking.pickle", "rb")
    parking = pickle.load(parking_file)
    parking_file.close()

    gestion = input('==================================================\n'
                    'Que gestion quieres realizar?:\n'
                    '1. Dar de alta\n'
                    '2. Modificar datos personales\n'
                    '3. Dar de baja el abono\n'
                    'Otro. Salir\n')

    if gestion == '1':
        print('Siga los siguientes pasos para darse de alta.')
        tipo_plaza = input('Introduzca el tipo de plaza que desea reservar (turismo, motocicleta o de movilidad '
                           'reducida): ')
        plazasDisp = [plaza for plaza in parking.lista_plazas
                      if not plaza.ocupada and
                      tipo_plaza == plaza.tipo and
                      plaza.abonado is None]
        if len(plazasDisp):
            tipo_abono = input('Introduzca el tipo de abono que desea (mensual, trimestral, semestral, anual: ')
            if tipo_abono == 'mensual' or \
                    tipo_abono == 'trimestral' or \
                    tipo_abono == 'semestral' or \
                    tipo_abono == 'anual':
                dni = input('Introduzca su DNI: ')
                nombre = input('Introduzca su nombre: ')
                apellidos = input('Introduzca sus apellidos: ')
                matr = input('Introduzca la matricula de su coche: ')
                n_tarjeta = input('Introduzca su numero de tarjeta de credito: ')

                print('El pago ha sido realizado con exito')
                nuevo_abono = Abono(tipo_abono)
                nuevo_abonado = Abonado(Vehiculo(matr, tipo_plaza), dni, nombre, apellidos, nuevo_abono, n_tarjeta)
                parking.lista_plazas[parking.lista_plazas.index(plazasDisp[0])].abonado = nuevo_abonado

                cobros_file = open("data/cobros.pickle", "rb")
                cobros = pickle.load(cobros_file)
                cobros.append(nuevo_abono.cobro)
                cobros_file = open("data/cobros.pickle", "wb")
                pickle.dump(cobros, cobros_file)
                cobros_file.close()

                parking_file = open("data/parking.pickle", "wb")
                pickle.dump(parking, parking_file)
                parking_file.close()

                abonados_file = open("data/abonado.pickle", "rb")
                abonados = pickle.load(abonados_file)
                abonados.append(nuevo_abonado)
                abonados_file = open("data/abonado.pickle", "wb")
                pickle.dump(abonados, abonados_file)
                abonados_file.close()

                abonos_file = open("data/abono.pickle", "rb")
                abonos = pickle.load(abonos_file)
                abonos.append(nuevo_abonado.abono)
                abonos_file = open("data/abono.pickle", "wb")
                pickle.dump(abonos, abonos_file)
                abonos_file.close()

                print(nuevo_abonado)
            else:
                print('El tipo de abono solicitado no existe.')
        else:
            print('No quedan plazas del tipo seleccionado')

    elif gestion == '2':
        dni = input("Antes de realizar cualquier operacion, introduce tu dni: ")
        abonados_file = open("data/abonado.pickle", "rb")
        abonados = pickle.load(abonados_file)
        abonados_file.close()

        op = input('==================================================\n'
                   'Que operacion quieres realizar?:\n'
                   '1. Modificar datos\n'
                   '2. Renovar abono\n'
                   'Otro. Salir\n')
        try:
            abonado_actual = next(abonado for abonado in abonados if dni == abonado.dni)
        except:
            print('Se ha detectado un error con el dni')
        if abonado_actual.dni == dni and op == '1':
            plazas = [plaza for plaza in parking.lista_plazas if plaza.abonado is not None]
            plaza = next(plaza for plaza in plazas if plaza.abonado.dni == dni)

            nuevo_dni = input("Introduce tu nuevo dni: ")
            nuevo_nombre = input("Introduce tu nuevo nombre: ")
            nuevo_apellidos = input("Introduce tus nuevos apellidos: ")
            nuevo_n_tarjeta = input("Introduce tu nuevo numero de tarjeta del banco: ")

            abonados[abonados.index(abonado_actual)].dni = nuevo_dni
            abonados[abonados.index(abonado_actual)].nombre = nuevo_nombre
            abonados[abonados.index(abonado_actual)].apellidos = nuevo_apellidos
            abonados[abonados.index(abonado_actual)].n_tarjeta = nuevo_n_tarjeta

            parking.lista_plazas[
                parking.lista_plazas.index(plaza)
            ].abonado = abonados[abonados.index(abonado_actual)]

            parking_file = open("data/parking.pickle", "wb")
            pickle.dump(parking, parking_file)
            parking_file.close()

            abonados_file = open("data/abonado.pickle", "wb")
            pickle.dump(abonados, abonados_file)
            abonados_file.close()
        elif abonado_actual.dni == dni and op == '2':
            abonos_file = open("data/abono.pickle", "rb")
            abonos = pickle.load(abonos_file)

            tipo = input('Que tipo de renovacion quieres realizar? (mensual, trimestral, semestral o anual): ')
            if tipo == 'mensual':
                dias = 30
                precio = 25.0
            elif tipo == 'trimestral':
                dias = 90
                precio = 70.0
            elif tipo == 'semestral':
                dias = 180
                precio = 130.0
            elif tipo == 'anual':
                dias = 360
                precio = 200.0
            old_abonado = abonado_actual

            abonado_actual.abono.f_cancelacion += datetime.timedelta(days=dias)
            abonado_actual.abono.cobro = Cobro(precio)

            abonados[abonados.index(old_abonado)] = abonado_actual

            cobros_file = open("data/cobros.pickle", "rb")
            cobros = pickle.load(cobros_file)
            cobros.append(abonado_actual.abono.cobro)
            cobros_file = open("data/cobros.pickle", "wb")
            pickle.dump(cobros, cobros_file)
            cobros_file.close()

            abonos_file = open("data/abono.pickle", "wb")
            pickle.dump(abonos, abonos_file)
            abonos_file.close()

            abonados_file = open("data/abonado.pickle", "wb")
            pickle.dump(abonados, abonados_file)
            abonados_file.close()
            print('Operacion realizada con exito')
            print(abonado_actual.abono)
        else:
            print('Operacion o DNI erroneos')


    elif gestion == '3':
        dni = input("Introduce tu dni y se procedera a dar de baja: ")
        abonados_file = open("data/abonado.pickle", "rb")
        abonados = pickle.load(abonados_file)
        abonados_file.close()
        try:
            abonado_actual = next(abonado for abonado in abonados if dni == abonado.dni)
        except:
            print('Se ha detectado un error con el dni')
        if abonado_actual.dni == dni:
            plazas = [plaza for plaza in parking.lista_plazas if plaza.abonado is not None]
            plaza = next(plaza for plaza in plazas if plaza.abonado.dni == dni)

            parking.lista_plazas[
                parking.lista_plazas.index(plaza)
            ].abonado = None

            abonados.remove(abonado_actual)

            parking_file = open("data/parking.pickle", "wb")
            pickle.dump(parking, parking_file)
            parking_file.close()

            abonados_file = open("data/abonado.pickle", "wb")
            pickle.dump(abonados, abonados_file)
            abonados_file.close()

            print('Baja realizada con exito')
        else:
            print('El abonado con DNI aportado no existe')

