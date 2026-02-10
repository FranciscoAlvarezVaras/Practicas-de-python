# ============================================================================
# GUIA 1 - SOLUCIONES: VARIABLES, TIPOS DE DATOS Y STRINGS
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 1
# Enriquecido con: MIT 6.0001 (OCW), Harvard CS50P (Pset 0)
#
# IMPORTANTE: Intenta resolver los ejercicios por tu cuenta antes de mirar!
# Aqui tienes las soluciones con explicaciones paso a paso.
# ============================================================================


# ---------------------------------------------------------------------------
# EJERCICIO 1: Creando variables y concatenando
# ---------------------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1: Variables y concatenacion")
print("=" * 50)

# Creamos cada variable con su tipo adecuado
calle = "Calle Mayor"          # str - texto entre comillas
numero = "15"                   # str - lo hacemos string para concatenar facil
ciudad = "Valencia"             # str
codigo_postal = "46001"         # str

# Concatenamos con f-string (la forma mas moderna y legible)
direccion_completa = f"{calle}, {numero}, {ciudad}, {codigo_postal}"

# Imprimimos
print(direccion_completa)

# Mostramos la longitud
print(f"Mi direccion tiene {len(direccion_completa)} caracteres")

# EXPLICACION:
# - f"..." es un f-string: permite meter variables dentro de {} en un texto
# - len() cuenta el numero de caracteres de un string (incluidos espacios)
# - Tambien se puede concatenar con +: calle + ", " + numero + ...
#   pero f-strings son mas limpios


# ---------------------------------------------------------------------------
# EJERCICIO 2: Variables bien y mal escritas
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2: Variables correctas e incorrectas")
print("=" * 50)

# a) mi_variable = "Economia"       -> CORRECTA: usa guion bajo, todo bien
# b) otra_var = "Ejercicio           -> MAL: falta cerrar las comillas "
# c) True = "Ejercicio"             -> MAL: True es palabra reservada de Python
# d) mi variab1e = "Alpha"          -> MAL: los nombres no pueden tener espacios
# e) import = 40                    -> MAL: import es palabra reservada
# f) 81mi_variable = "Agua"         -> MAL: no puede empezar por numero
# g) mi_variable10 = 6              -> CORRECTA: puede tener numeros (no al inicio)

print("a) CORRECTA - nombre valido con guion bajo")
print("b) MAL - falta cerrar comillas")
print("c) MAL - True es palabra reservada")
print("d) MAL - no se permiten espacios en nombres")
print("e) MAL - import es palabra reservada")
print("f) MAL - no puede empezar por numero")
print("g) CORRECTA - puede tener numeros si no es al inicio")

# REGLAS para nombres de variables:
# 1. Solo letras, numeros y guion bajo (_)
# 2. NO pueden empezar por numero
# 3. NO pueden ser palabras reservadas (True, False, if, else, import, etc.)
# 4. NO pueden tener espacios
# 5. Python distingue mayusculas de minusculas (edad != Edad)


# ---------------------------------------------------------------------------
# EJERCICIO 3: Tipos de datos (int, float, type, del)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 3: Tipos de datos")
print("=" * 50)

entero = 10           # int - numero entero
decimal = 3.14        # float - numero con decimales

print(f"entero es de tipo: {type(entero)}")    # <class 'int'>
print(f"decimal es de tipo: {type(decimal)}")  # <class 'float'>

suma = entero + decimal
print(f"suma = {suma}")
print(f"suma es de tipo: {type(suma)}")        # <class 'float'>

# Cuando sumas un int + float, Python convierte el resultado a float
# Esto se llama "coercion de tipos" - Python elige el tipo mas amplio

del entero    # Elimina la variable de la memoria
del decimal   # Ya no puedes usar estas variables despues de esto

# Si intentas: print(entero) -> NameError: name 'entero' is not defined


# ---------------------------------------------------------------------------
# EJERCICIO 4: Strings y sus metodos
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 4: Metodos de strings")
print("=" * 50)

frase = "A quien madruga, dios le ayuda"

# .upper() - convierte TODO a mayusculas
print(frase.upper())
# Resultado: "A QUIEN MADRUGA, DIOS LE AYUDA"

# .lower() - convierte TODO a minusculas
print(frase.lower())
# Resultado: "a quien madruga, dios le ayuda"

# .title() - primera letra de cada palabra en mayuscula
print(frase.title())
# Resultado: "A Quien Madruga, Dios Le Ayuda"

# .split() - divide el string por espacios y devuelve una LISTA
palabras = frase.split()
print(palabras)
# Resultado: ['A', 'quien', 'madruga,', 'dios', 'le', 'ayuda']

