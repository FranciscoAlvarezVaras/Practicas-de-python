# ============================================================================
# GUIA 6 - SOLUCIONES: CLASES, EXCEPCIONES Y MODULOS
# ============================================================================
# Autor: Francisco Alvarez Varas
# Basado en: Ejercicios EDEM MDA 2025/2026 - Clase 4
# Enriquecido con: MIT 6.0001 (OOP), Harvard CS50P (decoradores)
# ============================================================================


# ---------------------------------------------------------------------------
# EJERCICIO 1: CuentaBancaria
# ---------------------------------------------------------------------------
print("=" * 50)
print("EJERCICIO 1: CuentaBancaria")
print("=" * 50)


class CuentaBancaria:
    # __init__ es el CONSTRUCTOR: se ejecuta al crear un objeto
    def __init__(self, titular, saldo):
        self.titular = titular    # self.X = atributo del objeto
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad <= 0:
            print("Cantidad no valida")
        else:
            self.saldo += cantidad
            print(f"Depositados {cantidad} euros")

    def mostrar(self):
        return f"Titular: {self.titular} | Saldo: {self.saldo:.2f} euros"


# Crear un objeto (instancia) de la clase
mi_cuenta = CuentaBancaria("Francisco", 100.0)
print(mi_cuenta.mostrar())  # Titular: Francisco | Saldo: 100.00 euros

mi_cuenta.depositar(50)
print(mi_cuenta.mostrar())  # Saldo: 150.00 euros

mi_cuenta.depositar(-20)    # Cantidad no valida
print(mi_cuenta.mostrar())  # Saldo sigue en 150.00 euros

# ANATOMIA DE UNA CLASE:
# class NombreClase:
#     def __init__(self, parametros):
#         self.atributo = valor
#
#     def metodo(self):
#         # codigo que usa self.atributo
#
# CREAR OBJETO: variable = NombreClase(argumentos)
# USAR METODO:  variable.metodo()
# LEER ATRIBUTO: variable.atributo
#
# "self" es una referencia al propio objeto
# Siempre es el primer parametro de cada metodo
# Pero NO lo pasas al llamar: mi_cuenta.depositar(50) (no mi_cuenta.depositar(mi_cuenta, 50))


# ---------------------------------------------------------------------------
# EJERCICIO 2: Alumno
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 2: Alumno")
print("=" * 50)


class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []  # lista vacia al principio

    def agregar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print(f"Nota {nota} no valida (debe ser 0-10)")

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def mejor_nota(self):
        if len(self.notas) == 0:
            return 0
        return max(self.notas)

    def mostrar(self):
        print(f"Alumno: {self.nombre}")
        print(f"Notas: {self.notas}")
        print(f"Promedio: {self.promedio():.1f}")
        print(f"Mejor nota: {self.mejor_nota()}")


alumno1 = Alumno("Francisco")
alumno1.agregar_nota(8.5)
alumno1.agregar_nota(9.0)
alumno1.agregar_nota(7.5)
alumno1.agregar_nota(6.0)
alumno1.agregar_nota(10.0)
alumno1.agregar_nota(15)  # No valida
alumno1.mostrar()

# Las clases permiten AGRUPAR datos y funciones relacionadas
# Un Alumno TIENE notas y PUEDE agregar notas, ver promedio, etc.
# Esto se llama Programacion Orientada a Objetos (POO/OOP)


# ---------------------------------------------------------------------------
# EJERCICIO 3: Division segura con try/except
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 3: Division segura")
print("=" * 50)

numerador = 10
denominador = 0

try:
    resultado = numerador / denominador
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("No se puede dividir por cero")

# Ahora con un denominador valido
denominador = 3
try:
    resultado = numerador / denominador
    print(f"Resultado: {resultado:.2f}")
except ZeroDivisionError:
    print("No se puede dividir por cero")

# TRY/EXCEPT:
# try:
#     codigo que PUEDE fallar
# except TipoError:
#     que hacer si falla con ese error
# except OtroError:
#     que hacer si falla con otro error
# else:
#     codigo si NO hubo error (opcional)
# finally:
#     codigo que se ejecuta SIEMPRE (opcional)
#
# ERRORES COMUNES:
# ZeroDivisionError -> division por cero
# ValueError        -> valor incorrecto (ej: int("hola"))
# TypeError         -> tipo incorrecto (ej: "hola" + 5)
# KeyError          -> clave no existe en diccionario
# IndexError        -> indice fuera de rango en lista
# FileNotFoundError -> archivo no encontrado
# NameError         -> variable no definida


# ---------------------------------------------------------------------------
# EJERCICIO 4: Multiples excepciones
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 4: Multiples excepciones")
print("=" * 50)


