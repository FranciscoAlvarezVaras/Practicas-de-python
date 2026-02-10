# ============================================================================
# GUIA 10 - SOLUCIONES: AUTOMATIZACION Y PROCESAMIENTO DE DATOS (+ ETL)
# ============================================================================
# Autor: Francisco Alvarez Varas
# ============================================================================

import os
import csv
import json
import random
from datetime import datetime, timedelta


# ---------------------------------------------------------------------------
# EJERCICIO 1: Leer y escribir CSV
# ---------------------------------------------------------------------------
print("=" * 60)
print("EJERCICIO 1: CSV - Notas de alumnos")
print("=" * 60)

# Datos de ejemplo
alumnos = [
    {"nombre": "Ana", "nota": 8.5, "asignatura": "Python"},
    {"nombre": "Carlos", "nota": 6.0, "asignatura": "Python"},
    {"nombre": "Maria", "nota": 9.5, "asignatura": "Python"},
    {"nombre": "Luis", "nota": 7.0, "asignatura": "Python"},
    {"nombre": "Pilar", "nota": 5.5, "asignatura": "Python"},
]

# ESCRIBIR CSV
with open("notas.csv", "w", newline="", encoding="utf-8") as archivo:
    campos = ["nombre", "nota", "asignatura"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)

    escritor.writeheader()   # escribe la fila de cabecera
    escritor.writerows(alumnos)  # escribe todas las filas

print("  Archivo 'notas.csv' creado")

