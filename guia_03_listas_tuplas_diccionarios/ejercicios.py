# ============================================================================
# GUIA 3: LISTAS, TUPLAS Y DICCIONARIOS
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 1 (Ej. 6, 7)
# Enriquecido con: MIT 6.0001 (OCW), Harvard CS50P (estructuras de datos)
#
# INSTRUCCIONES:
# - Lee cada ejercicio y escribe tu codigo en "# TU CODIGO AQUI"
# - Ejecuta: python ejercicios.py
# ============================================================================


# ---------------------------------------------------------------------------
# EJERCICIO 1: Creando una lista con diferentes tipos
# ---------------------------------------------------------------------------
# Crea las siguientes variables y luego metelas TODAS en una lista:
#
# 1. "puntuacion" -> un int (ej: 85)
# 2. "nombre_equipo" -> un string con tu equipo favorito + espacio + deporte
# 3. "promedio_tiempo" -> un float con horas que estudias al dia
# 4. "es_habil" -> un bool (True si diestro, False si zurdo)
# 5. "lista_compras" -> una lista con 5 alimentos que mas comes
# 6. "tupla_mascotas" -> una tupla con 2 tuplas dentro
#    Cada tupla interna: (nombre, edad, especie) de una mascota
# 7. "dict_contactos" -> un diccionario con 3 claves:
#    "amigos" -> lista con 2 nombres completos
#    "telefonos" -> lista con 2 numeros
#    "emails" -> lista con 2 emails
#
# 8. Crea "lista_actividades" vacia y usa .append() para meter cada variable
# 9. Responde como comentario: como evitar duplicados al agregar?

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 2: Trabajando con diccionarios
# ---------------------------------------------------------------------------
# 1. Crea un diccionario "agenda" con:
#    "Ana" -> "654123987"
#    "Luis" -> "678555111"
#    "Marta" -> "622444333"
#
# 2. Imprime todas las claves (nombres)
# 3. Imprime todos los valores (telefonos)
# 4. Usa .get() para obtener el numero de "Luis"
# 5. Usa .get() para buscar "Pedro" (que no existe) - que pasa?
# 6. Agrega "Pedro" con su numero: "699888777"
# 7. Imprime todos los pares nombre-telefono con .items()
# 8. Elimina a "Marta" con .pop() y guarda su numero en una variable
# 9. Imprime la agenda final
# 10. Limpia toda la agenda con .clear() y confirma que esta vacia

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 3: Metodos de listas
# ---------------------------------------------------------------------------
# 1. Crea una lista "peliculas" con 4 titulos de tus pelis favoritas
# 2. Imprime todas las peliculas
# 3. Agrega "El Padrino" al final con .append()
# 4. Inserta "Memento" en la posicion 2 con .insert()
# 5. Elimina una pelicula con .remove()
# 6. Elimina y muestra la ultima pelicula con .pop()
#    Pregunta: se puede usar .pop() con cualquier posicion?
#    (escribe la respuesta como comentario)
# 7. Ordena la lista alfabeticamente con .sort()
# 8. Vacia la lista con .clear()

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 4: Accediendo a elementos (indexing y slicing)
# ---------------------------------------------------------------------------
# Dada la lista: frutas = ["manzana", "pera", "naranja", "kiwi", "melon"]
#
# 1. Imprime el primer elemento (indice 0)
# 2. Imprime el ultimo elemento (indice -1)
# 3. Imprime los elementos del 2do al 4to (slicing)
# 4. Imprime la lista al reves
# 5. Imprime cuantos elementos tiene la lista (len)
# 6. Comprueba si "kiwi" esta en la lista (in)

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 5: Tuplas
# ---------------------------------------------------------------------------
# 1. Crea una tupla "coordenadas" con valores (40.41, -3.70)
# 2. Intenta cambiar el primer valor. Que pasa? (escribe como comentario)
# 3. Accede al segundo valor e imprimelo
# 4. Crea una tupla "colores" con ("rojo", "verde", "azul")
# 5. Desempaqueta la tupla en 3 variables: c1, c2, c3
# 6. Imprime las 3 variables

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 6: Lista de diccionarios (combinando todo)
# ---------------------------------------------------------------------------
# Crea una lista de 3 diccionarios. Cada diccionario es un alumno con:
# - "nombre" (string)
# - "edad" (int)
# - "notas" (lista de 3 numeros)
#
# Luego:
# 1. Imprime el nombre del segundo alumno
# 2. Imprime la primera nota del tercer alumno
# 3. Agrega un nuevo alumno a la lista
# 4. Cambia la edad del primer alumno
# 5. Imprime toda la lista final

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 7: Inventario de tienda (MIT - estructuras de datos reales)
# ---------------------------------------------------------------------------
# Crea una lista de 5 productos. Cada producto es un diccionario con:
#   - "nombre": string (ej: "Laptop")
#   - "precio": float (ej: 999.99)
#   - "stock": int (ej: 15)
#   - "categoria": string (ej: "Electronica")
#
# Usa estas categorias: "Electronica", "Hogar", "Alimentacion"
# (al menos 2 productos deben compartir categoria)
#
# Luego escribe codigo para:
# 1. Encontrar el producto mas caro e imprimir su nombre y precio
#    (Pista: puedes recorrer la lista y comparar precios)
# 2. Calcular el valor total del inventario:
#    suma de (precio * stock) de cada producto
# 3. Agrupar productos por categoria en un NUEVO diccionario donde:
#    - La clave es la categoria (string)
#    - El valor es una lista de nombres de productos de esa categoria
#    Ejemplo resultado: {"Electronica": ["Laptop", "Telefono"], "Hogar": [...]}

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 8: Matriz como lista de listas (estilo MIT 6.0001)
# ---------------------------------------------------------------------------
# Las matrices se pueden representar como listas de listas en Python.
# Cada lista interna es una fila.
#
# 1. Crea la siguiente matriz 3x3:
#    matriz = [[1, 2, 3],
#              [4, 5, 6],
#              [7, 8, 9]]
#
# 2. Accede e imprime el elemento en fila 1, columna 2
#    (Recuerda: los indices empiezan en 0, asi que fila 1 = segunda fila)
#    Pista: matriz[fila][columna]
#
# 3. Calcula e imprime la suma de cada fila:
#    Fila 0: 1+2+3 = 6
#    Fila 1: 4+5+6 = 15
#    Fila 2: 7+8+9 = 24
#    (Pista: puedes usar sum() con cada sublista)
#
# 4. Calcula e imprime la suma de la diagonal principal:
#    Diagonal: matriz[0][0] + matriz[1][1] + matriz[2][2] = 1+5+9 = 15
#
# 5. Transponer la matriz (filas se convierten en columnas):
#    Original:     Transpuesta:
#    1 2 3         1 4 7
#    4 5 6   ->    2 5 8
#    7 8 9         3 6 9
#    Crea una nueva lista de listas con la matriz transpuesta
#    (Pista: el elemento [i][j] de la original va a [j][i] en la transpuesta)

# TU CODIGO AQUI:




print("\n--- Fin de la Guia 3 ---")
print("Compara tus respuestas con soluciones.py!")
