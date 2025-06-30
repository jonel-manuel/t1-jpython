# Desarrolle el programa que permita calcular la hipotenusa de un triángulo rectángulo
# usando la fórmula de Pitágoras: h = √(a² + b²)

import os
import math
os.system("cls")

cateto1 = float(input("Ingrese el valor del primer cateto: "))
cateto2 = float(input("Ingrese el valor del segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"La hipotenusa es: {hipotenusa:.2f}")