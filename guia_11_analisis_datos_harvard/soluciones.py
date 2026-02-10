# ============================================================================
# GUIA 11 - SOLUCIONES: ANALISIS DE DATOS (Estilo Harvard/MIT)
# ============================================================================
# Autor: Francisco Alvarez Varas
# ============================================================================

import csv
import json
import math
import random
import string
from collections import Counter
from datetime import datetime, timedelta


# ---------------------------------------------------------------------------
# EJERCICIO 1: Dataset de alumnos
# ---------------------------------------------------------------------------
print("=" * 60)
print("EJERCICIO 1: Analisis de alumnos")
print("=" * 60)

# Generar dataset
random.seed(42)  # seed fija para resultados reproducibles
NOMBRES = ["Ana", "Carlos", "Maria", "Luis", "Pilar", "Juan", "Laura",
           "Pedro", "Sofia", "Diego", "Elena", "Pablo", "Clara", "Jorge",
           "Marta", "Raul", "Lucia", "Alberto", "Rosa", "Francisco"]
GRUPOS = ["MDAA", "MDAB", "MIA"]

alumnos = []
for i in range(50):
    alumnos.append({
        "nombre": random.choice(NOMBRES) + f"_{i}",
        "edad": random.randint(18, 35),
        "nota_python": round(random.uniform(3, 10), 1),
        "nota_sql": round(random.uniform(2, 10), 1),
        "nota_docker": round(random.uniform(1, 10), 1),
        "grupo": random.choice(GRUPOS)
    })


def nota_media_alumno(alumno):
    """Calcula la media de las 3 asignaturas."""
    notas = [alumno["nota_python"], alumno["nota_sql"], alumno["nota_docker"]]
    return round(sum(notas) / len(notas), 2)


def mejores_alumnos(dataset, n=5):
    """Devuelve los n mejores alumnos por nota media."""
    con_media = [(a, nota_media_alumno(a)) for a in dataset]
    ordenados = sorted(con_media, key=lambda x: x[1], reverse=True)
    return ordenados[:n]


def estadisticas_por_grupo(dataset):
    """Calcula estadisticas por grupo."""
    grupos = {}
    for alumno in dataset:
        g = alumno["grupo"]
        if g not in grupos:
            grupos[g] = []
        grupos[g].append(nota_media_alumno(alumno))

    resultado = {}
    for grupo, medias in grupos.items():
        resultado[grupo] = {
            "n_alumnos": len(medias),
            "media": round(sum(medias) / len(medias), 2),
            "min": round(min(medias), 2),
            "max": round(max(medias), 2),
        }
    return resultado


def distribucion_notas(dataset, asignatura):
    """Distribuye notas en rangos."""
    rangos = {"Suspenso grave (0-2)": 0, "Suspenso (2-5)": 0,
              "Aprobado (5-7)": 0, "Notable (7-9)": 0,
              "Sobresaliente (9-10)": 0}

    for alumno in dataset:
        nota = alumno[asignatura]
        if nota < 2:
            rangos["Suspenso grave (0-2)"] += 1
        elif nota < 5:
            rangos["Suspenso (2-5)"] += 1
        elif nota < 7:
            rangos["Aprobado (5-7)"] += 1
        elif nota < 9:
            rangos["Notable (7-9)"] += 1
        else:
            rangos["Sobresaliente (9-10)"] += 1

    return rangos


# Mostrar resultados
print("\n  Top 5 mejores alumnos:")
for alumno, media in mejores_alumnos(alumnos, 5):
    print(f"    {alumno['nombre']} ({alumno['grupo']}): {media}")

print("\n  Estadisticas por grupo:")
for grupo, stats in estadisticas_por_grupo(alumnos).items():
    print(f"    {grupo}: media={stats['media']}, "
          f"min={stats['min']}, max={stats['max']}, "
          f"n={stats['n_alumnos']}")

