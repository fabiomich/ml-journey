# A.1 Crear listas

# Una lista es una colección ordenada y mutable. Ordenada = cada elemento tiene una posición fija. Mutable = puedes cambiar, añadir o quitar elementos después de crearla.

precios = [19.99, 5.50, 12.00, 3.75]
nombres = ["Ana", "Luis", "María"]
mixta = [1, "dos", 3.0, True]   # Python lo permite, pero no abuses
vacia = []

# A.2 Acceso por índice (indexación)

# El primer elemento está en la posición 0, no en la 1. Es la fuente número uno de errores al principio.

precios = [19.99, 5.50, 12.00, 3.75]
precios[0]    # 19.99
precios[1]    # 5.50
precios[-1]   # 3.75   ← índice negativo = desde el final
precios[-2]   # 12.00

# A.3 Slicing (rebanadas)
# lista[inicio:fin:paso] — el fin no se incluye.

precios = [19.99, 5.50, 12.00, 3.75, 8.20]
precios[1:3]    # [5.50, 12.00]       ← posiciones 1 y 2
precios[:2]     # [19.99, 5.50]       ← desde el inicio hasta posición 2
precios[3:]     # [3.75, 8.20]        ← desde posición 3 hasta el final
precios[::2]    # [19.99, 12.00, 8.20] ← uno sí, uno no
precios[::-1]   # [8.20, 3.75, 12.00, 5.50, 19.99] ← al revés

# A.4 Las operaciones que más vas a usar

precios = [19.99, 5.50, 12.00, 3.75]

len(precios)         # 4        ← cuántos elementos
sum(precios)         # 41.24    ← suma
min(precios)         # 3.75     ← mínimo
max(precios)         # 19.99    ← máximo
3.75 in precios      # True     ← ¿está?
100 in precios       # False

# A.5 Métodos que modifican la lista

precios = [19.99, 5.50, 12.00]

precios.append(3.75)          # añade al final → [19.99, 5.50, 12.00, 3.75]
precios.remove(5.50)          # elimina la primera ocurrencia → [19.99, 12.00, 3.75]
precios.sort()                # ordena asc → [3.75, 12.00, 19.99]
precios.sort(reverse=True)    # ordena desc → [19.99, 12.00, 3.75]
precios.reverse()             # invierte el orden actual

# Trampa importante: sort() modifica la lista y devuelve None. Si haces x = precios.sort() obtendrás x = None. La forma correcta es precios.sort() y usar precios después.


# EJERCICIOS

"""Ejercicio 1 — Crear y acceder
Crea una lista con 5 ciudades. Imprime:

La primera.

La última (con índice negativo).

La del medio (índice 2).

Ejercicio 2 — Slicing
Con la misma lista del ejercicio 1, imprime:

Las dos primeras.

Las dos últimas.

Las tres del medio.

La lista al revés.

Ejercicio 3 — Estadísticas básicas
Dado notas = [7.5, 8.0, 6.3, 9.2, 5.8, 7.9], imprime:

La cantidad de notas (usa len).

La nota más alta (max).

La nota más baja (min).

La suma (sum).

El promedio (sum(notas) / len(notas) redondeado a 2 decimales).

Ejercicio 4 — Modificar
Empieza con frutas = ["manzana", "plátano"] y:

Añade "naranja" al final.

Añade "uva" al final.

Elimina "plátano".

Ordena alfabéticamente.

Imprime la lista en cada paso para ver qué pasa.

Ejercicio 5 — Pertenencia
Dado inventario = ["teclado", "ratón", "monitor", "cable"], comprueba con in si "monitor" está y si "impresora" está. Imprime ambas respuestas."""

