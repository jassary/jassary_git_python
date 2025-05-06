#Recorrer una lista que tengan más de 5 letras y contengan la letra 'a'

Nombres=['Ana','Jassary','Frances','Jiyong']
for nombre in Nombres:
    if len(nombre) > 5 and 'a' in nombre.lower():
        print(nombre)
        
