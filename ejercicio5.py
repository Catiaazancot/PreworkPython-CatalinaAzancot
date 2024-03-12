'''Escribe un programa que calcule la suma de todos los números pares del 1 al 100.'''
i = 1
f = 100
suma = 0
while i <= f:
  if i % 2 == 0:
    print(i)
    suma = suma + i
  i+=1 
  
print("La suma de los números pares es: ", suma)


