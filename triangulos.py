import os

isActive=True
while isActive:

 os.system("clear")

 print("bienvenido al generador de triangulo")
 try:

   n=int(input("ingrese la base del triangulo"))
   if n==0:
     isActive=0
     print("gracias por usar el progrma")

     for i in range(1, n+1):
       print("*"* i)
   elif n>1:
     for i in range(1,n,+1):
      print("*"*i)
      input("presiona ENTER para continuar...")
   
   else:
      print("no existe ningun triamgulo con base 1")
 except ValueError:
   print("debe ingresar un numero entreo")