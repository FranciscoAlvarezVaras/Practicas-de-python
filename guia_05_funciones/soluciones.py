# ============================================================================
# GUIA 5 - SOLUCIONES: FUNCIONES
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 2 y 3
# Enriquecido con: MIT 6.0001 (OCW), Harvard CS50P
# ============================================================================

import math  # Necesario para el ejercicio 5


# ---------------------------------------------------------------------------
# EJERCICIO 1: Dia de la semana
# ---------------------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1: Dia de la semana")
print("=" * 50)


def dia_semana(numero):
    """Convierte un numero (1-7) al nombre del dia."""
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miercoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sabado",
        7: "Domingo"
    }
    return dias.get(numero, "Numero no valido")
    # .get() devuelve el valor por defecto si la clave no existe


print(dia_semana(1))   # Lunes
print(dia_semana(5))   # Viernes
print(dia_semana(10))  # Numero no valido

# ANATOMIA DE UNA FUNCION:
# def nombre_funcion(parametros):
#     """Docstring: explica que hace la funcion"""
#     codigo
#     return resultado
#
# - "def" indica que estas creando una funcion
# - Los parametros son las variables que recibe
# - "return" devuelve un resultado (si no pones return, devuelve None)


# ---------------------------------------------------------------------------
# EJERCICIO 2: Comparar numeros
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2: Comparar numeros")
print("=" * 50)


def comparar(a, b):
    if a == b:
        return "Son iguales"
    elif a > b:
        return "El primero es mayor"
    else:
        return "El segundo es mayor"


print(comparar(10, 5))   # El primero es mayor
print(comparar(3, 8))    # El segundo es mayor
print(comparar(7, 7))    # Son iguales


# ---------------------------------------------------------------------------
# EJERCICIO 3: Contar una letra
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 3: Contar una letra")
print("=" * 50)


def contar_letra(texto, letra):
    # Convertimos ambos a minusculas para comparar sin importar mayus/minus
    texto_lower = texto.lower()
    letra_lower = letra.lower()
    return texto_lower.count(letra_lower)


print(contar_letra("Hola Mundo", "o"))   # 2
print(contar_letra("Python", "P"))       # 1

# .count() cuenta cuantas veces aparece un substring en un string
# Tambien funciona con listas: [1,2,3,2].count(2) -> 2


# ---------------------------------------------------------------------------
# EJERCICIO 4: Conteo de todas las letras
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 4: Conteo de letras")
print("=" * 50)


def contar_todas_letras(texto):
    texto_lower = texto.lower()
    conteo = {}  # diccionario vacio

    for caracter in texto_lower:
        if caracter.isalpha():  # solo contar letras (no espacios ni signos)
            if caracter in conteo:
                conteo[caracter] += 1  # si ya existe, suma 1
            else:
                conteo[caracter] = 1   # si no existe, empieza en 1

    return conteo


print(contar_todas_letras("Hola Mundo"))
# {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}

# PATRON MUY COMUN: contar apariciones con diccionario
# 1. Crear diccionario vacio
# 2. Recorrer los elementos
# 3. Si el elemento ya esta como clave -> sumar 1
# 4. Si no esta -> crearlo con valor 1


# ---------------------------------------------------------------------------
# EJERCICIO 5: Areas con math.pi
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 5: Areas geometricas")
print("=" * 50)


def area_cuadrado(lado):
    return lado * lado
    # O tambien: lado ** 2


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_circulo(radio):
    return math.pi * radio ** 2
    # math.pi = 3.14159265... (mucho mas preciso que 3.14)


# a) 2 circulos de radio 10 + 1 triangulo de base 3 y altura 7
resultado_a = 2 * area_circulo(10) + area_triangulo(3, 7)
print(f"a) 2 circulos r=10 + triangulo 3x7 = {resultado_a:.2f}")

# b) cuadrado lado=10 + 3 circulos (r=4,6,6) + 5 triangulos (b=2, h=4)
resultado_b = (area_cuadrado(10)
               + area_circulo(4) + 2 * area_circulo(6)
               + 5 * area_triangulo(2, 4))
print(f"b) cuadrado + 3 circulos + 5 triangulos = {resultado_b:.2f}")

