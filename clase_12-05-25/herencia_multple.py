#hereda los atributos de una clase

class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        
    def persona_presentar(self):
        print(f'hola, me llamo {self.nombre} y tengo {self.edad} años y soy {self.pais}')
        
class Empleados:
    def __init__(self, cargo,horario, salario):
        self.cargo = cargo
        self.horario = horario
        self.salario = salario
        
    def empleado_presentar(self):
        print(f'Mi cargo es: {self.cargo} y mi horaio es de: {self.horario}')
        
class Jefe(Persona,Empleados):
    def __init__(self, nombre, edad, pais,cargo,horario,salario,empresa,deporte_fav,comida_fav):
        Persona.__init__(self,nombre,edad,pais)
        Empleados.__init__(self,cargo,horario,salario)
        self.empresa = empresa
        self.deporte_fav = deporte_fav
        self.comida_fav = comida_fav
        
    def presentar_jefe(self):
        print(f'''
              Soy el jefe de la emprese {self.empresa}, mi
            comida fav es {self.comida_fav}, mi deporte favorito es 
            {self.deporte_fav}''')
        
jefe1=Jefe('Jassary',25,'Nicaragua','jefa','7:00am - 4:00pm',400000, 'Ebay','voleyball','sushi')
jefe1.empleado_presentar()
jefe1.presentar_jefe()