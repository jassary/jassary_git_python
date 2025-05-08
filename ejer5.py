#5. Implementa una clase 'Rectángulo' con atributos base y altura, y métodos para calcular el área y el perímetro.

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

rec = Rectangulo(20, 30)
print('El área del rectángulo es de:', rec.calcular_area(), 'cm²')
print('El perímetro del rectángulo es de:', rec.calcular_perimetro(), 'cm')
