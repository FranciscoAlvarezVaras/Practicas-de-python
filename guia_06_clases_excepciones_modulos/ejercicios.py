# ============================================================================
# GUIA 6: CLASES, EXCEPCIONES Y MODULOS
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 4
# Enriquecido con: MIT 6.0001 (OOP), Harvard CS50P (decoradores)
#
# INSTRUCCIONES:
# - Lee cada ejercicio y escribe tu codigo en "# TU CODIGO AQUI"
# - Ejecuta: python ejercicios.py
# ============================================================================


# ---------------------------------------------------------------------------
# EJERCICIO 1: Tu primera clase - CuentaBancaria
# ---------------------------------------------------------------------------
# Crea una clase "CuentaBancaria" con:
#
# Atributos (en __init__):
# - titular (string)
# - saldo (float)
#
# Metodos:
# - depositar(cantidad): suma la cantidad al saldo
#   Si la cantidad es <= 0, imprime "Cantidad no valida"
# - mostrar(): devuelve un string: "Titular: X | Saldo: Y euros"
#
# Luego:
# 1. Crea una cuenta para ti con saldo 100
# 2. Deposita 50
# 3. Intenta depositar -20 (debe dar error)
# 4. Muestra el estado de la cuenta

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 2: Clase con mas metodos - Alumno
# ---------------------------------------------------------------------------
# Crea una clase "Alumno" con:
#
# Atributos:
# - nombre (string)
# - notas (lista vacia al principio)
#
# Metodos:
# - agregar_nota(nota): agrega una nota a la lista
#   Solo acepta notas entre 0 y 10
# - promedio(): devuelve el promedio de las notas
#   Si no hay notas, devuelve 0
# - mejor_nota(): devuelve la nota mas alta
# - mostrar(): imprime nombre, notas y promedio
#
# Luego:
# 1. Crea un alumno
# 2. Agrega 5 notas
# 3. Muestra su informacion

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 3: Try/Except - Division segura
# ---------------------------------------------------------------------------
# Crea un programa que:
# 1. Pida dos numeros al usuario (usa las variables directamente si no
#    quieres usar input)
# 2. Intente dividir el primero entre el segundo
# 3. Si hay division por cero, imprime "No se puede dividir por cero"
# 4. Si todo va bien, imprime el resultado
#
# Pista: ZeroDivisionError es el error que lanza Python

# TU CODIGO AQUI (version sin input para poder ejecutar el archivo):
# numerador = 10
# denominador = 0




# ---------------------------------------------------------------------------
# EJERCICIO 4: Try/Except multiples errores
# ---------------------------------------------------------------------------
# Crea una funcion "division_segura" que reciba dos valores (pueden ser
# strings o numeros) y:
# 1. Intente convertirlos a float
# 2. Intente dividirlos
# 3. Capture ValueError si no se pueden convertir
# 4. Capture ZeroDivisionError si se divide por cero
# 5. Devuelva el resultado o None si hay error

# TU CODIGO AQUI:




# Pruebas:
# print(division_segura(10, 3))       # 3.333...
# print(division_segura(10, 0))       # Error division por cero
# print(division_segura("abc", 3))    # Error conversion


# ---------------------------------------------------------------------------
# EJERCICIO 5: Lectura de archivos
# ---------------------------------------------------------------------------
# Crea un archivo de texto llamado "mi_lista.txt" con algunas palabras
# (una por linea). Luego:
# 1. Abre el archivo con open() y "with"
# 2. Lee cada linea
# 3. Guarda las palabras en una lista (usa .strip() para quitar saltos)
# 4. Imprime la lista
#
# Pista:
# with open("archivo.txt", encoding="utf-8") as f:
#     for linea in f:
#         palabra = linea.strip()

# TU CODIGO AQUI (primero crea el archivo mi_lista.txt):




