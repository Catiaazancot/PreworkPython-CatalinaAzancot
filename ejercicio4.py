'''Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.'''

texto = input("Ingrese una palabra: ")
vocales = "aeiouAEIOU"
contador = 0
for letra in texto:
  if letra in vocales:
    contador = contador + 1 

print(f"Esta palabra tiene {contador} vocales")


  
