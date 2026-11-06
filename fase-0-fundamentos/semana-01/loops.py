# A.6 Tu primer for

# El for recorre una colección elemento por elemento. Es el equivalente a decir "para cada precio en la lista, haz algo".

precios = [19.99, 5.50, 12.00, 3.75]

for p in precios:
    print(p)

# Esto imprime los 4 precios en 4 líneas. La variable p toma el valor de cada elemento en cada vuelta, no el índice.

# A.7 Patrón acumulador (el más útil de todos)
# Para sumar, contar o calcular un promedio manualmente:

precios = [19.99, 5.50, 12.00, 3.75]
total = 0
for p in precios:
    total = total + p
print(total)   # 41.24

"""
El patrón es siempre el mismo:

Inicializas el acumulador antes del for.

Lo actualizas dentro del for.

Lo usas después del for.
"""

# A.8 for con condición (filtrar)
# Un if dentro del for te permite operar solo sobre algunos elementos:

precios = [19.99, 5.50, 12.00, 3.75]
caros = []
for p in precios:
    if p > 10:
        caros.append(p)
print(caros)   # [19.99, 12.00]

# El if hace que append solo se ejecute para los precios mayores a 10.

# EJERCICIOS

"""
Ejercicio 6 — Recorrer y multiplicar
Dado precios = [19.99, 5.50, 12.00, 3.75], recorre la lista e imprime cada precio con IVA del 21% redondeado a 2 decimales. 
Salida esperada (una línea por precio):

24.19
6.66
14.52
4.54

Ejercicio 7 — Suma manual
Reimplementa sum(precios) sin usar sum(), solo con un for y un acumulador. Al final imprime el total y verifica que coincide con sum(precios).

Ejercicio 8 — Contar
Dado notas = [7.5, 8.0, 6.3, 9.2, 5.8, 7.9, 8.5, 4.2], cuenta cuántas notas son mayores o iguales a 7. Imprime el resultado. Salida esperada: 5.

Ejercicio 9 — Filtrar
Con la misma lista de notas, construye una nueva lista solo con las notas aprobadas (≥ 5). Imprime la lista resultante y su promedio.

Ejercicio 10 — Máximo manual (reto)
Encuentra el valor máximo de notas sin usar max(), solo con un for y una variable que guarde el máximo provisional. Compara el resultado con max(notas) para verificar.

Pista conceptual: inicializa maximo = notas[0], y en cada iteración pregúntate si n > maximo. Si es así, actualiza.
"""
