'''Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.'''

lista = int(input("Introduce el numero final de la lista: "))
par = 0 
impar = 0
for i in range(0, lista + 1):
  if i % 2 == 0:
    par += 1
  else: 
    impar += 1
    
print("El numero total de pares son: ", par)
print("El numero total de impares son: ", impar)