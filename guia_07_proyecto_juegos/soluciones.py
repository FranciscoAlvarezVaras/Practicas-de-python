# ============================================================================
# GUIA 7 - SOLUCIONES: PROYECTO FINAL - JUEGOS INTERACTIVOS
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 4 y Ahorcado
# Enriquecido con: MIT 6.0001 (Blackjack), Harvard CS50P (juegos)
#
# NOTA: Estos juegos usan input(). Para ver las soluciones sin jugar,
# cada proyecto tiene una VERSION DEMO que se ejecuta sola con datos
# simulados, y la VERSION INTERACTIVA comentada.
# ============================================================================

import random


# ---------------------------------------------------------------------------
# PROYECTO 1: Adivina la palabra secreta
# ---------------------------------------------------------------------------
print("=" * 50)
print("PROYECTO 1: Adivina la palabra (DEMO)")
print("=" * 50)

# --- VERSION DEMO (sin input, para ver la logica) ---
lista = ['sol', 'luna', 'estrella', 'cielo', 'nube']
palabra_secreta = random.choice(lista)
vidas = 3

# Simulamos las respuestas del jugador
respuestas_simuladas = ['luna', 'sol', 'nube']
intento_num = 0

print(f"[DEMO] Palabra secreta: {palabra_secreta}")

while vidas > 0:
    respuesta = respuestas_simuladas[intento_num]
    print(f"Intento {intento_num + 1}: '{respuesta}'")

    if respuesta == palabra_secreta:
        print("Ganaste!")
        break
    else:
        vidas -= 1
        print(f"Incorrecto. Quedan {vidas} vidas")
    intento_num += 1
else:
    # El "else" del while se ejecuta si el while termina SIN break
    print(f"Perdiste! La palabra era: {palabra_secreta}")

# --- VERSION INTERACTIVA (descomenta para jugar de verdad) ---
# lista = ['sol', 'luna', 'estrella', 'cielo', 'nube']
# palabra_secreta = random.choice(lista)
# vidas = 3
#
# print("Adivina la palabra secreta!")
# print(f"Pistas: tiene {len(palabra_secreta)} letras")
#
# while vidas > 0:
#     respuesta = input(f"({vidas} vidas) Tu palabra: ").strip().lower()
#
#     if respuesta == palabra_secreta:
#         print("Ganaste!")
#         break
#     else:
#         vidas -= 1
#         if vidas > 0:
#             print(f"Incorrecto. Quedan {vidas} vidas")
# else:
#     print(f"Perdiste! La palabra era: {palabra_secreta}")

# CONCEPTOS USADOS:
# - random.choice(lista) -> elige un elemento al azar
# - while con condicion -> bucle que se repite mientras sea True
# - break -> sale del bucle inmediatamente
# - else del while -> se ejecuta si el while NO fue interrumpido por break
# - input() + .strip().lower() -> leer y limpiar entrada del usuario


# ---------------------------------------------------------------------------
# PROYECTO 2: Contador interactivo
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("PROYECTO 2: Contador interactivo (DEMO)")
print("=" * 50)

# --- VERSION DEMO ---
objetivo = random.randint(15, 25)
total = 0
intentos = 5

# Simulamos las jugadas
jugadas_simuladas = [4, 5, 3, 5, 4]
jugada_num = 0

print(f"Objetivo: {objetivo}")

while intentos > 0 and total < objetivo:
    numero = jugadas_simuladas[jugada_num]
    print(f"  Jugada: {numero}")
    total += numero
    intentos -= 1
    jugada_num += 1
    print(f"  Total: {total} | Intentos restantes: {intentos}")

    if total >= objetivo:
        print("Has alcanzado el objetivo!")
        break
else:
    if total < objetivo:
        print(f"Te has quedado sin intentos. Total: {total}/{objetivo}")

# --- VERSION INTERACTIVA (descomenta para jugar) ---
# objetivo = random.randint(15, 25)
# total = 0
# intentos = 5
#
# print(f"Debes alcanzar: {objetivo}")
# print("Suma numeros del 1 al 5 para llegar al objetivo")
#
# while intentos > 0 and total < objetivo:
#     try:
#         texto = input(f"({intentos} intentos, total={total}) Numero 1-5: ")
#         numero = int(texto)
#
#         if numero < 1 or numero > 5:
#             print("Solo numeros del 1 al 5")
#             continue  # vuelve al inicio del while sin gastar intento
#
#         total += numero
#         intentos -= 1
#         print(f"Total: {total}")
#
#         if total >= objetivo:
#             print("Has alcanzado el objetivo!")
#             break
#     except ValueError:
#         print("Eso no es un numero valido. Intenta de nuevo.")
# else:
#     print(f"Te has quedado sin intentos. Total: {total}/{objetivo}")

