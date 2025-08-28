import os

isActive = True
while isActive:
    os.system("clear")
    print("Bienvenido al generador de triangulos")
    try:
        n = int(input("Ingrese la cantidad de la base del triangulo\nPresione 0 si desea salir: "))
        if n == 0:
            isActive = False
            print("Gracias por usar el programa")
        elif n > 1:
            for i in range(1, n+1):
                print("*"*i)
            input("Presione ENTER para continuar...")
        else:
            print("No existe un triangulo con base 1")
            input("Presione ENTER para continuar...")
    except ValueError:
        print("Debe ingresar un numero entero")
        input("Presione ENTER para continuar...")