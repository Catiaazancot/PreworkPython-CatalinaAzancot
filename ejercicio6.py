'''Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''

def palindromo(palabra):
  palabra = palabra.lower()
  a = 0
  b = len(palabra) -1 
  for i in palabra:
    if palabra[a] == palabra[b]:
      a += 1
      b -= 1
    else: 
      return False
  return True

palabra = input("Ingrese una palabra: ")
print(palindromo(palabra))

if palindromo(palabra):
  print("Esta es una palabra palindroma")
else:
  print("Esta no es una palabra palindroma")
