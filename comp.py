import os

os.system("clear")

print("bienvenido al comparador de numeros")


numero1=float(input("ingrese el primer numero: "))
numero2=float(input("ingrse el segundo numero: "))
numero3=float(input("ingrese el tercer numero: "))

if numero1>=numero2 and numero2 >= numero3:
    mayor=numero1
    print(f"el numero mayor de los tres es el: {mayor}")
elif numero1<=numero2 and numero2>= numero3:
    mayor2=numero2
    print(f"el numero mayor de los tres es el: {mayor2}")
elif numero1<=numero2 and numero2<= numero3:
    mayor3=numero3
    print(f"el numero mayor de los tres es el: {mayor3}")
else:
    print("opcion no valida")
     