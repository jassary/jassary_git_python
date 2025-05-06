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
        print(f'{self.nombre} dice: guau!')
        