# .replace(viejo, nuevo) - sustituye texto
print(frase.replace(",", ";"))
# Resultado: "A quien madruga; dios le ayuda"

# .replace() tambien sirve para eliminar (reemplazar por nada "")
print(frase.replace("a", ""))
# Resultado: "A quien mdrug, dios le yud"
# OJO: solo elimina las "a" minusculas, la "A" mayuscula se queda

# METODOS DE STRING MAS UTILES:
# .upper()      -> todo mayusculas
# .lower()      -> todo minusculas
# .title()      -> primera letra de cada palabra mayuscula
# .strip()      -> quita espacios al inicio y final
# .split()      -> divide en lista
# .replace()    -> reemplaza texto
# .count()      -> cuenta apariciones
# .startswith() -> comprueba si empieza por...
# .endswith()   -> comprueba si termina en...
# .find()       -> busca posicion de un texto


# ---------------------------------------------------------------------------
# EJERCICIO 5: Strings con comillas internas
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 5: Comillas internas")
print("=" * 50)

# Opcion 1: comillas simples por fuera, dobles por dentro
frase_comillas = 'Ella dijo "hola" y se fue'
print(frase_comillas)

# Opcion 2: escapar las comillas con \
frase_comillas2 = "Ella dijo \"hola\" y se fue"
print(frase_comillas2)

# Longitud con mensaje
print(f"Esta cadena tiene {len(frase_comillas)} caracteres")


# ---------------------------------------------------------------------------
# EJERCICIO 6: Slicing y metodos extra
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 6: Slicing y metodos extra")
print("=" * 50)

info = "Marina de Empresas 2025"

# Longitud
print(f"Longitud: {len(info)}")    # 23

# Primera letra - indice 0 (Python cuenta desde 0!)
print(f"Primera letra: {info[0]}")  # M

# Ultimas 4 letras con slicing negativo
print(f"Ultimas 4: {info[-4:]}")    # 2025

# Al reves con slicing de paso -1
print(f"Al reves: {info[::-1]}")    # 5202 saserpmE ed aniraM

# Contar apariciones de "a"
print(f"Veces que aparece 'a': {info.count('a')}")  # 3

# SLICING - como funciona: variable[inicio:fin:paso]
# info[0]     -> primer caracter
# info[-1]    -> ultimo caracter
# info[0:6]   -> desde posicion 0 hasta 5 (el 6 NO se incluye)
# info[:6]    -> igual que info[0:6]
# info[6:]    -> desde posicion 6 hasta el final
# info[-4:]   -> los ultimos 4 caracteres
# info[::-1]  -> todo al reves (paso -1)


# ---------------------------------------------------------------------------
# EJERCICIO 7: Conversion de tipos (inspirado en Harvard CS50P)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 7: Conversion de tipos")
print("=" * 50)

# int() convierte a entero
num_entero = int("42")
print(f"int('42') = {num_entero}, tipo: {type(num_entero)}")
# Resultado: 42, tipo: <class 'int'>

# float() convierte a decimal
num_decimal = float("3.14")
print(f"float('3.14') = {num_decimal}, tipo: {type(num_decimal)}")
# Resultado: 3.14, tipo: <class 'float'>

# str() convierte a texto
texto_num = str(100)
print(f"str(100) = '{texto_num}', tipo: {type(texto_num)}")
# Resultado: '100', tipo: <class 'str'>

# bool() convierte a booleano
bool_cero = bool(0)
print(f"bool(0) = {bool_cero}, tipo: {type(bool_cero)}")
# Resultado: False - el 0 es "falsy"

bool_texto = bool("hello")
print(f"bool('hello') = {bool_texto}, tipo: {type(bool_texto)}")
# Resultado: True - cualquier string no vacio es "truthy"

# CUIDADO con conversiones que fallan:
# int("hello") -> ValueError: invalid literal for int()
# float("abc") -> ValueError: could not convert string to float
# Python no puede adivinar que numero es "hello"!
#
# En programas reales usamos try/except para manejar esto:
print("\nIntentando int('hello'):")
try:
    resultado = int("hello")
except ValueError as e:
    print(f"  Error capturado: {e}")

# REGLAS DE CONVERSION:
# int("42")     -> 42       (string numerico a entero)
# float("3.14") -> 3.14     (string numerico a decimal)
# str(100)      -> "100"    (cualquier cosa a string, siempre funciona)
# bool(0)       -> False    (0, 0.0, "", [], {}, None son False)
# bool("hello") -> True     (todo lo demas es True)
# int("hello")  -> ERROR    (no se puede convertir texto no numerico)


