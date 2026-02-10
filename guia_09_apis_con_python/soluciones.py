# ============================================================================
# GUIA 9 - SOLUCIONES: APIs CON PYTHON (+ patrones reales)
# ============================================================================
# Autor: Francisco Alvarez Varas
# REQUISITO: pip install requests
# ============================================================================

import requests
import json

# Constante para verificar si requests funciona
API_DISPONIBLE = True


def hacer_peticion(url, descripcion=""):
    """Funcion auxiliar para hacer peticiones con manejo de errores."""
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()  # lanza error si status es 4xx o 5xx
        return respuesta.json()
    except requests.exceptions.ConnectionError:
        print(f"  Error de conexion{': ' + descripcion if descripcion else ''}")
        return None
    except requests.exceptions.Timeout:
        print(f"  Timeout{': ' + descripcion if descripcion else ''}")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"  Error HTTP: {e}")
        return None
    except Exception as e:
        print(f"  Error inesperado: {e}")
        return None


# ---------------------------------------------------------------------------
# EJERCICIO 1: Primera peticion - RandomUser
# ---------------------------------------------------------------------------
print("=" * 60)
print("EJERCICIO 1: API RandomUser")
print("=" * 60)

datos = hacer_peticion("https://randomuser.me/api/", "RandomUser")

if datos:
    persona = datos["results"][0]
    nombre = f"{persona['name']['first']} {persona['name']['last']}"
    email = persona["email"]
    pais = persona["location"]["country"]
    foto = persona["picture"]["medium"]

    print(f"  Nombre: {nombre}")
    print(f"  Email: {email}")
    print(f"  Pais: {pais}")
    print(f"  Foto: {foto}")

# CONCEPTOS API:
# requests.get(url) -> hace una peticion HTTP GET
# .json()           -> convierte la respuesta JSON a diccionario Python
# .status_code      -> codigo de estado (200=OK, 404=No encontrado, etc.)
# .raise_for_status() -> lanza error si el status es 4xx o 5xx
#
# JSON es el formato estandar para APIs:
# Es basicamente diccionarios y listas de Python
# {"clave": "valor", "lista": [1, 2, 3]}


# ---------------------------------------------------------------------------
# EJERCICIO 2: API del clima
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 2: API del Clima")
print("=" * 60)


def obtener_clima(ciudad="Valencia"):
    """Obtiene el clima actual de una ciudad."""
    url = f"https://wttr.in/{ciudad}?format=j1"
    datos = hacer_peticion(url, f"Clima de {ciudad}")

    if datos and "current_condition" in datos:
        actual = datos["current_condition"][0]
        temp = actual.get("temp_C", "?")
        sensacion = actual.get("FeelsLikeC", "?")
        humedad = actual.get("humidity", "?")
        desc = actual.get("weatherDesc", [{}])[0].get("value", "?")

        print(f"  Ciudad: {ciudad}")
        print(f"  Temperatura: {temp}C (sensacion: {sensacion}C)")
        print(f"  Clima: {desc}")
        print(f"  Humedad: {humedad}%")
        return datos
    return None


obtener_clima("Valencia")

# .get(clave, valor_defecto) es MAS SEGURO que [clave]
# Si la clave no existe, devuelve el valor por defecto en vez de error
# datos.get("temp_C", "?")  -> devuelve "?" si no existe "temp_C"


# ---------------------------------------------------------------------------
# EJERCICIO 3: API de universidades
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 3: Universidades de Espana")
print("=" * 60)

datos = hacer_peticion(
    "http://universities.hipolabs.com/search?country=Spain",
    "Universidades"
)

if datos:
    print(f"  Total universidades en Espana: {len(datos)}")
    print("\n  Primeras 10:")
    for i, uni in enumerate(datos[:10]):
        nombre = uni.get("name", "?")
        web = uni.get("web_pages", ["?"])[0] if uni.get("web_pages") else "?"
        print(f"    {i+1}. {nombre}")
        print(f"       Web: {web}")

    # Buscar EDEM
    edem = [u for u in datos if "EDEM" in u.get("name", "").upper()]
    if edem:
        print(f"\n  EDEM encontrada: {edem[0]['name']}")
    else:
        print("\n  EDEM no aparece en la base de datos")

