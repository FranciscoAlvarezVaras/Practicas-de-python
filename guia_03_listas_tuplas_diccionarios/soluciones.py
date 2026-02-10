# ============================================================================
# GUIA 3 - SOLUCIONES: LISTAS, TUPLAS Y DICCIONARIOS
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 1 (Ej. 6, 7)
# Enriquecido con: MIT 6.0001 (OCW), Harvard CS50P (estructuras de datos)
# ============================================================================


# ---------------------------------------------------------------------------
# EJERCICIO 1: Creando una lista con diferentes tipos
# ---------------------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1: Lista con diferentes tipos")
print("=" * 50)

puntuacion = 85
nombre_equipo = "Valencia Basketball"
promedio_tiempo = 4.5
es_habil = True
lista_compras = ["arroz", "pollo", "pasta", "tomate", "pan"]
tupla_mascotas = (("Luna", 3, "gato"), ("Rocky", 5, "perro"))
dict_contactos = {
    "amigos": ["Juan Pablo Perez", "Maria Garcia Lopez"],
    "telefonos": ["612345678", "698765432"],
    "emails": ["juanp@email.com", "maria@email.com"]
}

# Creamos la lista vacia y usamos .append() para agregar cada elemento
lista_actividades = []
lista_actividades.append(puntuacion)
lista_actividades.append(nombre_equipo)
lista_actividades.append(promedio_tiempo)
lista_actividades.append(es_habil)
lista_actividades.append(lista_compras)
lista_actividades.append(tupla_mascotas)
lista_actividades.append(dict_contactos)

print(f"Lista tiene {len(lista_actividades)} elementos")
for i, item in enumerate(lista_actividades):
    print(f"  [{i}] tipo={type(item).__name__}: {item}")

# Para evitar duplicados, puedes comprobar antes de agregar:
# if elemento not in lista_actividades:
#     lista_actividades.append(elemento)

# TIPOS DE DATOS EN PYTHON:
# int    -> numeros enteros: 1, 42, -5
# float  -> numeros decimales: 3.14, -0.5
# str    -> texto: "hola", 'mundo'
# bool   -> True o False
# list   -> coleccion ordenada y modificable: [1, 2, 3]
# tuple  -> coleccion ordenada e INMUTABLE: (1, 2, 3)
# dict   -> pares clave:valor: {"nombre": "Ana", "edad": 25}


# ---------------------------------------------------------------------------
# EJERCICIO 2: Trabajando con diccionarios
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2: Diccionarios")
print("=" * 50)

agenda = {
    "Ana": "654123987",
    "Luis": "678555111",
    "Marta": "622444333"
}

# .keys() -> devuelve todas las claves
print(f"Claves: {list(agenda.keys())}")
# Resultado: ['Ana', 'Luis', 'Marta']

# .values() -> devuelve todos los valores
print(f"Valores: {list(agenda.values())}")
# Resultado: ['654123987', '678555111', '622444333']

# .get() -> obtiene el valor de una clave (seguro, no da error)
print(f"Luis: {agenda.get('Luis')}")
# Resultado: 678555111

print(f"Pedro: {agenda.get('Pedro')}")
# Resultado: None (no existe, pero NO da error)
# Comparar con agenda["Pedro"] que daria KeyError!

# .get() con valor por defecto:
print(f"Pedro: {agenda.get('Pedro', 'No encontrado')}")
# Resultado: "No encontrado"

# Agregar nuevo contacto (simplemente asignar)
agenda["Pedro"] = "699888777"

# .items() -> devuelve pares (clave, valor)
print("\nTodos los contactos:")
for nombre, telefono in agenda.items():
    print(f"  {nombre}: {telefono}")

# .pop() -> elimina y DEVUELVE el valor (util para guardarlo)
marta_tel = agenda.pop("Marta")
print(f"\nEliminada Marta. Su telefono era: {marta_tel}")
print(f"Agenda actual: {agenda}")

