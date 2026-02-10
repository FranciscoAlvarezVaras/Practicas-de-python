# ============================================================================
# GUIA 12 - SOLUCIONES: PROYECTO INTEGRADOR - PYTHON + IA
# ============================================================================
# Autor: Francisco Alvarez Varas
# Inspirado en: Anthropic Cookbook, Anthropic SDK Python
# ============================================================================

import json
import random
import os
import csv
from datetime import datetime


# ---------------------------------------------------------------------------
# EJERCICIO 1: Chatbot con reglas
# ---------------------------------------------------------------------------
print("=" * 60)
print("EJERCICIO 1: Chatbot con reglas")
print("=" * 60)


class ChatBot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

        # Reglas: palabras clave por intencion
        self.reglas = {
            "saludo": ["hola", "hey", "buenos dias", "buenas", "hi"],
            "despedida": ["adios", "chao", "hasta luego", "bye", "nos vemos"],
            "estado": ["como estas", "que tal", "como te va"],
            "nombre": ["como te llamas", "tu nombre", "quien eres"],
            "ayuda": ["ayuda", "help", "necesito", "puedes"],
            "python": ["python", "programar", "codigo", "programa"],
            "gracias": ["gracias", "thanks", "genial", "perfecto"],
        }

        # Respuestas por intencion
        self.respuestas = {
            "saludo": ["Hola! En que puedo ayudarte?",
                       "Hey! Que necesitas?",
                       "Buenos dias! Estoy aqui para ayudar."],
            "despedida": ["Hasta luego! Fue un placer.",
                          "Adios! Vuelve cuando quieras."],
            "estado": ["Estoy funcionando perfectamente! Y tu?",
                       "Muy bien, gracias por preguntar!"],
            "nombre": [f"Me llamo {nombre}. Soy un chatbot creado en Python!"],
            "ayuda": ["Claro! Puedo hablar sobre Python, responder preguntas "
                      "basicas, o simplemente charlar."],
            "python": ["Python es un lenguaje genial! Que quieres saber?",
                       "Me encanta Python! Es muy versatil."],
            "gracias": ["De nada! Para eso estoy.",
                        "Un placer! Algo mas?"],
            "default": ["No estoy seguro de como responder a eso...",
                        "Interesante! Podrias ser mas especifico?",
                        "No entiendo bien. Prueba de otra forma."],
        }

    def clasificar(self, mensaje):
        """Detecta la intencion del mensaje."""
        mensaje_lower = mensaje.lower().strip()

        for intencion, palabras_clave in self.reglas.items():
            for palabra in palabras_clave:
                if palabra in mensaje_lower:
                    return intencion
        return "default"

    def responder(self, mensaje):
        """Genera una respuesta basada en la intencion detectada."""
        intencion = self.clasificar(mensaje)
        respuesta = random.choice(self.respuestas[intencion])

        # Guardar en historial
        self.historial.append({
            "usuario": mensaje,
            "bot": respuesta,
            "intencion": intencion,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        })

        return respuesta


# Demo (sin input interactivo para poder ejecutar el archivo)
bot = ChatBot("PyBot")

mensajes_demo = [
    "Hola!",
    "Como te llamas?",
    "Me puedes ayudar con Python?",
    "Gracias por la ayuda",
    "Adios!"
]

for msg in mensajes_demo:
    respuesta = bot.responder(msg)
    print(f"  Usuario: {msg}")
    print(f"  {bot.nombre}: {respuesta}\n")

# CONCEPTO CLAVE: El chatbot clasifica la INTENCION del mensaje
# Esto es la base de los chatbots reales (antes de la IA generativa)
# Los chatbots modernos (como ChatGPT/Claude) usan redes neuronales
# pero la idea es la misma: entender que quiere el usuario


# ---------------------------------------------------------------------------
# EJERCICIO 2: NLP basico
# ---------------------------------------------------------------------------
print("=" * 60)
print("EJERCICIO 2: NLP basico")
print("=" * 60)

PALABRAS_POSITIVAS = {"bueno", "genial", "excelente", "fantastico", "increible",
                      "perfecto", "maravilloso", "feliz", "amor", "mejor",
                      "bien", "bonito", "facil", "rapido", "util"}

PALABRAS_NEGATIVAS = {"malo", "terrible", "horrible", "odio", "peor", "feo",
                      "triste", "error", "problema", "dificil", "lento",
                      "complicado", "aburrido", "confuso", "frustrado"}

