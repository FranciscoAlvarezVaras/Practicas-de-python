# ============================================================================
# GUIA 8: ALGORITMOS Y PENSAMIENTO COMPUTACIONAL (Estilo MIT 6.0001)
# ============================================================================
# Autor: Francisco Alvarez Varas
# Inspirado en: MIT 6.0001 Lectures 3-4 & Problem Sets (OCW) y Harvard CS50P
# Fuentes:
#   - MIT OCW 6.0001: https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
#   - Harvard CS50P: https://cs50.harvard.edu/python/
#   - TheAlgorithms/Python: https://github.com/TheAlgorithms/Python
#
# NIVEL: Intermedio - Estos ejercicios te hacen PENSAR como programador
# En el MIT estos son los ejercicios que separan a los novatos de los buenos
# ============================================================================


# ---------------------------------------------------------------------------
# EJERCICIO 1: Calculadora de propinas (estilo Harvard CS50P)
# ---------------------------------------------------------------------------
# Crea un programa que:
# 1. Pida al usuario el coste de la comida (ej: "25.50")
# 2. Pida el porcentaje de propina (ej: "18")
# 3. Calcule la propina y el total
# 4. Imprima: "Propina: 4.59 euros" y "Total: 30.09 euros"
#
# VALIDACIONES (esto es lo que lo hace nivel MIT):
# - Si el usuario mete texto en vez de numero -> mensaje de error
# - Si el porcentaje es negativo -> mensaje de error
# - Redondea a 2 decimales
#
# Pista: usa try/except y round()

# TU CODIGO AQUI (version sin input para poder ejecutar):
# coste = 25.50
# porcentaje = 18




# ---------------------------------------------------------------------------
# EJERCICIO 2: Einstein - E=mc^2 (Harvard CS50P Pset 0)
# ---------------------------------------------------------------------------
# La famosa ecuacion de Einstein: E = m * c^2
# donde c = velocidad de la luz = 300000000 m/s
#
# Crea una funcion "einstein(masa)" que:
# - Reciba la masa en kg
# - Calcule la energia en Julios
# - Devuelva la energia formateada con separador de miles
#
# Ejemplo: einstein(1) -> "90,000,000,000,000,000 Julios"
# Ejemplo: einstein(50) -> resultado enorme
#
# Pista: para formatear con separador de miles: f"{numero:,}"

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 3: Cifrado Cesar (inspirado en MIT 6.0001 Pset 4)
# ---------------------------------------------------------------------------
# El cifrado Cesar desplaza cada letra del alfabeto un numero de posiciones.
# Ejemplo con desplazamiento 3:
#   "hola" -> "krod" (h->k, o->r, l->o, a->d)
#
# Crea dos funciones:
# 1. cifrar(texto, desplazamiento) -> texto cifrado
# 2. descifrar(texto_cifrado, desplazamiento) -> texto original
#
# Reglas:
# - Solo cifra letras (a-z), ignora numeros y signos
# - Mantiene mayusculas/minusculas
# - Si pasa de 'z', vuelve a 'a' (circular)
#
# Pista: usa ord() para obtener el codigo ASCII de una letra
#        usa chr() para convertir un codigo ASCII a letra
#        ord('a') = 97, ord('z') = 122
#        Para hacer circular: (posicion + desplazamiento) % 26

# TU CODIGO AQUI:




# Pruebas:
# print(cifrar("hola mundo", 3))           # "krod pxqgr"
# print(descifrar("krod pxqgr", 3))        # "hola mundo"
# print(cifrar("Python es GENIAL", 5))     # letras desplazadas 5


# ---------------------------------------------------------------------------
# EJERCICIO 4: Juego de Scrabble simplificado (MIT 6.0001 Pset 3)
# ---------------------------------------------------------------------------
# Cada letra vale unos puntos:
# a=1, b=3, c=3, d=2, e=1, f=4, g=2, h=4, i=1, j=8,
# k=5, l=1, m=3, n=1, o=1, p=3, q=10, r=1, s=1, t=1,
# u=1, v=4, w=4, x=8, y=4, z=10
#
# Crea una funcion "puntuacion_scrabble(palabra)" que:
# 1. Calcule los puntos de una palabra
# 2. BONUS: si la palabra usa TODAS las letras de la mano (7), suma 50 puntos
#
# Luego crea una funcion "mejor_palabra(lista_palabras)" que:
# - Reciba una lista de palabras
# - Devuelva la que tiene mayor puntuacion
#
# Ejemplo:
# puntuacion_scrabble("python") -> 14 (3+4+1+4+1+1)
# mejor_palabra(["python", "quiz", "hola"]) -> "quiz" (22 puntos)

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 5: Busqueda binaria (algoritmo fundamental en CS)
# ---------------------------------------------------------------------------
# La busqueda binaria encuentra un numero en una lista ORDENADA
# dividiendo la lista a la mitad en cada paso.
# Es MUCHO mas rapida que buscar uno por uno.
#
# Crea una funcion "busqueda_binaria(lista, objetivo)" que:
# - Reciba una lista ordenada y un numero a buscar
# - Devuelva el INDICE donde esta el numero, o -1 si no existe
# - Imprima cada paso para ver como funciona
#
# Algoritmo:
# 1. inicio = 0, fin = len(lista) - 1
# 2. Mientras inicio <= fin:
#    a. medio = (inicio + fin) // 2
#    b. Si lista[medio] == objetivo: encontrado!
#    c. Si lista[medio] < objetivo: buscar en la mitad derecha (inicio = medio + 1)
#    d. Si lista[medio] > objetivo: buscar en la mitad izquierda (fin = medio - 1)
# 3. Si sale del while: no encontrado, devolver -1