def division_segura(a, b):
    try:
        num_a = float(a)
        num_b = float(b)
        resultado = num_a / num_b
        return resultado
    except ValueError:
        print(f"Error: no se puede convertir '{a}' o '{b}' a numero")
        return None
    except ZeroDivisionError:
        print("Error: division por cero")
        return None


print(division_segura(10, 3))       # 3.333...
print(division_segura(10, 0))       # Error division por cero
print(division_segura("abc", 3))    # Error conversion

# Puedes capturar VARIOS tipos de error con distintos except
# Python prueba cada except en orden y ejecuta el primero que coincida


# ---------------------------------------------------------------------------
# EJERCICIO 5: Lectura de archivos
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 5: Lectura de archivos")
print("=" * 50)

# Primero creamos un archivo de prueba
with open("mi_lista.txt", "w", encoding="utf-8") as f:
    f.write("manzana\n")
    f.write("pera\n")
    f.write("naranja\n")
    f.write("kiwi\n")
    f.write("melon\n")

# Ahora lo leemos
palabras = []
with open("mi_lista.txt", encoding="utf-8") as f:
    for linea in f:
        palabra = linea.strip()  # quita \n y espacios
        if palabra:              # ignora lineas vacias
            palabras.append(palabra)

print(f"Palabras leidas: {palabras}")

# WITH open() as f:
# - "with" se encarga de CERRAR el archivo automaticamente
# - No necesitas f.close()
# - "r" = leer (default), "w" = escribir, "a" = agregar al final
# - encoding="utf-8" para caracteres especiales (acentos, enie, etc.)
#
# .strip() quita espacios y saltos de linea (\n) de los extremos
# Es MUY comun usarlo al leer archivos linea a linea


# ---------------------------------------------------------------------------
# EJERCICIO 6: API con requests
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 6: API con requests")
print("=" * 50)

try:
    import requests

    url = "https://api.agify.io?name=sofia"

    try:
        respuesta = requests.get(url)
        datos = respuesta.json()  # convierte JSON a diccionario Python

        print(f"Nombre: {datos['name']}")
        print(f"Edad estimada: {datos['age']}")
        print(f"Registros usados: {datos['count']}")
    except Exception as e:
        print(f"No se pudo conectar con la API: {e}")

except ImportError:
    print("El modulo 'requests' no esta instalado.")
    print("Instalalo con: pip install requests")

# MODULOS: archivos con codigo reutilizable
# import modulo            -> importa todo el modulo
# from modulo import algo  -> importa solo "algo"
#
# Modulos de Python (ya vienen instalados):
# math     -> funciones matematicas
# random   -> numeros aleatorios
# os       -> interactuar con el sistema operativo
# json     -> leer/escribir JSON
# datetime -> fechas y horas
#
# Modulos externos (instalar con pip):
# requests -> hacer peticiones HTTP
# pandas   -> analisis de datos
# numpy    -> calculo numerico


# ---------------------------------------------------------------------------
# EJERCICIO 7: Clase Producto
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 7: Clase Producto")
print("=" * 50)


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        if cantidad > self.stock:
            raise ValueError(
                f"Stock insuficiente. Solo quedan {self.stock} unidades"
            )
        self.stock -= cantidad
        print(f"Vendidas {cantidad} unidades de {self.nombre}")

    def reponer(self, cantidad):
        self.stock += cantidad
        print(f"Repuestas {cantidad} unidades de {self.nombre}")

    def aplicar_descuento(self, porcentaje):
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"Descuento de {porcentaje}% aplicado. "
              f"Nuevo precio: {self.precio:.2f}")

    def info(self):
        return (f"Producto: {self.nombre} | "
                f"Precio: {self.precio:.2f} euros | "
                f"Stock: {self.stock}")


# Crear producto
laptop = Producto("Laptop", 999.99, 10)
print(laptop.info())

# Vender 3
laptop.vender(3)
print(laptop.info())

# Aplicar descuento del 20%
laptop.aplicar_descuento(20)
print(laptop.info())

# Intentar vender mas del stock
try:
    laptop.vender(100)
except ValueError as e:
    print(f"Error: {e}")

# Reponer stock
laptop.reponer(5)
print(laptop.info())

# raise ValueError("mensaje") -> LANZA un error a proposito
# Es util para que la funcion avise al codigo que la llama
# El codigo que llama debe usar try/except para capturarlo
#
# "as e" guarda el mensaje de error en la variable "e"
# print(e) -> muestra el mensaje que pusimos en raise


# ---------------------------------------------------------------------------
# EJERCICIO 8: Herencia - Sistema de vehiculos (MIT 6.0001 OOP)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 8: Herencia - Sistema de vehiculos")
print("=" * 50)


