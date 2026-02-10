# ============================================================================
# GUIA 8 - SOLUCIONES: ALGORITMOS Y PENSAMIENTO COMPUTACIONAL (Estilo MIT)
# ============================================================================
# Autor: Francisco Alvarez Varas
# Inspirado en: MIT 6.0001 Lectures 3-4, Harvard CS50P, TheAlgorithms/Python
# ============================================================================

import random
import string
import time


# ---------------------------------------------------------------------------
# EJERCICIO 1: Calculadora de propinas (estilo Harvard CS50P)
# ---------------------------------------------------------------------------
print("=" * 60)
print("EJERCICIO 1: Calculadora de propinas")
print("=" * 60)


def calcular_propina(coste, porcentaje):
    """Calcula la propina y el total de una comida.
    Lanza ValueError si los valores son negativos."""
    # Validaciones - lanzamos excepcion (mejor practica que devolver strings)
    if coste < 0:
        raise ValueError("El coste no puede ser negativo")
    if porcentaje < 0:
        raise ValueError("El porcentaje no puede ser negativo")

    propina = round(coste * (porcentaje / 100), 2)
    total = round(coste + propina, 2)
    return propina, total


# Ejemplo sin input (para poder ejecutar el archivo)
coste = 25.50
porcentaje = 18

try:
    propina, total = calcular_propina(coste, porcentaje)
    print(f"Coste: {coste:.2f} euros")
    print(f"Propina ({porcentaje}%): {propina:.2f} euros")
    print(f"Total: {total:.2f} euros")
except ValueError as e:
    print(f"Error: {e}")

# Version interactiva (descomenta para probar):
# try:
#     coste = float(input("Coste de la comida: "))
#     porcentaje = float(input("Porcentaje de propina: "))
#     resultado = calcular_propina(coste, porcentaje)
#     if isinstance(resultado, str):
#         print(resultado)
#     else:
#         propina, total = resultado
#         print(f"Propina: {propina:.2f} euros")
#         print(f"Total: {total:.2f} euros")
# except ValueError:
#     print("Error: introduce un numero valido")

# CONCEPTO CLAVE: isinstance(variable, tipo)
# Comprueba si una variable es de un tipo determinado
# isinstance("hola", str)  -> True
# isinstance(42, int)      -> True
# isinstance((1,2), tuple) -> True


# ---------------------------------------------------------------------------
# EJERCICIO 2: Einstein - E=mc^2
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 2: Einstein E=mc^2")
print("=" * 60)

VELOCIDAD_LUZ = 300_000_000  # m/s (se pueden usar _ para legibilidad)


def einstein(masa):
    """Calcula la energia segun E=mc^2."""
    energia = masa * VELOCIDAD_LUZ ** 2
    return f"{energia:,} Julios"


print(f"1 kg de masa = {einstein(1)}")
print(f"0.001 kg (1 gramo) = {einstein(0.001)}")
print(f"50 kg = {einstein(50)}")

# CONCEPTO CLAVE: Formateo de numeros
# f"{numero:,}"   -> separador de miles: 1,000,000
# f"{numero:.2f}" -> 2 decimales: 3.14
# f"{numero:>10}" -> alineado a la derecha en 10 espacios
# f"{numero:010}" -> rellena con ceros: 0000000042

# CONSTANTES: en Python se escriben en MAYUSCULAS por convencion
# No hay "constantes reales" en Python, pero MAYUSCULAS indica
# que el valor NO debe cambiarse


# ---------------------------------------------------------------------------
# EJERCICIO 3: Cifrado Cesar (inspirado en MIT Pset 4)
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 3: Cifrado Cesar")
print("=" * 60)


def cifrar(texto, desplazamiento):
    """Cifra un texto usando el cifrado Cesar."""
    resultado = ""

    for caracter in texto:
        if caracter.isalpha():  # solo ciframos letras
            # Determinamos si es mayuscula o minuscula
            base = ord('A') if caracter.isupper() else ord('a')

            # Obtenemos la posicion (0-25), desplazamos, y hacemos circular
            posicion = ord(caracter) - base
            nueva_posicion = (posicion + desplazamiento) % 26
            nuevo_caracter = chr(base + nueva_posicion)

            resultado += nuevo_caracter
        else:
            resultado += caracter  # espacios, numeros, etc. se quedan igual

    return resultado


