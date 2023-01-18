from models.Parking import Parking
from models.Ticket import Ticket

p = Parking(20)

salir = False

print(p)

while not salir:
    entradaZona = input('==================================================\n'
                    'Donde quieres acceder?:\n'
                    '1.Zona de Clientes\n'
                    '2.Zona de Administrador\n')
    if entradaZona == '1':
        print('Estas en zona de clientes')
    elif entradaZona == '2':
        print('Estas en zona de administrador')
    else:
        print("Saliste del sistema")
        salir = True