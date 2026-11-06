Bloque C — Debug deliberado (15 min)
Crea debug_listas.py con estos bloques rotos. Cada uno tiene un error típico. Ejecútalos, lee el error, corrígelos y anota en un comentario la causa.

Bug 1:

precios = [10, 20, 30]
print(precios[3])

Bug 2:

precios = [10, 20, 30]
precios.sort()
resultado = precios.sort()
print(resultado)

Bug 3:

precios = [10, 20, 30]
for i in range(len(precios)):
    print(precios)

Bug 4:

precios = [10, 20, 30]
for p in precios:
    if p > 15:
        precios.remove(p)
print(precios)


