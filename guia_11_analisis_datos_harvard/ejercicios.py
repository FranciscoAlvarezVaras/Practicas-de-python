# ============================================================================
# GUIA 11: ANALISIS DE DATOS CON PYTHON (Estilo Harvard/MIT)
# ============================================================================
# Autor: Francisco Alvarez Varas
# Inspirado en:
#   - Harvard CS50P Week 6 (File I/O)
#   - MIT 6.0002 Introduction to Computational Thinking and Data Science
#   - Real Python Data Science tutorials
#
# SIN dependencias externas (sin pandas, sin numpy).
# Todo con Python puro para entender los fundamentos.
# Si dominas esto, pandas te parecera facilisimo.
# ============================================================================

import csv
import json
import random
from collections import Counter
from datetime import datetime, timedelta


# ---------------------------------------------------------------------------
# EJERCICIO 1: Crear y analizar un dataset de alumnos
# ---------------------------------------------------------------------------
# Crea un dataset simulado de 50 alumnos con:
# - nombre (str)
# - edad (int: 18-35)
# - nota_python (float: 0-10)
# - nota_sql (float: 0-10)
# - nota_docker (float: 0-10)
# - grupo (str: "MDAA", "MDAB", "MIA")
#
# Luego crea funciones para:
# 1. nota_media_alumno(alumno) -> media de sus 3 notas
# 2. mejores_alumnos(dataset, n) -> los n con mejor media
# 3. estadisticas_por_grupo(dataset) -> media, min, max de cada grupo
# 4. distribucion_notas(dataset, asignatura) -> cuantos alumnos en cada rango:
#    0-2: "Suspenso grave", 2-5: "Suspenso", 5-7: "Aprobado",
#    7-9: "Notable", 9-10: "Sobresaliente"
#
# Pista para generar datos: random.uniform(0, 10) da un float entre 0 y 10

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 2: Analisis de ventas por meses
# ---------------------------------------------------------------------------
# Genera datos de ventas de 12 meses con:
# - mes (str: "Enero", "Febrero", ...)
# - ingresos (float)
# - gastos (float)
# - clientes_nuevos (int)
#
# Crea funciones para:
# 1. beneficio_mensual(datos) -> lista de {mes, beneficio}
# 2. mejor_mes(datos) -> el mes con mas beneficio
# 3. peor_mes(datos) -> el mes con menos beneficio
# 4. tendencia(datos) -> "creciente", "decreciente" o "estable"
#    (compara la media de los primeros 6 meses vs los ultimos 6)
# 5. generar_grafico_texto(datos) -> grafico de barras en terminal:
#    Enero   | ████████████ 1200
#    Febrero | ████████ 800
#    Marzo   | ██████████████ 1400
#    (cada bloque = 100 euros)

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 3: Limpieza de datos (Data Cleaning)
# ---------------------------------------------------------------------------
# En la vida real, los datos NUNCA vienen limpios.
# Este ejercicio simula problemas reales que encontraras.
#
# Dado un dataset "sucio":
# datos_sucios = [
#     {"nombre": " Ana García ", "email": "ANA@EMAIL.COM", "edad": "25", "salario": "30,000"},
#     {"nombre": "carlos  LOPEZ", "email": "carlos@email", "edad": "abc", "salario": "28000"},
#     {"nombre": "", "email": "maria@email.com", "edad": "30", "salario": "35000"},
#     {"nombre": "Luis Pérez", "email": "luis@email.com", "edad": "-5", "salario": ""},
#     {"nombre": "Luis Pérez", "email": "luis@email.com", "edad": "28", "salario": "32000"},
# ]
#
# Crea funciones para:
# 1. limpiar_nombre(nombre) -> quitar espacios extra, formato titulo
# 2. limpiar_email(email) -> minusculas, validar que tiene "@" y "."
# 3. limpiar_edad(edad) -> convertir a int, marcar None si no valido
# 4. limpiar_salario(salario) -> quitar comas, convertir a float
# 5. eliminar_duplicados(dataset) -> quitar filas duplicadas
# 6. limpiar_dataset(dataset) -> aplicar todo y devolver datos limpios
#
# Imprime un resumen: datos originales vs datos limpios

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 4: Mini-sistema de recomendaciones
# ---------------------------------------------------------------------------
# Crea un sistema de recomendacion simple basado en similitud.
#
# Tienes usuarios con sus gustos de peliculas (1-5 estrellas):
# usuarios = {
#     "Ana":    {"Matrix": 5, "Inception": 4, "Interstellar": 5, "Titanic": 2},
#     "Carlos": {"Matrix": 4, "Inception": 5, "Avatar": 3, "Titanic": 1},
#     "Maria":  {"Interstellar": 5, "Titanic": 5, "Avatar": 4, "Matrix": 3},
#     "Luis":   {"Matrix": 5, "Inception": 5, "Interstellar": 4, "Avatar": 2},
# }
#
# Crea funciones para:
# 1. similitud(usuario1, usuario2) -> calcula que tan parecidos son
#    (suma de diferencias absolutas entre notas compartidas, invertido)
# 2. usuario_mas_parecido(usuario, todos_usuarios) -> encuentra el mas similar
# 3. recomendar(usuario, todos_usuarios) -> recomienda peliculas que
#    el usuario NO ha visto pero su usuario mas parecido si
#
# Pista similitud: menos diferencia = mas parecidos
# similitud = 1 / (1 + sum(abs(nota1 - nota2) for pelis en comun))

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 5: Encriptacion de datos (estilo MIT)
# ---------------------------------------------------------------------------
# Crea un sistema para encriptar/desencriptar datos sensibles
# usando un cifrado por sustitucion basado en una clave.
#
# 1. generar_clave() -> genera un alfabeto aleatorio mezclado
#    Original: "abcdefghij..." -> Clave: "qwertyuiop..."
# 2. encriptar(texto, clave) -> sustituye cada letra por su equivalente
# 3. desencriptar(texto_enc, clave) -> invierte el proceso
# 4. encriptar_csv(archivo_origen, archivo_destino, clave, columnas)
#    -> encripta solo ciertas columnas de un CSV
#
# Ejemplo:
# clave = generar_clave()
# encriptar("hola", clave) -> "xnvq" (depende de la clave)
# desencriptar("xnvq", clave) -> "hola"

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 6: Simulacion Monte Carlo (MIT 6.0002 estilo)
# ---------------------------------------------------------------------------
# Monte Carlo usa aleatoriedad para resolver problemas.
# Es IMPRESIONANTE en un portfolio y se usa mucho en finanzas y ciencia.
#
# Proyecto: Estimar el valor de PI usando puntos aleatorios
#
# Logica:
# - Imagina un cuadrado de lado 2 con un circulo inscrito de radio 1
# - Genera N puntos aleatorios dentro del cuadrado
# - Cuenta cuantos caen dentro del circulo (x^2 + y^2 <= 1)
# - PI ~ 4 * (puntos_dentro / puntos_totales)
#
# Crea una funcion "estimar_pi(n_puntos)" que:
# 1. Genere n puntos aleatorios (x, y) entre -1 y 1
# 2. Cuente cuantos caen dentro del circulo
# 3. Calcule la estimacion de PI
# 4. Muestre la precision vs el PI real (math.pi)
# 5. Prueba con 100, 1000, 10000, 100000 puntos
#    (veras que a mas puntos, mas precision!)

# TU CODIGO AQUI:




print("\n--- Fin de la Guia 11 ---")
print("Estos ejercicios son de nivel universitario avanzado.")
print("Si los completas, tu perfil como data analyst sera muy solido!")