# ---------------------------------------------------------------------------
# EJERCICIO 8: Batalla de Formateo de Strings (estilo MIT 6.0001)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 8: Formateo de strings")
print("=" * 50)

nombre = "Francisco"
edad = 25
nota = 9.567

# METODO 1: Concatenacion con +
# Necesitas str() para convertir numeros a texto
print("1) " + "Me llamo " + nombre + " y tengo " + str(edad) + " anios")
# Funciona pero es poco legible y propenso a errores

# METODO 2: Operador % (estilo C, antiguo)
# %s = string, %d = entero, %f = float
print("2) Me llamo %s y tengo %d anios" % (nombre, edad))
# Era el estandar antes de Python 3, todavia se ve en codigo antiguo

# METODO 3: .format()
# Usa {} como marcadores de posicion
print("3) Me llamo {} y tengo {} anios".format(nombre, edad))
# Mas flexible que %, permite reordenar con indices: {0}, {1}

# METODO 4: f-string (Python 3.6+) - EL ESTANDAR MODERNO
print(f"4) Me llamo {nombre} y tengo {edad} anios")
# La forma mas limpia, rapida y legible. USA ESTA SIEMPRE QUE PUEDAS.

# BONUS: Formateo de decimales con f-string
print(f"Nota con 1 decimal: {nota:.1f}")    # 9.6
print(f"Nota con 2 decimales: {nota:.2f}")  # 9.57
print(f"Nota sin decimales: {nota:.0f}")    # 10

# COMPARACION DE METODOS (de peor a mejor):
# 1. Concatenacion (+)  -> dificil de leer, necesita str()
# 2. Operador (%)       -> estilo antiguo, poco flexible
# 3. .format()          -> bueno, pero verboso
# 4. f-string (f"")     -> MODERNO, legible, rapido. RECOMENDADO.


# ---------------------------------------------------------------------------
# EJERCICIO 9: Voz Baja (inspirado en Harvard CS50P - Pset 0)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 9: Voz Baja")
print("=" * 50)

# 1. Convertir grito a voz baja
grito = "HOLA, COMO ESTAS? TODO BIEN POR AQUI!"
voz_baja = grito.lower()
print(f"Grito original: {grito}")
print(f"Voz baja: {voz_baja}")
# .lower() convierte TODAS las letras a minusculas

# 2. Convertir mezcla a minusculas
mezcla = "HoLa MuNdO, EsTo Es PyThOn"
print(f"\nMezcla original: {mezcla}")
print(f"Normalizada: {mezcla.lower()}")

# 3. Contar vocales, consonantes y otros
texto_analizar = "Programacion en Python 2025"
print(f"\nAnalizando: '{texto_analizar}'")

vocales = "aeiouAEIOU"
contador_vocales = 0
contador_consonantes = 0
contador_otros = 0

for caracter in texto_analizar:
    if caracter in vocales:
        contador_vocales += 1
    elif caracter.isalpha():
        # .isalpha() devuelve True si es una letra (no numero, no espacio)
        contador_consonantes += 1
    else:
        # Todo lo que no sea letra: numeros, espacios, signos
        contador_otros += 1

print(f"Vocales: {contador_vocales}")
print(f"Consonantes: {contador_consonantes}")
print(f"Otros (numeros, espacios, signos): {contador_otros}")

# EXPLICACION del bucle:
# for caracter in texto_analizar:  -> recorre cada caracter uno a uno
# Primero comprueba si es vocal (esta en la cadena "aeiouAEIOU")
# Si no es vocal, comprueba si es letra con .isalpha()
# Si tampoco es letra, es "otro" (numero, espacio, signo)

# 4. Caracteres ocultos con repr()
oculto = "Hola,\tmundo!\n"
print(f"\nprint normal: {oculto}", end="")  # Muestra tab y salto de linea
print(f"print con repr: {repr(oculto)}")
# repr() muestra la representacion "cruda" del string
# Veras: 'Hola,\tmundo!\n'
# \t = tabulador, \n = salto de linea

# METODOS DE CASO MAS UTILES:
# .lower()       -> todo minusculas
# .upper()       -> todo mayusculas
# .title()       -> primera letra de cada palabra mayuscula
# .capitalize()  -> solo primera letra del texto mayuscula
# .swapcase()    -> invierte mayusculas/minusculas
# .isalpha()     -> True si solo tiene letras
# .isdigit()     -> True si solo tiene numeros
# .isalnum()     -> True si solo tiene letras y numeros


print("\n--- Fin de las Soluciones Guia 1 ---")
