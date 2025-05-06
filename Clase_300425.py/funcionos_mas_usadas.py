#10 FUNCIONES PROPIAS MÁS USADAS EN PYTHON
#Una funcion propia (tambien llamada definida por el usuario) 
#es aquella que tu mismo creas usando la palabra reservada def nombre_de_la_funcion, estas funciones se diseñan para
#realizar tareas especificas según las necesidades del programa 

#EJEMPLO DE LA CLASE

def saludar():
    print('Hello, how are you guys?')
    saludar()

def saludo(nombre,genero):
    if genero == 'Masculino':
        adjetivo='papu'
    elif genero == 'Femenino':
        adjetivo='diva'
    else:
        adjetivo='Enfermo mental'
         
    print(f'Hello, my name is {nombre} im {genero} and you can call me {adjetivo}')
    
saludo('Jassary','Femenino')
saludo('Jassary','Maculino')
saludo('Jassary','F')

#Devuelva la suma de dos números
 
def suma_doble(num1,num2):
     return num1,num2 #Devuelve si el número es par
resultado=suma_doble(1,2)
print(resultado)
range(0,4)

def es_par(numero):
    return numero % 2 == 0