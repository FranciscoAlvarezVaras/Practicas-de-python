# ============================================================================
# GUIA 9: APIs CON PYTHON - Conecta con el mundo real (+ patrones reales)
# ============================================================================
# Autor: Francisco Alvarez Varas
# Inspirado en:
#   - Real Python API tutorials: https://realpython.com/api-integration-in-python/
#   - 4GeeksAcademy exercises: https://github.com/4GeeksAcademy/python-http-requests-api-tutorial-exercises
#   - public-apis/public-apis: https://github.com/public-apis/public-apis
#   - Real-world API patterns: parametros, paginacion, combinacion de endpoints
#
# REQUISITO: pip install requests
# (ejecuta en terminal: pip install requests)
#
# TODAS las APIs usadas son GRATUITAS y NO necesitan API key
# ============================================================================


# ---------------------------------------------------------------------------
# EJERCICIO 1: Tu primera peticion - Datos aleatorios
# ---------------------------------------------------------------------------
# Haz una peticion GET a esta API que devuelve datos de una persona ficticia:
# URL: https://randomuser.me/api/
#
# 1. Importa requests
# 2. Haz requests.get(url)
# 3. Convierte a JSON con .json()
# 4. Extrae e imprime:
#    - Nombre completo (first + last)
#    - Email
#    - Pais
#    - Foto (URL de la imagen)
#
# Pista: la respuesta tiene esta estructura:
# {"results": [{"name": {"first": "...", "last": "..."}, "email": "...", ...}]}

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 2: API del clima - Datos meteorologicos
# ---------------------------------------------------------------------------
# API gratuita del clima (no necesita key):
# URL: https://wttr.in/Valencia?format=j1
#
# 1. Haz la peticion GET
# 2. Del JSON, extrae:
#    - Temperatura actual (current_condition -> temp_C)
#    - Sensacion termica (current_condition -> FeelsLikeC)
#    - Descripcion del clima (current_condition -> weatherDesc)
#    - Humedad (current_condition -> humidity)
# 3. Imprime todo formateado bonito
# 4. BONUS: haz que el usuario pueda elegir la ciudad

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 3: API de universidades - Busqueda por pais
# ---------------------------------------------------------------------------
# API que devuelve universidades por pais:
# URL: http://universities.hipolabs.com/search?country=Spain
#
# 1. Haz la peticion
# 2. La respuesta es una LISTA de diccionarios
# 3. Imprime las primeras 10 universidades con:
#    - Nombre
#    - Web
#    - Dominio
# 4. Cuenta cuantas universidades hay en total en Espana
# 5. BONUS: busca si "EDEM" esta en la lista

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 4: API de Pokemon - Pokedex
# ---------------------------------------------------------------------------
# La PokeAPI es perfecta para aprender APIs:
# URL base: https://pokeapi.co/api/v2/pokemon/{nombre_o_id}
#
# 1. Pide el Pokemon "pikachu": https://pokeapi.co/api/v2/pokemon/pikachu
# 2. Extrae e imprime:
#    - Nombre
#    - ID en la Pokedex
#    - Tipos (puede tener mas de uno)
#    - Peso y altura
#    - Lista de sus primeras 5 habilidades (abilities)
# 3. BONUS: crea una funcion "buscar_pokemon(nombre)" que haga todo esto
# 4. BONUS 2: maneja el error si el Pokemon no existe (status_code 404)

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 5: API de paises - Proyecto completo
# ---------------------------------------------------------------------------
# API de informacion de paises:
# URL: https://restcountries.com/v3.1/name/{pais}
# Ejemplo: https://restcountries.com/v3.1/name/spain
#
# Crea un programa "explorador de paises" con estas funciones:
#
# 1. buscar_pais(nombre):
#    - Busca un pais y devuelve: nombre oficial, capital, poblacion,
#      region, idiomas, monedas, bandera (emoji)
#
# 2. comparar_paises(pais1, pais2):
#    - Compara dos paises y muestra cual tiene mas poblacion,
#      mas area, etc.
#
# 3. paises_por_region(region):
#    URL: https://restcountries.com/v3.1/region/{region}
#    - Busca todos los paises de una region (Europe, Americas, Asia...)
#    - Muestra los 5 mas poblados

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 6: API de criptomonedas - Datos financieros
# ---------------------------------------------------------------------------
# API de precios de criptomonedas:
# URL: https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=eur,usd
#
# 1. Obtener el precio de Bitcoin y Ethereum en EUR y USD
# 2. Crea una funcion "precio_crypto(moneda)" que devuelva el precio actual
#    Monedas validas: bitcoin, ethereum, cardano, solana, etc.
# 3. Formatea los precios con separador de miles
# 4. BONUS: guarda los precios en un diccionario y muestra una tabla

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 7: API de datos del espacio - NASA APOD
# ---------------------------------------------------------------------------
# La NASA tiene una API que devuelve la "Foto Astronomica del Dia":
# URL: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
# (DEMO_KEY funciona sin registro, pero tiene limite de peticiones)
#
# 1. Haz la peticion GET
# 2. Extrae: titulo, fecha, explicacion, url de la imagen
# 3. Imprime la informacion formateada
# 4. BONUS: la explicacion suele ser larga, muestra solo los primeros
#    200 caracteres seguidos de "..."

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 8: Creando tu propia "mini base de datos" con APIs
# ---------------------------------------------------------------------------
# Proyecto integrador: combina varias APIs para crear algo util
#
# Crea un programa "Mi Dashboard" que al ejecutarse muestre:
# 1. El clima actual de tu ciudad (wttr.in)
# 2. Un dato curioso aleatorio (https://uselessfacts.jsph.pl/api/v2/facts/random)
# 3. La foto astronomica del dia (NASA APOD)
# 4. Un chiste aleatorio (https://official-joke-api.appspot.com/random_joke)
#
# Formatea todo bonito con separadores y titulos
# Maneja errores: si una API falla, muestra "No disponible" y sigue

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 9: API con parametros y paginacion (patron real-world)
# ---------------------------------------------------------------------------
# En el mundo real, las APIs tienen MUCHOS endpoints y hay que combinar
# datos de varias peticiones. Esto es lo que hacen los ingenieros de datos
# y backend developers a diario.
#
# Usa la API JSONPlaceholder (API de prueba gratuita, sin key):
# Base URL: https://jsonplaceholder.typicode.com
#
# Endpoints disponibles:
# - /posts          -> todos los posts (100 posts)
# - /posts?userId=1 -> posts de un usuario especifico (parametro URL)
# - /users          -> todos los usuarios (10 usuarios)
# - /users/1        -> un usuario por ID
# - /posts/1/comments -> comentarios de un post (relacion anidada)
#
# Crea estas funciones:
#
# 1. obtener_posts(usuario_id):
#    - Obtiene todos los posts de un usuario especifico
#    - URL: https://jsonplaceholder.typicode.com/posts?userId={usuario_id}
#    - Devuelve una lista de posts (cada post tiene: id, title, body)
#
# 2. obtener_info_completa(usuario_id):
#    - Obtiene la info COMPLETA de un usuario:
#      a) Datos del usuario (/users/{id})
#      b) Todos sus posts (/posts?userId={id})
#      c) Para cada post, cuantos comentarios tiene (/posts/{id}/comments)
#    - Imprime todo formateado:
#      "Usuario: nombre (email)"
#      "Post 1: titulo (X comentarios)"
#      "Post 2: titulo (X comentarios)"
#      ...
#
# 3. buscar_posts(palabra_clave):
#    - Obtiene TODOS los posts (/posts)
#    - Filtra los que contengan la palabra clave en el titulo O en el body
#    - Devuelve la lista de posts que coinciden
#
# Este ejercicio demuestra: parametros URL, combinar multiples API calls,
# y procesamiento de datos reales.
#
# Pista: para parametros URL puedes usar f-strings directamente:
#   url = f"https://jsonplaceholder.typicode.com/posts?userId={id}"
# Pista: para buscar texto: if palabra.lower() in texto.lower()

# TU CODIGO AQUI:




print("\n--- Fin de la Guia 9 ---")
print("Ahora sabes conectar Python con CUALQUIER servicio de internet!")
print("Esto es una habilidad MUY valiosa en el mundo real.")
