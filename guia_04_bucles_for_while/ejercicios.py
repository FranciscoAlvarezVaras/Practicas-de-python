# ============================================================================
# GUIA 4: BUCLES - FOR Y WHILE
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
# EJERCICIO 1: For con lista y multiplicacion
# ---------------------------------------------------------------------------
# Crea dos variables:
# - "multiplicador" con un numero (ej: 3)
# - "numeros" con una lista de numeros (ej: [1, 5, 10, 15, 20])
# Recorre la lista con un for e imprime cada numero multiplicado

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 2: Range con numeros negativos
# ---------------------------------------------------------------------------
# Imprime los numeros del -10 al -1 (en ese orden)
# Pista: usa range(inicio, fin, paso)
# Recuerda: range(fin) NO incluye el valor "fin"

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 3: Divisibles por 5 y por 7
# ---------------------------------------------------------------------------
# Imprime todos los numeros entre 150 y 350 que sean
# divisibles por 5 Y divisibles por 7 al mismo tiempo
# Pista: usa el operador modulo % y el operador "and"

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 4: Piramide invertida de numeros
# ---------------------------------------------------------------------------
# Imprime este patron:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
#
# Pista: necesitas un bucle dentro de otro (bucle anidado)
# El bucle exterior va de 5 a 1
# El interior va desde ese numero hasta 1

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 5: Contar numeros "especiales"
# ---------------------------------------------------------------------------
# Un numero es "especial" si:
# - Es multiplo de 3, O
# - Contiene el digito '3'
#
# Crea una lista de numeros (ej: [3, 7, 13, 15, 23, 30, 33, 40, 50])
# Cuenta cuantos son "especiales" e imprime el total
#
# Pista para saber si contiene el digito 3:
# Convierte el numero a string con str() y usa "in"

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 6: Cuenta atras con "Pum!"
# ---------------------------------------------------------------------------
# Escribe un programa que haga cuenta atras desde n = 20 hasta 0
# - En cada paso, imprime el numero
# - PERO si el numero es divisible por 4, imprime "Pum!" en vez del numero
# - Cuando llegue a 0, imprime "Despegue!" (0 siempre es "Despegue!", no "Pum!")
#
# Pista: usa un bucle for con range(n, -1, -1)

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 7: Contar mayusculas, minusculas y digitos
# ---------------------------------------------------------------------------
# Dado el string: "Ole Python como mola! Me esta encantando. De verdad que SI"
#
# Recorrelo caracter a caracter y cuenta:
# - Cuantas letras en mayuscula (.isupper())
# - Cuantas letras en minuscula (.islower())
# - Cuantos digitos (.isdigit())
#
# Imprime los tres totales con f-strings

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 8: Enumerate - indices y caracteres
# ---------------------------------------------------------------------------
# Dado el string: "Python es divertido"
#
# 1. Primero recorrelo usando range(len(frase)) para obtener indice y letra
# 2. Imprime: "Indice: X, Letra: Y"
# 3. Cuando encuentres un espacio, imprime: "Espacio encontrado!"
# 4. BONUS: Haz lo mismo pero usando enumerate()
#
# Pista enumerate:
# for indice, letra in enumerate("hola"):
#     print(indice, letra)
# Salida: 0 h, 1 o, 2 l, 3 a

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 9: While - suma acumulada hasta 100
# ---------------------------------------------------------------------------
# 1. Crea una lista de numeros enteros (ej: [15, 20, 8, 35, 12, 25, 30])
# 2. Inicializa una variable "total" en 0
# 3. Con un while, suma los numeros uno a uno
# 4. Imprime cada suma parcial
# 5. Cuando total pase de 100, imprime "Limite superado" y detente
#
# Pista: necesitas un indice que avance manualmente (i += 1)

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 10: For con break y continue
# ---------------------------------------------------------------------------
# Dada la lista: [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#
# Recorre la lista e imprime solo los divisibles por 5
# Si encuentras un numero mayor que 150, DETENTE (break)
#
# Pista: "continue" salta al siguiente paso del bucle
#        "break" sale del bucle completamente

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 11: While con input - redondeo de precios
# ---------------------------------------------------------------------------
# (Este ejercicio usa input(), ejecutalo en terminal)
#
# 1. Pide al usuario un precio con decimales (ej: 12.98765)
# 2. Pide cuantos decimales quiere mostrar (ej: 2)
# 3. Usa round(precio, decimales) para redondear
# 4. Imprime: "El precio redondeado es: X"
#
# Pista: input() siempre devuelve string, convierte con float() e int()
# Comenta este ejercicio si da problemas al ejecutar el archivo completo

# TU CODIGO AQUI (descomenta para probar):
# precio = float(input("Introduce un precio: "))
# decimales = int(input("Cuantos decimales? "))
# print(f"El precio redondeado es: {round(precio, decimales)}")


# ---------------------------------------------------------------------------
# EJERCICIO 12: Numeros primos (MIT 6.0001 - clasico)
# ---------------------------------------------------------------------------
# Escribe codigo que encuentre todos los numeros primos entre 2 y 100.
# Un numero es primo si solo es divisible por 1 y por si mismo.
# Para cada primo encontrado, imprimelo.
# Al final, imprime el total de primos encontrados.
#
# Pista: para cada numero n, comprueba si algun numero desde 2
# hasta la raiz cuadrada de n lo divide exactamente.
# Si ninguno lo divide, es primo.
# Puedes usar int(n ** 0.5) para calcular la raiz cuadrada entera.
#
# Ejemplo de salida:
# 2 es primo
# 3 es primo
# 5 es primo
# ...
# Total de primos entre 2 y 100: XX

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 13: Patron de diamante (MIT - patrones con bucles)
# ---------------------------------------------------------------------------
# Dado n = 5, imprime un patron de diamante usando * y espacios:
#
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
#
# La mitad superior va de 1 a (2*n - 1) estrellas (numeros impares)
# La mitad inferior va de (2*(n-1) - 1) estrellas hacia abajo hasta 1
#
# Pista para cada fila:
# - Calcula cuantos espacios poner antes de las estrellas
# - Calcula cuantas estrellas poner
# - Usa " " * espacios + "*" * estrellas para construir cada linea
#
# Parte superior: para i en range(n), estrellas = 2*i + 1, espacios = n - 1 - i
# Parte inferior: para i en range(n-2, -1, -1), misma formula

# TU CODIGO AQUI:




print("\n--- Fin de la Guia 4 ---")
print("Compara tus respuestas con soluciones.py!")