# Palabras que NO aportan significado (stop words)
STOP_WORDS = {"el", "la", "los", "las", "un", "una", "de", "del", "en",
              "que", "es", "por", "con", "se", "su", "para", "como", "al",
              "no", "si", "ya", "o", "y", "a", "e", "muy", "mas", "pero"}


def analizar_sentimiento(texto):
    """Analiza si un texto es positivo, negativo o neutro."""
    palabras = texto.lower().split()
    palabras = [p.strip(".,!?;:") for p in palabras]

    positivas = sum(1 for p in palabras if p in PALABRAS_POSITIVAS)
    negativas = sum(1 for p in palabras if p in PALABRAS_NEGATIVAS)

    if positivas > negativas:
        return "positivo", positivas, negativas
    elif negativas > positivas:
        return "negativo", positivas, negativas
    else:
        return "neutro", positivas, negativas


def extraer_entidades(texto):
    """Extrae entidades basicas de un texto."""
    palabras = texto.split()
    entidades = {"emails": [], "numeros": [], "posibles_nombres": []}

    for palabra in palabras:
        limpia = palabra.strip(".,!?;:()")

        if "@" in limpia:
            entidades["emails"].append(limpia)
        elif limpia.isdigit():
            entidades["numeros"].append(int(limpia))
        elif limpia[0:1].isupper() and len(limpia) > 1 and limpia.isalpha():
            entidades["posibles_nombres"].append(limpia)

    return entidades


def resumir(texto, n_oraciones=2):
    """Devuelve las n oraciones mas importantes."""
    oraciones = [o.strip() for o in texto.split(".") if o.strip()]

    # Puntuar cada oracion por cantidad de palabras significativas
    puntuaciones = []
    for oracion in oraciones:
        palabras = oracion.lower().split()
        significativas = [p for p in palabras if p not in STOP_WORDS]
        puntuaciones.append((oracion, len(significativas)))

    # Ordenar por puntuacion y devolver las mejores
    ordenadas = sorted(puntuaciones, key=lambda x: x[1], reverse=True)
    return [o[0] + "." for o in ordenadas[:n_oraciones]]


# Pruebas
textos_test = [
    "Python es un lenguaje genial, facil y muy util para programar",
    "Este codigo es terrible, lento y muy complicado de entender",
    "Hoy es martes y hace sol en Valencia"
]

print("  Analisis de sentimiento:")
for texto in textos_test:
    sent, pos, neg = analizar_sentimiento(texto)
    print(f"    '{texto[:50]}...' -> {sent} (pos:{pos}, neg:{neg})")

print("\n  Extraccion de entidades:")
texto_ent = "Francisco mando un email a ana@email.com el dia 15 de marzo"
entidades = extraer_entidades(texto_ent)
print(f"    Texto: {texto_ent}")
for tipo, valores in entidades.items():
    if valores:
        print(f"    {tipo}: {valores}")

print("\n  Resumen:")
texto_largo = ("Python es un lenguaje de programacion poderoso. "
               "Fue creado por Guido van Rossum en 1991. "
               "Python tiene una sintaxis clara y legible. "
               "Es utilizado por Google y Netflix. "
               "Python es ideal para inteligencia artificial y analisis de datos")
resumen = resumir(texto_largo, 2)
for oracion in resumen:
    print(f"    {oracion}")


# ---------------------------------------------------------------------------
# EJERCICIO 3: Sistema Q&A
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 3: Sistema de preguntas y respuestas")
print("=" * 60)


class SistemaQA:
    def __init__(self, texto):
        self.texto = texto
        self.oraciones = [o.strip() + "." for o in texto.split(".")
                          if o.strip()]

    def _palabras_clave(self, pregunta):
        """Extrae palabras clave de una pregunta."""
        palabras = pregunta.lower().strip("?!").split()
        return [p for p in palabras if p not in STOP_WORDS and len(p) > 2]

    def responder(self, pregunta):
        """Busca la oracion mas relevante para la pregunta."""
        claves = self._palabras_clave(pregunta)

        if not claves:
            return "No entiendo la pregunta."

        mejor_oracion = ""
        mejor_puntuacion = 0

        for oracion in self.oraciones:
            oracion_lower = oracion.lower()
            puntuacion = sum(1 for c in claves if c in oracion_lower)

            if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion
                mejor_oracion = oracion

        if mejor_puntuacion > 0:
            return mejor_oracion
        return "No encontre informacion sobre eso en el texto."