# :.2f formatea el numero a 2 decimales
# import math -> importa el modulo math con funciones matematicas
# math.pi, math.sqrt(), math.floor(), math.ceil(), etc.


# ---------------------------------------------------------------------------
# EJERCICIO 6: Argumentos posicionales
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 6: Argumentos posicionales")
print("=" * 50)


def presentar(nombre, apellido, edad):
    print(f"Hola, me llamo {nombre} {apellido} y tengo {edad} anios.")


presentar("Francisco", "Alvarez", 25)

# Los argumentos posicionales se pasan EN ORDEN
# presentar("Francisco", "Alvarez", 25)
#            ^nombre      ^apellido  ^edad


# ---------------------------------------------------------------------------
# EJERCICIO 7: Keyword-only arguments
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 7: Keyword-only")
print("=" * 50)


def perfil(nombre, edad, *, ciudad, profesion):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    print(f"Profesion: {profesion}")


perfil("Francisco", 25, ciudad="Valencia", profesion="Data Analyst")

# El * separa los posicionales de los keyword-only
# nombre, edad -> se pueden pasar por posicion: perfil("Fran", 25, ...)
# ciudad, profesion -> OBLIGATORIO pasarlos por nombre: ciudad="Valencia"
# Si intentas: perfil("Fran", 25, "Valencia", "Analyst") -> TypeError!


# ---------------------------------------------------------------------------
# EJERCICIO 8: *args
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 8: *args")
print("=" * 50)


def sumar_todos(*args):
    total = 0
    for numero in args:
        total += numero
    return total
    # Forma corta: return sum(args)


print(sumar_todos(1, 3, 5, 7))      # 16
print(sumar_todos(10, 20))           # 30
print(sumar_todos(1, 2, 3, 4, 5))   # 15

# *args recoge TODOS los argumentos posicionales en una TUPLA
# sumar_todos(1, 3, 5) -> args = (1, 3, 5)
# Puedes recorrerla con for, acceder por indice, etc.


# ---------------------------------------------------------------------------
# EJERCICIO 9: **kwargs
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 9: **kwargs")
print("=" * 50)


def ficha_socio(**kwargs):
    for clave, valor in kwargs.items():
        print(f"  {clave}: {valor}")


ficha_socio(nombre="Francisco", edad=25, libro_fav="El Principito")

# **kwargs recoge argumentos por nombre en un DICCIONARIO
# ficha_socio(nombre="Francisco", edad=25)
# -> kwargs = {"nombre": "Francisco", "edad": 25}


# ---------------------------------------------------------------------------
# EJERCICIO 10: *args + **kwargs combinados
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 10: args + kwargs")
print("=" * 50)


def mostrar_detalles(*args, **kwargs):
    print("Detalles generales:")
    for detalle in args:
        print(f"  - {detalle}")

    print("Propiedades:")
    for clave, valor in kwargs.items():
        print(f"  {clave} = {valor}")

    print(f"\nTipo de args: {type(args)}")     # <class 'tuple'>
    print(f"Tipo de kwargs: {type(kwargs)}")   # <class 'dict'>


mostrar_detalles("Detalle 1", "Detalle 2", color="rojo", talla="M")

# ORDEN DE PARAMETROS (regla obligatoria):
# 1. Posicionales normales
# 2. *args
# 3. Keyword-only (tras *)
# 4. **kwargs
# def funcion(pos1, pos2, *args, kw1, kw2, **kwargs):


# ---------------------------------------------------------------------------
# EJERCICIO 11: Lambdas
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 11: Lambdas")
print("=" * 50)

# Lambda = funcion en una sola linea, anonima (sin nombre obligatorio)
doble = lambda x: x * 2
sumar_10 = lambda x: x + 10

print(f"doble(5) = {doble(5)}")       # 10
print(f"sumar_10(5) = {sumar_10(5)}")  # 15

# Lambda es equivalente a:
# def doble(x):
#     return x * 2
#
# Se usan para funciones simples y cortas
# Muy utiles con map(), filter(), sorted()
#
# NOTA PEP 8: Asignar lambdas a variables (como arriba) NO es lo
# recomendado. PEP 8 dice: "usa def en vez de lambda si necesitas nombre".
# El uso correcto de lambda es en linea: sorted(datos, key=lambda x: x[1])
# Aqui lo hacemos asi solo para demostrar la sintaxis.


