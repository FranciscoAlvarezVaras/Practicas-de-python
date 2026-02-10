# ============================================================================
# GUIA 12: PROYECTO INTEGRADOR - PYTHON + IA (Anthropic/Claude)
# ============================================================================
# Autor: Francisco Alvarez Varas
# Inspirado en:
#   - Anthropic Cookbook: https://github.com/anthropics/anthropic-cookbook
#   - Anthropic SDK Python: https://github.com/anthropics/anthropic-sdk-python
#   - Real Python API tutorials
#
# Esta guia combina TODO lo aprendido en las guias 1-11 para crear
# proyectos reales que integran Python con Inteligencia Artificial.
#
# NOTA: Los ejercicios 1-5 funcionan SIN API key (simulacion local).
# El ejercicio 6 usa la API real de Anthropic (necesita API key).
#
# Para instalar: pip install anthropic  (solo para el ejercicio 6)
# ============================================================================

import json
import random
import os
from datetime import datetime


# ---------------------------------------------------------------------------
# EJERCICIO 1: Simulador de chatbot con reglas (sin IA)
# ---------------------------------------------------------------------------
# Antes de usar IA, vamos a entender como funciona un chatbot basico.
# Crea un chatbot que responda segun reglas predefinidas.
#
# Clase ChatBot:
#   - nombre (str)
#   - reglas (dict): {"saludo": ["hola", "hey", "buenos dias"],
#                     "despedida": ["adios", "chao", "hasta luego"],
#                     "estado": ["como estas", "que tal"]}
#   - respuestas (dict): {"saludo": "Hola! Como puedo ayudarte?",
#                         "despedida": "Hasta luego!",
#                         "estado": "Estoy bien, gracias por preguntar!"}
#
# Metodos:
# - clasificar(mensaje) -> detecta la intencion del mensaje
# - responder(mensaje) -> devuelve la respuesta adecuada
# - conversar() -> bucle interactivo (input/output)
# - historial -> guarda todas las conversaciones
#
# Pista: para clasificar, comprueba si alguna palabra clave
# esta en el mensaje del usuario (con "in")

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 2: Procesador de lenguaje natural basico (NLP)
# ---------------------------------------------------------------------------
# Crea funciones que analicen texto de forma inteligente:
#
# 1. analizar_sentimiento(texto) -> "positivo", "negativo" o "neutro"
#    Basado en listas de palabras positivas y negativas:
#    positivas = ["bueno", "genial", "excelente", "fantastico", "increible",
#                 "perfecto", "maravilloso", "feliz", "amor", "mejor"]
#    negativas = ["malo", "terrible", "horrible", "odio", "peor", "feo",
#                 "triste", "error", "problema", "dificil"]
#
# 2. extraer_entidades(texto) -> detectar nombres, emails, fechas, numeros
#    Pista: usa expresiones simples, no regex
#    - Emails: busca palabras con "@"
#    - Numeros: busca palabras que sean digitos
#    - Palabras capitalizadas podrian ser nombres propios
#
# 3. resumir(texto, n_oraciones) -> devuelve las n oraciones mas importantes
#    Pista: la "importancia" puede ser la longitud o cantidad de palabras clave

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 3: Sistema de preguntas y respuestas (Q&A)
# ---------------------------------------------------------------------------
# Crea un sistema que responda preguntas sobre un texto dado.
#
# Clase SistemaQA:
#   - texto_base (str): el texto sobre el que se hacen preguntas
#   - oraciones (list): el texto dividido en oraciones
#
# Metodo responder(pregunta):
# 1. Extrae las palabras clave de la pregunta (quita "que", "es", "el", etc.)
# 2. Busca la oracion del texto que mas palabras clave comparte
# 3. Devuelve esa oracion como respuesta
#
# Ejemplo:
# texto = "Python es un lenguaje de programacion. Fue creado por Guido van
#          Rossum en 1991. Python es muy popular para analisis de datos."
# pregunta = "Quien creo Python?"
# respuesta -> "Fue creado por Guido van Rossum en 1991."

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 4: Generador de datos con plantillas (mock data)
# ---------------------------------------------------------------------------
# En IA y data science necesitas datos de prueba constantemente.
# Crea un generador de datos falsos pero realistas.
#
# Clase GeneradorDatos:
#   - nombres_m, nombres_f (listas de nombres)
#   - apellidos (lista)
#   - ciudades (lista)
#   - empresas (lista)
#
# Metodos:
# - persona() -> dict con nombre, edad, email, ciudad, empresa, puesto
# - dataset(n) -> lista de n personas
# - exportar_csv(datos, archivo)
# - exportar_json(datos, archivo)
#
# Los emails se generan automaticamente: nombre.apellido@empresa.com

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 5: Pipeline de datos (ETL simplificado)
# ---------------------------------------------------------------------------
# ETL = Extract, Transform, Load. Es el proceso fundamental en data.
#
# Crea un pipeline que:
# 1. EXTRACT: genera o carga datos "crudos" (usa el generador del ej. 4)
# 2. TRANSFORM: limpia, valida, enriquece los datos
#    - Normalizar nombres (titulo case)
#    - Validar emails
#    - Agregar campo "rango_edad" ("joven", "adulto", "senior")
#    - Agregar campo "fecha_procesamiento"
#    - Eliminar duplicados
# 3. LOAD: guarda los datos procesados en JSON
#
# Clase Pipeline:
#   - pasos (lista de funciones)
#   - agregar_paso(funcion)
#   - ejecutar(datos) -> aplica todos los pasos en orden
#   - log (lista de mensajes de cada paso)

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 6: Integracion REAL con Claude API (Anthropic)
# ---------------------------------------------------------------------------
# NOTA: Este ejercicio necesita:
# 1. pip install anthropic
# 2. Una API key de Anthropic (https://console.anthropic.com)
# 3. Configurar la variable de entorno ANTHROPIC_API_KEY
#
# Si no tienes API key, lee el codigo de la solucion para entender
# como funciona la integracion.
#
# Crea un asistente de Python que:
# 1. Reciba una pregunta sobre Python
# 2. Use la API de Claude para generar una respuesta
# 3. Guarde el historial de preguntas/respuestas en JSON
# 4. Tenga un modo "profesor" que explique conceptos paso a paso
#
# Estructura basica:
# import anthropic
# client = anthropic.Anthropic()  # usa ANTHROPIC_API_KEY automaticamente
# message = client.messages.create(
#     model="claude-sonnet-4-5-20250929",
#     max_tokens=1024,
#     messages=[{"role": "user", "content": "tu pregunta"}]
# )
# print(message.content[0].text)

# TU CODIGO AQUI (necesita API key):




print("\n--- Fin de la Guia 12 ---")
print("Has completado TODAS las guias!")
print("Desde variables basicas hasta IA - un viaje impresionante.")
