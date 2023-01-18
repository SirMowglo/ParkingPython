from models.Ticket import Ticket



ticket = Ticket("1231-FCK", "A3", "123456")

entrada = input('==================================================\n'
      'Donde quieres acceder?:\n'
      '1.Zona de Clientes\n'
      '2.Zona de Administrador')

if entrada =='1':
    print('Estas en zona de clientes')
elif entrada == '2':
    print('Estas en zona de administrador')
else:
    print("Saliste del sistema")