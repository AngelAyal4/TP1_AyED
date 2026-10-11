import pickle
import os


# (la carpeta debe existir antes de ejecutar el programa!!!)

CARPETA = "c:\\tp3\\"
RUTA_CATEGORIAS = CARPETA + "categorias.dat"

LARGO_NOMBRE = 30
LARGO_PREGUNTA = 200


# ---------------------------------------------------------------
# REGISTRO
# ---------------------------------------------------------------
class Categoria:
    def __init__(self):
        self.NroCategoria = 0                       # int (consecutivo desde 1)
        self.NombreCategoria = " "                  # str(30)
        self.Pregunta = " "                         # str(200)
        self.Estado = "A"                           # str: A = Activa / I = Inactiva


# ---------------------------------------------------------------
# FUNCIONES
# ---------------------------------------------------------------
def formatear(texto, largo):
    resultado = ""
    i = 0
    while i < largo:
        if i < len(texto):
            resultado = resultado + texto[i]
        else:
            resultado = resultado + " "
        i = i + 1
    return resultado


def archivo_vacio():
    vacio = True
    if os.path.exists(RUTA_CATEGORIAS):
        if os.path.getsize(RUTA_CATEGORIAS) > 0:
            vacio = False
    return vacio


def alta_categoria(nro, nombre, pregunta):
    reg = Categoria()
    reg.NroCategoria = nro
    reg.NombreCategoria = formatear(nombre, LARGO_NOMBRE)
    reg.Pregunta = formatear(pregunta, LARGO_PREGUNTA)
    reg.Estado = "A"
    archivo = open(RUTA_CATEGORIAS, "ab")
    pickle.dump(reg, archivo)
    archivo.close()


def cargar_categorias_iniciales():
    alta_categoria(1, "Edad Famosos", "¿Quién tiene más años?")
    alta_categoria(2, "Dinero Famosos", "¿Qué famoso es más rico?")
    alta_categoria(3, "Países", "¿Qué país tiene más habitantes?")
    alta_categoria(4, "Duración Películas", "¿Qué película dura más?")


def listar_categorias():
    print("NRO | NOMBRE                         | EST | PREGUNTA")
    print("-" * 80)
    archivo = open(RUTA_CATEGORIAS, "rb")
    tamanio = os.path.getsize(RUTA_CATEGORIAS)
    while archivo.tell() < tamanio:
        reg = pickle.load(archivo)
        print(reg.NroCategoria, "|", reg.NombreCategoria, "|", reg.Estado, "|", reg.Pregunta)
    archivo.close()


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------
def principal():
    if os.path.exists(CARPETA):
        if archivo_vacio():
            cargar_categorias_iniciales()
            print("categorias.dat creado con las categorías iniciales.")
        else:
            print("categorias.dat ya existe, no se vuelve a crear.")
        listar_categorias()
    else:
        print("No existe la carpeta " + CARPETA)
        print("Créela manualmente y vuelva a ejecutar el programa.")


def salir():
    print("Bye Bye")
    input()

def cerrarArchivos():
    arLoContacto.close()

def ejecutarCase(o):
    if o == 1:
        alta_categoria()
    if o == 2:
        mostrar_categoria()
    if o == 3:
        modificar_categoria()
    if o == 4:
        eliminar_categoria()
    if o == 5:
        listar_categorias()
    if o == 0:
        salir()


def mostrarMenu():
    os.system("cls")
    print("1- Alta")
    print("2 – Mostrar una categoría")
    print("3 – Modificar datos de una categoría")
    print("4 – Eliminar categoría (Baja lógica)")
    print("5 - Mostrar todas las categorías")
    print("0 – Fin del programa")


def menu():
    mostrarMenu()
    opcion = input("Ingresar opción deseada: ")
    while not validarIngresoEntero(opcion, 0, 5):
        opcion = input("Ingresar opción deseada: ")
    opcion = int(opcion)
    ejecutarCase(opcion)
    while opcion != 0:
        mostrarMenu()
        opcion = input("Ingresar opción deseada: ")
        while not validarIngresoEntero(opcion, 0, 5):
            opcion = input("Ingresar opción deseada: ")
        opcion = int(opcion)
        ejecutarCase(opcion)

global arFiCategoria
global arLoCategoria

abrirArchivo()
menu()
cerrarArchivos()