# ============================================================================
# GUIA 5: FUNCIONES
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 2 y 3
# Enriquecido con: MIT 6.0001 (OCW), Harvard CS50P
#
# INSTRUCCIONES:
# - Lee cada ejercicio y escribe tu codigo en "# TU CODIGO AQUI"
# - Ejecuta: python ejercicios.py
# ============================================================================


# ---------------------------------------------------------------------------
# EJERCICIO 1: Funcion basica - dia de la semana
# ---------------------------------------------------------------------------
# Crea una funcion "dia_semana" que reciba un numero del 1 al 7
# y devuelva el nombre del dia como string.
# - 1 -> "Lunes", 2 -> "Martes", ... 7 -> "Domingo"
# - Si el numero no esta entre 1 y 7, devuelve "Numero no valido"
#
# Pista: puedes usar un diccionario o if/elif

# TU CODIGO AQUI:




# Pruebas:
# print(dia_semana(1))   # Lunes
# print(dia_semana(5))   # Viernes
# print(dia_semana(10))  # Numero no valido


# ---------------------------------------------------------------------------
# EJERCICIO 2: Funcion con retorno - comparar numeros
# ---------------------------------------------------------------------------
# Crea una funcion "comparar" que reciba dos numeros y devuelva:
# - "Son iguales" si son iguales
# - "El primero es mayor" si el primero es mayor
# - "El segundo es mayor" si el segundo es mayor

# TU CODIGO AQUI:




# Pruebas:
# print(comparar(10, 5))   # El primero es mayor
# print(comparar(3, 8))    # El segundo es mayor
# print(comparar(7, 7))    # Son iguales


# ---------------------------------------------------------------------------
# EJERCICIO 3: Funcion - contar letra en texto
# ---------------------------------------------------------------------------
# Crea una funcion "contar_letra" que reciba:
# - Un texto (string)
# - Una letra (string de un caracter)
# Devuelve cuantas veces aparece esa letra (sin importar mayusc/minusc)
#
# Pista: convierte todo a minusculas con .lower()

# TU CODIGO AQUI:




# Pruebas:
# print(contar_letra("Hola Mundo", "o"))   # 2
# print(contar_letra("Python", "P"))       # 1


# ---------------------------------------------------------------------------
# EJERCICIO 4: Funcion - conteo de letras (diccionario)
# ---------------------------------------------------------------------------
# Crea una funcion "contar_todas_letras" que reciba un texto y devuelva
# un diccionario con cada letra y cuantas veces aparece.
# - Convierte a minusculas
# - Ignora espacios y signos (solo cuenta letras con .isalpha())
#
# Ejemplo: "Hola" -> {'h': 1, 'o': 1, 'l': 1, 'a': 1}

# TU CODIGO AQUI:




# Pruebas:
# print(contar_todas_letras("Hola Mundo"))
# Esperado: {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}


# ---------------------------------------------------------------------------
# EJERCICIO 5: Funciones de areas (math.pi)
# ---------------------------------------------------------------------------
# Importa el modulo math para usar math.pi
# Crea 3 funciones:
# 1. area_cuadrado(lado) -> lado * lado
# 2. area_triangulo(base, altura) -> (base * altura) / 2
# 3. area_circulo(radio) -> math.pi * radio ** 2
#
# Luego calcula:
# a) 2 circulos de radio 10 + 1 triangulo de base 3 y altura 7
# b) 1 cuadrado de lado 10 + 3 circulos (radio 4, 6, 6) + 5 triangulos (base 2, altura 4)

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 6: Argumentos posicionales
# ---------------------------------------------------------------------------
# Crea una funcion "presentar" que reciba 3 argumentos: nombre, apellido, edad
# Debe imprimir: "Hola, me llamo [nombre] [apellido] y tengo [edad] anios."

# TU CODIGO AQUI:




# Prueba:
# presentar("Francisco", "Alvarez", 25)


