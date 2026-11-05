# Bug 1:
#nombre = Ana
# Se ajusta para que sea un string
nombre = "Ana"

# Bug 2:
'''
edad = "25"
print(edad + 5)

se debe convertir edad a int o float
'''

# Bug 3:
'''
precio = 19.99
cantidad = "3"
total = precio * cantidad

cantidad se debe convertir primero antes de usarse
'''

# Bug 4:
'''
nombre = "Ana"
print("Hola " + nombre + ", tienes " + 25 + " años")

No se puede concatenar valores numericos como 25, se debe incluir entre comillas
'''

nombre = "Ana"
print("Hola " + nombre + ", tienes " + 25 + " años")