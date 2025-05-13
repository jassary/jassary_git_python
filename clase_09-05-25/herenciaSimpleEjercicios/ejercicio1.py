#Ejercicios sencillos de herencia simple en python

#I- Ejercicios que heredan solo métodos

#1.Crea uns clase 'saludo' con un método que diga 'hola', luego crea una clase
#'saludo formal' que herede ese método.

class saludo:
    def saludar(self):
        print('hola a todos')
        
class saludo_formal(saludo):
    def __init__(self):
        super().__init__()
        
saludo = saludo_formal()
saludo.saludar()