#Compara si 10 es mayor que 5 y muestra el resultado.

resultado_1 = 10 > 5
print("¿10 es mayor que 5?", resultado_1)

#Compara si 7 es menor que 3 y muestra el resultado.

resultado_2 = 7 < 3
print("¿7 es menor que 3?", resultado_2)

#Verifica si 8 es igual a 8 y muestra el resultado.

resultado_3 = 8 == 8
print("¿8 es igual a 8?", resultado_3) 

#Compara si 12 es diferente de 15 y muestra el resultado.

resultado_4 = 12 != 15
print("¿12 es diferente de 15?", resultado_4)

#Verifica si 20 es mayor o igual a 20.

resultado_5 = 20 >= 20
print("¿20 es mayor o igual a 20?", resultado_5)

#Verifica si 9 es menor o igual a 7.

resultado_6 = 9 <= 7
print("¿9 es menor o igual a 7?", resultado_6)

#Usa una variable para comparar dos números y mostrar el resultado.

a = 5
b = 8
resultado_7 = a < b
print(f"¿{a} es menor que {b}?", resultado_7)

#Comprueba si dos cadenas de texto son iguales.

cadena_1 = "jassary"
cadena_2 = "yazari"
resultado_8 = cadena_1 == cadena_2
print(f"¿'{cadena_1}' es igual a '{cadena_2}'?", resultado_8)

#mi nombre fue lo único que se me ocurrió para comparar XD

#Compara si "Python" es diferente de "JavaScript".

resultado_9 = "Python" != "JavaScript"
print("¿'Python' es diferente de 'JavaScript'?", resultado_9)

#Verifica si la longitud de una lista es mayor que 5.

lista = ["jassary","frances","heyling","sherry","rommel","isaac"]
resultado_10 = len(lista) > 5
print("¿La longitud de la lista es mayor que 5?", resultado_10) 

#(el resultado saldrá TRUE porque coloqué 6 nombres en la lista)


# 11. Compara dos números introducidos por el usuario.
#(aquí me viene lo hard 💀)


num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
resultado_11 = num1 == num2
print(f"¿{num1} es igual a {num2}?", resultado_11)

#(tuve que investigar para qué servía las funciones Int e Input
#porque se me había olvidado xd, ya le sé si 🤑


#Verifica si un número es par comparando con el módulo 2.


numero = 6
resultado_12 = numero % 2 == 0
print(f"¿{numero} es par?", resultado_12) 


#Usa 'is' para comparar si dos variables apuntan al mismo objeto.

x = "i love cookies"
y = x
resultado_13 = x is y
print(f"¿x e y apuntan al mismo objeto?", resultado_13)

#Verifica si una palabra está contenida en una frase con "in".

frase = "jiyong know as GD is the king of kpop"
palabra = "jiyong"
resultado_14 = palabra in frase
print(f"¿'{palabra}' está en la frase?", resultado_14)

#Compara si una variable booleana es True o False.

es_verdadero = True
resultado_15 = es_verdadero is True
print(f"¿es_verdadero es True?", resultado_15)