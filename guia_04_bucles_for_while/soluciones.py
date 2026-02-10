# ============================================================================
# GUIA 4 - SOLUCIONES: BUCLES - FOR Y WHILE
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 2 y 3
# Enriquecido con: MIT 6.0001 (OCW), Harvard CS50P
# ============================================================================


# ---------------------------------------------------------------------------
# EJERCICIO 1: For con lista y multiplicacion
# ---------------------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1: For con multiplicacion")
print("=" * 50)

multiplicador = 3
numeros = [1, 5, 10, 15, 20]

for numero in numeros:
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")

# FOR recorre cada elemento de la lista uno a uno
# En cada vuelta, "numero" toma el siguiente valor de la lista
# Vuelta 1: numero = 1
# Vuelta 2: numero = 5
# Vuelta 3: numero = 10
# ...


# ---------------------------------------------------------------------------
# EJERCICIO 2: Range con numeros negativos
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2: Range negativos")
print("=" * 50)

for i in range(-10, 0):
    print(i)

# range(inicio, fin) -> genera numeros desde inicio hasta fin-1
# range(-10, 0) genera: -10, -9, -8, ..., -2, -1
# El 0 NO se incluye (como siempre en range)

# Tambien funciona: range(-10, 0, 1) donde 1 es el paso
# range(inicio, fin, paso):
# range(0, 10, 2)   -> 0, 2, 4, 6, 8
# range(10, 0, -1)  -> 10, 9, 8, ..., 1
# range(10, 0, -2)  -> 10, 8, 6, 4, 2


# ---------------------------------------------------------------------------
# EJERCICIO 3: Divisibles por 5 y por 7
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 3: Divisibles por 5 y por 7")
print("=" * 50)

for i in range(150, 351):
    if i % 5 == 0 and i % 7 == 0:
        print(i)

# % (modulo) da el resto de la division
# Si el resto es 0, el numero es divisible
# 150 % 5 = 0 (divisible), 150 % 7 = 3 (NO divisible)
# 175 % 5 = 0 Y 175 % 7 = 0 -> SI es divisible por ambos
# Resultado: 175, 210, 245, 280, 315, 350


# ---------------------------------------------------------------------------
# EJERCICIO 4: Piramide invertida
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 4: Piramide invertida")
print("=" * 50)

for fila in range(5, 0, -1):           # fila = 5, 4, 3, 2, 1
    for numero in range(fila, 0, -1):   # numeros desde fila hasta 1
        print(numero, end=" ")          # end=" " imprime sin salto de linea
    print()                             # salto de linea al final de cada fila

# Desglose:
# fila=5: range(5,0,-1) -> 5 4 3 2 1
# fila=4: range(4,0,-1) -> 4 3 2 1
# fila=3: range(3,0,-1) -> 3 2 1
# fila=2: range(2,0,-1) -> 2 1
# fila=1: range(1,0,-1) -> 1

# print(x, end=" ") -> imprime sin saltar de linea (agrega espacio)
# print()            -> salta de linea (linea vacia)


# ---------------------------------------------------------------------------
# EJERCICIO 5: Contar numeros "especiales"
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 5: Numeros especiales")
print("=" * 50)

lista = [3, 7, 13, 15, 23, 30, 33, 40, 50]
contador = 0

for num in lista:
    # Condicion 1: multiplo de 3
    es_multiplo_3 = num % 3 == 0
    # Condicion 2: contiene el digito '3'
    contiene_3 = "3" in str(num)

    if es_multiplo_3 or contiene_3:
        print(f"  {num} es especial (multiplo3={es_multiplo_3}, "
              f"contiene3={contiene_3})")
        contador += 1

print(f"Total numeros especiales: {contador}")

# str(num) convierte el numero a string para poder buscar caracteres
# str(13) = "13", y "3" in "13" es True


# ---------------------------------------------------------------------------
# EJERCICIO 6: Cuenta atras con "Pum!"
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 6: Cuenta atras")
print("=" * 50)

n = 20
for i in range(n, -1, -1):
    if i == 0:
        print("Despegue!")
    elif i % 4 == 0:
        print("Pum!")
    else:
        print(i)

