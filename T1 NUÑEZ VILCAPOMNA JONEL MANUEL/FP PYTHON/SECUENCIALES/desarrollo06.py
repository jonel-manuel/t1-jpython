
import os
os.system("cls")
radio=float(input(" ingrersar el radio del cilindro: "))
altura=float(input("ingresar la altura del cilindro: "))

area=2*3.14159265359*radio*(radio+altura)
volumen=3.14159265359*(radio**2*altura)

print("area total del cilindro: ",area)
print("volumen del cilindro :",volumen)

print(f"area total del cilindro: ",round(area,2))
print(f"volumen del cilindro:",round(volumen,2))
