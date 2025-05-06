#Mostrar los números entre 0 y 30 que sean divisibles entre 2 y entre 3
for i in range(0,31):
    if i % 2 == 0 and i % 3 == 0:
        print('El resultado es:', i)