# ---------------------------------------------------------------------------
# EJERCICIO 12: Parametros por defecto
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 12: Parametros por defecto")
print("=" * 50)


def venta_online(pedido, fecha_entrega, incidencia=False):
    if incidencia:
        print("Contacte con Att. Cliente")
    else:
        print(f"Su pedido {pedido} se entregara el {fecha_entrega}")


venta_online("PED-001", "15/03/2025")
# Sin incidencia -> usa el valor por defecto False
venta_online("PED-002", "20/03/2025", incidencia=True)

# Los parametros con valor por defecto van AL FINAL
# def funcion(obligatorio1, obligatorio2, opcional=valor_defecto):


# ---------------------------------------------------------------------------
# EJERCICIO 13: Conversion con try/except
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 13: Conversion segura")
print("=" * 50)


def a_numero(texto):
    try:
        resultado = int(texto)
        return resultado
    except ValueError:
        print(f"Error: '{texto}' no es convertible a entero")
        return None


print(a_numero("42"))      # 42
print(a_numero("hola"))    # Error + None
print(a_numero("3.14"))    # Error + None (int no acepta "3.14")

# try/except: manejo de errores
# try: intenta ejecutar el codigo
# except TipoDeError: si falla con ese error, ejecuta esto
# Es MUCHO mejor que dejar que el programa se rompa


# ---------------------------------------------------------------------------
# EJERCICIO 14: Calcular promedio
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 14: Promedio")
print("=" * 50)


def calcular_promedio(numeros):
    if len(numeros) == 0:
        print("No hay datos para calcular")
        return None

    return sum(numeros) / len(numeros)


print(calcular_promedio([8, 6, 9, 7, 10]))  # 8.0
print(calcular_promedio([]))                  # None

# sum() suma todos los elementos de una lista
# len() cuenta cuantos elementos hay
# promedio = suma_total / cantidad_elementos


# ---------------------------------------------------------------------------
# EJERCICIO 15: Restar pares con *args
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 15: Restar pares")
print("=" * 50)


def restar_pares(*args, total=50):
    for num in args:
        if num % 2 == 0:  # es par si el resto de dividir entre 2 es 0
            total -= num
    return total


print(restar_pares(1, 2, 3, 4, 5, 6))   # 50 - 2 - 4 - 6 = 38
print(restar_pares(10, 20, 30))          # 50 - 10 - 20 - 30 = -10


# ---------------------------------------------------------------------------
# EJERCICIO 16: Piramide como funcion
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 16: Piramide funcion")
print("=" * 50)


def piramide(n):
    for fila in range(n, 0, -1):
        for numero in range(fila, 0, -1):
            print(numero, end=" ")
        print()


print("Piramide de 5:")
piramide(5)
print("\nPiramide de 3:")
piramide(3)

# Convertir codigo en funcion = REUTILIZAR
# En vez de copiar/pegar el bucle cada vez, llamas piramide(n)
# Esto es uno de los principios mas importantes: DRY
# DRY = Don't Repeat Yourself (No Te Repitas)


# ---------------------------------------------------------------------------
# EJERCICIO 17: Funcion recursiva - Factorial (MIT 6.0001 - recursion)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 17: Factorial recursivo e iterativo")
print("=" * 50)


def factorial(n):
    """Calcula n! usando recursion."""
    if n < 0:
        return "Error: factorial no definido para numeros negativos"
    if n == 0:
        return 1  # Caso base: 0! = 1
    return n * factorial(n - 1)  # Caso recursivo


def factorial_iterativo(n):
    """Calcula n! usando un bucle (iterativo)."""
    if n < 0:
        return "Error: factorial no definido para numeros negativos"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i  # resultado = resultado * i
    return resultado


print(f"factorial(5) = {factorial(5)}")                    # 120
print(f"factorial(0) = {factorial(0)}")                    # 1
print(f"factorial(-3) = {factorial(-3)}")                  # Error
print(f"factorial_iterativo(5) = {factorial_iterativo(5)}")  # 120
print(f"factorial_iterativo(10) = {factorial_iterativo(10)}")  # 3628800

