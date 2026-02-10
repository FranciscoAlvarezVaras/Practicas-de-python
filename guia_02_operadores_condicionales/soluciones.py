# ============================================================================
# GUIA 2 - SOLUCIONES: OPERADORES Y CONDICIONALES
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 1 (Ej. 4, 8) y Repaso
# Enriquecido con: MIT 6.0001 (OCW), Harvard CS50P (condicionales)
# ============================================================================


# ---------------------------------------------------------------------------
# EJERCICIO 1: Operadores aritmeticos
# ---------------------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1: Operadores aritmeticos")
print("=" * 50)

a = 10
b = 3

print(f"a + b = {a + b}")          # 13  (suma)
print(f"a - b = {a - b}")          # 7   (resta)
print(f"a * b = {a * b}")          # 30  (multiplicacion)
print(f"a / b = {a / b}")          # 3.333... (division - siempre da float)
print(f"a % b = {a % b}")          # 1   (modulo: el resto de dividir 10/3)
print(f"a // b = {a // b}")        # 3   (division entera: sin decimales)
print(f"a ** b = {a ** b}")        # 1000 (potencia: 10 elevado a 3)
print(f"raiz de a = {a ** 0.5}")   # 3.162... (raiz cuadrada = potencia 0.5)
print(f"(a+b)*2-5 = {(a + b) * 2 - 5}")  # 21

# RESUMEN OPERADORES ARITMETICOS:
# +   suma
# -   resta
# *   multiplicacion
# /   division (siempre devuelve float)
# //  division entera (redondea hacia -infinito: 7//2=3, -7//2=-4)
# %   modulo (resto de la division)
# **  potencia


# ---------------------------------------------------------------------------
# EJERCICIO 2: Operadores de comparacion
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2: Operadores de comparacion")
print("=" * 50)

a = 10
b = 3

print(f"a == b: {a == b}")         # False (10 no es igual a 3)
print(f"a != b: {a != b}")         # True  (10 es distinto de 3)
print(f"a > b: {a > b}")           # True  (10 es mayor que 3)
print(f"b <= a: {b <= a}")         # True  (3 es menor o igual que 10)
print(f"a+5 >= b*2: {a + 5 >= b * 2}")  # True (15 >= 6)

# IMPORTANTE: == compara valores, = asigna valores
# No confundir: a == b (compara) vs a = b (asigna)


# ---------------------------------------------------------------------------
# EJERCICIO 3: Operadores logicos
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 3: Operadores logicos")
print("=" * 50)

a = 10
b = 3

# and: ambas condiciones deben ser True
print(f"a>5 and b<5: {a > 5 and b < 5}")    # True (ambas son True)

# or: al menos una condicion debe ser True
print(f"a<5 or b<5: {a < 5 or b < 5}")      # True (b<5 es True)

# not: invierte el resultado
print(f"not (a==b): {not (a == b)}")          # True (a!=b, not False = True)

# Combinando and y not
print(f"a>5 and not a==10: {a > 5 and not a == 10}")  # False
# a > 5 es True, pero a == 10 tambien es True, not True = False
# True and False = False

# TABLA DE VERDAD:
# True  and True  = True
# True  and False = False
# False and True  = False
# False and False = False
#
# True  or True  = True
# True  or False = True
# False or True  = True
# False or False = False
#
# not True  = False
# not False = True


# ---------------------------------------------------------------------------
# EJERCICIO 4: Comparaciones con tipos mixtos
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 4: Tipos mixtos")
print("=" * 50)

A = 4
B = "Text"
C = 4.1

print(f"A == B: {A == B}")      # False (un int no es igual a un string)
print(f"A != C: {A != C}")      # True  (4 no es igual a 4.1)
print(f"A > C: {A > C}")        # False (4 no es mayor que 4.1)
print(f"C <= A: {C <= A}")      # False (4.1 no es menor o igual que 4)
print(f"B != C: {B != C}")      # True  (un string no es igual a un float)

# OJO: No se puede comparar con > o < un string con un numero
# print(B > C)  -> TypeError! No puedes ordenar texto vs numero


# ---------------------------------------------------------------------------
# EJERCICIO 5: Operadores de pertenencia
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 5: Operadores de pertenencia")
print("=" * 50)

numeros = [1, 2, 3, 4, 5]
print(f"3 in numeros: {3 in numeros}")          # True
print(f"6 not in numeros: {6 not in numeros}")   # True

texto = "python"
print(f"'y' in texto: {'y' in texto}")            # True
print(f"'z' not in texto: {'z' not in texto}")    # True

# "in" funciona con: listas, tuplas, strings, diccionarios, sets
# Es MUY util para buscar si algo existe dentro de una coleccion


# ---------------------------------------------------------------------------
# EJERCICIO 6: Operadores de asignacion
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 6: Operadores de asignacion")
print("=" * 50)

