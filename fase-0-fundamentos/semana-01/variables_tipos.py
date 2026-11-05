# A.1 Variables y tipos básicos

nombre = "Ana"        # str
edad = 25             # int
altura = 1.68         # float
es_estudiante = True  # bool

# A.2 Operadores aritméticos

a, b = 17, 5
a + b   # 22
a - b   # 12
a * b   # 85
a / b   # 3.4   ← siempre devuelve float
a // b  # 3     ← división entera (descarta decimales)
a % b   # 2     ← resto
a ** b  # 1419857 (potencia)

# La distinción / vs // es la que más confunde al principio. / siempre da float, // da el cociente entero.
# A.3 Comparaciones (devuelven bool)

edad = 20
edad == 20   # True
edad != 20   # False
edad >= 18   # True
edad < 18    # False

# A.4 F-strings (la forma moderna de imprimir)

nombre = "Ana"
edad = 25
print(f"Me llamo {nombre} y tengo {edad} años")

# La f antes de las comillas permite meter variables entre { }. Es lo que usarás el 90% del tiempo.

# A.5 Conversión de tipos

int("42")      # 42
float("3.14")  # 3.14
str(123)       # "123"
int("5") + 3   # 8
"5" + 3        # TypeError ← no se puede sumar str + int