print("\n  Distribucion notas Python:")
for rango, cantidad in distribucion_notas(alumnos, "nota_python").items():
    barra = "#" * cantidad
    print(f"    {rango:<25} {barra} ({cantidad})")

# random.seed(42) -> hace que random genere siempre los mismos numeros
# Esto es CLAVE en ciencia de datos para reproducibilidad


# ---------------------------------------------------------------------------
# EJERCICIO 2: Analisis de ventas con grafico
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 2: Ventas mensuales")
print("=" * 60)

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

ventas_mensuales = []
for i, mes in enumerate(MESES):
    base = 8000 + i * 200  # tendencia creciente
    ventas_mensuales.append({
        "mes": mes,
        "ingresos": round(base + random.uniform(-1000, 2000), 2),
        "gastos": round(base * 0.6 + random.uniform(-500, 500), 2),
        "clientes_nuevos": random.randint(10, 50)
    })


def beneficio_mensual(datos):
    return [{"mes": d["mes"],
             "beneficio": round(d["ingresos"] - d["gastos"], 2)} for d in datos]


def mejor_mes(datos):
    beneficios = beneficio_mensual(datos)
    return max(beneficios, key=lambda x: x["beneficio"])


def peor_mes(datos):
    beneficios = beneficio_mensual(datos)
    return min(beneficios, key=lambda x: x["beneficio"])


def tendencia(datos):
    beneficios = beneficio_mensual(datos)
    primera_mitad = sum(b["beneficio"] for b in beneficios[:6]) / 6
    segunda_mitad = sum(b["beneficio"] for b in beneficios[6:]) / 6
    diferencia = segunda_mitad - primera_mitad
    if diferencia > 500:
        return "creciente"
    elif diferencia < -500:
        return "decreciente"
    return "estable"


def grafico_texto(datos, escala=200):
    """Genera un grafico de barras en la terminal."""
    beneficios = beneficio_mensual(datos)
    print(f"\n  Grafico de beneficios (cada bloque = {escala} EUR):")
    for b in beneficios:
        bloques = max(0, int(b["beneficio"] / escala))
        barra = "#" * bloques
        print(f"    {b['mes']:<12} | {barra} {b['beneficio']:,.0f}")


print(f"  Mejor mes: {mejor_mes(ventas_mensuales)}")
print(f"  Peor mes: {peor_mes(ventas_mensuales)}")
print(f"  Tendencia: {tendencia(ventas_mensuales)}")
grafico_texto(ventas_mensuales)


# ---------------------------------------------------------------------------
# EJERCICIO 3: Limpieza de datos
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 3: Limpieza de datos")
print("=" * 60)

datos_sucios = [
    {"nombre": " Ana García ", "email": "ANA@EMAIL.COM", "edad": "25", "salario": "30,000"},
    {"nombre": "carlos  LOPEZ", "email": "carlos@email", "edad": "abc", "salario": "28000"},
    {"nombre": "", "email": "maria@email.com", "edad": "30", "salario": "35000"},
    {"nombre": "Luis Pérez", "email": "luis@email.com", "edad": "-5", "salario": ""},
    {"nombre": "Luis Pérez", "email": "luis@email.com", "edad": "28", "salario": "32000"},
]


def limpiar_nombre(nombre):
    """Quita espacios extra y pone formato Titulo."""
    nombre = " ".join(nombre.split())  # quita espacios multiples
    return nombre.title() if nombre else None


def limpiar_email(email):
    """Limpia y valida un email."""
    email = email.strip().lower()
    if "@" in email and "." in email.split("@")[-1]:
        return email
    return None  # email no valido


def limpiar_edad(edad):
    """Convierte a int y valida."""
    try:
        edad_int = int(edad)
        if 0 < edad_int < 120:
            return edad_int
    except (ValueError, TypeError):
        pass
    return None


def limpiar_salario(salario):
    """Limpia y convierte salario."""
    if not salario:
        return None
    try:
        salario_limpio = salario.replace(",", "").replace(" ", "")
        return float(salario_limpio)
    except ValueError:
        return None


