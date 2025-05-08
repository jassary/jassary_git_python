#8. Diseña una clase 'Libro' con atributos título, autor y año. 
# Agrega un método para mostrar la información del libro.

class libro:
    def __init__(self,titulo,autor,año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        
    def informacion_del_libro(self):
        print(f'El autor del libro {self.titulo} es {self.autor}, y se escribió en el año {self.año}')
        
libro1=libro('Maria','Jorge Isaac',1867)
libro2=libro('Don Quijote de la Mancha', 'Miguel de Cervantes',1605)
libro1.informacion_del_libro()
libro2.informacion_del_libro()