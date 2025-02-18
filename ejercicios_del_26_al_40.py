import math
import random

#Suma dos números y muestra el resultado.

suma = 10 + 20
print("Suma:", suma)

#Resta dos números y muestra el resultado.

resta = 30 - 20
print("Resta:", resta)

#Multiplica dos números y muestra el resultado.

multiplicacion = 80 * 40
print("Multiplicación:", multiplicacion)

#Divide dos números y muestra el resultado.

division = 30 / 3
print("División:", division)

#Calcula el módulo de una división y muéstralo.

modulo = 20 % 3
print("el módulo es:", modulo)

#Calcula el exponente de un número elevado a otro.

exponente = 2 ** 3
print("El exponte es:", exponente)

#Suma tres números y muestra el resultado.

suma_tres = 10 + 5 + 3
print("el resultado es:", suma_tres)

#Calcula el promedio de tres números.

promedio = (10 + 5 + 3) / 3
print("el proemdio es proemdio es:", promedio)

#Convierte un número negativo a positivo usando abs().

numero_negativo = -5
numero_positivo = abs(numero_negativo)
print("Número positivo:", numero_positivo)

#Realiza una operación combinada de suma, resta y multiplicación.

operacion_combinada = (10 + 5) - (3 * 2)
print("Operación combinada:", operacion_combinada)

#Muestra el resultado de dividir dos números y redondearlo con round().

division_redondeada = round(10 / 3, 2)
print("División redondeada:", division_redondeada)

#Usa floor() para redondear un número hacia abajo.

numero_decimal = 10.75
redondeo_abajo =math.floor(numero_decimal)
print("Redondeo hacia abajo:", redondeo_abajo)

#Usa ceil() para redondear un número hacia arriba.

numero_decimal2=9.70
redondeo_arriba = math.ceil(numero_decimal2)
print("Redondeo hacia arriba:", redondeo_arriba)

#Calcula la raíz cuadrada de un número con math.sqrt().

raiz_cuadrada =math.sqrt(16)
print("Raíz cuadrada:", raiz_cuadrada)

#Genera un número aleatorio entre 1 y 100 con random.randint().
numero_aleatorio = random.randint(1, 100)
print("Número aleatorio:", numero_aleatorio)