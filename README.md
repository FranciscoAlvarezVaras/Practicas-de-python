# PRACTICA DE PYTHON

<div align=center>
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" width="120">
</div>

Repositorio de practica personal de Python para el **Master en Big Data & Cloud de EDEM (MDA 2025/2026)**.

Contiene **12 guias progresivas** con **113 ejercicios** que cubren desde variables basicas hasta integracion con IA, inspirados en curriculos de MIT 6.0001, Harvard CS50P y patrones de la industria real.

---

## Estructura del repositorio

Cada guia contiene dos archivos:

| Archivo | Descripcion |
|---------|-------------|
| `ejercicios.py` | Enunciados con espacio para escribir tu codigo (`# TU CODIGO AQUI`) |
| `soluciones.py` | Soluciones completas con explicaciones detalladas |

```
PYTHON_PRACTICE/
|
|-- guia_01_variables_tipos_strings/
|-- guia_02_operadores_condicionales/
|-- guia_03_listas_tuplas_diccionarios/
|-- guia_04_bucles_for_while/
|-- guia_05_funciones/
|-- guia_06_clases_excepciones_modulos/
|-- guia_07_proyecto_juegos/
|-- guia_08_algoritmos_estilo_MIT/
|-- guia_09_apis_con_python/
|-- guia_10_automatizacion_datos/
|-- guia_11_analisis_datos_harvard/
|-- guia_12_proyecto_IA_anthropic/
|
|-- README.md  (este archivo)
```

---

## Indice de guias

### Modulo Basico (Guias 1-4)

Fundamentos del lenguaje. Si nunca has programado, empieza aqui.

| # | Guia | Ejercicios | Conceptos clave |
|---|------|-----------|-----------------|
| 01 | [Variables, Tipos y Strings](guia_01_variables_tipos_strings/) | 9 | `int`, `float`, `str`, `bool`, `f-string`, `type()`, `len()`, rebanado (slicing), `repr()` |
| 02 | [Operadores y Condicionales](guia_02_operadores_condicionales/) | 12 | `+`, `-`, `*`, `/`, `//`, `%`, `**`, `==`, `!=`, `and`, `or`, `not`, `in`, `if/elif/else`, IMC, triangulos |
| 03 | [Listas, Tuplas y Diccionarios](guia_03_listas_tuplas_diccionarios/) | 8 | `list`, `tuple`, `dict`, `.append()`, `.pop()`, `.get()`, slicing, matrices, inventarios |
| 04 | [Bucles For y While](guia_04_bucles_for_while/) | 13 | `for`, `while`, `range()`, `enumerate()`, `break`, `continue`, numeros primos, patron diamante |

### Modulo Intermedio (Guias 5-7)

Funciones, clases y proyectos completos. El salto de calidad.

| # | Guia | Ejercicios | Conceptos clave |
|---|------|-----------|-----------------|
| 05 | [Funciones](guia_05_funciones/) | 18 | `def`, `return`, `*args`, `**kwargs`, `lambda`, parametros por defecto, recursion, `map()`, `filter()` |
| 06 | [Clases, Excepciones y Modulos](guia_06_clases_excepciones_modulos/) | 9 | `class`, `__init__`, `self`, herencia, `super()`, `try/except`, `raise`, decoradores, `import` |
| 07 | [Proyecto: Juegos Interactivos](guia_07_proyecto_juegos/) | 5 proyectos | Adivina la palabra, Contador, Ahorcado, Piedra/Papel/Tijeras, Blackjack |

### Modulo Avanzado (Guias 8-10)

Algoritmos, APIs y automatizacion. Nivel profesional.

| # | Guia | Ejercicios | Conceptos clave |
|---|------|-----------|-----------------|
| 08 | [Algoritmos estilo MIT](guia_08_algoritmos_estilo_MIT/) | 10 | Cifrado Cesar, Scrabble, busqueda binaria, ordenamiento burbuja, Fibonacci, biseccion, memoizacion |
| 09 | [APIs con Python](guia_09_apis_con_python/) | 9 | `requests`, JSON, REST, RandomUser, PokeAPI, NASA APOD, CoinGecko, parametros URL, paginacion |
| 10 | [Automatizacion de Datos](guia_10_automatizacion_datos/) | 8 | CSV, JSON, archivos, logger, ETL pipeline, `csv.DictWriter`, `json.dump()`, `os.path` |

