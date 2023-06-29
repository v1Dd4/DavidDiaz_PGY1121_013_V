from funciones import registrar_auto,buscar_auto,impresion_certificados
import os 
import time as tm

menu = True

while menu:
    try:
        os.system('cls')
        print('BIENVENIDO A LA ASEGURADORA "AUTOSEGURO"')
        print('1)Registrar un auto')
        print('2)Buscar un auto por su patente')
        print('3)Imprimir certificados de emision de contaminantes, anotaciones vigente y multas')
        print('4)Salir')
        op = int(input('Ingrese el numero de su operacion\n'))
        if op < 5 and op > 0:
            if op == 1:
                os.system('cls')
                registrar_auto()
                tm.sleep(2)
            elif op == 2:
                os.system('cls')
                buscar_auto()
                tm.sleep(10)
            elif op == 3:
                os.system('cls')
                impresion_certificados()
                tm.sleep(15)
            else: 
                os.system('cls')
                print('ESO ES TOD- ESO ES TOD- ESO ES TODO AMIGOS!!! (DAVID EL INFORMATICO DIAZ)\nVERSION DEL PROGRAMA: V1.0')
                menu = False
                tm.sleep(5)
    except:
        print('ocurrio un error, ingrese una opcion valida')
        tm.sleep(2)