'''Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''
print("Introduce tu peso: ")
peso = float(input())
print("Introduce tu estatura: ")
estatura = float(input())

IMC = peso / estatura

print("Tu IMC es: ", IMC)