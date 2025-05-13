#Diseña una clase de 'circulo' que tenga un atributo radio y metodos para calcular el area y el perimetro
import math 
class circulo:
    def __init__(self,radio):
        self.radio = radio
    def calcuar_area(self):
        return math.pi* (self.radio**2)
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
circulo1= circulo(5)
circulo2= circulo(20)
circulo3= circulo(30)

print('el area del circulo es',circulo1.calcuar_area(),
      'y el perimetro es de', circulo1.calcular_perimetro())
print('el area del circulo es',circulo2.calcuar_area(),
      'y el perimetro es de', circulo2.calcular_perimetro())
print('el area del circulo es',circulo3.calcuar_area(),
      'y el perimetro es de', circulo3.calcular_perimetro())