# ---------------------------------------------------------------------------
# EJERCICIO 7: Argumentos keyword-only
# ---------------------------------------------------------------------------
# Crea una funcion "perfil" que reciba:
# - nombre (posicional obligatorio)
# - edad (posicional obligatorio)
# - ciudad (keyword-only, solo se puede pasar por nombre)
# - profesion (keyword-only)
# Imprime todos los datos
#
# Pista: los argumentos despues de * son keyword-only
# def funcion(pos1, pos2, *, kw1, kw2):

# TU CODIGO AQUI:




# Prueba:
# perfil("Francisco", 25, ciudad="Valencia", profesion="Data Analyst")


# ---------------------------------------------------------------------------
# EJERCICIO 8: *args - suma variable
# ---------------------------------------------------------------------------
# Crea una funcion "sumar_todos" que reciba cualquier cantidad de numeros
# con *args y devuelva la suma total.
#
# *args recoge todos los argumentos posicionales en una tupla

# TU CODIGO AQUI:




# Pruebas:
# print(sumar_todos(1, 3, 5, 7))      # 16
# print(sumar_todos(10, 20))           # 30
# print(sumar_todos(1, 2, 3, 4, 5))   # 15


# ---------------------------------------------------------------------------
# EJERCICIO 9: **kwargs - ficha de biblioteca
# ---------------------------------------------------------------------------
# Crea una funcion "ficha_socio" que reciba **kwargs
# e imprima cada clave y valor en formato: "clave: valor"
#
# **kwargs recoge todos los argumentos por nombre en un diccionario

# TU CODIGO AQUI:




# Prueba:
# ficha_socio(nombre="Francisco", edad=25, libro_fav="El Principito")


# ---------------------------------------------------------------------------
# EJERCICIO 10: Funcion con *args y **kwargs combinados
# ---------------------------------------------------------------------------
# Crea una funcion "mostrar_detalles" que reciba:
# - *args (detalles generales)
# - **kwargs (propiedades especificas)
# Primero imprime cada detalle de args
# Luego imprime cada propiedad de kwargs como "clave = valor"
# Finalmente imprime el tipo de args y kwargs

# TU CODIGO AQUI:




# Prueba:
# mostrar_detalles("Detalle 1", "Detalle 2", color="rojo", talla="M")


# ---------------------------------------------------------------------------
# EJERCICIO 11: Funcion lambda
# ---------------------------------------------------------------------------
# 1. Crea una funcion lambda que multiplique un numero por 2
# 2. Crea una funcion lambda que sume 10 a un numero
# 3. Usa ambas para transformar el numero 5

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 12: Funciones con parametros por defecto
# ---------------------------------------------------------------------------
# Crea una funcion "venta_online" que reciba:
# - pedido (string, obligatorio)
# - fecha_entrega (string, obligatorio)
# - incidencia (bool, por defecto False)
#
# Si incidencia es True: imprime "Contacte con Att. Cliente"
# Si incidencia es False: imprime "Su pedido [pedido] se entregara el [fecha]"

# TU CODIGO AQUI:




# Pruebas:
# venta_online("PED-001", "15/03/2025")
# venta_online("PED-002", "20/03/2025", incidencia=True)


# ---------------------------------------------------------------------------
# EJERCICIO 13: Funcion - convertir string a numero
# ---------------------------------------------------------------------------
# Crea una funcion "a_numero" que reciba un string e intente convertirlo
# a int. Si no se puede convertir, imprime "Error: no es convertible"
# y devuelve None.
#
# Pista: usa try/except ValueError

# TU CODIGO AQUI:




# Pruebas:
# print(a_numero("42"))      # 42
# print(a_numero("hola"))    # Error: no es convertible / None
# print(a_numero("3.14"))    # Error: no es convertible / None (int no acepta decimales)


# ---------------------------------------------------------------------------
# EJERCICIO 14: Funcion - calcular promedio
# ---------------------------------------------------------------------------
# Crea una funcion "calcular_promedio" que reciba una lista de numeros
# y devuelva el promedio (media aritmetica).
# Si la lista esta vacia, devuelve None y muestra un mensaje.

