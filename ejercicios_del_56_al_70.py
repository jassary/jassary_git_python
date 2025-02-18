#Concatena dos cadenas usando el operador +

cadena1 = "Jassary Del Carmen"
cadena2 = "Espinoza Amador"
resultado = cadena1 + " " + cadena2
print(resultado)

#Concatena tres cadenas en una sola variable

primer_cadena = "hola a todos"
segunda_cadena = "mi nombre es"
tercera_cadena = "jassary espinoza amador"
resultado = primer_cadena + " " + segunda_cadena + " " + tercera_cadena
print(resultado)

#Une una cadena y un número convirtiéndolo a string

texto = "Tengo"
numero = 18
edad1= "años de edad"
resultado = texto + " " + str(numero) + "edad1"
print(resultado)

#Concatena una cadena y una variable usando f-strings

mensaje1 = "a todo el público presente"
mensaje = f"Hola, {mensaje1}"
print(mensaje)

#Une dos cadenas con el método join()

cadena3 = "kwon"
cadena4 = "jiyong"
resultado = " ".join([cadena3, cadena4])
print(resultado)

#Concatena elementos de una lista en una sola cadena

lista = ["uno", "dos", "tres"]
resultado = "".join(lista)
print(resultado)

#Muestra el resultado de una suma dentro de una cadena usando f-strings

a = 3
b = 4
resultado = f"La suma de {a} y {b} es {a + b}"
print(resultado)

#Concatena dos cadenas separadas por un espacio

cadena5 = "jung"
cadena6 = "hoseok"
resultado = cadena5 + " " + cadena6
print(resultado)

#Usa format() para unir una cadena con variables

nombre = "Jassary"
edad = 25
mensaje = "Mi nombre es {} y tengo {} años.".format(nombre, edad)
print(mensaje)

#Concatena una cadena varias veces con el operador *

cadena = "taehyung"
resultado = cadena * 3
print(resultado)

#Une elementos de una lista con comas entre ellos

lista = ["rhode", "rare beauty", "fenty beauty"]
resultado = ", ".join(lista)
print(resultado)

#Concatena nombre y apellido en una sola variable

nombre = "Jassary del Carmen"
apellido = "Espinoza Amador"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

#Usa una variable para almacenar una oración y modificarla con +=

oracion = "hello"
oracion += " world"
print(oracion)

#Usa f-strings para mostrar nombre y edad en un mensaje

nombre = "kwon jiyong"
edad = 36
mensaje = f"el nombre real de GD es {nombre} y tiene {edad} años de edad."
print(mensaje)

#Concatena dos frases ingresadas por el usuario

frase1 = input("Ingresa la primera frase: ")
frase2 = input("Ingresa la segunda frase: ")
resultado = frase1 + " " + frase2
print(resultado)