# .clear() -> vacia el diccionario
agenda.clear()
print(f"Agenda vacia: {agenda}")
print(f"Esta vacia? {len(agenda) == 0}")

# METODOS DE DICCIONARIOS MAS UTILES:
# .keys()        -> todas las claves
# .values()      -> todos los valores
# .items()       -> pares (clave, valor)
# .get(clave)    -> valor sin error si no existe
# .pop(clave)    -> elimina y devuelve el valor
# .update(dict2) -> agrega/actualiza con otro diccionario
# .clear()       -> vacia el diccionario


# ---------------------------------------------------------------------------
# EJERCICIO 3: Metodos de listas
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 3: Metodos de listas")
print("=" * 50)

peliculas = ["Inception", "The Matrix", "Interstellar", "Gladiator"]
print(f"Original: {peliculas}")

# .append() -> agrega al FINAL
peliculas.append("El Padrino")
print(f"Tras append: {peliculas}")

# .insert(posicion, elemento) -> inserta en posicion especifica
peliculas.insert(2, "Memento")
print(f"Tras insert(2): {peliculas}")

# .remove(elemento) -> elimina la PRIMERA aparicion de ese valor
peliculas.remove("Gladiator")
print(f"Tras remove Gladiator: {peliculas}")

# .pop() -> elimina y devuelve el ultimo elemento
ultima = peliculas.pop()
print(f"pop() devolvio: {ultima}")
print(f"Tras pop: {peliculas}")

# Si, .pop(indice) funciona con cualquier posicion:
# peliculas.pop(0)  -> elimina y devuelve el primero
# peliculas.pop(2)  -> elimina y devuelve el de posicion 2

# .sort() -> ordena alfabeticamente (modifica la lista original)
peliculas.sort()
print(f"Ordenada: {peliculas}")

# .clear() -> vacia la lista
peliculas.clear()
print(f"Vacia: {peliculas}")

# METODOS DE LISTAS MAS UTILES:
# .append(x)     -> agrega al final
# .insert(i, x)  -> inserta en posicion i
# .remove(x)     -> elimina primera aparicion de x
# .pop()          -> elimina y devuelve el ultimo (o .pop(i) por indice)
# .sort()         -> ordena (modifica la lista)
# .reverse()      -> invierte el orden
# .count(x)       -> cuenta apariciones de x
# .index(x)       -> posicion de la primera aparicion de x
# .clear()        -> vacia la lista
# .copy()         -> crea una copia


# ---------------------------------------------------------------------------
# EJERCICIO 4: Indexing y Slicing
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 4: Indexing y Slicing")
print("=" * 50)

frutas = ["manzana", "pera", "naranja", "kiwi", "melon"]

# Indices:    0         1        2        3       4
# Negativos: -5        -4       -3       -2      -1

print(f"Primero: {frutas[0]}")       # manzana
print(f"Ultimo: {frutas[-1]}")       # melon
print(f"Del 2do al 4to: {frutas[1:4]}")  # ['pera', 'naranja', 'kiwi']
# OJO: el indice final NO se incluye! [1:4] = posiciones 1, 2, 3

print(f"Al reves: {frutas[::-1]}")   # ['melon', 'kiwi', ...]
print(f"Total elementos: {len(frutas)}")  # 5
print(f"kiwi esta? {'kiwi' in frutas}")    # True

# SLICING: lista[inicio:fin:paso]
# frutas[:]     -> toda la lista (copia)
# frutas[2:]    -> desde posicion 2 al final
# frutas[:3]    -> desde el inicio hasta posicion 2
# frutas[::2]   -> cada 2 elementos
# frutas[::-1]  -> toda la lista al reves


# ---------------------------------------------------------------------------
# EJERCICIO 5: Tuplas
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 5: Tuplas")
print("=" * 50)

coordenadas = (40.41, -3.70)

# Las tuplas son INMUTABLES - no se pueden cambiar!
# coordenadas[0] = 41.0  -> TypeError: 'tuple' object does not support item assignment
# Esta es la diferencia principal con las listas