# LIST COMPREHENSION (muy importante):
# [expresion for variable in lista if condicion]
# Es un for + if en una linea que crea una nueva lista
# [u for u in datos if "EDEM" in u["name"]]
# = filtra solo las universidades que contienen "EDEM"


# ---------------------------------------------------------------------------
# EJERCICIO 4: PokeAPI
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 4: Pokedex con PokeAPI")
print("=" * 60)


def buscar_pokemon(nombre):
    """Busca un Pokemon en la PokeAPI."""
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    datos = hacer_peticion(url, f"Pokemon {nombre}")

    if datos:
        print(f"  Nombre: {datos['name'].capitalize()}")
        print(f"  ID: #{datos['id']}")

        tipos = [t["type"]["name"] for t in datos["types"]]
        print(f"  Tipos: {', '.join(tipos)}")

        print(f"  Peso: {datos['weight'] / 10} kg")
        print(f"  Altura: {datos['height'] / 10} m")

        habilidades = [a["ability"]["name"] for a in datos["abilities"][:5]]
        print(f"  Habilidades: {', '.join(habilidades)}")

        return datos
    return None


buscar_pokemon("pikachu")
print()
buscar_pokemon("charizard")
print()
buscar_pokemon("pokemon_que_no_existe")  # Test error 404


# ---------------------------------------------------------------------------
# EJERCICIO 5: Explorador de paises
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 5: Explorador de Paises")
print("=" * 60)


def buscar_pais(nombre):
    """Busca informacion detallada de un pais."""
    url = f"https://restcountries.com/v3.1/name/{nombre}"
    datos = hacer_peticion(url, f"Pais {nombre}")

    if datos and isinstance(datos, list) and len(datos) > 0:
        pais = datos[0]
        nombre_oficial = pais.get("name", {}).get("official", "?")
        capital = pais.get("capital", ["?"])[0] if pais.get("capital") else "?"
        poblacion = pais.get("population", 0)
        region = pais.get("region", "?")
        area = pais.get("area", 0)
        bandera = pais.get("flag", "")

        # Idiomas: es un diccionario {"spa": "Spanish", "cat": "Catalan"}
        idiomas_dict = pais.get("languages", {})
        idiomas = ", ".join(idiomas_dict.values())

        # Monedas
        monedas_dict = pais.get("currencies", {})
        monedas = ", ".join(
            f"{v.get('name', '?')} ({v.get('symbol', '?')})"
            for v in monedas_dict.values()
        )

        print(f"  {nombre_oficial}")
        print(f"  Capital: {capital}")
        print(f"  Poblacion: {poblacion:,}")
        print(f"  Area: {area:,} km2")
        print(f"  Region: {region}")
        print(f"  Idiomas: {idiomas}")
        print(f"  Monedas: {monedas}")

        return pais
    return None


def comparar_paises(nombre1, nombre2):
    """Compara dos paises."""
    print(f"\n  --- Comparacion: {nombre1} vs {nombre2} ---")

    url1 = f"https://restcountries.com/v3.1/name/{nombre1}"
    url2 = f"https://restcountries.com/v3.1/name/{nombre2}"

    datos1 = hacer_peticion(url1)
    datos2 = hacer_peticion(url2)

    if datos1 and datos2:
        p1 = datos1[0]
        p2 = datos2[0]

        pob1 = p1.get("population", 0)
        pob2 = p2.get("population", 0)
        area1 = p1.get("area", 0)
        area2 = p2.get("area", 0)

        n1 = p1.get("name", {}).get("common", nombre1)
        n2 = p2.get("name", {}).get("common", nombre2)

        print(f"  Poblacion: {n1}={pob1:,} vs {n2}={pob2:,}")
        print(f"    Mas poblado: {n1 if pob1 > pob2 else n2}")

        print(f"  Area: {n1}={area1:,}km2 vs {n2}={area2:,}km2")
        print(f"    Mas grande: {n1 if area1 > area2 else n2}")


buscar_pais("spain")
print()
buscar_pais("japan")
comparar_paises("spain", "france")


# ---------------------------------------------------------------------------
# EJERCICIO 6: Criptomonedas
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 6: Precios Crypto")
print("=" * 60)


