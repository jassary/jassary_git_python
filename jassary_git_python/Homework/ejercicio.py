#se necesita un programa que me muestre un mensaje, segun el rango de calificaciones
#0-59 (aplazado), 60-69 (regular),  70-79 (bueno), 80-89 (muy bueno), 90-100 (excelente)

calificacion= int(input("ingrese su caificacion: "))
if calificacion<=50:
    print('El estudiante está reprobado')
elif calificacion<=69:
    print('el estudiante tiene una nota regular')
elif calificacion<=79:
    print('el estudiante tiene una nota buena')
elif calificacion<=89:
    print('el estudiante tiene una nota muy buena')
elif calificacion>=90:
    print('el estudiante tiene una nota excelnete')