# range(20, -1, -1) genera: 20, 19, 18, ..., 1, 0
# -1 como fin porque queremos incluir el 0
# -1 como paso para ir hacia atras


# ---------------------------------------------------------------------------
# EJERCICIO 7: Contar tipos de caracteres
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 7: Contar caracteres")
print("=" * 50)

texto = "Ole Python como mola! Me esta encantando. De verdad que SI"
mayusculas = 0
minusculas = 0
digitos = 0

for caracter in texto:
    if caracter.isupper():
        mayusculas += 1
    elif caracter.islower():
        minusculas += 1
    elif caracter.isdigit():
        digitos += 1
    # Los espacios y signos no entran en ninguna categoria

print(f"Mayusculas: {mayusculas}")
print(f"Minusculas: {minusculas}")
print(f"Digitos: {digitos}")

# METODOS DE CARACTER:
# .isupper()  -> True si es mayuscula
# .islower()  -> True si es minuscula
# .isdigit()  -> True si es digito (0-9)
# .isalpha()  -> True si es letra (mayus o minus)
# .isspace()  -> True si es espacio


# ---------------------------------------------------------------------------
# EJERCICIO 8: Enumerate
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 8: Enumerate")
print("=" * 50)

frase = "Python es divertido"

# FORMA 1: con range(len())
print("--- Con range(len()) ---")
for i in range(len(frase)):
    print(f"Indice: {i}, Letra: {frase[i]}")
    if frase[i] == " ":
        print("  Espacio encontrado!")

# FORMA 2: con enumerate() - MAS PYTHONICA (recomendada)
print("\n--- Con enumerate() ---")
for indice, letra in enumerate(frase):
    print(f"Indice: {indice}, Letra: {letra}")
    if letra == " ":
        print("  Espacio encontrado!")

# enumerate() devuelve pares (indice, valor) automaticamente
# Es mas limpio que usar range(len(...))
# Siempre que necesites el indice Y el valor, usa enumerate()


# ---------------------------------------------------------------------------
# EJERCICIO 9: While - suma acumulada
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 9: Suma acumulada con while")
print("=" * 50)

numeros = [15, 20, 8, 35, 12, 25, 30]
total = 0
i = 0  # indice que controlamos manualmente

while i < len(numeros) and total <= 100:
    total += numeros[i]
    print(f"Sumando {numeros[i]} -> Total: {total}")
    if total > 100:
        print("Limite superado!")
        break  # sale del while inmediatamente
    i += 1

# WHILE vs FOR:
# FOR: cuando sabes cuantas vueltas dar (recorrer lista, range)
# WHILE: cuando no sabes cuantas vueltas, depende de una condicion
#
# while condicion:
#     codigo
#     actualizar_algo  (si no, bucle infinito!)
#
# CUIDADO: si la condicion nunca se hace False, el bucle es infinito!
# Siempre asegurate de que algo cambie para que el while termine


# ---------------------------------------------------------------------------
# EJERCICIO 10: Break y Continue
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 10: Break y Continue")
print("=" * 50)

lista = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for num in lista:
    if num > 150:
        print(f"  {num} > 150, deteniendo bucle!")
        break       # sale del bucle completamente
    if num % 5 != 0:
        continue    # si NO es divisible por 5, salta al siguiente
    print(f"  {num} es divisible por 5")

# BREAK: sale del bucle inmediatamente
# CONTINUE: salta al siguiente paso (no ejecuta el resto del bloque)
#
# Ejemplo de continue:
# for i in range(5):
#     if i == 2:
#         continue  # salta el 2
#     print(i)
# Salida: 0, 1, 3, 4 (se salta el 2)


# ---------------------------------------------------------------------------
# EJERCICIO 11: Input y round
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 11: Redondeo (ejemplo sin input)")
print("=" * 50)

# Version sin input (para que se pueda ejecutar el archivo)
precio = 12.98765
decimales = 2
print(f"El precio redondeado es: {round(precio, decimales)}")

# round(numero, decimales) redondea al numero de decimales indicado
# round(12.98765, 2)  -> 12.99
# round(12.98765, 0)  -> 13.0
# round(12.98765, 4)  -> 12.9877

