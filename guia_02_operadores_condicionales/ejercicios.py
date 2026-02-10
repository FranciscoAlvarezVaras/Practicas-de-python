# ============================================================================
# GUIA 2: OPERADORES Y CONDICIONALES
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 1 (Ej. 4, 8) y Repaso
# Enriquecido con: MIT 6.0001 (OCW), Harvard CS50P (condicionales)
#
# INSTRUCCIONES:
# - Lee cada ejercicio con atencion
# - Escribe tu codigo debajo de "# TU CODIGO AQUI"
# - Ejecuta: python ejercicios.py
# ============================================================================


# ---------------------------------------------------------------------------
# EJERCICIO 1: Operadores aritmeticos
# ---------------------------------------------------------------------------
# Crea dos variables: a = 10, b = 3
# Calcula e imprime:
# 1. La suma (a + b)
# 2. La resta (a - b)
# 3. La multiplicacion (a * b)
# 4. La division (a / b)
# 5. El modulo - resto de la division (a % b)
# 6. La division entera (a // b)
# 7. La potencia (a ** b)
# 8. La raiz cuadrada de a (pista: a ** 0.5)
# 9. El resultado de: (a + b) * 2 - 5

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 2: Operadores de comparacion
# ---------------------------------------------------------------------------
# Usando a = 10, b = 3, calcula e imprime (el resultado sera True o False):
# 1. a es igual a b?            (==)
# 2. a es distinto de b?        (!=)
# 3. a es mayor que b?          (>)
# 4. b es menor o igual que a?  (<=)
# 5. a + 5 es mayor o igual que b * 2?   (>=)

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 3: Operadores logicos (and, or, not)
# ---------------------------------------------------------------------------
# Usando a = 10, b = 3:
# 1. a > 5 Y b < 5? (and)
# 2. a < 5 O b < 5? (or)
# 3. Aplica "not" a (a == b)
# 4. a es mayor que 5 Y NO es igual a 10?

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 4: Comparaciones con tipos mixtos
# ---------------------------------------------------------------------------
# Dadas estas variables:
# A = 4
# B = "Text"
# C = 4.1
#
# Comprueba e imprime:
# 1. A y B son equivalentes?
# 2. A y C NO son equivalentes?
# 3. A es mayor que C?
# 4. C es menor o igual que A?
# 5. B NO es equivalente a C?

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 5: Operadores de pertenencia (in, not in)
# ---------------------------------------------------------------------------
# 1. Crea una lista: numeros = [1, 2, 3, 4, 5]
# 2. Comprueba si 3 esta en la lista
# 3. Comprueba si 6 NO esta en la lista
# 4. Crea un string: texto = "python"
# 5. Comprueba si "y" esta en texto
# 6. Comprueba si "z" NO esta en texto

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 6: Operadores de asignacion (+=, -=, *=, etc.)
# ---------------------------------------------------------------------------
# 1. Crea x = 10
# 2. Sumale 5 con +=
# 3. Restale 3 con -=
# 4. Multiplica por 2 con *=
# 5. Divide entre 4 con /=
# 6. Calcula el modulo entre 3 con %=
# 7. Eleva a la potencia 3 con **=
# 8. Division entera entre 2 con //=
# Imprime x despues de cada operacion para ver como cambia

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 7: Condicional simple (if/else)
# ---------------------------------------------------------------------------
# Crea una variable "nota" con un valor entre 0 y 100.
# Imprime segun la nota:
# - >= 90: "Excelente"
# - 70-89: "Bueno"
# - 50-69: "Suficiente"
# - < 50: "Insuficiente"
#
# Pista: usa if, elif, elif, else

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 8: Condicionales con diccionarios
# ---------------------------------------------------------------------------
# Dada esta lista de personas:
#
# gente = [
#     {"nombre": "Jamiro", "edad": 45},
#     {"nombre": "Juan",   "edad": 35},
#     {"nombre": "Paco",   "edad": 34},
#     {"nombre": "Pepe",   "edad": 14},
#     {"nombre": "Pilar",  "edad": 24},
#     {"nombre": "Laura",  "edad": 24},
#     {"nombre": "Jenny",  "edad": 10},
# ]
#
# 1. Usando gente[3] (Pepe): imprime "mayor" si edad >= 18, sino "menor"
# 2. Usando gente[1] (Juan): imprime si su nombre empieza por "J" o no
# 3. Usando gente[2] (Paco): imprime si su nombre tiene 4 letras o no
# 4. Usando gente[4] (Pilar): imprime si su edad es par o impar
# 5. Usando gente[0] (Jamiro): imprime si su nombre termina en "o" o no

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 9: Condicionales con operadores logicos
# ---------------------------------------------------------------------------
# Usando la misma lista "gente" del ejercicio anterior:
#
# 1. gente[1] (Juan): imprime "J y <40" si empieza por J Y edad < 40
# 2. gente[5] (Laura): imprime "contiene a" si la "a" esta en su nombre
#    (sin importar mayusculas)
# 3. gente[4] (Pilar): imprime "rango 20-35" si edad entre 20 y 35
# 4. gente[2] (Paco): imprime "no J y >30" si NO empieza por J Y edad > 30
# 5. Compara gente[1] y gente[2]: imprime quien es mayor de edad

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 10: Variable booleana y condicional
# ---------------------------------------------------------------------------
# 1. Crea una variable "festivo" de tipo bool (True o False)
# 2. Si festivo es True, imprime: "Hoy es fiesta, voy a descansar!"
# 3. Si festivo es False, imprime: "No es fiesta, toca trabajar!"

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 11: Calculadora de IMC (estilo Harvard CS50P)
# ---------------------------------------------------------------------------
# El Indice de Masa Corporal (IMC/BMI) se calcula como:
#   IMC = peso_kg / (altura_m ** 2)
#
# 1. Crea las variables: peso_kg = 75, altura_m = 1.75
# 2. Calcula el IMC y guardalo en una variable
# 3. Imprime el IMC con 1 decimal
# 4. Clasifica el resultado con if/elif/else:
#    - IMC < 18.5:        "Bajo peso"
#    - 18.5 <= IMC < 25:  "Peso normal"
#    - 25 <= IMC < 30:    "Sobrepeso"
#    - IMC >= 30:         "Obesidad"
# 5. Imprime un mensaje completo, ejemplo:
#    "IMC: 24.5 -> Peso normal"

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 12: Clasificador de triangulos (MIT - pensamiento geometrico)
# ---------------------------------------------------------------------------
# Dados 3 lados de un posible triangulo: a = 5, b = 5, c = 5
#
# 1. Primero verifica si forman un triangulo valido:
#    La suma de cualquier par de lados debe ser MAYOR que el tercer lado
#    (a + b > c) AND (a + c > b) AND (b + c > a)
#
# 2. Si NO es valido, imprime: "No es un triangulo valido"
#
# 3. Si ES valido, clasifica el tipo:
#    - Equilatero: los 3 lados son iguales
#    - Isosceles: exactamente 2 lados son iguales
#    - Escaleno: los 3 lados son diferentes
#
# 4. Ademas, comprueba si es un triangulo rectangulo:
#    Ordena los lados de menor a mayor y comprueba si:
#    lado_menor**2 + lado_medio**2 == lado_mayor**2 (Teorema de Pitagoras)
#    PISTA: usa sorted([a, b, c]) para ordenarlos
#    PISTA: por decimales, compara con una tolerancia:
#    abs(menor**2 + medio**2 - mayor**2) < 0.0001
#
# 5. Prueba con estos valores y verifica tus resultados:
#    a=5, b=5, c=5   -> Equilatero
#    a=3, b=4, c=5   -> Escaleno + Rectangulo
#    a=5, b=5, c=3   -> Isosceles
#    a=1, b=2, c=10  -> No valido

# TU CODIGO AQUI:




print("\n--- Fin de la Guia 2 ---")
print("Compara tus respuestas con soluciones.py!")
