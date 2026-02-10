# ============================================================================
# GUIA 10: AUTOMATIZACION Y PROCESAMIENTO DE DATOS (+ ETL Pipeline)
# ============================================================================
# Autor: Francisco Alvarez Varas
# Inspirado en:
#   - Automate the Boring Stuff with Python (Al Sweigart)
#   - Real Python tutorials: https://realpython.com/
#   - MIT 6.0001 file I/O exercises & data processing patterns
#   - Harvard CS50P File I/O pset
#   - ETL pipelines (industria real de data engineering)
#
# Este es el tipo de proyecto que IMPRESIONA en un portfolio.
# Automatizar tareas repetitivas es una de las habilidades mas
# valiosas de Python en el mundo laboral.
# ============================================================================

import os
import csv
import json
from datetime import datetime


# ---------------------------------------------------------------------------
# EJERCICIO 1: Leer y escribir archivos CSV (Harvard CS50P estilo)
# ---------------------------------------------------------------------------
# CSV (Comma Separated Values) es el formato mas comun para datos.
# Piensa en el como un Excel simplificado.
#
# 1. Crea una lista de diccionarios con datos de 5 alumnos:
#    [{"nombre": "Ana", "nota": 8.5, "asignatura": "Python"}, ...]
# 2. Escribe estos datos en un archivo CSV llamado "notas.csv"
#    usando el modulo csv (csv.DictWriter)
# 3. Lee el archivo CSV y carga los datos de vuelta en una lista
#    usando csv.DictReader
# 4. Calcula e imprime:
#    - Nota media de la clase
#    - Alumno con mejor nota
#    - Alumno con peor nota
#
# Pista: csv.DictWriter necesita fieldnames=["nombre", "nota", "asignatura"]

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 2: Procesamiento de datos JSON
# ---------------------------------------------------------------------------
# JSON es el formato que usan las APIs (lo vimos en la Guia 9).
# Ahora aprenderemos a guardarlo y cargarlo desde archivos.
#
# 1. Crea un diccionario complejo con tu "perfil de programador":
#    {
#      "nombre": "Francisco",
#      "skills": ["Python", "SQL", "Docker"],
#      "experiencia": {"Python": "3 meses", "SQL": "2 meses"},
#      "proyectos": [
#        {"nombre": "Ahorcado", "tecnologia": "Python", "completado": True},
#        {"nombre": "API Dashboard", "tecnologia": "Python", "completado": False}
#      ]
#    }
# 2. Guarda este diccionario en "perfil.json" con json.dump()
# 3. Carga el archivo con json.load()
# 4. Modifica el perfil: agrega un nuevo skill y un nuevo proyecto
# 5. Vuelve a guardarlo
#
# Pista: json.dump(datos, archivo, indent=4, ensure_ascii=False)

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 3: Analizador de texto (frecuencia de palabras)
# ---------------------------------------------------------------------------
# Este es un clasico de MIT/Harvard. Analizar texto automaticamente.
#
# Dado un texto largo (puedes inventar un parrafo o usar uno famoso):
#
# Crea funciones para:
# 1. contar_palabras(texto) -> total de palabras
# 2. frecuencia_palabras(texto) -> diccionario {palabra: veces}
# 3. top_palabras(texto, n) -> las n palabras mas frecuentes
# 4. estadisticas(texto) -> diccionario con:
#    - total_palabras
#    - total_caracteres
#    - promedio_largo_palabra
#    - palabra_mas_larga
#    - total_oraciones (cuenta los puntos ".")
#
# Pista: para encontrar las top n palabras, puedes usar:
# sorted(diccionario.items(), key=lambda x: x[1], reverse=True)[:n]

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 4: Gestor de tareas (TODO app en terminal)
# ---------------------------------------------------------------------------
# Crea un gestor de tareas que guarde las tareas en un archivo JSON.
# Es un proyecto COMPLETO que combina: clases, archivos, menus, validacion.
#
# Clase Tarea:
#   - titulo (str)
#   - descripcion (str)
#   - completada (bool)
#   - fecha_creacion (str)
#   - prioridad (str): "alta", "media", "baja"
#
# Clase GestorTareas:
#   - tareas (lista de Tarea)
#   - agregar_tarea(titulo, descripcion, prioridad)
#   - completar_tarea(indice)
#   - eliminar_tarea(indice)
#   - listar_tareas(filtro=None) -> muestra todas, o solo completadas/pendientes
#   - guardar(archivo) -> guarda en JSON
#   - cargar(archivo) -> carga desde JSON
#
# Menu interactivo:
# 1. Agregar tarea
# 2. Ver tareas
# 3. Completar tarea
# 4. Eliminar tarea
# 5. Guardar y salir

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 5: Generador de informes automaticos
# ---------------------------------------------------------------------------
# Imagina que eres analista de datos y cada dia necesitas generar
# un informe con datos de ventas.
#
# 1. Crea datos de ventas simulados para 30 dias:
#    Cada dia tiene: fecha, producto, unidades, precio_unitario
#    (Usa random para generar datos aleatorios pero realistas)
#
# 2. Guarda los datos en "ventas.csv"
#
# 3. Crea una funcion "generar_informe(archivo_csv)" que lea los datos
#    y genere un informe con:
#    - Total de ingresos
#    - Producto mas vendido (en unidades)
#    - Producto que genero mas ingresos
#    - Dia con mas ventas
#    - Promedio de ventas diarias
#    - Guarda el informe en "informe.txt"
#
# Este tipo de automatizacion es MUY valorado en empresas

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 6: Organizador de archivos (Automatizacion real)
# ---------------------------------------------------------------------------
# Crea un script que organice archivos por extension.
# NO ejecutar en carpetas importantes - solo en una carpeta de prueba!
#
# Funcion "organizar_carpeta(ruta)":
# 1. Lee todos los archivos de la carpeta
# 2. Crea subcarpetas por tipo:
#    - imagenes/ (.jpg, .png, .gif)
#    - documentos/ (.pdf, .docx, .txt)
#    - datos/ (.csv, .json, .xlsx)
#    - codigo/ (.py, .js, .html)
#    - otros/ (todo lo demas)
# 3. (NO mover realmente - solo SIMULAR imprimiendo que haria)
#
# Pista: os.path.splitext("archivo.pdf") -> ("archivo", ".pdf")
#        os.listdir(ruta) -> lista de archivos

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 7: Sistema de registro (Logging basico)
# ---------------------------------------------------------------------------
# En el mundo real, los programas necesitan guardar logs (registros)
# de lo que hacen para poder depurar errores.
#
# Crea una clase "Logger" que:
# 1. Al crear, reciba el nombre del archivo de log
# 2. Tenga metodos: info(mensaje), warning(mensaje), error(mensaje)
# 3. Cada mensaje se guarda en el archivo con formato:
#    [2025-02-09 14:30:25] [INFO] Mensaje aqui
#    [2025-02-09 14:30:26] [WARNING] Algo raro paso
#    [2025-02-09 14:30:27] [ERROR] Algo fallo!
# 4. Tambien imprime por pantalla
#
# Pista: datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 8: Pipeline ETL completo (MIT/Industry standard pattern)
# ---------------------------------------------------------------------------
# ETL = Extract, Transform, Load
# Este es EL patron mas importante en data engineering.
# Es exactamente lo que hacen los data engineers en empresas como
# Google, Amazon, BBVA, Telefonica, etc.
#
# Crea una clase Pipeline con estos metodos:
#
# 1. extract():
#    - Crea un archivo CSV con datos de empleados de ejemplo:
#      nombre, departamento, salario, fecha_ingreso
#    - Incluye al menos 10 empleados con datos variados
#    - Algunos nombres pueden tener espacios extra o mayusculas raras
#    - Lee el CSV y devuelve los datos como lista de diccionarios
#
# 2. transform(datos):
#    - Limpia los nombres (quitar espacios extra, capitalizar)
#    - Calcula los anhos de experiencia desde fecha_ingreso hasta hoy
#    - Asigna una categoria salarial:
#      * "junior" si salario < 30000
#      * "mid" si salario >= 30000 y < 50000
#      * "senior" si salario >= 50000
#    - Calcula el salario promedio por departamento
#    - Devuelve los datos transformados y las estadisticas
#
# 3. load(datos_transformados, estadisticas):
#    - Guarda los datos transformados en un nuevo CSV: "empleados_procesados.csv"
#    - Genera un archivo JSON con el resumen/estadisticas: "resumen_etl.json"
#
# 4. run():
#    - Ejecuta extract() -> transform() -> load() en secuencia
#    - Imprime el progreso de cada etapa
#    - Mide el tiempo total del pipeline
#
# Pista: from datetime import datetime
#        fecha = datetime.strptime("2020-03-15", "%Y-%m-%d")
#        hoy = datetime.now()
#        anhos = (hoy - fecha).days / 365.25

# TU CODIGO AQUI:




print("\n--- Fin de la Guia 10 ---")
print("Estos proyectos demuestran habilidades reales de automatizacion.")
print("Son PERFECTOS para tu portfolio!")