x = 10
print(f"x = {x}")       # 10

x += 5                   # x = x + 5
print(f"x += 5 -> {x}")  # 15

x -= 3                   # x = x - 3
print(f"x -= 3 -> {x}")  # 12

x *= 2                   # x = x * 2
print(f"x *= 2 -> {x}")  # 24

x /= 4                   # x = x / 4
print(f"x /= 4 -> {x}")  # 6.0 (division siempre da float)

x %= 3                   # x = x % 3
print(f"x %%= 3 -> {x}") # 0.0

x = 2                    # reseteamos para que el ejemplo tenga sentido
x **= 3                  # x = x ** 3
print(f"x **= 3 -> {x}") # 8

x //= 2                  # x = x // 2
print(f"x //= 2 -> {x}") # 4

# Son atajos: en vez de escribir x = x + 5, escribes x += 5


# ---------------------------------------------------------------------------
# EJERCICIO 7: Condicional simple
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 7: Condicional de notas")
print("=" * 50)

nota = 75

# if: primera condicion
# elif: "else if" - si la anterior no se cumple, prueba esta
# else: si ninguna se cumple, ejecuta esto

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Bueno")
elif nota >= 50:
    print("Suficiente")
else:
    print("Insuficiente")

# Con nota = 75, el resultado es "Bueno"
# IMPORTANTE: el orden importa! Python evalua de arriba a abajo
# y ejecuta el PRIMER bloque que sea True

# ESTRUCTURA:
# if condicion1:
#     codigo si condicion1 es True
# elif condicion2:
#     codigo si condicion2 es True (y condicion1 era False)
# elif condicion3:
#     codigo si condicion3 es True
# else:
#     codigo si NINGUNA condicion fue True


# ---------------------------------------------------------------------------
# EJERCICIO 8: Condicionales con diccionarios
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 8: Condicionales con diccionarios")
print("=" * 50)

gente = [
    {"nombre": "Jamiro", "edad": 45},
    {"nombre": "Juan",   "edad": 35},
    {"nombre": "Paco",   "edad": 34},
    {"nombre": "Pepe",   "edad": 14},
    {"nombre": "Pilar",  "edad": 24},
    {"nombre": "Laura",  "edad": 24},
    {"nombre": "Jenny",  "edad": 10},
]

# 1. Pepe - mayor o menor de edad
p = gente[3]  # {"nombre": "Pepe", "edad": 14}
if p["edad"] >= 18:
    print(f"{p['nombre']}: mayor de edad")
else:
    print(f"{p['nombre']}: menor de edad")
# Resultado: "Pepe: menor de edad"

# 2. Juan - empieza por J?
p = gente[1]
if p["nombre"].startswith("J"):
    print(f"{p['nombre']}: empieza por J")
else:
    print(f"{p['nombre']}: no empieza por J")

# 3. Paco - tiene 4 letras?
p = gente[2]
if len(p["nombre"]) == 4:
    print(f"{p['nombre']}: tiene 4 letras")
else:
    print(f"{p['nombre']}: no tiene 4 letras")

# 4. Pilar - edad par o impar?
p = gente[4]
if p["edad"] % 2 == 0:
    print(f"{p['nombre']}: edad par ({p['edad']})")
else:
    print(f"{p['nombre']}: edad impar ({p['edad']})")

# 5. Jamiro - termina en "o"?
p = gente[0]
if p["nombre"].endswith("o"):
    print(f"{p['nombre']}: termina en 'o'")
else:
    print(f"{p['nombre']}: no termina en 'o'")

# ACCESO A DICCIONARIOS:
# p["nombre"]  -> accede al valor de la clave "nombre"
# p["edad"]    -> accede al valor de la clave "edad"


# ---------------------------------------------------------------------------
# EJERCICIO 9: Condicionales con operadores logicos
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 9: Condicionales con logicos")
print("=" * 50)

# 1. Juan: empieza por J Y edad < 40
p = gente[1]
if p["nombre"].startswith("J") and p["edad"] < 40:
    print(f"{p['nombre']}: J y <40")
else:
    print(f"{p['nombre']}: no cumple")

# 2. Laura: contiene "a" (case-insensitive)
p = gente[5]
if "a" in p["nombre"].lower():
    print(f"{p['nombre']}: contiene 'a'")
else:
    print(f"{p['nombre']}: no contiene 'a'")
# .lower() convierte a minusculas para buscar sin importar mayus/minus

# 3. Pilar: edad entre 20 y 35
p = gente[4]
if 20 <= p["edad"] <= 35:
    print(f"{p['nombre']}: rango 20-35")
else:
    print(f"{p['nombre']}: fuera de rango")
# En Python puedes encadenar comparaciones: 20 <= x <= 35

# 4. Paco: NO empieza por J Y edad > 30
p = gente[2]
if not p["nombre"].startswith("J") and p["edad"] > 30:
    print(f"{p['nombre']}: no J y >30")