# TU CODIGO AQUI:




# Pruebas:
# numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
# print(busqueda_binaria(numeros, 23))   # Deberia devolver 5
# print(busqueda_binaria(numeros, 100))  # Deberia devolver -1


# ---------------------------------------------------------------------------
# EJERCICIO 6: Ordenamiento burbuja (Bubble Sort)
# ---------------------------------------------------------------------------
# El algoritmo de ordenamiento burbuja compara pares adyacentes
# y los intercambia si estan en el orden incorrecto.
# Se repite hasta que no hay mas intercambios.
#
# Crea una funcion "bubble_sort(lista)" que:
# - Ordene la lista de menor a mayor
# - Imprima la lista despues de cada pasada completa
# - Devuelva la lista ordenada
# - Cuente cuantos intercambios hizo
#
# Ejemplo:
# bubble_sort([64, 34, 25, 12, 22, 11, 90])
# Pasada 1: [34, 25, 12, 22, 11, 64, 90]
# Pasada 2: [25, 12, 22, 11, 34, 64, 90]
# ...

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 7: Generador de contrasenas seguras
# ---------------------------------------------------------------------------
# Crea un programa que genere contrasenas seguras.
#
# Funcion "generar_contrasena(longitud, usar_mayus, usar_numeros, usar_simbolos)":
# - longitud: int (minimo 8)
# - usar_mayus: bool
# - usar_numeros: bool
# - usar_simbolos: bool
# - Devuelve una contrasena aleatoria
#
# Funcion "evaluar_seguridad(contrasena)":
# - Devuelve "Debil", "Media", "Fuerte" o "Muy fuerte"
# - Criterios:
#   < 8 caracteres: Debil
#   Solo letras: Media
#   Letras + numeros: Fuerte
#   Letras + numeros + simbolos + mayusculas: Muy fuerte
#
# Pista: import random, import string
# string.ascii_lowercase = "abcdef...z"
# string.ascii_uppercase = "ABCDEF...Z"
# string.digits = "0123456789"
# string.punctuation = "!@#$%..."

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 8: Fibonacci y recursion (clasico MIT)
# ---------------------------------------------------------------------------
# La secuencia de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Cada numero es la suma de los dos anteriores.
#
# Crea DOS versiones:
# 1. fibonacci_iterativo(n) -> devuelve los primeros n numeros (con bucle)
# 2. fibonacci_recursivo(n) -> devuelve el n-esimo numero (la funcion se
#    llama a si misma)
#
# Luego compara la velocidad de ambos para n=30
#
# Pista recursion: la funcion se llama a si misma
# def fibonacci_recursivo(n):
#     if n <= 0: return 0
#     if n == 1: return 1
#     return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 9: Busqueda por biseccion - Raiz cuadrada (MIT 6.0001 Lecture 3)
# ---------------------------------------------------------------------------
# En el MIT este es uno de los primeros algoritmos que ensena Guttag.
# Buscar la raiz cuadrada de un numero SIN usar math.sqrt.
#
# Implementa una funcion "raiz_biseccion(x, epsilon=0.01)" que:
# 1. Dado un numero x, encuentre su raiz cuadrada con precision epsilon
# 2. Algoritmo de biseccion:
#    - low = 0, high = max(1, x)
#    - estimacion = (low + high) / 2
#    - Si abs(estimacion**2 - x) < epsilon -> encontrado!
#    - Si estimacion**2 < x -> buscar en la mitad superior (low = estimacion)
#    - Si estimacion**2 > x -> buscar en la mitad inferior (high = estimacion)
# 3. Cuenta cuantas iteraciones necesita
# 4. Devuelve (resultado, iteraciones)
#
# Pruebas:
# raiz_biseccion(25)        -> ~5.0 (pocas iteraciones)
# raiz_biseccion(0.5)       -> ~0.707... (funciona con menores que 1!)
# raiz_biseccion(123456789) -> ~11111.11... (funciona con numeros enormes!)
#
# Pista: abs(x) devuelve el valor absoluto
# Pista: max(1, x) es necesario para que funcione con numeros menores que 1

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 10: Memoizacion - Fibonacci optimizado (MIT 6.0001 Lecture 4)
# ---------------------------------------------------------------------------
# En el ejercicio 8 vimos que fibonacci_recursivo es MUY lento.
# La razon: recalcula los mismos valores miles de veces.
#
# La MEMOIZACION es la solucion: guardar resultados ya calculados
# en un diccionario (cache) para no recalcularlos.
# Esto es la introduccion a la PROGRAMACION DINAMICA (dynamic programming),
# un tema clave en MIT 6.0001 y en entrevistas tecnicas.
#
# Crea una funcion "fibonacci_memo(n, cache={})" que:
# 1. Si n ya esta en cache, devuelve cache[n] directamente
# 2. Si no, calcula fibonacci_memo(n-1) + fibonacci_memo(n-2)
# 3. Guarda el resultado en cache[n] antes de devolverlo
# 4. Devuelve el n-esimo numero de Fibonacci
#
# Luego compara la velocidad con fibonacci_recursivo del ejercicio 8:
# - fibonacci_recursivo(35) -> LENTO (varios segundos)
# - fibonacci_memo(35) -> INSTANTANEO
#
# Pista: los argumentos por defecto mutables ({}) se comparten entre
#        llamadas, lo cual aqui es una VENTAJA (el cache persiste)
#
# BONUS: Prueba con n=100 (imposible con recursion naive, trivial con memo)

# TU CODIGO AQUI:




print("\n--- Fin de la Guia 8 ---")
print("Estos ejercicios son de nivel MIT/Harvard.")
print("Si los dominas, tu nivel de Python es MUY solido!")
