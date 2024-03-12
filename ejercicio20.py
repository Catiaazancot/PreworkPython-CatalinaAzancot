#Crea un programa que sume todos los números en una lista ingresada por el usuario

lista = int(input("Ingrese el numero final de la lista: "))
b = 0
for i in range(1, lista + 1):
  b = b + i

print("La suma es: ",b)