#Recorrer una lista de precios e imprimir los que sean menores a 100 y mayores a 50
Precios=[230,450,20,50,90,15,40]
for precio in Precios:
    if precio > 50 and precio < 100:
        print('El resultado es:', precio)
        