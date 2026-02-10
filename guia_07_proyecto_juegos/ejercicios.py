# ============================================================================
# GUIA 7: PROYECTO FINAL - JUEGOS INTERACTIVOS
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 4 (Juegos) y Ahorcado
# Enriquecido con: MIT 6.0001 (Blackjack), Harvard CS50P (juegos)
#
# En esta guia ponemos en practica TODO lo aprendido:
# Variables, condicionales, bucles, funciones, listas, diccionarios,
# input/output, random, try/except
#
# INSTRUCCIONES:
# - Estos ejercicios usan input(), asi que ejecutalos uno a uno
# - Escribe tu codigo en "# TU CODIGO AQUI"
# - Ejecuta: python ejercicios.py
# ============================================================================

import random  # Lo necesitaremos para varios juegos


# ---------------------------------------------------------------------------
# PROYECTO 1: Adivina la palabra secreta
# ---------------------------------------------------------------------------
# Reglas:
# - Hay una lista de 5 palabras
# - random.choice() elige una al azar
# - El jugador tiene 3 intentos para adivinarla
# - Si acierta: "Ganaste!"
# - Si se queda sin intentos: "Perdiste! La palabra era: X"
#
# Pasos:
# 1. Crea la lista de palabras
# 2. Usa random.choice(lista) para elegir la secreta
# 3. Variable "vidas" = 3
# 4. Bucle while: mientras queden vidas
# 5. Dentro: pide input, compara, actualiza vidas
# 6. Si acierta: print y break
# 7. Si pierde: usa el "else" del while para el mensaje de derrota
#
# PISTA: el "else" de un while se ejecuta si el while termina
# SIN break (es decir, si se agotaron las vidas)

# TU CODIGO AQUI (descomenta para jugar):
# lista = ['sol', 'luna', 'estrella', 'cielo', 'nube']
# palabra_secreta = random.choice(lista)
# vidas = 3
# ...


# ---------------------------------------------------------------------------
# PROYECTO 2: Contador interactivo
# ---------------------------------------------------------------------------
# Reglas:
# - random.randint(15, 25) genera el numero objetivo
# - El jugador suma numeros del 1 al 5 para llegar al objetivo
# - Tiene 5 intentos
# - Si alcanza o supera el objetivo: "Has alcanzado el objetivo!"
# - Si se acaban los intentos: "Te has quedado sin intentos"
#
# Pasos:
# 1. objetivo = random.randint(15, 25)
# 2. total = 0, intentos = 5
# 3. while: intentos > 0 y total < objetivo
# 4. Pedir input (numero 1-5), convertir a int
# 5. Usar try/except ValueError por si no es numero
# 6. Sumar al total, restar intento
# 7. Comprobar si gano o perdio

# TU CODIGO AQUI (descomenta para jugar):
# objetivo = random.randint(15, 25)
# print(f"Debes alcanzar: {objetivo}")
# total = 0
# intentos = 5
# ...


# ---------------------------------------------------------------------------
# PROYECTO 3: Ahorcado simplificado
# ---------------------------------------------------------------------------
# Este es el proyecto mas completo. Combina TODO lo aprendido.
#
# Reglas:
# - Hay una lista de palabras
# - Se elige una al azar
# - El jugador intenta adivinar letra a letra
# - Tiene un numero limitado de intentos (por ejemplo 6)
# - Se muestra el progreso: _ _ a _ _ o
# - Si adivina toda la palabra: gana
# - Si se queda sin intentos: pierde
#
# Pasos detallados:
# 1. Lista de palabras y elegir una con random.choice()
# 2. Crear una lista "progreso" con "_" del mismo largo que la palabra
#    Pista: progreso = ["_"] * len(palabra)
# 3. Variable intentos (6) y lista "letras_usadas" (vacia)
# 4. Bucle while: mientras queden intentos Y haya "_" en progreso
# 5. Mostrar progreso: " ".join(progreso) -> "_ _ a _ _ o"
# 6. Pedir una letra al usuario
# 7. Comprobar si ya la uso (si esta en letras_usadas)
# 8. Si la letra esta en la palabra: actualizar progreso
#    (recorrer la palabra y donde coincida, poner la letra)
# 9. Si NO esta: restar un intento
# 10. Al final: comprobar si gano o perdio
#
# PISTAS:
# - Para recorrer la palabra con indice: for i in range(len(palabra))
# - Para actualizar: if palabra[i] == letra: progreso[i] = letra
# - Para comprobar si gano: "_" not in progreso