# CONCEPTOS USADOS:
# - random.randint(a, b) -> numero aleatorio entre a y b (ambos incluidos)
# - try/except ValueError -> manejar entrada no numerica
# - continue -> salta al siguiente paso del bucle (no gasta intento)
# - while con DOS condiciones (and)


# ---------------------------------------------------------------------------
# PROYECTO 3: Ahorcado simplificado
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("PROYECTO 3: Ahorcado (DEMO)")
print("=" * 50)

# --- VERSION DEMO ---
palabras = ["python", "variable", "funcion", "bucle", "clase"]
palabra = random.choice(palabras)
progreso = ["_"] * len(palabra)
intentos = 6
letras_usadas = []

# Simulamos las letras que introduce el jugador
letras_simuladas = list("aeioupythfnclsrbm")  # muchas letras para cubrir
letra_idx = 0

print(f"[DEMO] Palabra: {palabra} ({len(palabra)} letras)")
print(f"Progreso: {' '.join(progreso)}")

while intentos > 0 and "_" in progreso:
    if letra_idx >= len(letras_simuladas):
        break
    letra = letras_simuladas[letra_idx]
    letra_idx += 1

    # Saltar letras ya usadas
    if letra in letras_usadas:
        continue

    letras_usadas.append(letra)

    # Comprobar si la letra esta en la palabra
    if letra in palabra:
        # Actualizar progreso
        for i in range(len(palabra)):
            if palabra[i] == letra:
                progreso[i] = letra
        print(f"  '{letra}' -> Bien! {' '.join(progreso)}")
    else:
        intentos -= 1
        print(f"  '{letra}' -> No esta. Quedan {intentos} intentos")

# Resultado
if "_" not in progreso:
    print(f"GANASTE! La palabra era: {palabra}")
else:
    print(f"PERDISTE. La palabra era: {palabra}")

print(f"Letras usadas: {', '.join(letras_usadas)}")

# --- VERSION INTERACTIVA (descomenta para jugar) ---
# palabras = ["python", "variable", "funcion", "bucle", "clase"]
# palabra = random.choice(palabras)
# progreso = ["_"] * len(palabra)
# intentos = 6
# letras_usadas = []
#
# print("AHORCADO")
# print(f"La palabra tiene {len(palabra)} letras")
#
# while intentos > 0 and "_" in progreso:
#     print(f"\n{' '.join(progreso)}")
#     print(f"Intentos: {intentos} | Usadas: {', '.join(letras_usadas)}")
#
#     letra = input("Introduce una letra: ").strip().lower()
#
#     # Validaciones
#     if len(letra) != 1 or not letra.isalpha():
#         print("Introduce UNA sola letra")
#         continue
#
#     if letra in letras_usadas:
#         print("Ya usaste esa letra!")
#         continue
#
#     letras_usadas.append(letra)
#
#     if letra in palabra:
#         for i in range(len(palabra)):
#             if palabra[i] == letra:
#                 progreso[i] = letra
#         print("Bien!")
#     else:
#         intentos -= 1
#         print(f"No esta! Quedan {intentos} intentos")
#
# # Resultado final
# print(f"\n{' '.join(progreso)}")
# if "_" not in progreso:
#     print(f"GANASTE! La palabra era: {palabra}")
# else:
#     print(f"PERDISTE. La palabra era: {palabra}")

# CONCEPTOS USADOS:
# - ["_"] * len(palabra) -> crea lista de guiones del tamano de la palabra
# - " ".join(lista) -> une los elementos con espacio: "_ _ a _ _ o"
# - for i in range(len(palabra)) -> recorrer con indice
# - "_" not in progreso -> comprobar si quedan letras por adivinar
# - .isalpha() -> comprobar que es una letra
# - continue -> volver al inicio del while sin ejecutar el resto


# ---------------------------------------------------------------------------
# PROYECTO 4: Piedra, Papel, Tijeras (BONUS)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("PROYECTO 4: Piedra Papel Tijeras (DEMO)")
print("=" * 50)

# --- VERSION DEMO ---
opciones = ["piedra", "papel", "tijeras"]
victorias_j = 0
victorias_m = 0

# Simulamos 3 rondas
jugadas_jugador = ["piedra", "tijeras", "papel"]

for ronda in range(3):
    jugador = jugadas_jugador[ronda]
    maquina = random.choice(opciones)

    print(f"\nRonda {ronda + 1}: Jugador={jugador}, Maquina={maquina}")

    if jugador == maquina:
        print("  Empate!")
    elif ((jugador == "piedra" and maquina == "tijeras") or
          (jugador == "tijeras" and maquina == "papel") or
          (jugador == "papel" and maquina == "piedra")):
        print("  Gana el jugador!")
        victorias_j += 1
    else:
        print("  Gana la maquina!")
        victorias_m += 1