# TU CODIGO AQUI:




# Pruebas:
# print(calcular_promedio([8, 6, 9, 7, 10]))  # 8.0
# print(calcular_promedio([]))                  # None


# ---------------------------------------------------------------------------
# EJERCICIO 15: Funcion - restar pares con *args
# ---------------------------------------------------------------------------
# Crea una funcion "restar_pares" que tenga total=50 por defecto
# y reciba *args con numeros.
# Resta a total SOLO los numeros que sean pares.
# Devuelve el total final.

# TU CODIGO AQUI:




# Pruebas:
# print(restar_pares(1, 2, 3, 4, 5, 6))   # 50 - 2 - 4 - 6 = 38
# print(restar_pares(10, 20, 30))          # 50 - 10 - 20 - 30 = -10


# ---------------------------------------------------------------------------
# EJERCICIO 16: Piramide como funcion
# ---------------------------------------------------------------------------
# Crea una funcion "piramide" que reciba un numero n
# e imprima la piramide invertida de la Guia 4.
# n=5 imprime:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# TU CODIGO AQUI:




# Pruebas:
# piramide(5)
# piramide(3)


# ---------------------------------------------------------------------------
# EJERCICIO 17: Funcion recursiva - Factorial (MIT 6.0001 - recursion)
# ---------------------------------------------------------------------------
# Crea una funcion "factorial(n)" que calcule n! usando RECURSION.
# factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
#
# Reglas:
# - Caso base: factorial(0) = 1
# - Caso recursivo: factorial(n) = n * factorial(n - 1)
# - Si n es negativo, devuelve un mensaje de error (string)
#
# Tambien crea una funcion "factorial_iterativo(n)" que haga lo mismo
# pero usando un bucle for o while (sin recursion), para comparar.
#
# Pista recursion:
# La funcion se llama a si misma con un problema mas pequeno.
# Siempre necesita un "caso base" que detenga la recursion.
# factorial(3) -> 3 * factorial(2) -> 3 * 2 * factorial(1) -> 3 * 2 * 1 * factorial(0) -> 3 * 2 * 1 * 1 = 6

# TU CODIGO AQUI:




# Pruebas:
# print(factorial(5))              # 120
# print(factorial(0))              # 1
# print(factorial(-3))             # Mensaje de error
# print(factorial_iterativo(5))    # 120


# ---------------------------------------------------------------------------
# EJERCICIO 18: Funciones de primera clase (MIT - avanzado)
# ---------------------------------------------------------------------------
# En Python, las funciones son "ciudadanos de primera clase": se pueden
# guardar en variables, pasar como argumentos y devolver desde funciones.
#
# 1. Crea una funcion "aplicar(func, lista)" que reciba:
#    - func: una funcion que se aplicara a cada elemento
#    - lista: una lista de valores
#    Devuelve una NUEVA lista con el resultado de func(elemento)
#    para cada elemento de la lista original.
#
# 2. Pruebala con:
#    - lambda x: x * 2       (duplicar cada elemento)
#    - lambda x: x ** 2      (elevar al cuadrado)
#    - Una lista de strings con la funcion len (longitud de cada string)
#
# 3. BONUS: muestra que map() y filter() hacen algo similar:
#    - list(map(func, lista)) equivale a aplicar(func, lista)
#    - list(filter(func, lista)) filtra elementos donde func devuelve True
#
# Pista: dentro de aplicar(), simplemente haz un for que llame a func(elem)
# para cada elemento y guarde el resultado en una nueva lista.

# TU CODIGO AQUI:




# Pruebas:
# print(aplicar(lambda x: x * 2, [1, 2, 3, 4, 5]))       # [2, 4, 6, 8, 10]
# print(aplicar(lambda x: x ** 2, [1, 2, 3, 4, 5]))       # [1, 4, 9, 16, 25]
# print(aplicar(len, ["hola", "mundo", "Python"]))          # [4, 5, 6]


print("\n--- Fin de la Guia 5 ---")
print("Compara tus respuestas con soluciones.py!")