# ---------------------------------------------------------------------------
# EJERCICIO 6: Modulo requests - API publica
# ---------------------------------------------------------------------------
# Haz una peticion GET a: https://api.agify.io?name=sofia
# Esta API predice la edad segun el nombre.
#
# 1. Importa requests (pip install requests si no lo tienes)
# 2. Haz requests.get(url)
# 3. Convierte la respuesta a JSON con .json()
# 4. Imprime: nombre, edad estimada, numero de registros
# 5. Si hay error de conexion, imprime un mensaje
#
# NOTA: Necesitas conexion a internet para este ejercicio
# Si no tienes requests instalado, comenta este ejercicio

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 7: Clase Producto (juntando todo)
# ---------------------------------------------------------------------------
# Crea una clase "Producto" con:
#
# Atributos:
# - nombre (string)
# - precio (float)
# - stock (int)
#
# Metodos:
# - vender(cantidad): reduce el stock
#   Si no hay suficiente stock, lanza ValueError
# - reponer(cantidad): aumenta el stock
# - aplicar_descuento(porcentaje): reduce el precio
#   Ejemplo: 20% de descuento sobre precio 100 = precio final 80
# - info(): devuelve string con toda la info
#
# Usa try/except al vender para manejar stock insuficiente

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 8: Herencia - Sistema de vehiculos (MIT 6.0001 OOP)
# ---------------------------------------------------------------------------
# La HERENCIA permite crear clases que heredan atributos y metodos de otra.
# Es uno de los pilares de la Programacion Orientada a Objetos.
#
# Crea una clase base "Vehiculo" con:
#   Atributos (en __init__):
#   - marca (string)
#   - modelo (string)
#   - anio (int)
#   - velocidad (float, por defecto 0)
#
#   Metodos:
#   - acelerar(km): suma km a la velocidad
#   - frenar(km): resta km a la velocidad (no puede ser menor que 0)
#   - info(): devuelve string con marca, modelo, anio y velocidad
#
# Crea una subclase "Coche" que herede de Vehiculo:
#   - Atributo extra: num_puertas (int)
#   - Sobreescribe info() para incluir num_puertas
#   - Usa super().__init__() para llamar al constructor del padre
#
# Crea una subclase "Moto" que herede de Vehiculo:
#   - Atributo extra: tipo (string: "deportiva" o "urbana")
#   - Sobreescribe info() para incluir el tipo
#   - Usa super().__init__() para llamar al constructor del padre
#
# Luego:
# 1. Crea un Coche("Toyota", "Corolla", 2023, num_puertas=4)
# 2. Crea una Moto("Yamaha", "MT-07", 2024, tipo="deportiva")
# 3. Acelera el coche a 120 km/h
# 4. Acelera la moto a 80 km/h
# 5. Frena el coche 30 km/h
# 6. Muestra info() de ambos
#
# PISTA: La herencia se define asi:
# class Hijo(Padre):
#     def __init__(self, param1, param2, nuevo_param):
#         super().__init__(param1, param2)  # llama al __init__ del padre
#         self.nuevo_atributo = nuevo_param

# TU CODIGO AQUI:




# ---------------------------------------------------------------------------
# EJERCICIO 9: Decoradores basicos (Harvard CS50P avanzado)
# ---------------------------------------------------------------------------
# Un DECORADOR es una funcion que envuelve a otra funcion para
# anadirle funcionalidad sin modificar su codigo original.
#
# Crea una funcion "medir_tiempo" que actue como decorador:
# 1. Recibe una funcion como parametro
# 2. Define una funcion interna "wrapper" (envoltorio) que:
#    a. Guarda el tiempo actual con time.time()
#    b. Ejecuta la funcion original
#    c. Guarda el tiempo de nuevo
#    d. Calcula la diferencia (tiempo que tardo)
#    e. Imprime: "Funcion X tardo Y segundos"
#    f. Devuelve el resultado de la funcion original
# 3. Devuelve la funcion wrapper (envoltorio)
#
# Luego:
# 1. Aplica @medir_tiempo a una funcion "suma_grande" que sume los
#    numeros del 0 al 999999 con un bucle for
# 2. Llama a suma_grande() y observa el tiempo
#
# PISTA: Estructura de un decorador:
# import time
#
# def medir_tiempo(funcion):
#     def wrapper(*args, **kwargs):
#         # medir inicio con time.time()
#         resultado = funcion(*args, **kwargs)
#         # medir fin con time.time()
#         # imprimir diferencia
#         return resultado
#     return wrapper
#
# @medir_tiempo
# def mi_funcion():
#     ...

# TU CODIGO AQUI:




print("\n--- Fin de la Guia 6 ---")
print("Compara tus respuestas con soluciones.py!")