def descifrar(texto_cifrado, desplazamiento):
    """Descifra un texto cifrado con Cesar (desplazar en sentido contrario)."""
    return cifrar(texto_cifrado, -desplazamiento)


# Pruebas
texto_original = "Hola Mundo"
cifrado = cifrar(texto_original, 3)
descifrado = descifrar(cifrado, 3)

print(f"Original:    {texto_original}")
print(f"Cifrado(+3): {cifrado}")
print(f"Descifrado:  {descifrado}")

print(f"\ncifrar('Python es GENIAL', 5) = {cifrar('Python es GENIAL', 5)}")
print(f"descifrar('Udymts jx LJSNFQ', 5) = {descifrar('Udymts jx LJSNFQ', 5)}")

# COMO FUNCIONA:
# ord('a') = 97   -> codigo ASCII del caracter
# chr(97) = 'a'   -> caracter desde codigo ASCII
#
# Para 'h' con desplazamiento 3:
# posicion = ord('h') - ord('a') = 104 - 97 = 7
# nueva_posicion = (7 + 3) % 26 = 10
# nuevo_caracter = chr(97 + 10) = chr(107) = 'k'
#
# % 26 hace que sea circular:
# 'x' (posicion 23) + 3 = 26, 26 % 26 = 0 -> 'a'
# 'y' (posicion 24) + 3 = 27, 27 % 26 = 1 -> 'b'
# 'z' (posicion 25) + 3 = 28, 28 % 26 = 2 -> 'c'


# ---------------------------------------------------------------------------
# EJERCICIO 4: Scrabble simplificado (MIT Pset 3)
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 4: Scrabble")
print("=" * 60)

# Valores de cada letra en Scrabble
VALORES_SCRABBLE = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
    'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
    'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


def puntuacion_scrabble(palabra, tamano_mano=7):
    """Calcula los puntos de una palabra en Scrabble."""
    puntos = 0
    for letra in palabra.lower():
        if letra in VALORES_SCRABBLE:
            puntos += VALORES_SCRABBLE[letra]

    # Bonus de 50 puntos si usa todas las letras de la mano
    if len(palabra) == tamano_mano:
        puntos += 50

    return puntos


def mejor_palabra(lista_palabras):
    """Encuentra la palabra con mayor puntuacion."""
    mejor = ""
    mejor_puntos = 0

    for palabra in lista_palabras:
        puntos = puntuacion_scrabble(palabra)
        if puntos > mejor_puntos:
            mejor_puntos = puntos
            mejor = palabra

    return mejor, mejor_puntos


# Pruebas
palabras = ["python", "quiz", "hola", "jazz", "exquisito"]
print("Puntuaciones:")
for p in palabras:
    print(f"  '{p}' = {puntuacion_scrabble(p)} puntos")

ganadora, puntos = mejor_palabra(palabras)
print(f"\nMejor palabra: '{ganadora}' con {puntos} puntos")

# CONCEPTO: Diccionarios como tablas de busqueda (lookup tables)
# En vez de usar muchos if/elif, usamos un diccionario
# Es mas rapido y mas limpio


# ---------------------------------------------------------------------------
# EJERCICIO 5: Busqueda binaria
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 5: Busqueda Binaria")
print("=" * 60)


def busqueda_binaria(lista, objetivo):
    """Busca un elemento en una lista ordenada usando busqueda binaria."""
    inicio = 0
    fin = len(lista) - 1
    pasos = 0

    while inicio <= fin:
        pasos += 1
        medio = (inicio + fin) // 2

        print(f"  Paso {pasos}: buscando en [{inicio}:{fin}], "
              f"medio={medio}, valor={lista[medio]}")

        if lista[medio] == objetivo:
            print(f"  Encontrado en indice {medio} en {pasos} pasos!")
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1  # buscar en la mitad derecha
        else:
            fin = medio - 1     # buscar en la mitad izquierda

    print(f"  No encontrado (en {pasos} pasos)")
    return -1


numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(f"Lista: {numeros}")
print(f"\nBuscando 23:")
busqueda_binaria(numeros, 23)
print(f"\nBuscando 100:")
busqueda_binaria(numeros, 100)

# POR QUE ES IMPORTANTE:
# Busqueda lineal (uno por uno): necesita N pasos en el peor caso
# Busqueda binaria: necesita log2(N) pasos en el peor caso
#
# Para 1,000,000 de elementos:
# Lineal: hasta 1,000,000 pasos
# Binaria: maximo 20 pasos!
#
# Esto se llama COMPLEJIDAD ALGORITMICA:
# O(n)     = lineal (lenta para listas grandes)
# O(log n) = logaritmica (muy rapida)
# O(1)     = constante (instantanea, ej: acceder por indice)


# ---------------------------------------------------------------------------
# EJERCICIO 6: Bubble Sort
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 6: Bubble Sort")
print("=" * 60)


def bubble_sort(lista):
    """Ordena una lista usando el algoritmo Bubble Sort."""
    # Hacemos una copia para no modificar la original
    arr = lista.copy()
    n = len(arr)
    intercambios_totales = 0

    for pasada in range(n - 1):
        intercambios_en_pasada = 0

        for i in range(n - 1 - pasada):
            if arr[i] > arr[i + 1]:
                # Intercambiamos
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                intercambios_en_pasada += 1
                intercambios_totales += 1

        print(f"  Pasada {pasada + 1}: {arr} "
              f"({intercambios_en_pasada} intercambios)")

        # Optimizacion: si no hubo intercambios, ya esta ordenada
        if intercambios_en_pasada == 0:
            print("  Ya esta ordenada!")
            break

    print(f"  Total intercambios: {intercambios_totales}")
    return arr


lista_desordenada = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {lista_desordenada}")
ordenada = bubble_sort(lista_desordenada)
print(f"Ordenada: {ordenada}")

# INTERCAMBIO DE VARIABLES en Python (muy elegante):
# a, b = b, a  ->  intercambia los valores sin variable temporal
# En otros lenguajes necesitas: temp = a; a = b; b = temp

# COMPLEJIDAD:
# Bubble Sort: O(n^2) - lento para listas grandes
# Python's sorted(): O(n log n) - mucho mas rapido (usa TimSort)
# Bubble Sort es educativo, pero en la practica usa sorted() o .sort()


# ---------------------------------------------------------------------------
# EJERCICIO 7: Generador de contrasenas
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 7: Generador de contrasenas")
print("=" * 60)


def generar_contrasena(longitud=12, usar_mayus=True,
                       usar_numeros=True, usar_simbolos=True):
    """Genera una contrasena segura aleatoria."""
    if longitud < 8:
        longitud = 8
        print("Longitud minima ajustada a 8")

    caracteres = string.ascii_lowercase  # siempre incluye minusculas

    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += "!@#$%&*+-=?"  # subset de simbolos comunes

    # Generamos la contrasena eligiendo caracteres al azar
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena


def evaluar_seguridad(contrasena):
    """Evalua la seguridad de una contrasena."""
    tiene_minus = any(c.islower() for c in contrasena)
    tiene_mayus = any(c.isupper() for c in contrasena)
    tiene_num = any(c.isdigit() for c in contrasena)
    tiene_simb = any(not c.isalnum() for c in contrasena)

    puntos = sum([tiene_minus, tiene_mayus, tiene_num, tiene_simb])

    if len(contrasena) < 8:
        return "Debil"
    elif puntos <= 1:
        return "Media"
    elif puntos <= 2:
        return "Fuerte"
    else:
        return "Muy fuerte"


# Generar y evaluar contrasenas
for _ in range(3):
    pwd = generar_contrasena(longitud=16)
    seguridad = evaluar_seguridad(pwd)
    print(f"  {pwd} -> {seguridad}")

# Probar evaluaciones
print(f"\n  'password' -> {evaluar_seguridad('password')}")
print(f"  'Pass123' -> {evaluar_seguridad('Pass123')}")
print(f"  'P@ss1234' -> {evaluar_seguridad('P@ss1234')}")

