#EJERCICIOS DE PROGRAMACION EN CLASES Y METODOS 

#1 Crear una clase llamada 'persona' con los atributos nombre y edad. Agrega un método
#que imprima un saludo con el nombre.

class persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f'Hola a todos mi nombre es {self.nombre} y tengo la edad de {self.edad} años')
        
persona1= persona('Jassary',17)
persona2= persona('Kwon Jiyong',36)
persona1.saludar()
persona2.saludar()