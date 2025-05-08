import random
# 1. Incrementar número hasta 50, mostrando múltiplos de 7 mayores a 20
n = 0
while n <= 50:
    if n > 20 and n % 7 == 0:
        print("Ejercicio 1:", n)
    n += 1

# 2. Pedir números hasta que el usuario ingrese uno >100 y divisible por 5
while True:
    num = int(input("Ejercicio 2 - Ingresa un número: "))
    if num > 100 and num % 5 == 0:
        print("Número válido:", num)
        break

# 3. Conteo regresivo desde 30, solo pares menores a 20
n = 30
while n >= 0:
    if n < 20 and n % 2 == 0:
        print("Ejercicio 3:", n)
    n -= 1

# 4. Sumar del 1 al 20, saltando los menores a 5 o mayores a 15
n = 1
suma = 0
while n <= 20:
    if 5 <= n <= 15:
        suma += n
    n += 1
print("Ejercicio 4 - Suma:", suma)

# 5. Pedir palabras y mostrar las que tienen >4 letras y contienen 'e'
while True:
    palabra = input("Ejercicio 5 - Escribe una palabra ('salir' para terminar): ")
    if palabra == "salir":
        break
    if len(palabra) > 4 and "e" in palabra:
        print("Palabra válida:", palabra)

# 6. Números aleatorios entre 1 y 100 hasta encontrar uno >50 y múltiplo de 10
while True:
    num = random.randint(1, 100)
    print("Ejercicio 6 - Número generado:", num)
    if num > 50 and num % 10 == 0:
        print("¡Número válido encontrado!")
        break

# 7. Intentos hasta adivinar número entre 1 y 10
secreto = random.randint(1, 10)
intentos = 0
while True:
    intento = int(input("Ejercicio 7 - Adivina el número (1-10): "))
    intentos += 1
    if intento == secreto:
        print(f"¡Correcto! Adivinaste en {intentos} intentos.")
        break

# 8. Añadir a lista hasta tener 5 pares mayores a 10
lista = []
while len(lista) < 5:
    num = int(input("Ejercicio 8 - Ingresa un número: "))
    if num % 2 == 0 and num > 10:
        lista.append(num)
print("Lista final:", lista)

# 9. Leer edades mientras estén entre 1 y 119
while True:
    edad = int(input("Ejercicio 9 - Ingresa una edad: "))
    if edad <= 0 or edad >= 120:
        print("Edad inválida. Fin del programa.")
        break
    print("Edad válida:", edad)

# 10. Simular cuenta bancaria
saldo = 500
while saldo >= 100:
    retiro = int(input(f"Ejercicio 10 - Saldo actual: {saldo}. ¿Cuánto deseas retirar?: "))
    if retiro <= saldo:
        saldo -= retiro
    else:
        print("No tienes suficiente saldo.")
print(f"Operaciones finalizadas. Saldo actual: {saldo}")