def precio_crypto(*monedas):
    """Obtiene precios de criptomonedas en EUR y USD."""
    ids = ",".join(monedas)
    url = (f"https://api.coingecko.com/api/v3/simple/price"
           f"?ids={ids}&vs_currencies=eur,usd")
    datos = hacer_peticion(url, "CoinGecko")

    if datos:
        print(f"  {'Moneda':<15} {'EUR':>12} {'USD':>12}")
        print(f"  {'-'*39}")
        for moneda in monedas:
            if moneda in datos:
                eur = datos[moneda].get("eur", 0)
                usd = datos[moneda].get("usd", 0)
                print(f"  {moneda.capitalize():<15} {eur:>12,.2f} {usd:>12,.2f}")
            else:
                print(f"  {moneda.capitalize():<15} {'N/A':>12} {'N/A':>12}")


precio_crypto("bitcoin", "ethereum", "cardano", "solana")

# FORMATEO AVANZADO DE STRINGS:
# f"{texto:<15}"    -> alineado a la izquierda, 15 espacios
# f"{texto:>15}"    -> alineado a la derecha, 15 espacios
# f"{texto:^15}"    -> centrado en 15 espacios
# f"{numero:>12,.2f}" -> derecha, 12 espacios, separador miles, 2 decimales


# ---------------------------------------------------------------------------
# EJERCICIO 7: NASA APOD
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 7: NASA - Foto del Dia")
print("=" * 60)

datos = hacer_peticion(
    "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY",
    "NASA APOD"
)

if datos:
    titulo = datos.get("title", "?")
    fecha = datos.get("date", "?")
    explicacion = datos.get("explanation", "?")
    url_img = datos.get("url", "?")

    print(f"  Titulo: {titulo}")
    print(f"  Fecha: {fecha}")
    print(f"  Imagen: {url_img}")
    # Mostrar solo los primeros 200 caracteres
    if len(explicacion) > 200:
        print(f"  Descripcion: {explicacion[:200]}...")
    else:
        print(f"  Descripcion: {explicacion}")


# ---------------------------------------------------------------------------
# EJERCICIO 8: Mi Dashboard (proyecto integrador)
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 8: Mi Dashboard Personal")
print("=" * 60)

# 1. Clima
print("\n  [CLIMA]")
obtener_clima("Valencia")

# 2. Dato curioso
print("\n  [DATO CURIOSO]")
dato = hacer_peticion(
    "https://uselessfacts.jsph.pl/api/v2/facts/random",
    "Dato curioso"
)
if dato:
    print(f"  {dato.get('text', 'No disponible')}")

# 3. Chiste
print("\n  [CHISTE DEL DIA]")
chiste = hacer_peticion(
    "https://official-joke-api.appspot.com/random_joke",
    "Chiste"
)
if chiste:
    print(f"  {chiste.get('setup', '?')}")
    print(f"  {chiste.get('punchline', '?')}")

# 4. NASA
print("\n  [NASA - FOTO DEL DIA]")
nasa = hacer_peticion(
    "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY",
    "NASA"
)
if nasa:
    print(f"  {nasa.get('title', 'No disponible')}")
    print(f"  {nasa.get('url', '')}")

print("\n" + "=" * 60)

# PATRON PROFESIONAL para APIs:
# 1. SIEMPRE maneja errores (try/except o verificar status_code)
# 2. Usa timeout para no esperar infinito
# 3. Verifica que la respuesta tiene los campos esperados (.get())
# 4. Separa la logica en funciones reutilizables
# 5. No hagas demasiadas peticiones seguidas (rate limiting)
#
# CODIGOS DE ESTADO HTTP:
# 200 -> OK (todo bien)
# 201 -> Created (recurso creado)
# 400 -> Bad Request (peticion mal formada)
# 401 -> Unauthorized (necesitas autenticacion)
# 403 -> Forbidden (no tienes permiso)
# 404 -> Not Found (no existe)
# 429 -> Too Many Requests (has hecho demasiadas peticiones)
# 500 -> Internal Server Error (error del servidor)


# ---------------------------------------------------------------------------
# EJERCICIO 9: API con parametros y paginacion (patron real-world)
# ---------------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO 9: JSONPlaceholder - Parametros y combinacion")
print("=" * 60)

BASE_URL_JP = "https://jsonplaceholder.typicode.com"