print(f"\nResultado final: Jugador {victorias_j} - {victorias_m} Maquina")
if victorias_j > victorias_m:
    print("EL JUGADOR GANA!")
elif victorias_m > victorias_j:
    print("LA MAQUINA GANA!")
else:
    print("EMPATE!")

# --- VERSION INTERACTIVA (descomenta para jugar) ---
# opciones = ["piedra", "papel", "tijeras"]
# victorias_j = 0
# victorias_m = 0
#
# for ronda in range(3):
#     print(f"\n--- Ronda {ronda + 1} ---")
#     jugador = input("Elige (piedra/papel/tijeras): ").strip().lower()
#
#     if jugador not in opciones:
#         print("Opcion no valida!")
#         continue
#
#     maquina = random.choice(opciones)
#     print(f"Maquina eligio: {maquina}")
#
#     if jugador == maquina:
#         print("Empate!")
#     elif (jugador == "piedra" and maquina == "tijeras" or
#           jugador == "tijeras" and maquina == "papel" or
#           jugador == "papel" and maquina == "piedra"):
#         print("Ganas tu!")
#         victorias_j += 1
#     else:
#         print("Gana la maquina!")
#         victorias_m += 1
#
# print(f"\nFINAL: Tu {victorias_j} - {victorias_m} Maquina")


# ---------------------------------------------------------------------------
# PROYECTO 5: Blackjack simplificado (MIT 6.0001 estilo proyecto final)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("PROYECTO 5: Blackjack simplificado (DEMO)")
print("=" * 50)

# --- VERSION DEMO (sin input, decisiones simuladas) ---

# Definir la baraja: 4 palos x 13 cartas
cartas = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
baraja = cartas * 4  # 52 cartas (4 palos)

# Diccionario con el valor de cada carta
valores = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
    '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}


def calcular_mano(mano):
    """Calcula el valor total de una mano de Blackjack.
    Si hay Ases y el total supera 21, el As vale 1 en vez de 11."""
    total = 0
    ases = 0
    for carta in mano:
        total += valores[carta]
        if carta == 'A':
            ases += 1
    # Si nos pasamos de 21 y tenemos Ases, convertir de 11 a 1
    while total > 21 and ases > 0:
        total -= 10  # 11 - 10 = 1 (el As pasa a valer 1)
        ases -= 1
    return total


def mostrar_mano(nombre, mano, ocultar_primera=False):
    """Muestra las cartas de una mano."""
    if ocultar_primera:
        cartas_str = "[??] " + " ".join(mano[1:])
        print(f"  {nombre}: {cartas_str}")
    else:
        cartas_str = " ".join(mano)
        total = calcular_mano(mano)
        print(f"  {nombre}: {cartas_str} (Total: {total})")


def repartir_carta(baraja_actual):
    """Reparte una carta aleatoria de la baraja.
    NOTA: Usa random.choice (con reemplazo). En un Blackjack real,
    las cartas se retiran de la baraja al repartirse."""
    return random.choice(baraja_actual)


# --- Inicio del juego ---
print("\n--- Nueva partida de Blackjack ---\n")

# Repartir cartas iniciales
mano_jugador = [repartir_carta(baraja), repartir_carta(baraja)]
mano_dealer = [repartir_carta(baraja), repartir_carta(baraja)]

# Mostrar manos iniciales (dealer oculta una carta)
print("Reparto inicial:")
mostrar_mano("Jugador", mano_jugador)
mostrar_mano("Dealer", mano_dealer, ocultar_primera=True)

# Turno del jugador (DEMO: decisiones simuladas)
# Estrategia simple: pedir si tiene menos de 17, plantarse si tiene 17 o mas
print("\n--- Turno del jugador ---")

while calcular_mano(mano_jugador) < 17:
    nueva_carta = repartir_carta(baraja)
    mano_jugador.append(nueva_carta)
    print(f"  Jugador pide carta: {nueva_carta}")
    mostrar_mano("Jugador", mano_jugador)

    if calcular_mano(mano_jugador) > 21:
        print("  SE PASO! El jugador supero 21")
        break

total_jugador = calcular_mano(mano_jugador)

if total_jugador <= 21:
    print(f"  Jugador se planta con {total_jugador}")

    # Turno del dealer: roba hasta tener 17 o mas
    print("\n--- Turno del dealer ---")
    mostrar_mano("Dealer", mano_dealer)

    while calcular_mano(mano_dealer) < 17:
        nueva_carta = repartir_carta(baraja)
        mano_dealer.append(nueva_carta)
        print(f"  Dealer pide carta: {nueva_carta}")
        mostrar_mano("Dealer", mano_dealer)

    total_dealer = calcular_mano(mano_dealer)

    # Determinar ganador
    print("\n--- Resultado ---")
    mostrar_mano("Jugador", mano_jugador)
    mostrar_mano("Dealer", mano_dealer)

    if total_dealer > 21:
        print("  Dealer se paso de 21. JUGADOR GANA!")
    elif total_jugador > total_dealer:
        print("  JUGADOR GANA!")
    elif total_dealer > total_jugador:
        print("  DEALER GANA!")
    else:
        print("  EMPATE!")