def eliminar_duplicados(dataset):
    """Elimina filas duplicadas basandose en nombre + email."""
    vistos = set()
    unicos = []
    for fila in dataset:
        clave = (fila.get("nombre", ""), fila.get("email", ""))
        if clave not in vistos:
            vistos.add(clave)
            unicos.append(fila)
    return unicos


def limpiar_dataset(dataset):
    """Aplica todas las limpiezas y devuelve datos limpios."""
    limpios = []
    errores = 0

    for fila in dataset:
        limpia = {
            "nombre": limpiar_nombre(fila.get("nombre", "")),
            "email": limpiar_email(fila.get("email", "")),
            "edad": limpiar_edad(fila.get("edad", "")),
            "salario": limpiar_salario(fila.get("salario", "")),
        }

        # Solo incluir si tiene al menos nombre o email
        if limpia["nombre"] or limpia["email"]:
            limpios.append(limpia)
        else:
            errores += 1

    limpios = eliminar_duplicados(limpios)
    return limpios, errores


# Ejecutar limpieza
print(f"  Datos originales: {len(datos_sucios)} filas")
for d in datos_sucios:
    print(f"    {d}")

limpios, errores = limpiar_dataset(datos_sucios)
print(f"\n  Datos limpios: {len(limpios)} filas (descartados: {errores})")
for d in limpios:
    print(f"    {d}")

# set() -> conjunto, no permite duplicados
# Es PERFECTO para detectar duplicados rapidamente


# ---------------------------------------------------------------------------
# EJERCICIO 4: Sistema de recomendaciones
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 4: Recomendador de peliculas")
print("=" * 60)

usuarios = {
    "Ana":    {"Matrix": 5, "Inception": 4, "Interstellar": 5, "Titanic": 2},
    "Carlos": {"Matrix": 4, "Inception": 5, "Avatar": 3, "Titanic": 1},
    "Maria":  {"Interstellar": 5, "Titanic": 5, "Avatar": 4, "Matrix": 3},
    "Luis":   {"Matrix": 5, "Inception": 5, "Interstellar": 4, "Avatar": 2},
}


def similitud(user1, user2):
    """Calcula similitud entre dos usuarios (0-1, donde 1 = identicos)."""
    pelis_comunes = set(user1.keys()) & set(user2.keys())
    if not pelis_comunes:
        return 0

    diferencias = sum(abs(user1[p] - user2[p]) for p in pelis_comunes)
    return 1 / (1 + diferencias)


def usuario_mas_parecido(nombre, todos):
    """Encuentra el usuario mas similar."""
    usuario = todos[nombre]
    mejor_nombre = None
    mejor_sim = -1

    for otro_nombre, otro_gustos in todos.items():
        if otro_nombre == nombre:
            continue
        sim = similitud(usuario, otro_gustos)
        if sim > mejor_sim:
            mejor_sim = sim
            mejor_nombre = otro_nombre

    return mejor_nombre, mejor_sim


def recomendar(nombre, todos):
    """Recomienda peliculas que el usuario no ha visto."""
    parecido, sim = usuario_mas_parecido(nombre, todos)
    pelis_usuario = set(todos[nombre].keys())
    pelis_parecido = set(todos[parecido].keys())

    # Peliculas que tiene el parecido pero no el usuario
    nuevas = pelis_parecido - pelis_usuario

    recomendaciones = []
    for peli in nuevas:
        nota = todos[parecido][peli]
        if nota >= 3:  # solo recomendar si el parecido le dio 3+
            recomendaciones.append((peli, nota))

    return parecido, recomendaciones


# Probar recomendaciones
for nombre in usuarios:
    parecido, sim = usuario_mas_parecido(nombre, usuarios)
    _, recs = recomendar(nombre, usuarios)

    print(f"\n  {nombre}:")
    print(f"    Mas parecido a: {parecido} (similitud: {sim:.2f})")
    if recs:
        for peli, nota in recs:
            print(f"    Recomendacion: {peli} (nota del parecido: {nota}/5)")
    else:
        print(f"    Sin recomendaciones nuevas")