def obtener_posts(usuario_id):
    """Obtiene todos los posts de un usuario especifico."""
    url = f"{BASE_URL_JP}/posts?userId={usuario_id}"
    datos = hacer_peticion(url, f"Posts del usuario {usuario_id}")
    if datos:
        print(f"  Usuario {usuario_id} tiene {len(datos)} posts")
        return datos
    return []


def obtener_info_completa(usuario_id):
    """Obtiene info completa de un usuario: datos + posts + comentarios."""
    # 1. Datos del usuario
    usuario = hacer_peticion(
        f"{BASE_URL_JP}/users/{usuario_id}",
        f"Usuario {usuario_id}"
    )
    if not usuario:
        print(f"  No se pudo obtener el usuario {usuario_id}")
        return None

    print(f"  Usuario: {usuario.get('name', '?')} ({usuario.get('email', '?')})")
    print(f"  Ciudad: {usuario.get('address', {}).get('city', '?')}")
    print(f"  Empresa: {usuario.get('company', {}).get('name', '?')}")

    # 2. Posts del usuario
    posts = obtener_posts(usuario_id)

    # 3. Para cada post, contar comentarios
    print(f"\n  Posts y comentarios:")
    total_comentarios = 0
    for i, post in enumerate(posts[:5]):  # Solo mostramos los 5 primeros
        comentarios = hacer_peticion(
            f"{BASE_URL_JP}/posts/{post['id']}/comments",
            f"Comentarios post {post['id']}"
        )
        n_comentarios = len(comentarios) if comentarios else 0
        total_comentarios += n_comentarios

        # Truncar titulo si es muy largo
        titulo = post.get("title", "?")
        if len(titulo) > 50:
            titulo = titulo[:50] + "..."
        print(f"    {i+1}. {titulo} ({n_comentarios} comentarios)")

    if len(posts) > 5:
        print(f"    ... y {len(posts) - 5} posts mas")

    print(f"\n  Total comentarios (primeros 5 posts): {total_comentarios}")
    return usuario


def buscar_posts(palabra_clave):
    """Busca posts que contengan una palabra clave en titulo o body."""
    todos_los_posts = hacer_peticion(
        f"{BASE_URL_JP}/posts",
        "Todos los posts"
    )
    if not todos_los_posts:
        return []

    palabra = palabra_clave.lower()
    resultados = [
        post for post in todos_los_posts
        if palabra in post.get("title", "").lower()
        or palabra in post.get("body", "").lower()
    ]

    print(f"  Busqueda '{palabra_clave}': {len(resultados)} resultados "
          f"de {len(todos_los_posts)} posts totales")

    for i, post in enumerate(resultados[:5]):
        titulo = post.get("title", "?")
        if len(titulo) > 60:
            titulo = titulo[:60] + "..."
        print(f"    {i+1}. [Post #{post['id']}] {titulo}")

    if len(resultados) > 5:
        print(f"    ... y {len(resultados) - 5} resultados mas")

    return resultados


# Pruebas
print("\n--- Posts del usuario 1 ---")
posts_u1 = obtener_posts(1)

print("\n--- Info completa del usuario 3 ---")
obtener_info_completa(3)

print("\n--- Buscar posts con 'qui' ---")
buscar_posts("qui")

print("\n--- Buscar posts con 'voluptatem' ---")
buscar_posts("voluptatem")

# PATRONES REALES DE APIs:
# 1. PARAMETROS URL (?key=value): filtrar datos del lado del servidor
#    /posts?userId=1  -> solo posts del usuario 1
#    Es mas eficiente que traer TODO y filtrar en Python
#
# 2. ENDPOINTS ANIDADOS (/recurso/{id}/sub-recurso):
#    /posts/1/comments -> comentarios del post 1
#    Esto se llama "resource nesting" en REST APIs
#
# 3. COMBINAR PETICIONES:
#    En el mundo real casi nunca una sola peticion te da todo.
#    Tienes que combinar datos de multiples endpoints.
#    Ejemplo: obtener usuario + sus posts + comentarios de cada post
#
# 4. PAGINACION:
#    APIs grandes devuelven datos "por paginas" para no saturar
#    JSONPlaceholder no pagina, pero APIs reales usan:
#    /posts?page=1&limit=10  -> primera pagina, 10 resultados


print("\n--- Fin de las Soluciones Guia 9 ---")