# TU CODIGO AQUI (descomenta para jugar):
# palabras = ["python", "variable", "funcion", "bucle", "clase"]
# palabra = random.choice(palabras)
# progreso = ["_"] * len(palabra)
# intentos = 6
# letras_usadas = []
# ...


# ---------------------------------------------------------------------------
# PROYECTO 4: Piedra, Papel, Tijeras (BONUS)
# ---------------------------------------------------------------------------
# Reglas:
# - El jugador elige: piedra, papel o tijeras
# - La maquina elige al azar con random.choice()
# - Piedra gana a Tijeras, Tijeras gana a Papel, Papel gana a Piedra
# - Se juegan 3 rondas
# - Al final se muestra quien gano mas rondas
#
# Pasos:
# 1. opciones = ["piedra", "papel", "tijeras"]
# 2. Contadores: victorias_jugador = 0, victorias_maquina = 0
# 3. Bucle for de 3 rondas
# 4. Pedir input al jugador
# 5. Maquina elige con random.choice(opciones)
# 6. Comparar y actualizar contadores
# 7. Al final: mostrar resultado

# TU CODIGO AQUI (descomenta para jugar):
# opciones = ["piedra", "papel", "tijeras"]
# victorias_j = 0
# victorias_m = 0
# ...


# ---------------------------------------------------------------------------
# PROYECTO 5: Blackjack simplificado (MIT 6.0001 estilo proyecto final)
# ---------------------------------------------------------------------------
# Reglas del Blackjack simplificado:
# - Las cartas del 2 al 10 valen su numero
# - J, Q, K valen 10
# - A (As) vale 11, pero si te pasas de 21 vale 1
# - Se reparten 2 cartas al jugador y 2 al dealer
# - El jugador puede "pedir" carta o "plantarse"
# - Si el jugador supera 21, pierde (se paso)
# - Si se planta, el dealer roba hasta tener 17 o mas
# - Gana quien este mas cerca de 21 sin pasarse
#
# Pasos:
# 1. Crea una lista "baraja" con las cartas: 2-10, J, Q, K, A
#    (repite x4 para los 4 palos)
# 2. Usa random.choice(baraja) para repartir cartas
# 3. Crea una funcion "calcular_mano(mano)" que devuelva el valor total
#    - Suma el valor de cada carta
#    - Si hay un As y el total supera 21, cuenta el As como 1 en vez de 11
# 4. Crea una funcion "mostrar_mano(nombre, mano)" que imprima las cartas
# 5. Logica del juego:
#    a. Repartir 2 cartas al jugador y 2 al dealer
#    b. Mostrar cartas del jugador y UNA del dealer
#    c. El jugador decide: pedir o plantarse (en DEMO, simula las decisiones)
#    d. Si el jugador se pasa de 21, pierde
#    e. Si se planta, el dealer roba hasta >= 17
#    f. Comparar totales y determinar ganador
#
# PISTA: Para el valor de las cartas, usa un diccionario:
# valores = {'2': 2, '3': 3, ..., '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
#
# NOTA: Esta es una VERSION DEMO con decisiones simuladas (sin input)

# TU CODIGO AQUI:




print("\n--- Fin de la Guia 7 ---")
print("Estos son proyectos completos que combinan todo lo aprendido.")
print("Mira soluciones.py para ver las soluciones comentadas.")