# La version interactiva seria:
# precio = float(input("Introduce un precio: "))
# decimales = int(input("Cuantos decimales? "))
# print(f"El precio redondeado es: {round(precio, decimales)}")

# input() SIEMPRE devuelve string
# Hay que convertir: float("12.5") -> 12.5, int("3") -> 3


# ---------------------------------------------------------------------------
# EJERCICIO 12: Numeros primos (MIT 6.0001 - clasico)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 12: Numeros primos")
print("=" * 50)

contador_primos = 0

for n in range(2, 101):
    es_primo = True
    # Solo necesitamos comprobar divisores hasta la raiz cuadrada de n
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            es_primo = False
            break  # ya sabemos que no es primo, no seguimos
    if es_primo:
        print(f"  {n} es primo")
        contador_primos += 1

print(f"\nTotal de primos entre 2 y 100: {contador_primos}")

# POR QUE SOLO HASTA LA RAIZ CUADRADA?
# Si n = 36, sus divisores son: 1, 2, 3, 4, 6, 9, 12, 18, 36
# sqrt(36) = 6. Los divisores vienen en "parejas":
# 2 x 18, 3 x 12, 4 x 9, 6 x 6
# Si no encontramos divisor hasta sqrt(n), no lo hay despues tampoco.
# Esto hace el algoritmo mucho mas eficiente.
#
# CONCEPTO MIT 6.0001: "Exhaustive enumeration" (enumeracion exhaustiva)
# Probamos TODOS los posibles divisores sistematicamente.
# Es un enfoque de "fuerza bruta" pero funciona bien para rangos pequenos.
#
# int(n ** 0.5) calcula la raiz cuadrada entera:
# int(25 ** 0.5) = int(5.0) = 5
# int(24 ** 0.5) = int(4.898...) = 4
#
# OPTIMIZACION: el break sale del bucle interno cuando encontramos
# un divisor. No tiene sentido seguir comprobando si ya sabemos
# que no es primo. Esto ahorra tiempo en numeros grandes.


# ---------------------------------------------------------------------------
# EJERCICIO 13: Patron de diamante (MIT - patrones con bucles)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 13: Patron de diamante")
print("=" * 50)

n = 5

# Parte superior del diamante (incluyendo la fila central)
for i in range(n):
    espacios = n - 1 - i
    estrellas = 2 * i + 1
    print(" " * espacios + "*" * estrellas)

# Parte inferior del diamante (espejo de la superior, sin repetir el centro)
for i in range(n - 2, -1, -1):
    espacios = n - 1 - i
    estrellas = 2 * i + 1
    print(" " * espacios + "*" * estrellas)

# DESGLOSE PASO A PASO (n=5):
#
# PARTE SUPERIOR - range(5) -> i = 0, 1, 2, 3, 4
# i=0: espacios=4, estrellas=1  -> "    *"
# i=1: espacios=3, estrellas=3  -> "   ***"
# i=2: espacios=2, estrellas=5  -> "  *****"
# i=3: espacios=1, estrellas=7  -> " *******"
# i=4: espacios=0, estrellas=9  -> "*********"
#
# PARTE INFERIOR - range(3, -1, -1) -> i = 3, 2, 1, 0
# i=3: espacios=1, estrellas=7  -> " *******"
# i=2: espacios=2, estrellas=5  -> "  *****"
# i=1: espacios=3, estrellas=3  -> "   ***"
# i=0: espacios=4, estrellas=1  -> "    *"
#
# FORMULAS CLAVE:
# estrellas = 2 * i + 1    (genera impares: 1, 3, 5, 7, 9)
# espacios = n - 1 - i     (va decreciendo para centrar)
#
# CONCEPTO MIT: los patrones con bucles anidados son fundamentales
# para entender como controlar la iteracion y construir salidas
# estructuradas. El truco esta en encontrar la formula matematica
# que relaciona la fila (i) con la cantidad de caracteres.
#
# " " * 3 = "   " (3 espacios)
# "*" * 5 = "*****" (5 estrellas)
# La concatenacion + los une: "   " + "*****" = "   *****"


print("\n--- Fin de las Soluciones Guia 4 ---")
