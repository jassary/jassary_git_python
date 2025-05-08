class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo
        self.edad = edad      # atributo

    def saludar(self):        # método
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class animal:
    def __init__(self,nombre):
        self.nombre = nombre
        
    def ladrar(self): #metodo
        print(f'El {self.nombre} dice: guau!')
        
class gato:
    def __init__(self, nombre, color, tamaño, sexo):
        self.nombre = nombre
        self.color = color 
        self.tamaño = tamaño
        self.sexon = sexo
        
    def maullar(self):
        print(f'El gato {self.nombre} dice: miua!')
        