# COMO FUNCIONA LA RECURSION (paso a paso):
# factorial(4):
#   return 4 * factorial(3)
#     return 3 * factorial(2)
#       return 2 * factorial(1)
#         return 1 * factorial(0)
#           return 1            <-- caso base, empieza a "volver"
#         return 1 * 1 = 1
#       return 2 * 1 = 2
#     return 3 * 2 = 6
#   return 4 * 6 = 24
#
# PARTES DE UNA FUNCION RECURSIVA:
# 1. CASO BASE: la condicion que DETIENE la recursion (n == 0)
#    Sin caso base -> recursion infinita -> error RecursionError
# 2. CASO RECURSIVO: la funcion se llama a si misma con un problema
#    MAS PEQUENO (n - 1). Cada llamada acerca al caso base.
#
# RECURSION vs ITERACION:
# - Recursion: mas elegante y natural para problemas recursivos
#   (arboles, fractales, divide y venceras)
# - Iteracion: mas eficiente en memoria (no crea muchas llamadas)
# - Python tiene un limite de recursion (~1000 llamadas por defecto)
#
# CONCEPTO MIT 6.0001: La recursion es fundamental en ciencias de
# la computacion. Muchos algoritmos clasicos (ordenacion, busqueda,
# recorrido de grafos) se expresan naturalmente de forma recursiva.


# ---------------------------------------------------------------------------
# EJERCICIO 18: Funciones de primera clase (MIT - avanzado)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 18: Funciones de primera clase")
print("=" * 50)


def aplicar(func, lista):
    """Aplica una funcion a cada elemento de una lista."""
    resultado = []
    for elemento in lista:
        resultado.append(func(elemento))
    return resultado


# Pruebas con diferentes funciones
numeros = [1, 2, 3, 4, 5]
palabras = ["hola", "mundo", "Python", "es", "genial"]

# 1. Duplicar cada elemento
duplicados = aplicar(lambda x: x * 2, numeros)
print(f"Duplicar {numeros}: {duplicados}")
# [2, 4, 6, 8, 10]

# 2. Elevar al cuadrado
cuadrados = aplicar(lambda x: x ** 2, numeros)
print(f"Cuadrados {numeros}: {cuadrados}")
# [1, 4, 9, 16, 25]

# 3. Longitud de cada string (usando la funcion len directamente)
longitudes = aplicar(len, palabras)
print(f"Longitudes de {palabras}: {longitudes}")
# [4, 5, 6, 2, 6]

# EQUIVALENCIA CON map() y filter():
print("\n--- Equivalencia con map() ---")
# map(funcion, iterable) aplica la funcion a cada elemento
# Devuelve un iterador, hay que convertirlo a lista con list()
duplicados_map = list(map(lambda x: x * 2, numeros))
print(f"map duplicar: {duplicados_map}")

# filter(funcion, iterable) filtra elementos donde funcion devuelve True
print("\n--- filter() para filtrar ---")
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"filter pares de {numeros}: {pares}")
# [2, 4]

palabras_largas = list(filter(lambda x: len(x) > 3, palabras))
print(f"filter palabras largas: {palabras_largas}")
# ['hola', 'mundo', 'Python', 'genial']

# POR QUE ESTO ES IMPORTANTE:
# En Python, las funciones son "objetos de primera clase" (first-class objects).
# Esto significa que una funcion:
# 1. Se puede guardar en una variable: f = len
# 2. Se puede pasar como argumento: aplicar(len, lista)
# 3. Se puede devolver desde otra funcion
#
# Nuestra funcion aplicar() es basicamente lo que hace map() internamente.
# La diferencia es que map() devuelve un iterador (mas eficiente en memoria)
# y aplicar() devuelve una lista directamente.
#
# CONCEPTO MIT 6.0001: "Higher-order functions" (funciones de orden superior)
# Son funciones que reciben o devuelven otras funciones.
# Este concepto es la base de la programacion funcional y se usa
# muchisimo en data science con pandas, numpy, etc.
#
# En el futuro veras:
# df.apply(funcion)     -> aplica funcion a cada fila/columna de un DataFrame
# df.map(funcion)       -> aplica funcion a cada elemento
# sorted(lista, key=funcion) -> ordena usando funcion como criterio


print("\n--- Fin de las Soluciones Guia 5 ---")