### Modulo Especializado (Guias 11-12)

Analisis de datos e integracion con IA. El cierre del ciclo.

| # | Guia | Ejercicios | Conceptos clave |
|---|------|-----------|-----------------|
| 11 | [Analisis de Datos (Harvard)](guia_11_analisis_datos_harvard/) | 6 | Datasets, estadisticas por grupo, distribucion de notas, recomendaciones, cifrado, Monte Carlo |
| 12 | [Proyecto IA (Anthropic/Claude)](guia_12_proyecto_IA_anthropic/) | 6 | Chatbot con reglas, NLP basico, Q&A, generador de datos, pipeline ETL, API de Claude |

---

## Como usar estas guias

### 1. Abre el archivo de ejercicios

```bash
cd PYTHON_PRACTICE/guia_01_variables_tipos_strings
python ejercicios.py
```

### 2. Escribe tu codigo

Busca las secciones marcadas con `# TU CODIGO AQUI` y escribe tu solucion.

### 3. Compara con las soluciones

```bash
python soluciones.py
```

Cada solucion incluye comentarios explicativos con los conceptos clave.

---

## Requisitos

- **Python 3.8+** (recomendado 3.10 o superior)
- **requests** (solo para Guia 9): `pip install requests`
- **anthropic** (solo para Guia 12, ejercicio 6): `pip install anthropic`

No se necesitan `pandas`, `numpy` ni otras librerias externas. Todo esta hecho con Python puro para entender los fundamentos.

---

## Fuentes e inspiracion

| Fuente | Que aporta |
|--------|-----------|
| [MIT 6.0001 (Intro. a Ciencias de la Computacion)](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) | Pensamiento computacional, biseccion, memoizacion, recursion |
| [Harvard CS50P (Intro. a Programacion con Python)](https://cs50.harvard.edu/python/) | Ejercicios practicos, Voz Baja, validacion de tipos |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | Implementaciones de referencia de algoritmos clasicos |
| [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) | Patrones de integracion con Claude API |
| Ejercicios EDEM MDA 2025/2026 | Clases 1-4 del master (base de las guias 1-7) |

---

## Mapa de conceptos

```
GUIA 1: Variables          GUIA 2: Condicionales      GUIA 3: Estructuras
   |                          |                          |
   v                          v                          v
 int, float, str           if/elif/else              list, dict, tuple
 f-strings, len()          and, or, not              .append(), .get()
 type(), rebanado           in, not in                rebanado, matrices
        \                     |                        /
         \                    |                       /
          +-------------------+----------------------+
                              |
                              v
                      GUIA 4: Bucles
                       for, while
                       range, enumerate
                       break, continue
                              |
                 +------------+------------+
                 |                         |
                 v                         v
          GUIA 5: Funciones        GUIA 6: Clases/OOP
          def, return, lambda      class, __init__, self
          *args, **kwargs          herencia, super()
          recursion                try/except, decoradores
                 |                         |
                 +------------+------------+
                              |
                              v
                    GUIA 7: Proyectos
                    (combina todo lo anterior)
                    Ahorcado, Blackjack, PDP
                              |
              +---------------+---------------+
              |               |               |
              v               v               v
       GUIA 8: Algo      GUIA 9: APIs    GUIA 10: Auto
       Busqueda binaria   requests        CSV, JSON
       Ord. burbuja       REST APIs       ETL pipeline
       Memoizacion        Paginacion      Registro
              |               |               |
              +---------------+---------------+
                              |
                 +------------+------------+
                 |                         |
                 v                         v
        GUIA 11: Analisis         GUIA 12: IA
        Datasets, Monte Carlo     Claude API
        Recomendaciones           NLP, Chatbots
        Estadisticas              Pipelines con IA
```

---

## Autor

**Francisco Alvarez Varas**
- Master en Big Data & Cloud - EDEM (Grupo MDAB, 2025/2026)
- LinkedIn: [frankalvarezv](https://www.linkedin.com/in/frankalvarezv/)
- Email: Francisco92varas@gmail.com
