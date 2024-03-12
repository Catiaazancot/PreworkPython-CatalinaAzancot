''' Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''

precio_sin_propina = float(input("Precio sin propina: "))
propina = precio_sin_propina * 0.15 
precio_total = precio_sin_propina + propina

print("Propina : ", propina)
print("Precio total: ", precio_total)