'''Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.'''

edad = int(input("Introduce tu edad: "))
x = edad 
if x > 18:
  print("Este usuario es mayor de edad")
else:
  print("Este usuario es menor de edad")