else:
    print("\n--- Resultado ---")
    mostrar_mano("Jugador", mano_jugador)
    mostrar_mano("Dealer", mano_dealer)
    print("  Jugador se paso de 21. DEALER GANA!")

# --- VERSION INTERACTIVA (descomenta para jugar de verdad) ---
# mano_jugador = [repartir_carta(baraja), repartir_carta(baraja)]
# mano_dealer = [repartir_carta(baraja), repartir_carta(baraja)]
#
# print("Reparto inicial:")
# mostrar_mano("Jugador", mano_jugador)
# mostrar_mano("Dealer", mano_dealer, ocultar_primera=True)
#
# # Turno del jugador
# while calcular_mano(mano_jugador) <= 21:
#     decision = input("Pedir o Plantarse? (p/s): ").strip().lower()
#     if decision == 'p':
#         nueva_carta = repartir_carta(baraja)
#         mano_jugador.append(nueva_carta)
#         mostrar_mano("Jugador", mano_jugador)
#         if calcular_mano(mano_jugador) > 21:
#             print("TE PASASTE de 21!")
#             break
#     elif decision == 's':
#         break
#     else:
#         print("Escribe 'p' para pedir o 's' para plantarte")
#
# total_jugador = calcular_mano(mano_jugador)
# if total_jugador <= 21:
#     print("\nTurno del dealer:")
#     mostrar_mano("Dealer", mano_dealer)
#     while calcular_mano(mano_dealer) < 17:
#         nueva_carta = repartir_carta(baraja)
#         mano_dealer.append(nueva_carta)
#         mostrar_mano("Dealer", mano_dealer)
#     total_dealer = calcular_mano(mano_dealer)
#     if total_dealer > 21:
#         print("El dealer se paso! GANAS!")
#     elif total_jugador > total_dealer:
#         print("GANAS!")
#     elif total_dealer > total_jugador:
#         print("PIERDE! Gana el dealer")
#     else:
#         print("EMPATE!")
# else:
#     print("Dealer gana. Mejor suerte la proxima.")

# CONCEPTOS USADOS:
# - Funciones con parametros por defecto (ocultar_primera=False)
# - Diccionarios para mapear cartas a valores
# - Listas como manos de cartas
# - random.choice() para repartir cartas aleatorias
# - Bucles while con condicion para decidir hit/stand
# - Logica condicional para determinar ganador
# - El As flexible (11 o 1) es un problema clasico de MIT 6.0001


# ============================================================================
# RESUMEN FINAL: QUE HEMOS APRENDIDO
# ============================================================================
print("\n" + "=" * 60)
print("RESUMEN: TODO LO QUE HAS APRENDIDO EN PYTHON")
print("=" * 60)

print("""
GUIA 1: Variables y Tipos de Datos
  - Crear variables (int, float, str, bool)
  - f-strings para formatear texto
  - len(), type(), del
  - Metodos de strings: .upper(), .lower(), .split(), .replace()

GUIA 2: Operadores y Condicionales
  - Aritmeticos: + - * / // % **
  - Comparacion: == != > < >= <=
  - Logicos: and, or, not
  - Pertenencia: in, not in
  - Condicionales: if, elif, else

GUIA 3: Listas, Tuplas y Diccionarios
  - Listas []: .append(), .insert(), .remove(), .pop(), .sort()
  - Tuplas (): inmutables, desempaquetado
  - Diccionarios {}: .keys(), .values(), .items(), .get(), .pop()
  - Slicing: lista[inicio:fin:paso]

GUIA 4: Bucles
  - for: recorrer listas, range(), enumerate()
  - while: condicion, break, continue
  - Bucles anidados
  - else del while

GUIA 5: Funciones
  - def, return, parametros posicionales
  - *args, **kwargs
  - Parametros por defecto
  - Keyword-only arguments
  - Lambda functions

GUIA 6: Clases, Excepciones y Modulos
  - class, __init__, self, metodos
  - try/except/else/finally
  - raise para lanzar errores
  - import, modulos: math, random, os, requests
  - Lectura de archivos con open() y with

GUIA 7: Proyectos (combinando todo)
  - Juego de adivinar palabras
  - Contador interactivo
  - Ahorcado
  - Piedra, Papel, Tijeras
  - Blackjack simplificado (MIT 6.0001)

Siguiente paso: Practica, practica, practica!
""")

print("--- Fin de las Soluciones Guia 7 ---")
