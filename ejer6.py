#V7. Crea una clase 'Estudiante' que almacene el nombre, edad y promedio
#. Agrega un método que indique si el estudiante está aprobado (promedio >= 60).

class Estudiantes:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
        
    def aprobacion(self):
        if self.promedio >= 60:
            print('El estudiante está aprobado')
        else:
            print('El estudiante está reprobado')

est= Estudiantes
Estudiante1 = est('Jassary', 17, 90)
Estudiante1.aprobacion()


