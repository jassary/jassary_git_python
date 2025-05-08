#Imprimir números del 1 al 50 solo si son múltiplos de 3 o de 5.

for i in range (1,51):
    if i % 3 == 0 or i % 5 == 0:
        print(i)