# Demo
texto_base = (
    "Python es un lenguaje de programacion creado por Guido van Rossum. "
    "Fue lanzado por primera vez en 1991. "
    "Python es muy popular para analisis de datos y machine learning. "
    "Las empresas como Google y Netflix usan Python extensivamente. "
    "Python tiene una comunidad muy grande y activa. "
    "El nombre Python viene del grupo de comedia Monty Python"
)

qa = SistemaQA(texto_base)

preguntas = [
    "Quien creo Python?",
    "Cuando se lanzo Python?",
    "Para que se usa Python?",
    "Que empresas usan Python?",
    "De donde viene el nombre Python?",
]

for pregunta in preguntas:
    respuesta = qa.responder(pregunta)
    print(f"  P: {pregunta}")
    print(f"  R: {respuesta}\n")


# ---------------------------------------------------------------------------
# EJERCICIO 4: Generador de datos
# ---------------------------------------------------------------------------
print("=" * 60)
print("EJERCICIO 4: Generador de datos")
print("=" * 60)


class GeneradorDatos:
    NOMBRES_M = ["Carlos", "Luis", "Juan", "Pedro", "Francisco",
                 "Diego", "Pablo", "Jorge", "Miguel", "Raul"]
    NOMBRES_F = ["Ana", "Maria", "Laura", "Sofia", "Elena",
                 "Marta", "Pilar", "Clara", "Lucia", "Rosa"]
    APELLIDOS = ["Garcia", "Lopez", "Martinez", "Rodriguez", "Fernandez",
                 "Gonzalez", "Sanchez", "Perez", "Gomez", "Ruiz"]
    CIUDADES = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao",
                "Malaga", "Zaragoza", "Murcia", "Palma", "Alicante"]
    EMPRESAS = ["TechCorp", "DataSoft", "CloudInn", "AIVentures",
                "DevHub", "NetWorks", "ByteLab", "CodeBase"]
    PUESTOS = ["Developer", "Data Analyst", "Project Manager",
               "Designer", "DevOps", "Data Scientist", "QA Engineer"]

    def persona(self):
        """Genera una persona ficticia."""
        genero = random.choice(["M", "F"])
        nombre = random.choice(
            self.NOMBRES_M if genero == "M" else self.NOMBRES_F
        )
        apellido = random.choice(self.APELLIDOS)
        empresa = random.choice(self.EMPRESAS)

        return {
            "nombre": nombre,
            "apellido": apellido,
            "edad": random.randint(22, 55),
            "email": f"{nombre.lower()}.{apellido.lower()}@{empresa.lower()}.com",
            "ciudad": random.choice(self.CIUDADES),
            "empresa": empresa,
            "puesto": random.choice(self.PUESTOS),
            "salario": round(random.uniform(25000, 80000), 2),
        }

    def dataset(self, n=10):
        """Genera n personas."""
        return [self.persona() for _ in range(n)]

    def exportar_csv(self, datos, archivo):
        """Exporta datos a CSV."""
        if not datos:
            return
        with open(archivo, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=datos[0].keys())
            writer.writeheader()
            writer.writerows(datos)

    def exportar_json(self, datos, archivo):
        """Exporta datos a JSON."""
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)


# Demo
gen = GeneradorDatos()
muestra = gen.dataset(5)

print("  5 personas generadas:")
for p in muestra:
    print(f"    {p['nombre']} {p['apellido']} | {p['puesto']} en {p['empresa']} "
          f"| {p['ciudad']} | {p['salario']:,.0f} EUR")


# ---------------------------------------------------------------------------
# EJERCICIO 5: Pipeline ETL
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 5: Pipeline ETL")
print("=" * 60)


class Pipeline:
    def __init__(self, nombre="Pipeline"):
        self.nombre = nombre
        self.pasos = []
        self.log = []

    def agregar_paso(self, funcion, descripcion=""):
        """Agrega un paso al pipeline."""
        self.pasos.append((funcion, descripcion))

    def ejecutar(self, datos):
        """Ejecuta todos los pasos en orden."""
        self.log = []
        self.log.append(f"[INICIO] {self.nombre} - {len(datos)} registros")

        for i, (funcion, descripcion) in enumerate(self.pasos):
            antes = len(datos)
            datos = funcion(datos)
            despues = len(datos) if isinstance(datos, list) else "N/A"
            msg = f"[PASO {i+1}] {descripcion}: {antes} -> {despues} registros"
            self.log.append(msg)
            print(f"    {msg}")

        self.log.append(f"[FIN] Pipeline completado")
        return datos


