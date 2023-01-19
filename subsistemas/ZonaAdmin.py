import pickle

from models.Parking import Parking


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
