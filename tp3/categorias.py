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
        self.NombreCategoria = " " * LARGO_NOMBRE   # str(30)
        self.Pregunta = " " * LARGO_PREGUNTA        # str(200)
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


principal()