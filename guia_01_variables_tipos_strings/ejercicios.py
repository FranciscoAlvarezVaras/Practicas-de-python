# ============================================================================
# GUIA 1: VARIABLES, TIPOS DE DATOS Y STRINGS
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 1
# Enriquecido con: MIT 6.0001 (OCW), Harvard CS50P (Pset 0)
#
# INSTRUCCIONES:
# - Lee cada ejercicio con atencion
# - Escribe tu codigo debajo de donde dice "# TU CODIGO AQUI"
# - Ejecuta el archivo para comprobar: python ejercicios.py
# - Si te atascas, consulta soluciones.py (pero intenta primero!)
# ============================================================================


# ---------------------------------------------------------------------------
# EJERCICIO 1: Creando variables y concatenando
# ---------------------------------------------------------------------------
# 1. Crea una variable "calle" con el nombre de tu calle
# 2. Crea una variable "numero" con el numero de tu casa
# 3. Crea una variable "ciudad" con tu ciudad
# 4. Crea una variable "codigo_postal" con tu codigo postal
# 5. Crea una variable "direccion_completa" que junte todas las anteriores
#    separadas por comas
# 6. Imprime la direccion completa por pantalla
# 7. Imprime un mensaje que diga: "Mi direccion tiene X caracteres"
#    (usa f-strings y len())

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 2: Variables bien y mal escritas
# ---------------------------------------------------------------------------
# Mira las siguientes variables. Piensa cuales estan MAL y por que.
# Luego descomenta cada una (quita el #) y ejecuta para comprobar.
#
# a) mi_variable = "Economia"
# b) otra_var = "Ejercicio
# c) True = "Ejercicio"
# d) mi variab1e = "Alpha"
# e) import = 40
# f) 81mi_variable = "Agua"
# g) mi_variable10 = 6
#
# Escribe aqui debajo un comentario explicando cuales fallan y por que:

# TU RESPUESTA AQUI (como comentario):
# a) ...
# b) ...
# c) ...
# d) ...
# e) ...
# f) ...
# g) ...


# ---------------------------------------------------------------------------
# EJERCICIO 3: Tipos de datos (int, float, type, del)
# ---------------------------------------------------------------------------
# 1. Crea una variable "entero" de tipo int (ejemplo: 10)
# 2. Crea una variable "decimal" de tipo float (ejemplo: 3.14)
# 3. Imprime el tipo de cada una usando type()
# 4. Crea una variable "suma" que sea la suma de ambas
# 5. Imprime el tipo de "suma". Que tipo es? Escribe un comentario
# 6. Elimina las variables "entero" y "decimal" con del

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 4: Strings y sus metodos
# ---------------------------------------------------------------------------
# Usa la frase: "A quien madruga, dios le ayuda"
#
# 1. Guardala en una variable llamada "frase"
# 2. Imprime la frase toda en MAYUSCULAS
# 3. Imprime la frase toda en minusculas
# 4. Imprime la frase con la primera letra de cada palabra en mayuscula
# 5. Crea una lista dividiendo la frase por espacios (split)
# 6. Sustituye las comas "," por puntos y comas ";"
# 7. Elimina todas las letras "a" minusculas de la frase

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 5: Mas strings - longitud y comillas internas
# ---------------------------------------------------------------------------
# 1. Crea un string que contenga comillas internas. Ejemplo:
#    Ella dijo "hola" y se fue
#    (Pista: usa comillas simples por fuera o escapa con \")
# 2. Imprime ese string
# 3. Imprime cuantos caracteres tiene con un mensaje:
#    "Esta cadena tiene X caracteres"

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 6: Variable con informacion personal
# ---------------------------------------------------------------------------
# Trabaja con la variable: info = "Marina de Empresas 2025"
#
# 1. Imprime la longitud de la variable
# 2. Imprime solo la primera letra
# 3. Imprime las ultimas 4 letras (pista: usa slicing con [-4:])
# 4. Imprime la variable al reves (pista: usa [::-1])
# 5. Cuenta cuantas veces aparece la letra "a" (usa .count())

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 7: Conversion de tipos (inspirado en Harvard CS50P)
# ---------------------------------------------------------------------------
# Python permite convertir entre tipos con funciones: int(), float(), str(),
# bool(). Pero no siempre funciona...
#
# 1. Convierte el string "42" a int y guardalo en variable "num_entero"
# 2. Convierte el string "3.14" a float y guardalo en "num_decimal"
# 3. Convierte el numero 100 a string y guardalo en "texto_num"
# 4. Convierte el numero 0 a bool y guardalo en "bool_cero"
# 5. Convierte el string "hello" a bool y guardalo en "bool_texto"
# 6. Imprime cada variable y su tipo con type()
# 7. PREGUNTA: Que pasa si intentas int("hello")? Y float("abc")?
#    Escribe tu prediccion como comentario y luego prueba
#    (puedes envolverlo en try/except o simplemente comentar la linea)

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 8: Batalla de Formateo de Strings (estilo MIT 6.0001)
# ---------------------------------------------------------------------------
# En Python hay 4 formas de formatear strings. Practica las 4:
#
# Dados: nombre = "Francisco", edad = 25, nota = 9.567
#
# 1. CONCATENACION: Imprime "Me llamo Francisco y tengo 25 anios"
#    usando + (recuerda: necesitas str() para convertir numeros)
# 2. OPERADOR %: Imprime lo mismo usando % (estilo C)
#    Ejemplo: "Hola %s, tienes %d anios" % (nombre, edad)
# 3. METODO .format(): Imprime lo mismo usando .format()
#    Ejemplo: "Hola {}, tienes {} anios".format(nombre, edad)
# 4. F-STRING: Imprime lo mismo usando f"..."
# 5. BONUS: Usando f-string, imprime la nota con solo 1 decimal
#    Pista: f"{nota:.1f}" formatea a 1 decimal

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 9: Voz Baja (inspirado en Harvard CS50P - Pset 0)
# ---------------------------------------------------------------------------
# 1. Dada la variable: grito = "HOLA, COMO ESTAS? TODO BIEN POR AQUI!"
#    Convierte el texto a "voz baja" (todo minusculas) e imprimelo
#
# 2. Dada la variable: mezcla = "HoLa MuNdO, EsTo Es PyThOn"
#    Convierte a minusculas e imprimelo
#
# 3. Dada la variable: texto_analizar = "Programacion en Python 2025"
#    Cuenta cuantas vocales (a, e, i, o, u) tiene (sin importar mayusculas)
#    Cuenta cuantas consonantes tiene (letras que no son vocales ni numeros
#    ni espacios ni signos)
#    Cuenta cuantos caracteres "otros" hay (numeros, espacios, signos)
#    Imprime los 3 contadores
#
# 4. Dada la variable: oculto = "Hola,\tmundo!\n"
#    Imprime la variable normalmente con print()
#    Imprime con repr() para ver los caracteres ocultos (\t, \n, etc.)
#    Pista: print(repr(oculto))

# TU CODIGO AQUI:




print("\n--- Fin de la Guia 1 ---")
print("Si has completado todos los ejercicios, revisa soluciones.py")
print("para comparar tus respuestas!")