# CONCEPTOS CLAVE:
# string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# string.digits = '0123456789'
# random.choice(secuencia) = elige un elemento al azar
# ''.join(lista) = une los elementos en un string
# any(iterable) = True si al menos un elemento es True
# sum([True, False, True]) = 2 (True = 1, False = 0)

# COMPRENSION DE GENERADOR:
# (expresion for variable in iterable)
# Es como un for en una linea que genera valores uno a uno
# any(c.isdigit() for c in "hola3") chequea cada caracter


# ---------------------------------------------------------------------------
# EJERCICIO 8: Fibonacci iterativo y recursivo
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 8: Fibonacci")
print("=" * 60)


def fibonacci_iterativo(n):
    """Devuelve los primeros n numeros de Fibonacci (con bucle)."""
    if n <= 0:
        return []
    if n == 1:
        return [0]

    secuencia = [0, 1]
    for i in range(2, n):
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)

    return secuencia


def fibonacci_recursivo(n):
    """Devuelve el n-esimo numero de Fibonacci (recursion)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# Secuencia iterativa
print("Primeros 15 Fibonacci (iterativo):")
print(fibonacci_iterativo(15))

# Comparar velocidad
print("\nComparacion de velocidad:")

inicio = time.time()
resultado_iter = fibonacci_iterativo(30)
tiempo_iter = time.time() - inicio
print(f"  Iterativo (30 numeros): {tiempo_iter:.6f} segundos")

inicio = time.time()
resultado_rec = fibonacci_recursivo(30)
tiempo_rec = time.time() - inicio
print(f"  Recursivo (numero 30):  {tiempo_rec:.6f} segundos")

print(f"\n  El recursivo es ~{tiempo_rec/max(tiempo_iter, 0.000001):.0f}x "
      f"mas lento!")

# RECURSION: una funcion que se llama a si misma
# fibonacci_recursivo(4)
#   = fibonacci_recursivo(3) + fibonacci_recursivo(2)
#   = (fib(2) + fib(1)) + (fib(1) + fib(0))
#   = ((fib(1) + fib(0)) + 1) + (1 + 0)
#   = ((1 + 0) + 1) + (1 + 0)
#   = 3
#
# PROBLEMA: la recursion recalcula los mismos valores muchas veces
# fib(30) llama a fib(29) y fib(28), pero fib(29) tambien llama a fib(28)
# Es MUY ineficiente para numeros grandes
#
# SOLUCION AVANZADA: memoizacion (guardar resultados calculados)
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def fibonacci_memo(n):
#     if n <= 1: return n
#     return fibonacci_memo(n-1) + fibonacci_memo(n-2)


# ---------------------------------------------------------------------------
# EJERCICIO 9: Busqueda por biseccion - Raiz cuadrada (MIT 6.0001 Lecture 3)
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 9: Biseccion - Raiz cuadrada")
print("=" * 60)


def raiz_biseccion(x, epsilon=0.01):
    """Encuentra la raiz cuadrada de x usando busqueda por biseccion."""
    if x < 0:
        print(f"  Error: no existe raiz cuadrada real de {x}")
        return None, 0

    low = 0
    high = max(1.0, x)  # max(1, x) para que funcione con x < 1
    estimacion = (low + high) / 2.0
    iteraciones = 0

    while abs(estimacion ** 2 - x) >= epsilon:
        iteraciones += 1
        if estimacion ** 2 < x:
            low = estimacion     # buscar en la mitad superior
        else:
            high = estimacion    # buscar en la mitad inferior
        estimacion = (low + high) / 2.0

    return estimacion, iteraciones


# Pruebas
numeros_prueba = [25, 0.5, 123456789]
for num in numeros_prueba:
    resultado, iters = raiz_biseccion(num)
    print(f"  raiz({num}) = {resultado:.6f} (en {iters} iteraciones)")
    print(f"    Verificacion: {resultado:.6f}^2 = {resultado**2:.6f}")

# COMO FUNCIONA LA BISECCION:
# Es el mismo principio que la busqueda binaria pero aplicado a un rango
# continuo de numeros reales en vez de una lista.
#
# Ejemplo con raiz(25):
#   low=0, high=25 -> estimacion=12.5 -> 12.5^2=156.25 > 25 -> high=12.5
#   low=0, high=12.5 -> estimacion=6.25 -> 6.25^2=39.06 > 25 -> high=6.25
#   low=0, high=6.25 -> estimacion=3.125 -> 3.125^2=9.77 < 25 -> low=3.125
#   ... y asi se va acercando a 5.0
#
# COMPLEJIDAD: O(log(rango/epsilon))
# Para max(1, x) = 25 y epsilon = 0.01:
#   log2(25 / 0.01) = log2(2500) ~ 11 iteraciones
#
# POR QUE max(1, x)?
# Si x = 0.5, la raiz es ~0.707 que es MAYOR que x.
# Sin max(1, x), high = 0.5 y nunca encontrariamos 0.707.
# Con max(1, x), high = 1.0 y el rango [0, 1] contiene 0.707.


# ---------------------------------------------------------------------------
# EJERCICIO 10: Memoizacion - Fibonacci optimizado (MIT 6.0001 Lecture 4)
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 10: Fibonacci con Memoizacion")
print("=" * 60)


def fibonacci_memo(n, cache={}):
    """Fibonacci con memoizacion (programacion dinamica)."""
    if n in cache:
        return cache[n]

    if n <= 0:
        resultado = 0
    elif n == 1:
        resultado = 1
    else:
        resultado = fibonacci_memo(n - 1, cache) + fibonacci_memo(n - 2, cache)

    cache[n] = resultado
    return resultado


# Comparacion de velocidad con la version recursiva naive (del ejercicio 8)
print("Comparacion: recursivo naive vs memoizado")

n_test = 35

# Version recursiva naive (la del ejercicio 8)
inicio = time.time()
resultado_naive = fibonacci_recursivo(n_test)
tiempo_naive = time.time() - inicio
print(f"  fibonacci_recursivo({n_test}) = {resultado_naive}")
print(f"    Tiempo: {tiempo_naive:.4f} segundos")

# Version memoizada
# Limpiamos el cache para medir desde cero
fibonacci_memo.__defaults__[0].clear()

inicio = time.time()
resultado_memo = fibonacci_memo(n_test)
tiempo_memo = time.time() - inicio
print(f"  fibonacci_memo({n_test}) = {resultado_memo}")
print(f"    Tiempo: {tiempo_memo:.6f} segundos")

if tiempo_memo > 0:
    ratio = tiempo_naive / tiempo_memo
    print(f"\n  La version memoizada es ~{ratio:,.0f}x mas rapida!")
else:
    print(f"\n  La version memoizada es practicamente instantanea!")

# Bonus: numeros grandes que serian imposibles con recursion naive
print(f"\n  fibonacci_memo(100) = {fibonacci_memo(100)}")
print(f"  fibonacci_memo(200) = {fibonacci_memo(200)}")
print("  (Imposible con recursion naive - tardaria siglos)")

# MEMOIZACION - CONCEPTO CLAVE:
# La recursion naive recalcula los mismos valores MUCHAS veces:
#   fib(5) = fib(4) + fib(3)
#   fib(4) = fib(3) + fib(2)  <- fib(3) se calcula 2 veces!
#   fib(3) = fib(2) + fib(1)  <- fib(2) se calcula 3 veces!
#
# Con memoizacion, cada valor se calcula UNA SOLA VEZ y se guarda.
#
# COMPLEJIDAD:
# Sin memo: O(2^n)  -> exponencial, crece absurdamente rapido
# Con memo: O(n)    -> lineal, cada valor se calcula una vez
#
# TRUCO PYTHON: cache={} como argumento por defecto
# En Python, los argumentos mutables por defecto se crean UNA vez
# y se COMPARTEN entre todas las llamadas. Normalmente esto es un
# bug (Mutable Default Argument), pero aqui lo aprovechamos como cache.
#
# ALTERNATIVA PROFESIONAL: @functools.lru_cache
# from functools import lru_cache
# @lru_cache(maxsize=None)
# def fib(n):
#     if n <= 1: return n
#     return fib(n-1) + fib(n-2)


print("\n--- Fin de las Soluciones Guia 8 ---")
print("Estos ejercicios estan al nivel de MIT 6.0001")
