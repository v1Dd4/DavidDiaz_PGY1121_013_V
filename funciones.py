import os
import time as tm
import random

##Tipo, patente, marca y precio, multas (monto y fecha), fecha de registro del vehículo y nombre del dueño.


lista_autos = []
infraccines = ['EXCESO DE VELOCIDAD EN CARRETERA','PASO DE SEMAFORO EN ROJO','PASO DE DISCO PARE']

def registrar_auto():
    tipo = input('ingrese el tipo de vehiculo (automovil, van, etc)\n')
    patente = input('ingrese patente del auto (considere poner los caracteres sin espacios)\n')
    while not check_patente(patente):
        print('patente ingresada no valida, ingrese una patente valida')
        patente = input('ingrese patente del auto\n')
    marca = input('ingrese la marca del auto\n')
    while not check_marca(marca):
        print('La marca excede el numero de caracteres, ingrese una patente valida\n')
        marca = input('ingrese la marca del auto\n')
    precio = int(input('ingrese el precio del auto: $'))
    while not check_precio(precio):
        print('El precio del auto debe ser mayor a $5000000')
        precio = int(input('ingrese el precio del auto: $'))
    precio = f'${precio}'
    posmul = input('¿El auto posee multas?\n1)SI\n2)NO\n')
    if posmul == '1':
        monto_mul = input('Ingrese el monto de su multa $')
        fecha_mul = input('ingrese la fecha en que fue multado (DD/MM/AAAA)\n(CONSIDERE NO PONER SLASHS)\n')
        posmul = [f'MONTO: ${monto_mul}',f'FECHA MULTA: {fecha_mul[:2]}/{fecha_mul[2:4]}/{fecha_mul[4:]}']
    elif posmul == '2':
        posmul = 'NO POSEE MULTAS'
    else:
        print('opcion invalida vuelva a intentar')
    fecha_registro = input('ingrese fecha de registro (DD/MM/AAAA)\n(CONSIDERE NO PONER SLASHS)\n')
    nombre_dueño = input('ingrese el nombre del dueño del auto\n')
    rut = f'{random.randint(20,33)}.{random.randint(133,981)}.{random.randint(133,981)}-{random.randint(0,9)}'
    auto = [tipo,patente,marca,precio,posmul,f'{fecha_registro[:2]}/{fecha_registro[2:4]}/{fecha_registro[4:]}',nombre_dueño,rut]
    lista_autos.append(auto)

def check_patente(patente):
    if len(patente) == 6:
        return True
    else:
        return False

def check_marca(marca):
    if len(marca) > 15 or len(marca) < 2:
        return False
    else:
        return True

def check_precio(precio):
    if precio < 5000000:
        return False
    else:
        return True

def buscar_auto():
    os.system('cls')
    buscador = input('Ingrese la patente del auto a buscar (considere poner los caracteres sin espacio)\n')
    for i in range(len(lista_autos)):
        if lista_autos[i][1] == buscador:
            print('PATENTE BUSCADA:',lista_autos[i][1])
            print('TIPO AUTO:',lista_autos[i][0])
            print('MARCA AUTO:',lista_autos[i][2])
            print('PRECIO:',lista_autos[i][3])
            print('MULTAS:',lista_autos[i][4])
            print('FECHA REGISTRO:',lista_autos[i][5])
            print('NOMBRE DEL DUEÑO:',lista_autos[i][6])
        else:
            print('patente no encontrada')
            tm.sleep(2)

def impresion_certificados():
    os.system('cls')
    buscador = input('Ingrese la patente del auto a buscar para imprimir\nlos certificados (considere poner los caracteres sin espacio)\n')
    for i in range(len(lista_autos)):
        if lista_autos[i][1] == buscador:
            os.system('cls')
            print('------------------------------------------------------------')
            print('Certificado de emisiones\n')
            print(f'FECHA REVISION:{random.randint(1,31)}/{random.randint(0,12)}/{random.randint(2000,2023)}')
            print(f'Patente:{lista_autos[i][1]}')
            print(f'Nombre del dueño:{lista_autos[i][6]}')
            print('------------------------------------------------------------')
            print('Certificado de anotaciones vigentes\n')
            print('PATENTE BUSCADA:',lista_autos[i][1])
            print('TIPO AUTO:',lista_autos[i][0])
            print('MARCA AUTO:',lista_autos[i][2])
            print(F'NUMERO DE POLIZA:{random.randint(199999,999999)}')
            print(f'FECHA VENCIMIENTO POLIZA:{random.randint(1,31)}/{random.randint(0,12)}/{random.randint(2023,2030)}')
            print('----DATOS DEL PROPETARIO----')
            print('NOMBRE DEL DUEÑO:',lista_autos[i][6])
            print(f'RUT DEL DUEÑO:{lista_autos[i][7]}')
            print('------------------------------------------------------------')
            print('Certificado registro de multas de transito\n')
            if lista_autos[i][4] == 'NO POSEE MULTAS':
                print(f'EL AUTO DE PATENTE {lista_autos[i][1]} NO POSEE MULTAS')
                print('------------------------------------------------------------')
            else:
                print(f'ID MULTA: {random.randint(1000,3400)}')
                print(f'INFRACCION:{infraccines[random.randint(0,2)]}')
                print(f'{lista_autos[i][4]}')
                print('TIPO MONEDA DE MULTA: CLP')
                print('----DATOS DEL PROPIETARIO----')
                print(f'NOMBRE DEL DUEÑO:{lista_autos[i][6]}')
                print(F'RUT DEL DUEÑO:{lista_autos[i][7]}')
                print('------------------------------------------------------------')
                print(f'Valor impresion de certificados:${random.randint(1500,3500)}')
                
        elif not lista_autos[i][1] == buscador:
            print('buscando')
            tm.sleep(2)
        else:
            print('patente no encontrada')
            tm.sleep(2)