print(f"Segundo valor: {coordenadas[1]}")  # -3.70

colores = ("rojo", "verde", "azul")

# Desempaquetado: asignar cada valor de la tupla a una variable
c1, c2, c3 = colores
print(f"c1={c1}, c2={c2}, c3={c3}")

# DIFERENCIA LISTA vs TUPLA:
# Lista []  -> Mutable (se puede modificar)   -> para datos que cambian
# Tupla ()  -> Inmutable (NO se puede cambiar) -> para datos fijos
# Ejemplo: coordenadas, dias de la semana, meses del ano


# ---------------------------------------------------------------------------
# EJERCICIO 6: Lista de diccionarios
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 6: Lista de diccionarios")
print("=" * 50)

alumnos = [
    {"nombre": "Ana", "edad": 22, "notas": [8.5, 9.0, 7.5]},
    {"nombre": "Carlos", "edad": 24, "notas": [6.0, 7.5, 8.0]},
    {"nombre": "Maria", "edad": 21, "notas": [9.5, 9.0, 10.0]},
]

# Nombre del segundo alumno
print(f"Segundo alumno: {alumnos[1]['nombre']}")  # Carlos
# alumnos[1] accede al segundo diccionario
# ['nombre'] accede a la clave "nombre" de ese diccionario

# Primera nota del tercer alumno
print(f"Primera nota del 3ro: {alumnos[2]['notas'][0]}")  # 9.5
# alumnos[2] -> tercer diccionario (Maria)
# ['notas'] -> la lista de notas
# [0] -> primer elemento de esa lista

# Agregar nuevo alumno
alumnos.append({"nombre": "Luis", "edad": 23, "notas": [7.0, 8.5, 6.5]})

# Cambiar edad del primer alumno
alumnos[0]["edad"] = 23

# Imprimir todo
print("\nLista final de alumnos:")
for alumno in alumnos:
    promedio = sum(alumno["notas"]) / len(alumno["notas"]) if alumno["notas"] else 0
    print(f"  {alumno['nombre']}, {alumno['edad']} anios, "
          f"notas: {alumno['notas']}, promedio: {promedio:.1f}")

# Esta estructura (lista de diccionarios) es MUY comun en programacion
# Es parecida a una tabla/base de datos:
# - Cada diccionario es una "fila"
# - Cada clave es una "columna"


# ---------------------------------------------------------------------------
# EJERCICIO 7: Inventario de tienda (MIT - estructuras de datos reales)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 7: Inventario de tienda")
print("=" * 50)

# Creamos la lista de productos (lista de diccionarios)
productos = [
    {"nombre": "Laptop",       "precio": 999.99, "stock": 15, "categoria": "Electronica"},
    {"nombre": "Telefono",     "precio": 699.50, "stock": 30, "categoria": "Electronica"},
    {"nombre": "Aspiradora",   "precio": 149.99, "stock": 20, "categoria": "Hogar"},
    {"nombre": "Cafe molido",  "precio": 8.50,   "stock": 100, "categoria": "Alimentacion"},
    {"nombre": "Lampara LED",  "precio": 29.99,  "stock": 45, "categoria": "Hogar"},
]

# 1. Encontrar el producto mas caro
producto_caro = productos[0]  # Empezamos asumiendo que el primero es el mas caro
for producto in productos:
    if producto["precio"] > producto_caro["precio"]:
        producto_caro = producto

print(f"Producto mas caro: {producto_caro['nombre']} "
      f"({producto_caro['precio']} EUR)")
# Resultado: Laptop (999.99 EUR)

# EXPLICACION: Recorremos todos los productos. Si encontramos uno con
# precio mayor que nuestro "candidato" actual, lo reemplazamos.
# Al terminar el bucle, tenemos el mas caro.