# LEER CSV
alumnos_leidos = []
with open("notas.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        fila["nota"] = float(fila["nota"])  # CSV lee todo como string!
        alumnos_leidos.append(fila)

# Analisis
notas = [a["nota"] for a in alumnos_leidos]
nota_media = sum(notas) / len(notas) if notas else 0
mejor = max(alumnos_leidos, key=lambda a: a["nota"])
peor = min(alumnos_leidos, key=lambda a: a["nota"])

print(f"  Nota media: {nota_media:.1f}")
print(f"  Mejor: {mejor['nombre']} ({mejor['nota']})")
print(f"  Peor: {peor['nombre']} ({peor['nota']})")

# CSV - COMO FUNCIONA:
# csv.DictWriter -> escribe diccionarios como filas CSV
#   .writeheader() -> escribe la cabecera (nombres de columnas)
#   .writerows(lista) -> escribe todas las filas
# csv.DictReader -> lee filas CSV como diccionarios
#   for fila in lector: -> cada fila es un dict {"nombre": "Ana", "nota": "8.5"}
#   OJO: CSV lee TODO como string, hay que convertir numeros con float()/int()
#
# newline="" en Windows es importante para evitar lineas en blanco extra

# max/min con key:
# max(lista, key=lambda x: x["nota"]) -> busca el maximo segun la nota
# lambda x: x["nota"] le dice a max() QUE campo comparar


# ---------------------------------------------------------------------------
# EJERCICIO 2: JSON
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 2: JSON - Perfil de programador")
print("=" * 60)

perfil = {
    "nombre": "Francisco Alvarez Varas",
    "skills": ["Python", "SQL", "Docker"],
    "experiencia": {
        "Python": "3 meses",
        "SQL": "2 meses",
        "Docker": "1 mes"
    },
    "proyectos": [
        {"nombre": "Ahorcado", "tecnologia": "Python", "completado": True},
        {"nombre": "API Dashboard", "tecnologia": "Python", "completado": False}
    ]
}

# GUARDAR JSON
with open("perfil.json", "w", encoding="utf-8") as f:
    json.dump(perfil, f, indent=4, ensure_ascii=False)
    # indent=4 -> formatea bonito con indentacion
    # ensure_ascii=False -> permite caracteres especiales (acentos)

print("  Archivo 'perfil.json' creado")

# CARGAR JSON
with open("perfil.json", "r", encoding="utf-8") as f:
    perfil_cargado = json.load(f)

# Modificar
perfil_cargado["skills"].append("PySpark")
perfil_cargado["proyectos"].append({
    "nombre": "Guia Python EDEM",
    "tecnologia": "Python",
    "completado": True
})

# Guardar actualizado
with open("perfil.json", "w", encoding="utf-8") as f:
    json.dump(perfil_cargado, f, indent=4, ensure_ascii=False)

print(f"  Skills: {perfil_cargado['skills']}")
print(f"  Proyectos: {len(perfil_cargado['proyectos'])}")

# JSON vs CSV:
# CSV -> datos tabulares (como Excel), filas y columnas
# JSON -> datos estructurados/anidados (diccionarios dentro de diccionarios)
# Ambos son texto plano, legibles por humanos


# ---------------------------------------------------------------------------
# EJERCICIO 3: Analizador de texto
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 3: Analizador de texto")
print("=" * 60)

TEXTO_EJEMPLO = """Python es un lenguaje de programacion poderoso y facil de aprender.
Tiene estructuras de datos eficientes y de alto nivel. Python es ideal
para programacion orientada a objetos. La elegante sintaxis de Python y
su tipado dinamico hacen de Python un lenguaje ideal para scripting y
desarrollo rapido de aplicaciones. Python es utilizado por empresas como
Google y Netflix. Aprender Python es una excelente decision."""


def contar_palabras(texto):
    """Cuenta el total de palabras en un texto."""
    return len(texto.split())


def frecuencia_palabras(texto):
    """Devuelve un diccionario con la frecuencia de cada palabra."""
    palabras = texto.lower().split()
    # Limpiar signos de puntuacion
    palabras = [p.strip(".,;:!?()\"'") for p in palabras]

    frecuencia = {}
    for palabra in palabras:
        if palabra:  # ignorar strings vacios
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia


def top_palabras(texto, n=5):
    """Devuelve las n palabras mas frecuentes."""
    freq = frecuencia_palabras(texto)
    # sorted con key=lambda ordena por el valor (frecuencia)
    ordenadas = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return ordenadas[:n]


def estadisticas(texto):
    """Calcula estadisticas completas del texto."""
    palabras = texto.split()
    oraciones = texto.count(".")

    return {
        "total_palabras": len(palabras),
        "total_caracteres": len(texto),
        "promedio_largo_palabra": sum(len(p) for p in palabras) / len(palabras) if palabras else 0,
        "palabra_mas_larga": max(palabras, key=len) if palabras else "",
        "total_oraciones": oraciones,
    }


print(f"  Total palabras: {contar_palabras(TEXTO_EJEMPLO)}")
print(f"\n  Top 5 palabras:")
for palabra, veces in top_palabras(TEXTO_EJEMPLO, 5):
    print(f"    '{palabra}': {veces} veces")

stats = estadisticas(TEXTO_EJEMPLO)
print(f"\n  Estadisticas:")
for clave, valor in stats.items():
    if isinstance(valor, float):
        print(f"    {clave}: {valor:.1f}")
    else:
        print(f"    {clave}: {valor}")

# sorted() con key y lambda:
# sorted(lista, key=lambda x: criterio, reverse=True)
# Esto ordena la lista segun el criterio que definas
# sorted([("a", 3), ("b", 1)], key=lambda x: x[1]) -> [("b",1), ("a",3)]


# ---------------------------------------------------------------------------
# EJERCICIO 4: Gestor de Tareas
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 4: Gestor de Tareas")
print("=" * 60)


class Tarea:
    def __init__(self, titulo, descripcion="", prioridad="media"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False
        self.fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.prioridad = prioridad

    def completar(self):
        self.completada = True

    def a_dict(self):
        """Convierte la tarea a diccionario (para guardar en JSON)."""
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "completada": self.completada,
            "fecha_creacion": self.fecha_creacion,
            "prioridad": self.prioridad
        }

    @classmethod
    def desde_dict(cls, datos):
        """Crea una Tarea desde un diccionario (para cargar de JSON)."""
        tarea = cls(datos["titulo"], datos["descripcion"], datos["prioridad"])
        tarea.completada = datos["completada"]
        tarea.fecha_creacion = datos["fecha_creacion"]
        return tarea

    def __str__(self):
        estado = "OK" if self.completada else "PENDIENTE"
        return (f"[{estado}] [{self.prioridad.upper()}] "
                f"{self.titulo} ({self.fecha_creacion})")


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar(self, titulo, descripcion="", prioridad="media"):
        tarea = Tarea(titulo, descripcion, prioridad)
        self.tareas.append(tarea)
        print(f"  + Tarea agregada: {titulo}")

    def completar(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completar()
            print(f"  Completada: {self.tareas[indice].titulo}")
        else:
            print("  Indice no valido")

    def eliminar(self, indice):
        if 0 <= indice < len(self.tareas):
            eliminada = self.tareas.pop(indice)
            print(f"  - Eliminada: {eliminada.titulo}")
        else:
            print("  Indice no valido")

    def listar(self, filtro=None):
        for i, tarea in enumerate(self.tareas):
            if filtro == "pendientes" and tarea.completada:
                continue
            if filtro == "completadas" and not tarea.completada:
                continue
            print(f"    {i}. {tarea}")

    def guardar(self, archivo="tareas.json"):
        datos = [t.a_dict() for t in self.tareas]
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
        print(f"  Guardado en {archivo}")

    def cargar(self, archivo="tareas.json"):
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                datos = json.load(f)
            self.tareas = [Tarea.desde_dict(d) for d in datos]
            print(f"  Cargadas {len(self.tareas)} tareas desde {archivo}")
        except FileNotFoundError:
            print(f"  Archivo {archivo} no encontrado")


# Demo
gestor = GestorTareas()
gestor.agregar("Estudiar Python", "Completar guias 1-7", "alta")
gestor.agregar("Hacer ejercicio", "Ir al gym", "media")
gestor.agregar("Comprar comida", "Supermercado", "baja")
gestor.agregar("Revisar APIs", "Guia 9", "alta")

gestor.completar(0)  # Completar "Estudiar Python"

print("\n  Todas las tareas:")
gestor.listar()

print("\n  Solo pendientes:")
gestor.listar(filtro="pendientes")

gestor.guardar()

# @classmethod: metodo de CLASE (no de instancia)
# Se llama con: Tarea.desde_dict(datos) en vez de tarea.desde_dict(datos)
# Es un patron comun para crear objetos desde datos externos (JSON, CSV)
# "cls" es como "self" pero para la clase misma


# ---------------------------------------------------------------------------
# EJERCICIO 5: Generador de informes
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 5: Informe de ventas")
print("=" * 60)

# Generar datos simulados
productos = ["Laptop", "Teclado", "Raton", "Monitor", "Auriculares"]
precios = {"Laptop": 899, "Teclado": 49, "Raton": 29, "Monitor": 349, "Auriculares": 79}

ventas = []
fecha_base = datetime(2025, 1, 1)

for dia in range(30):
    fecha = fecha_base + timedelta(days=dia)
    # 1-3 ventas por dia
    for _ in range(random.randint(1, 3)):
        producto = random.choice(productos)
        unidades = random.randint(1, 5)
        ventas.append({
            "fecha": fecha.strftime("%Y-%m-%d"),
            "producto": producto,
            "unidades": unidades,
            "precio_unitario": precios[producto]
        })

# Guardar en CSV
with open("ventas.csv", "w", newline="", encoding="utf-8") as f:
    campos = ["fecha", "producto", "unidades", "precio_unitario"]
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(ventas)


def generar_informe(archivo_csv):
    """Genera un informe de ventas desde un archivo CSV."""
    # Leer datos
    datos = []
    with open(archivo_csv, "r", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            fila["unidades"] = int(fila["unidades"])
            fila["precio_unitario"] = int(fila["precio_unitario"])
            fila["ingreso"] = fila["unidades"] * fila["precio_unitario"]
            datos.append(fila)

    # Calcular metricas
    total_ingresos = sum(d["ingreso"] for d in datos)

    # Ventas por producto
    por_producto = {}
    for d in datos:
        p = d["producto"]
        if p not in por_producto:
            por_producto[p] = {"unidades": 0, "ingresos": 0}
        por_producto[p]["unidades"] += d["unidades"]
        por_producto[p]["ingresos"] += d["ingreso"]

    mas_vendido = max(por_producto.items(), key=lambda x: x[1]["unidades"])
    mas_ingresos = max(por_producto.items(), key=lambda x: x[1]["ingresos"])

    # Ventas por dia
    por_dia = {}
    for d in datos:
        fecha = d["fecha"]
        por_dia[fecha] = por_dia.get(fecha, 0) + d["ingreso"]
    mejor_dia = max(por_dia.items(), key=lambda x: x[1])

    promedio_diario = total_ingresos / len(por_dia)

    # Generar informe
    informe = f"""
{'='*50}
INFORME DE VENTAS
Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')}
{'='*50}

Total de ingresos: {total_ingresos:,.2f} EUR
Total de transacciones: {len(datos)}
Promedio diario: {promedio_diario:,.2f} EUR

Producto mas vendido (uds): {mas_vendido[0]} ({mas_vendido[1]['unidades']} uds)
Mayor ingreso por producto: {mas_ingresos[0]} ({mas_ingresos[1]['ingresos']:,} EUR)
Mejor dia de ventas: {mejor_dia[0]} ({mejor_dia[1]:,} EUR)

Desglose por producto:
"""
    for prod, datos_prod in sorted(por_producto.items()):
        informe += f"  {prod:<15} {datos_prod['unidades']:>5} uds  {datos_prod['ingresos']:>10,} EUR\n"

    # Guardar en archivo
    with open("informe.txt", "w", encoding="utf-8") as f:
        f.write(informe)

    print(informe)
    print("  Informe guardado en 'informe.txt'")


generar_informe("ventas.csv")


# ---------------------------------------------------------------------------
# EJERCICIO 6: Organizador de archivos (simulado)
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 6: Organizador de archivos (simulacion)")
print("=" * 60)

CATEGORIAS = {
    "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "documentos": [".pdf", ".docx", ".doc", ".txt", ".odt"],
    "datos": [".csv", ".json", ".xlsx", ".xls", ".xml"],
    "codigo": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}


def clasificar_archivo(nombre_archivo):
    """Clasifica un archivo segun su extension."""
    _, extension = os.path.splitext(nombre_archivo)
    extension = extension.lower()

    for categoria, extensiones in CATEGORIAS.items():
        if extension in extensiones:
            return categoria
    return "otros"


def organizar_carpeta(ruta=".", simular=True):
    """Organiza archivos de una carpeta por tipo (simulacion por defecto)."""
    if not os.path.exists(ruta):
        print(f"  La ruta '{ruta}' no existe")
        return

    archivos = [f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))]

    movimientos = {}
    for archivo in archivos:
        categoria = clasificar_archivo(archivo)
        if categoria not in movimientos:
            movimientos[categoria] = []
        movimientos[categoria].append(archivo)

    for categoria, archivos_cat in movimientos.items():
        print(f"\n  [{categoria.upper()}] ({len(archivos_cat)} archivos)")
        for archivo in archivos_cat[:5]:
            destino = os.path.join(ruta, categoria, archivo)
            if simular:
                print(f"    (simulado) {archivo} -> {categoria}/")

    return movimientos


# Simular con archivos ficticios
archivos_ficticios = [
    "foto1.jpg", "datos.csv", "script.py", "informe.pdf",
    "notas.txt", "estilo.css", "perfil.json", "imagen.png"
]
print("  Clasificacion de archivos ficticios:")
for archivo in archivos_ficticios:
    cat = clasificar_archivo(archivo)
    print(f"    {archivo} -> {cat}/")

# os.path.splitext("archivo.pdf") -> ("archivo", ".pdf")
# os.path.exists(ruta) -> True si la ruta existe
# os.path.isfile(ruta) -> True si es un archivo (no carpeta)
# os.listdir(ruta) -> lista de archivos y carpetas en esa ruta


# ---------------------------------------------------------------------------
# EJERCICIO 7: Logger (sistema de registro)
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 7: Sistema de Logger")
print("=" * 60)


class Logger:
    def __init__(self, archivo="app.log"):
        self.archivo = archivo
        # Limpiar archivo anterior
        with open(self.archivo, "w", encoding="utf-8") as f:
            f.write("")

    def _registrar(self, nivel, mensaje):
        """Metodo interno para registrar un mensaje."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"[{timestamp}] [{nivel}] {mensaje}"

        # Imprimir por pantalla
        print(f"    {linea}")

        # Guardar en archivo
        with open(self.archivo, "a", encoding="utf-8") as f:
            f.write(linea + "\n")

    def info(self, mensaje):
        self._registrar("INFO", mensaje)

    def warning(self, mensaje):
        self._registrar("WARNING", mensaje)

    def error(self, mensaje):
        self._registrar("ERROR", mensaje)


# Ejemplo de uso
log = Logger("mi_app.log")
log.info("Aplicacion iniciada")
log.info("Cargando datos...")
log.warning("El archivo de configuracion no existe, usando valores por defecto")
log.info("Datos cargados correctamente")
log.error("Error al conectar con la base de datos")
log.info("Reintentando conexion...")
log.info("Conexion exitosa")

print(f"\n  Log guardado en 'mi_app.log'")

# METODO CON _ (underscore):
# _registrar es un metodo "privado" por convencion
# El _ al inicio indica que es de uso interno, no deberia
# llamarse desde fuera de la clase
# En Python no hay metodos privados reales, es solo convencion


# ---------------------------------------------------------------------------
# EJERCICIO 8: Pipeline ETL completo (MIT/Industry standard pattern)
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 8: Pipeline ETL")
print("=" * 60)

import time as time_module


class Pipeline:
    """Pipeline ETL (Extract, Transform, Load) para datos de empleados."""

    def __init__(self):
        self.archivo_entrada = "empleados_raw.csv"
        self.archivo_salida = "empleados_procesados.csv"
        self.archivo_resumen = "resumen_etl.json"

    def extract(self):
        """EXTRACT: Crea datos de ejemplo y los lee desde CSV."""
        print("  [EXTRACT] Creando datos de ejemplo...")

        # Datos de empleados (algunos con nombres "sucios" a proposito)
        empleados = [
            {"nombre": "  ana garcia  ", "departamento": "Tecnologia",
             "salario": "55000", "fecha_ingreso": "2018-03-15"},
            {"nombre": "CARLOS LOPEZ", "departamento": "Ventas",
             "salario": "28000", "fecha_ingreso": "2023-06-01"},
            {"nombre": " maria FERNANDEZ ", "departamento": "Tecnologia",
             "salario": "62000", "fecha_ingreso": "2017-01-10"},
            {"nombre": "luis  martinez", "departamento": "RRHH",
             "salario": "35000", "fecha_ingreso": "2021-09-20"},
            {"nombre": "PILAR  SANCHEZ", "departamento": "Ventas",
             "salario": "42000", "fecha_ingreso": "2019-11-05"},
            {"nombre": "  jorge RUIZ ", "departamento": "Tecnologia",
             "salario": "48000", "fecha_ingreso": "2020-02-28"},
            {"nombre": "elena DIAZ", "departamento": "RRHH",
             "salario": "25000", "fecha_ingreso": "2024-01-15"},
            {"nombre": " david MORENO  ", "departamento": "Ventas",
             "salario": "31000", "fecha_ingreso": "2022-04-10"},
            {"nombre": "laura JIMENEZ", "departamento": "Tecnologia",
             "salario": "70000", "fecha_ingreso": "2015-08-22"},
            {"nombre": " pablo ALVAREZ ", "departamento": "RRHH",
             "salario": "38000", "fecha_ingreso": "2020-07-01"},
        ]

        # Escribir CSV "sucio"
        with open(self.archivo_entrada, "w", newline="", encoding="utf-8") as f:
            campos = ["nombre", "departamento", "salario", "fecha_ingreso"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(empleados)

        # Leer CSV
        datos = []
        with open(self.archivo_entrada, "r", encoding="utf-8") as f:
            for fila in csv.DictReader(f):
                datos.append(dict(fila))

        print(f"  [EXTRACT] {len(datos)} registros extraidos desde CSV")
        return datos

    def transform(self, datos):
        """TRANSFORM: Limpia, enriquece y calcula estadisticas."""
        print("  [TRANSFORM] Procesando datos...")

        hoy = datetime.now()
        datos_transformados = []

        for registro in datos:
            # 1. Limpiar nombre: quitar espacios extra, capitalizar
            nombre_limpio = " ".join(registro["nombre"].split()).title()

            # 2. Convertir salario a numero
            salario = int(registro["salario"])

            # 3. Calcular anhos de experiencia
            fecha_ingreso = datetime.strptime(
                registro["fecha_ingreso"], "%Y-%m-%d"
            )
            anhos_exp = round((hoy - fecha_ingreso).days / 365.25, 1)

            # 4. Asignar categoria salarial
            if salario < 30000:
                categoria = "junior"
            elif salario < 50000:
                categoria = "mid"
            else:
                categoria = "senior"

            datos_transformados.append({
                "nombre": nombre_limpio,
                "departamento": registro["departamento"],
                "salario": salario,
                "fecha_ingreso": registro["fecha_ingreso"],
                "anhos_experiencia": anhos_exp,
                "categoria": categoria,
            })

        # Calcular estadisticas por departamento
        departamentos = {}
        for emp in datos_transformados:
            dept = emp["departamento"]
            if dept not in departamentos:
                departamentos[dept] = {"salarios": [], "empleados": 0}
            departamentos[dept]["salarios"].append(emp["salario"])
            departamentos[dept]["empleados"] += 1

        estadisticas = {
            "total_empleados": len(datos_transformados),
            "salario_promedio_global": round(
                sum(e["salario"] for e in datos_transformados)
                / len(datos_transformados), 2
            ),
            "por_departamento": {},
            "por_categoria": {"junior": 0, "mid": 0, "senior": 0},
        }

        for dept, info in departamentos.items():
            estadisticas["por_departamento"][dept] = {
                "empleados": info["empleados"],
                "salario_promedio": round(
                    sum(info["salarios"]) / len(info["salarios"]), 2
                ),
                "salario_min": min(info["salarios"]),
                "salario_max": max(info["salarios"]),
            }

        for emp in datos_transformados:
            estadisticas["por_categoria"][emp["categoria"]] += 1

        print(f"  [TRANSFORM] {len(datos_transformados)} registros transformados")
        print(f"  [TRANSFORM] Departamentos: {list(departamentos.keys())}")
        return datos_transformados, estadisticas

    def load(self, datos_transformados, estadisticas):
        """LOAD: Guarda datos procesados en CSV y resumen en JSON."""
        print("  [LOAD] Guardando resultados...")

        # Guardar CSV procesado
        campos = ["nombre", "departamento", "salario", "fecha_ingreso",
                  "anhos_experiencia", "categoria"]
        with open(self.archivo_salida, "w", newline="", encoding="utf-8") as f:
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(datos_transformados)

        print(f"  [LOAD] CSV guardado: {self.archivo_salida}")

        # Guardar resumen JSON
        resumen = {
            "fecha_ejecucion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "estadisticas": estadisticas,
        }
        with open(self.archivo_resumen, "w", encoding="utf-8") as f:
            json.dump(resumen, f, indent=4, ensure_ascii=False)

        print(f"  [LOAD] JSON guardado: {self.archivo_resumen}")

    def run(self):
        """Ejecuta el pipeline completo: Extract -> Transform -> Load."""
        print("\n  === INICIO DEL PIPELINE ETL ===")
        inicio = time_module.time()

        # Extract
        datos_raw = self.extract()

        # Transform
        datos_procesados, estadisticas = self.transform(datos_raw)

        # Load
        self.load(datos_procesados, estadisticas)

        tiempo_total = time_module.time() - inicio
        print(f"\n  === PIPELINE COMPLETADO en {tiempo_total:.3f} segundos ===")

        # Mostrar resumen
        print(f"\n  Resumen:")
        print(f"    Total empleados: {estadisticas['total_empleados']}")
        print(f"    Salario promedio: {estadisticas['salario_promedio_global']:,.2f} EUR")
        print(f"    Categorias: {estadisticas['por_categoria']}")
        print(f"\n    Por departamento:")
        for dept, info in estadisticas["por_departamento"].items():
            print(f"      {dept}: {info['empleados']} empleados, "
                  f"promedio {info['salario_promedio']:,.2f} EUR")

        return datos_procesados, estadisticas


# Ejecutar el pipeline
pipeline = Pipeline()
pipeline.run()

# ETL - CONCEPTO CLAVE:
# ETL (Extract, Transform, Load) es el flujo basico de DATA ENGINEERING:
#
# EXTRACT: obtener datos de la fuente (CSV, API, base de datos, etc.)
#   -> Los datos suelen estar "sucios": nombres mal escritos, formatos
#      inconsistentes, valores faltantes, etc.
#
# TRANSFORM: limpiar y enriquecer los datos
#   -> Estandarizar formatos, calcular nuevos campos, agregar categorias,
#      calcular estadisticas, validar datos, etc.
#
# LOAD: guardar los datos procesados en el destino
#   -> Puede ser otro CSV, una base de datos, un data warehouse, etc.
#
# En el mundo real se usan herramientas como:
# - Apache Airflow (orquestacion de pipelines)
# - Apache Spark / PySpark (procesamiento distribuido)
# - dbt (transformaciones SQL)
# - Pandas (transformaciones en Python)
#
# PATRON DE DISENO: Pipeline como clase
# Encapsular cada etapa en un metodo permite:
# 1. Probar cada etapa independientemente
# 2. Reutilizar etapas en otros pipelines
# 3. Manejar errores por etapa
# 4. Medir rendimiento de cada etapa


# Limpieza de archivos de prueba
for archivo in ["notas.csv", "perfil.json", "ventas.csv",
                "informe.txt", "tareas.json", "mi_app.log",
                "empleados_raw.csv", "empleados_procesados.csv",
                "resumen_etl.json"]:
    if os.path.exists(archivo):
        os.remove(archivo)

print("\n--- Fin de las Soluciones Guia 10 ---")
