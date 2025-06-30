

#desarrolle un programa que determine de un cilindro
# area base= pi*radio**2
# area lateral= 2*radio*altura
#area total= 2*area base*area lateral


radio=float(input("ingresar el radio: "))
altura=float(input("ingresar la altura: "))

areab=3.14159265359*(radio**2)
areal=2*3.14159265359*radio*altura
areat=2*areab*areal

print(f"area base: ",round(areab,2))
print(f"area lateral: ",round(areal,2))
print(f"area total: ",round(areat,2))