# 2. Valor total del inventario
valor_total = 0
for producto in productos:
    valor_producto = producto["precio"] * producto["stock"]
    valor_total += valor_producto

print(f"\nValor total del inventario: {valor_total:.2f} EUR")
# Cada producto contribuye: precio * unidades en stock
# Es la suma de todo lo que vale la tienda si vendiera todo

# 3. Agrupar por categoria (diccionario de listas)
por_categoria = {}
for producto in productos:
    cat = producto["categoria"]
    if cat not in por_categoria:
        # Si la categoria no existe aun, creamos una lista vacia
        por_categoria[cat] = []
    por_categoria[cat].append(producto["nombre"])

print("\nProductos por categoria:")
for categoria, nombres in por_categoria.items():
    print(f"  {categoria}: {nombres}")
# Resultado:
#   Electronica: ['Laptop', 'Telefono']
#   Hogar: ['Aspiradora', 'Lampara LED']
#   Alimentacion: ['Cafe molido']

# EXPLICACION del agrupamiento:
# - Creamos un diccionario vacio por_categoria
# - Para cada producto, obtenemos su categoria
# - Si esa categoria no existe como clave, la creamos con lista vacia
# - Luego agregamos el nombre del producto a la lista de esa categoria
# Este patron (agrupar por clave) es MUY comun en programacion real


# ---------------------------------------------------------------------------
# EJERCICIO 8: Matriz como lista de listas (estilo MIT 6.0001)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 8: Matriz como lista de listas")
print("=" * 50)

# 1. Crear la matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for fila in matriz:
    print(f"  {fila}")

# 2. Acceder a fila 1, columna 2
# fila 1 = segunda fila (indice 1), columna 2 = tercera columna (indice 2)
elemento = matriz[1][2]
print(f"\nElemento en fila 1, columna 2: {elemento}")
# Resultado: 6
# matriz[1] devuelve [4, 5, 6], y luego [2] devuelve el 6

# 3. Suma de cada fila
print("\nSuma de cada fila:")
for i, fila in enumerate(matriz):
    print(f"  Fila {i}: {fila} = {sum(fila)}")
# sum() recibe una lista y devuelve la suma de todos sus elementos
# enumerate() nos da el indice (i) y el valor (fila) a la vez

# 4. Suma de la diagonal principal
# Diagonal = elementos donde fila == columna: [0][0], [1][1], [2][2]
suma_diagonal = 0
for i in range(len(matriz)):
    suma_diagonal += matriz[i][i]
print(f"\nSuma de la diagonal: {suma_diagonal}")
# 1 + 5 + 9 = 15

# 5. Transponer la matriz
# La transpuesta intercambia filas por columnas
# Elemento [i][j] de la original -> [j][i] de la transpuesta
filas = len(matriz)
columnas = len(matriz[0])

# Creamos una nueva matriz con las dimensiones intercambiadas
transpuesta = []
for j in range(columnas):
    nueva_fila = []
    for i in range(filas):
        nueva_fila.append(matriz[i][j])
    transpuesta.append(nueva_fila)

print("\nMatriz transpuesta:")
for fila in transpuesta:
    print(f"  {fila}")
# Original:      Transpuesta:
# [1, 2, 3]      [1, 4, 7]
# [4, 5, 6]  ->  [2, 5, 8]
# [7, 8, 9]      [3, 6, 9]

# EXPLICACION de la transposicion:
# - Recorremos las COLUMNAS de la original (j = 0, 1, 2)
# - Para cada columna, recorremos las FILAS (i = 0, 1, 2)
# - Tomamos matriz[i][j] y lo ponemos en la nueva fila
# - Asi la columna 0 de la original (1, 4, 7) se convierte en fila 0

# NOTA AVANZADA: En Python se puede hacer con list comprehension:
# transpuesta = [[matriz[i][j] for i in range(filas)] for j in range(columnas)]
# Esto es mas compacto pero hace exactamente lo mismo


print("\n--- Fin de las Soluciones Guia 3 ---")
