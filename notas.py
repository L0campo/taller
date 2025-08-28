import os

os.system("clear")

print("bienvenido al comparador para descubrir si apruebas")

nota=float(input("ingrese la primera nota"))
nota2=float(input("ingrese la segunda nota"))
nota3=float(input("ingrese la tercera nota"))
nota4=float(input("ingrese la cuarta nota"))
nota5=float(input("ingrese la quinta nota nota"))

promedio=(nota+nota2+nota3+nota4+nota5)/5

if promedio>=3.5:
    print(f"felicidades aprobaste con una nota de {promedio: .2f}")
else:
    print(F"lo siento reprobaste con una nota de {promedio: .2f}")