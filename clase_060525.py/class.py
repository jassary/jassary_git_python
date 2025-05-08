marca_laptop1= 'toshiba'
pantalla_laptop1= '14'
procesador_laptop1= 'i5'
memoria_laptop= '8 gb'
marca_laptop2= 'Dell'
pantalla_laptop2= '15'
procesador_laptop2= 'i7'
memoria_laptop2= '32 gb'
print(marca_laptop1, pantalla_laptop1) #las variables no estan asociados, no tiene una logica correcto
 #es por eso que se programa de esta manera, todos los lenguaes utilizan este tipo de paradigma
 
class laptop(): #Por lo general no se usan los '():'
    marca='toshiba'
    pantalla='14' 
    disco='250 gb'
    memoria='8 gb'
    color='rojo' #este tipo de atributo se llama estaticos porque definimos esos valores
                 #ahorita esatamos creando un molde de laptops 

laptop_1 = laptop()
laptop_2 = laptop()

laptop_1.marca='hp'
laptop_2.marca='Lenovo'

print(laptop_1.marca)
print(laptop_2.marca)
print(laptop_1.marca) #esta manera no es correcta

#atributos instanciados basicamente es que nosotros tenemos la capacidad de cambiar los datos de los atributos
#primero definimos la clase de objeto.

class laptop:
    def __init__(self,marca,pantalla,procesador, disco, memoria):
        self.marca = marca
        self.pantalla = pantalla
        self.procesador = procesador
        self.disco = disco
        self.memoria = memoria
    def presentar(self):
        print(f'La marca es {self.marca} y es una gran marca')
        
    def descuento(self):
        print(f'Esta marca tiene un descuento del 15% por ser procesador {self.procesador}')
           
laptop1=laptop('hp','14','i5','250 gb', '8gb')
laptop2=laptop('Lenovo','15','i9','32','500 gb')
print(laptop1.marca,laptop1.pantalla)
laptop1.presentar()
laptop2.presentar()