# Funciones de transformacion
def normalizar_nombres(datos):
    for d in datos:
        d["nombre"] = d["nombre"].strip().title()
        d["apellido"] = d["apellido"].strip().title()
    return datos


def validar_emails(datos):
    for d in datos:
        email = d.get("email", "")
        if "@" not in email or "." not in email:
            d["email_valido"] = False
        else:
            d["email_valido"] = True
    return datos


def agregar_rango_edad(datos):
    for d in datos:
        edad = d.get("edad", 0)
        if edad < 30:
            d["rango_edad"] = "joven"
        elif edad < 45:
            d["rango_edad"] = "adulto"
        else:
            d["rango_edad"] = "senior"
    return datos


def agregar_timestamp(datos):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for d in datos:
        d["procesado_en"] = ts
    return datos


def eliminar_duplicados_pipeline(datos):
    vistos = set()
    unicos = []
    for d in datos:
        clave = d.get("email", "")
        if clave not in vistos:
            vistos.add(clave)
            unicos.append(d)
    return unicos


# Crear y ejecutar pipeline
gen = GeneradorDatos()
datos_crudos = gen.dataset(20)

etl = Pipeline("ETL Empleados")
etl.agregar_paso(normalizar_nombres, "Normalizar nombres")
etl.agregar_paso(validar_emails, "Validar emails")
etl.agregar_paso(agregar_rango_edad, "Agregar rango de edad")
etl.agregar_paso(agregar_timestamp, "Agregar timestamp")
etl.agregar_paso(eliminar_duplicados_pipeline, "Eliminar duplicados")

datos_procesados = etl.ejecutar(datos_crudos)

print(f"\n  Resultado: {len(datos_procesados)} registros procesados")
print(f"  Ejemplo: {json.dumps(datos_procesados[0], indent=4, ensure_ascii=False)}")

# PIPELINE: patron muy usado en data engineering
# Los datos pasan por una serie de transformaciones en orden
# Es como una cadena de montaje: cada paso hace una cosa
# ETL (Extract, Transform, Load) es la base de data engineering


# ---------------------------------------------------------------------------
# EJERCICIO 6: Integracion con Claude API (Anthropic)
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 6: Integracion con Claude API")
print("=" * 60)