else:
    print(f"{p['nombre']}: no cumple")

# 5. Comparar Juan vs Paco: quien es mayor
a = gente[1]
b = gente[2]
if a["edad"] > b["edad"]:
    print(f"Mayor: {a['nombre']} ({a['edad']})")
elif b["edad"] > a["edad"]:
    print(f"Mayor: {b['nombre']} ({b['edad']})")
else:
    print("Empate de edad")


# ---------------------------------------------------------------------------
# EJERCICIO 10: Variable booleana
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 10: Booleano y condicional")
print("=" * 50)

festivo = True

if festivo:
    print("Hoy es fiesta, voy a descansar!")
else:
    print("No es fiesta, toca trabajar!")

# OJO: "if festivo:" es lo mismo que "if festivo == True:"
# Python entiende que si la variable es bool, puedes usarla directamente

# Valores "falsy" en Python (se evaluan como False):
# False, 0, 0.0, "", [], {}, None
# Todo lo demas es "truthy" (se evalua como True)


# ---------------------------------------------------------------------------
# EJERCICIO 11: Calculadora de IMC (estilo Harvard CS50P)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 11: Calculadora de IMC")
print("=" * 50)

peso_kg = 75
altura_m = 1.75

# Formula del IMC: peso dividido por altura al cuadrado
imc = peso_kg / (altura_m ** 2)

# Clasificacion con if/elif/else
if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"Peso: {peso_kg} kg, Altura: {altura_m} m")
print(f"IMC: {imc:.1f} -> {categoria}")

# Con peso=75, altura=1.75: IMC = 75 / (1.75^2) = 75 / 3.0625 = 24.5
# Resultado: "IMC: 24.5 -> Peso normal"

# EXPLICACION:
# - altura_m ** 2 calcula el cuadrado de la altura
# - No necesitamos "18.5 <= imc" en el segundo elif porque si llegamos
#   ahi, ya sabemos que imc >= 18.5 (la primera condicion fue False)
# - Esto es un patron MUY comun: clasificar un valor numerico en rangos
# - {imc:.1f} formatea el float con 1 decimal

# NOTA sobre salud: El IMC es una medida simplificada. No considera
# masa muscular, distribucion de grasa ni otros factores importantes.


# ---------------------------------------------------------------------------
# EJERCICIO 12: Clasificador de triangulos (MIT - pensamiento geometrico)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 12: Clasificador de triangulos")
print("=" * 50)

# Probamos con varios conjuntos de lados
casos = [
    (5, 5, 5),    # Equilatero
    (3, 4, 5),    # Escaleno + Rectangulo
    (5, 5, 3),    # Isosceles
    (1, 2, 10),   # No valido
]

for a, b, c in casos:
    print(f"\nLados: a={a}, b={b}, c={c}")

    # Paso 1: Verificar si es un triangulo valido
    # La desigualdad triangular: la suma de dos lados cualesquiera
    # debe ser MAYOR que el tercer lado
    es_valido = (a + b > c) and (a + c > b) and (b + c > a)

    if not es_valido:
        print("  -> No es un triangulo valido")
        continue  # Salta al siguiente caso

    # Paso 2: Clasificar el tipo de triangulo
    if a == b == c:
        tipo = "Equilatero (3 lados iguales)"
    elif a == b or b == c or a == c:
        tipo = "Isosceles (2 lados iguales)"
    else:
        tipo = "Escaleno (3 lados diferentes)"

    print(f"  -> {tipo}")

    # Paso 3: Comprobar si es rectangulo (Pitagoras)
    # Ordenamos los lados para que el mayor sea el ultimo
    lados = sorted([a, b, c])
    menor, medio, mayor = lados[0], lados[1], lados[2]

    # Usamos tolerancia para evitar errores de punto flotante
    # En vez de ==, comprobamos que la diferencia sea minuscula
    if abs(menor**2 + medio**2 - mayor**2) < 0.0001:
        print(f"  -> Es rectangulo! ({menor}^2 + {medio}^2 = "
              f"{menor**2} + {medio**2} = {menor**2 + medio**2} "
              f"= {mayor}^2 = {mayor**2})")
    else:
        print("  -> No es rectangulo")

# EXPLICACION:
# - sorted([a, b, c]) devuelve una lista ordenada de menor a mayor
# - continue: salta el resto del bucle y pasa a la siguiente iteracion
# - abs(): valor absoluto (convierte negativos a positivos)
# - La tolerancia (0.0001) es necesaria porque los floats no son exactos
#   Ejemplo: 0.1 + 0.2 = 0.30000000000000004 (no exactamente 0.3)
# - a == b == c: Python permite encadenar comparaciones de igualdad
# - a == b or b == c or a == c: basta que DOS lados sean iguales


print("\n--- Fin de las Soluciones Guia 2 ---")
