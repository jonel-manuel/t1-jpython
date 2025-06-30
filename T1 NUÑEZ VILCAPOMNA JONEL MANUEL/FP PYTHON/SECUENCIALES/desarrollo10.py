import os
os.system("cls")

numero = int(input("Ingrese un número de 4 cifras: "))

d1 = numero // 1000
d2 = (numero // 100) % 10
d3 = (numero // 10) % 10
d4 = numero % 10

invertido = d4 * 1000 + d3 * 100 + d2 * 10 + d1

print(f"El número invertido es: {invertido}")