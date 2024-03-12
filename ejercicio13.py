'''Escribe un programa que determine si un número ingresado por el usuario es primo
o no.'''

n = int(input("Ingrese un numero: "))
x = 1
f = 0
while x <= n:
  if n % x == 0:
    f = f + 1
  x = x + 1 
if f == 2: 
  print("El numero ",n," es primo")
else:
  print("El numero",n," no es primo")