class AsistentePython:
    """Asistente de Python usando la API de Claude.
    NOTA: Cada llamada a la API tiene un coste. Revisa tus limites en
    console.anthropic.com antes de hacer muchas consultas."""

    def __init__(self):
        self.historial = []
        self.api_disponible = False

        try:
            import anthropic
            self.client = anthropic.Anthropic()
            self.api_disponible = True
            print("  API de Anthropic conectada!")
        except ImportError:
            print("  [INFO] anthropic no instalado. pip install anthropic")
        except Exception as e:
            print(f"  [INFO] API no disponible: {e}")

    def preguntar(self, pregunta, modo_profesor=False):
        """Envia una pregunta a Claude y devuelve la respuesta."""
        if not self.api_disponible:
            return self._respuesta_simulada(pregunta)

        # Construir el prompt segun el modo
        if modo_profesor:
            sistema = ("Eres un profesor de Python del MIT. Explica los "
                       "conceptos paso a paso, con ejemplos simples. "
                       "Usa analogias para que un novato entienda.")
        else:
            sistema = ("Eres un asistente de Python. Responde de forma "
                       "concisa y con ejemplos de codigo cuando sea util.")

        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-5-20250929",
                max_tokens=1024,
                system=sistema,
                messages=[{"role": "user", "content": pregunta}]
            )
            respuesta = message.content[0].text
        except Exception as e:
            respuesta = f"Error al consultar la API: {e}"

        # Guardar en historial
        self.historial.append({
            "pregunta": pregunta,
            "respuesta": respuesta,
            "modo": "profesor" if modo_profesor else "asistente",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        return respuesta

    def _respuesta_simulada(self, pregunta):
        """Respuesta simulada cuando no hay API disponible."""
        respuestas = {
            "lista": "Una lista en Python es una coleccion ordenada y "
                     "modificable. Se crea con []. Ejemplo: mi_lista = [1, 2, 3]",
            "funcion": "Una funcion se define con 'def'. Ejemplo:\n"
                       "def saludar(nombre):\n    return f'Hola {nombre}'",
            "diccionario": "Un diccionario almacena pares clave:valor. "
                           "Ejemplo: persona = {'nombre': 'Ana', 'edad': 25}",
            "for": "El bucle for recorre elementos: for x in [1,2,3]: print(x)",
            "clase": "Una clase agrupa datos y funciones:\n"
                     "class Perro:\n    def __init__(self, nombre):\n"
                     "        self.nombre = nombre",
        }

        pregunta_lower = pregunta.lower()
        for clave, resp in respuestas.items():
            if clave in pregunta_lower:
                return f"[SIMULADO] {resp}"

        return ("[SIMULADO] Para obtener respuestas reales, configura "
                "tu API key de Anthropic. Visita: https://console.anthropic.com")

    def guardar_historial(self, archivo="historial_chat.json"):
        """Guarda el historial en JSON."""
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(self.historial, f, indent=4, ensure_ascii=False)


# Demo
asistente = AsistentePython()

preguntas_demo = [
    "Que es una lista en Python?",
    "Como se crea una funcion?",
    "Explicame que es un diccionario",
]

for pregunta in preguntas_demo:
    print(f"\n  Pregunta: {pregunta}")
    respuesta = asistente.preguntar(pregunta)
    print(f"  Respuesta: {respuesta[:200]}...")

# COMO FUNCIONA LA API DE CLAUDE:
# 1. Instalas: pip install anthropic
# 2. Configuras tu API key:
#    export ANTHROPIC_API_KEY="tu-api-key-aqui"  (Linux/Mac)
#    set ANTHROPIC_API_KEY=tu-api-key-aqui       (Windows)
# 3. Creas un cliente: client = anthropic.Anthropic()
# 4. Envias un mensaje:
#    message = client.messages.create(
#        model="claude-sonnet-4-5-20250929",  # modelo a usar
#        max_tokens=1024,                # largo maximo de respuesta
#        system="instrucciones",         # como debe comportarse
#        messages=[{"role": "user", "content": "pregunta"}]
#    )
# 5. Lees la respuesta: message.content[0].text
#
# Es el mismo patron que usamos con requests.get() en la Guia 9:
# envias datos -> recibes respuesta -> la procesas
# La diferencia es que aqui la respuesta es INTELIGENTE


# ============================================================================
# RESUMEN FINAL DE TODAS LAS GUIAS
# ============================================================================
print("\n" + "=" * 60)
print("FELICIDADES! HAS COMPLETADO LAS 12 GUIAS DE PYTHON")
print("=" * 60)

print("""
RECORRIDO COMPLETO:

  FUNDAMENTOS (Guias 1-7):
    1. Variables, Tipos, Strings
    2. Operadores, Condicionales
    3. Listas, Tuplas, Diccionarios
    4. Bucles (for, while)
    5. Funciones (*args, **kwargs, lambda)
    6. Clases, Excepciones, Modulos
    7. Proyectos: Juegos interactivos

  NIVEL AVANZADO (Guias 8-12):
    8. Algoritmos estilo MIT (Cifrado, Scrabble, Fibonacci)
    9. APIs con Python (requests, JSON, APIs reales)
   10. Automatizacion y Procesamiento de Datos (CSV, JSON, ETL)
   11. Analisis de Datos estilo Harvard (Monte Carlo, NLP, Recomendaciones)
   12. Integracion con IA (Chatbot, NLP, Claude API)

  FUENTES DE INSPIRACION:
    - MIT 6.0001 (OCW)
    - Harvard CS50P
    - Anthropic Cookbook
    - TheAlgorithms/Python
    - Real Python

  SIGUIENTE NIVEL:
    - pandas y numpy para data science
    - Flask/FastAPI para crear APIs
    - PySpark para big data (ya lo viste en clase!)
    - Machine Learning con scikit-learn

  Tu viaje de Python apenas empieza. Sigue practicando!
""")

# Limpieza
for archivo in ["historial_chat.json"]:
    if os.path.exists(archivo):
        os.remove(archivo)

print("--- Fin de las Soluciones Guia 12 ---")
