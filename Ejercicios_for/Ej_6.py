#Mostrar los colores de una lista que empiezen con la letra 'b' y tengan más de 4 letras 
Colores=['Marrón', 'Rosa','Azul','Amarillo','Celeste','blanco']
for color in Colores:
    if color.startswith('b') and len(color) > 4:
        print('El resulatado es:', color)
        