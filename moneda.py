import os



menuinicio=(""""bienvenido al conversor de monedas elija la opcion que desea:
\n1. COP → USD
\n2. USD → JPY
\n3. JPY → COP
\n4. salir""")





isActive=True

while isActive:
    os.system ("clear")
    print(menuinicio)
    opcion=int(input("\n seleciones una opcion 1-4: "))

    if opcion==1:
        print("convercion de COP → USD")
        cop=float(input("ingrese el monto que desea convertir: "))
        USD=(cop/4032.70)
        print(f"la convercion es de: {USD}USD")
        input("presiona ENTER para continuar...")
    
    elif opcion==2:
        print("convercion de USD → JPY")
        USD2=float(input("ingrese el monto que desea convertir: "))
        JPY=(USD2*146.97)
        print(f"la convercion es de: {JPY}JPY")
        input("presiona ENTER para continuar...")
    
    elif opcion==3:
        print("convercion de JPY → COP")
        JPY2=float(input("ingrese el monto que desea convertir: "))
        COP2=(JPY2*0.037)
        input("presiona ENTER para continuar...")

    elif opcion==4:
        print("saliendo")
        input("presiona ENTER para continuar...")
        isActive=False

    else: 
        print("opcion no valida")