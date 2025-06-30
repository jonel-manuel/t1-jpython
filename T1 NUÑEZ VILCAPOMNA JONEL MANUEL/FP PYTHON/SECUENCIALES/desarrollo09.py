


#desarrolle un  programa que lea un numero entero y determine la  suma de susu cifras .
# asumir que el numero es positivo y de  4 cifras

numero=int(input("ingrerse el numero entero positivo de 4 cifras: "))

if 1000 <= numero <= 9999:
    cifra1= numero// 1000
    cifra2= (numero %1000)// 100
    cifra3= (numero % 100)//10
    cifra4= numero % 10

suma=(cifra1+cifra2+cifra3+cifra4)

print(f"la suma de las cifras es :",(suma))
