#Verifica si un número es positivo o negativo:

numero = -5
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
    
#Comprueba si una persona es mayor de edad:

edad = 20
if edad >= 18:
    print("La persona es mayor de edad")
else:
    print("La persona es menor de edad")

#Evalúa si un número es par o impar:

numero = 4
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

#Determina si una palabra tiene más de 5 letras:

palabra = "Python"
if len(palabra) > 5:
    print("La palabra tiene más de 5 letras")
else:
    print("La palabra tiene 5 o menos letras")
    
#Compara dos números y muestra cuál es mayor:

numero1 = 10
numero2 = 15
if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
elif numero1 < numero2:
    print(f"{numero2} es mayor que {numero1}")
else:
    print("Ambos números son iguales")
    
#Verifica si un usuario ha ingresado la contraseña correcta:

contraseña_correcta = "jass123"
contraseña_ingresada = input("Ingresa la contraseña: ")
if contraseña_ingresada == contraseña_correcta:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
    
#Evalúa si un número está dentro de un rango específico:

numero = 25
if 10 <= numero <= 30:
    print("El número está dentro del rango")
else:
    print("El número está fuera del rango")
    
#Determina si una cadena está vacía o tiene contenido:

cadena = ""
if cadena:
    print("La cadena tiene contenido")
else:
    print("La cadena está vacía")
    
#Usa elif para clasificar un número en rango bajo, medio o alto:

numero = 75
if numero < 30:
    print("El número es bajo")
elif 30 <= numero <= 70:
    print("El número es medio")
else:
    print("El número es alto")
    
#Evalúa si una persona puede entrar a un evento por su edad:

edad = 18
if edad >= 18:
    print("La persona puede entrar al evento")
else:
    print("La persona no puede entrar al evento")
    
#Determina si un año es bisiesto o no:

año = 2024
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"{año} es un año bisiesto")
else:
    print(f"{año} no es un año bisiesto")
    
#Evalúa si una lista tiene elementos antes de acceder a ellos:
    

lista = [1, 2, 3]
if lista:
    print("La lista tiene elementos")
else:
    print("La lista está vacía")
    
#Usa condicionales para verificar si un número es múltiplo de 3 y 5:

numero = 15
if numero % 3 == 0 and numero % 5 == 0:
    print("El número es múltiplo de 3 y 5")
else:
    print("El número no es múltiplo de 3 y 5")
    
#Crea un sistema de login con usuario y contraseña:

usuario_correcto = "sary_rantk"
contraseña_correcta = "jass123456"
usuario = input("Ingresa el usuario: ")
contraseña = input("Ingresa la contraseña: ")

if usuario == usuario_correcto and contraseña == contraseña_correcta:
    print("Acceso concedido")
else:
    print("Acceso denegado")
    
#Determina si una variable contiene un valor específico:

variable = "Hola"
if variable == "Hola":
    print("La variable contiene 'Hola'")
else:
    print("La variable no contiene 'Hola'")
    
#Evalúa si un estudiante aprobó o reprobó con base en su calificación:

calificacion = 7
if calificacion >= 6:
    print("El estudiante aprobó")
else:
    print("El estudiante reprobó")
    
#Verifica si una persona tiene acceso VIP o normal en un evento:

acceso_vip = True
if acceso_vip:
    print("Acceso VIP")
else:
    print("Acceso normal")
    
#Usa una variable booleana para decidir si mostrar un mensaje:

mostrar_mensaje = True
if mostrar_mensaje:
    print("Este es un mensaje")
else:
    print("No se muestra ningún mensaje")
    
#Evalúa si una letra ingresada es vocal o consonante:

letra = input("Ingresa una letra: ").lower()
if letra in 'aeiou':
    print(f"{letra} es una vocal")
else:
    print(f"{letra} es una consonante")
    
#Compara tres números y determina el mayor:

numero1 = 10
numero2 = 25
numero3 = 15
mayor = max(numero1, numero2, numero3)
print(f"El número mayor es {mayor}")