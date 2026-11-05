'''
Ejercicio 1 — Presentación
Crea tres variables: tu nombre, tu edad y tu altura en metros. Imprime con f-string:
Me llamo [nombre], tengo [edad] años y mido [altura] metros

Ejercicio 2 — Cálculo con impuesto
Dado precio = 19.99 y cantidad = 3, calcula el total con IVA del 21%. Imprime el resultado redondeado a 2 decimales con round(valor, 2).
Salida esperada: Total con IVA: 72.56

Ejercicio 3 — Los siete operadores
Dado a = 17 y b = 5, imprime cada operador con una etiqueta:

Ejercicio 4 — Comparaciones
Dado edad = 20, imprime tres booleanos en una sola línea (puedes usar print(cond1, cond2, cond3)):

¿Es mayor o igual a 18?

¿Es exactamente 20?

¿Es menor que 18?
Salida esperada: True True False

Ejercicio 5 — Conversión de tipos
Dado texto = "123":

Conviértelo a int, súmale 7 e imprime (debe dar 130).

Conviértelo a float, súmale 0.5 e imprime (debe dar 123.5).

Ejercicio 6 — Investigación (el más interesante)
Ejecuta estas tres líneas y observa:
'''

print("Ejercicio 1 — Presentación")
nombre = "fabian"
edad = 30
altura = 1.86
print(f"Me llamo {nombre}, tengo {edad} años y mido {altura} metros")

print("\nEjercicio 2 — Cálculo con impuesto")

precio = 19.99 
cantidad = 3
iva = precio * cantidad * 0.21
valor = precio * cantidad + iva
print(f"Total con IVA: {round(valor, 2)}")

print("\nEjercicio 3 — Los siete operadores")

a = 17 
b = 5

print(f"Suma: {a+b}")
print(f"Resta: {a-b}")
print(f"Multiplicación: {a*b}")
print(f"División: {a/b}")
print(f"División entera: {a//b}")
print(f"Módulo: {a%b}")
print(f"Potencia: {a**b}")

print("\nEjercicio 4 — Comparaciones")

edad = 20

print(edad >= 18, edad == 20, edad <= 18)

print("\nEjercicio 5 — Conversión de tipos")

texto = "123"

print(int(texto)+7)
print(float(texto)+0.5)

print("\nEjercicio 6 — Investigación (el más interesante)")

a = 0.1
b = 0.2
print(a + b)
print(a + b == 0.3)