class Vehiculo:
    """Clase base para todos los vehiculos."""
    def __init__(self, marca, modelo, anio, velocidad=0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = velocidad

    def acelerar(self, km):
        self.velocidad += km
        print(f"{self.marca} {self.modelo} acelera a {self.velocidad} km/h")

    def frenar(self, km):
        self.velocidad -= km
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"{self.marca} {self.modelo} frena a {self.velocidad} km/h")

    def info(self):
        return (f"{self.marca} {self.modelo} ({self.anio}) "
                f"| Velocidad: {self.velocidad} km/h")


class Coche(Vehiculo):
    """Subclase de Vehiculo con numero de puertas."""
    def __init__(self, marca, modelo, anio, num_puertas=4, velocidad=0):
        # super().__init__() llama al __init__ de Vehiculo
        super().__init__(marca, modelo, anio, velocidad)
        self.num_puertas = num_puertas

    def info(self):
        # Sobreescribimos info() para incluir num_puertas
        base = super().info()
        return f"{base} | Puertas: {self.num_puertas}"


class Moto(Vehiculo):
    """Subclase de Vehiculo con tipo de moto."""
    def __init__(self, marca, modelo, anio, tipo="urbana", velocidad=0):
        super().__init__(marca, modelo, anio, velocidad)
        self.tipo = tipo

    def info(self):
        base = super().info()
        return f"{base} | Tipo: {self.tipo}"


# Crear objetos
mi_coche = Coche("Toyota", "Corolla", 2023, num_puertas=4)
mi_moto = Moto("Yamaha", "MT-07", 2024, tipo="deportiva")

# Usar metodos heredados
mi_coche.acelerar(120)
mi_moto.acelerar(80)
mi_coche.frenar(30)

# Mostrar info (cada uno usa su version sobreescrita)
print(mi_coche.info())
print(mi_moto.info())

# Demostrar que isinstance funciona con herencia
print(f"\nmi_coche es Vehiculo? {isinstance(mi_coche, Vehiculo)}")  # True
print(f"mi_coche es Coche? {isinstance(mi_coche, Coche)}")          # True
print(f"mi_coche es Moto? {isinstance(mi_coche, Moto)}")            # False

# HERENCIA:
# - La clase hija (Coche, Moto) HEREDA todo de la clase padre (Vehiculo)
# - Puede SOBREESCRIBIR metodos para cambiar su comportamiento
# - super() permite acceder a los metodos del padre
# - isinstance(obj, Clase) -> True si obj es de esa clase o de una hija
#
# Por que usar herencia?
# - Evita repetir codigo (DRY: No Te Repitas / Don't Repeat Yourself)
# - Coche y Moto comparten acelerar() y frenar() sin reescribirlos
# - Cada subclase solo define lo que es DIFERENTE


# ---------------------------------------------------------------------------
# EJERCICIO 9: Decoradores basicos (Harvard CS50P avanzado)
# ---------------------------------------------------------------------------
print("\n" + "=" * 50)
print("EJERCICIO 9: Decoradores basicos")
print("=" * 50)

import time
import functools


def medir_tiempo(funcion):
    """Decorador que mide cuanto tarda una funcion en ejecutarse."""
    @functools.wraps(funcion)  # preserva __name__, __doc__ de la funcion original
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        duracion = fin - inicio
        print(f"Funcion '{funcion.__name__}' tardo {duracion:.6f} segundos")
        return resultado
    return wrapper


@medir_tiempo
def suma_grande():
    """Suma los numeros del 0 al 999999 con un bucle for."""
    total = 0
    for i in range(1000000):
        total += i
    return total


@medir_tiempo
def suma_rapida():
    """Suma los numeros del 0 al 999999 con sum() y range()."""
    return sum(range(1000000))


# Llamar a las funciones decoradas
resultado1 = suma_grande()
print(f"Resultado suma_grande: {resultado1}")

resultado2 = suma_rapida()
print(f"Resultado suma_rapida: {resultado2}")

# DECORADORES:
# - Un decorador ENVUELVE una funcion para anadirle funcionalidad
# - @medir_tiempo encima de def es equivalente a:
#   suma_grande = medir_tiempo(suma_grande)
# - *args y **kwargs permiten que el wrapper (envoltorio) acepte CUALQUIER argumento
# - funcion.__name__ devuelve el nombre original de la funcion
#
# Usos comunes de decoradores:
# - Medir tiempo de ejecucion (como este ejemplo)
# - Logging (registrar llamadas a funciones)
# - Cache (guardar resultados para no recalcular)
# - Validacion de parametros
# - Autenticacion en aplicaciones web


# Limpiamos el archivo de prueba
import os
if os.path.exists("mi_lista.txt"):
    os.remove("mi_lista.txt")

print("\n--- Fin de las Soluciones Guia 6 ---")