# set() operaciones:
# set1 & set2  -> interseccion (elementos en ambos)
# set1 | set2  -> union (elementos en cualquiera)
# set1 - set2  -> diferencia (en set1 pero no en set2)
# Muy utiles para comparar colecciones


# ---------------------------------------------------------------------------
# EJERCICIO 5: Encriptacion de datos
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 5: Cifrado por sustitucion")
print("=" * 60)


def generar_clave():
    """Genera un alfabeto mezclado como clave."""
    alfabeto = list(string.ascii_lowercase)
    mezclado = alfabeto.copy()
    random.shuffle(mezclado)  # mezcla aleatoriamente
    return dict(zip(alfabeto, mezclado))


def invertir_clave(clave):
    """Invierte la clave para descifrar."""
    return {v: k for k, v in clave.items()}


def encriptar_texto(texto, clave):
    """Encripta texto usando sustitucion."""
    resultado = ""
    for c in texto:
        if c.lower() in clave:
            nuevo = clave[c.lower()]
            resultado += nuevo.upper() if c.isupper() else nuevo
        else:
            resultado += c
    return resultado


def desencriptar_texto(texto, clave):
    """Desencripta texto usando la clave invertida."""
    clave_inv = invertir_clave(clave)
    return encriptar_texto(texto, clave_inv)


# Demo
clave = generar_clave()
print(f"  Clave (primeras 10): {dict(list(clave.items())[:10])}")

original = "Hola Francisco, tus datos estan seguros"
cifrado = encriptar_texto(original, clave)
descifrado = desencriptar_texto(cifrado, clave)

print(f"  Original:    {original}")
print(f"  Cifrado:     {cifrado}")
print(f"  Descifrado:  {descifrado}")
print(f"  Correcto: {original == descifrado}")

# dict(zip(lista1, lista2)) -> crea diccionario emparejando elementos
# zip("abc", "xyz") -> [("a","x"), ("b","y"), ("c","z")]
# dict(zip("abc", "xyz")) -> {"a": "x", "b": "y", "c": "z"}

# dict comprehension: {v: k for k, v in dict.items()}
# Invierte claves y valores del diccionario
# {"a": "x"} -> {"x": "a"}


# ---------------------------------------------------------------------------
# EJERCICIO 6: Simulacion Monte Carlo
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 6: Monte Carlo - Estimar PI")
print("=" * 60)


def estimar_pi(n_puntos):
    """Estima PI usando el metodo Monte Carlo."""
    dentro = 0

    for _ in range(n_puntos):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Si x^2 + y^2 <= 1, el punto esta dentro del circulo
        if x**2 + y**2 <= 1:
            dentro += 1

    pi_estimado = 4 * dentro / n_puntos
    return pi_estimado


# Probar con diferentes cantidades de puntos
print(f"  PI real: {math.pi}")
print(f"  {'Puntos':<12} {'PI estimado':<15} {'Error':<10}")
print(f"  {'-'*37}")

for n in [100, 1_000, 10_000, 100_000, 1_000_000]:
    pi_est = estimar_pi(n)
    error = abs(pi_est - math.pi)
    print(f"  {n:<12,} {pi_est:<15.6f} {error:<10.6f}")

# MONTE CARLO: usar aleatoriedad para resolver problemas
# Se usa en:
# - Finanzas (valoracion de opciones)
# - Fisica (simulacion de particulas)
# - Inteligencia Artificial (busqueda de soluciones)
# - Estadistica (estimacion de distribuciones)
#
# La idea clave: si generas SUFICIENTES puntos aleatorios,
# las proporciones convergen al valor real.
# Mas puntos = mas precision (pero mas tiempo de calculo)

# NOTACION CIENTIFICA EN PYTHON:
# 1_000_000 es igual a 1000000
# Los _ son solo para legibilidad (Python los ignora)


print("\n--- Fin de las Soluciones Guia 11 ---")
