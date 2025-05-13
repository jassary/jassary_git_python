#Herencia simple con atributos
#La herencia es un principio de la POO que permite que permite que una clase
#entre llamada clases derivada o subclase herede atributos y metodos de otra clase (llamada clase base, superclase o clase, padre)
#esto permite promueve la reutilizacion, de codigo organizacion jerarquia y extenicibilidad

#HERNCIA SIMPLE OCURRE CUANDO UNA SUBCLASE HEREDA DE UNA SUBCLASE

#EJEMPLO

class deporte:
    def __init__(self,nombre_deporte,horario,fecha_inicio):
        self.nombre_deporte = nombre_deporte
        self.horario = horario
        self.fecha_inicio = fecha_inicio
        
    def dificultad(self):
        if self.nombre_deporte == 'baseball':
            print(f'dificultad moderada')
        elif self.nombre_deporte == 'basketball':
            print('dificultad dificil')
            
class deportista(deporte):
    def __init__(self, nombre_deporte, horario, fecha_inicio,nombre_persona,edad):
        super().__init__(nombre_deporte, horario, fecha_inicio) 
        self.nombre_persona = nombre_persona
        self.edad = edad
        
persona1=deportista('baseball','yuki',23)
persona2=deportista('basketball','yoongi',30)
persona1.dificultad()
persona2.dificultad()