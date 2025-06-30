
import os
os.system("cls")

#desarrolle un programa que determine el area y perimetro de un rectangulo sabiendo 
# Área = base × altura o A = b × h   y  2*(base+altura)

base=float(input("ingrese la base:"))
altura=float(input("ingrese la altura:"))

area=(base*altura)
perimetro=2*(base+altura)


print(f"area:",round(area,2))
print(f"perimetro: ",round(perimetro,2))

