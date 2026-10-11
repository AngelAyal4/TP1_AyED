import pickle
import os


# ---------------------------------------------------------------
# RUTA DEL ARCHIVO
# Si existe c:\tp3\ se usa esa carpeta (enunciado).
# Si no existe (por ejemplo al probar en Linux), es portable:
# el .dat se crea junto a este .py.
# ---------------------------------------------------------------
CARPETA = "c:\\tp3\\"
if not os.path.exists(CARPETA):
    CARPETA = os.path.dirname(__file__) + os.sep

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
        self.Estado = "A"                           # A = Activa / I = Inactiva


# ---------------------------------------------------------------
# ARCHIVO (handle persistente, acceso directo con pickle)
# ---------------------------------------------------------------
def abrirArchivo():
    global arLoCategorias
    if os.path.exists(RUTA_CATEGORIAS):
        arLoCategorias = open(RUTA_CATEGORIAS, "r+b")
    else:
        print("El archivo " + RUTA_CATEGORIAS + " NO existía y fue creado")
        arLoCategorias = open(RUTA_CATEGORIAS, "w+b")


def cerrarArchivos():
    arLoCategorias.close()


def tamanioRegistro():
    # ponytail: tamanio fijo asume NroCategoria < 256 (pickle codifica el
    # int en 1 byte). Con 256+ categorias el registro cambiaria de tamano.
    arLoCategorias.seek(0, 0)
    pickle.load(arLoCategorias)
    tam = arLoCategorias.tell()
    return tam


def cantidadRegistros():
    tam = os.path.getsize(RUTA_CATEGORIAS)
    cant = 0
    if tam > 0:
        cant = tam // tamanioRegistro()
    return cant


def archivo_vacio():
    tam = os.path.getsize(RUTA_CATEGORIAS) if os.path.exists(RUTA_CATEGORIAS) else 0
    vacio = tam == 0
    return vacio


# ---------------------------------------------------------------
# VALIDACIONES Y FORMATEO
# ---------------------------------------------------------------
def sinAcentos(texto):
    # Normaliza a ASCII: un caracter acentuado ocupa mas de 1 byte en UTF-8
    # y haria que los registros midan distinto (rompe el acceso directo).
    resultado = ""
    i = 0
    while i < len(texto):
        c = texto[i]
        if c == "á" or c == "à" or c == "ä" or c == "â" or c == "Á" or c == "À" or c == "Ä" or c == "Â":
            resultado = resultado + "a"
        elif c == "é" or c == "è" or c == "ë" or c == "ê" or c == "É" or c == "È" or c == "Ë" or c == "Ê":
            resultado = resultado + "e"
        elif c == "í" or c == "ì" or c == "ï" or c == "î" or c == "Í" or c == "Ì" or c == "Ï" or c == "Î":
            resultado = resultado + "i"
        elif c == "ó" or c == "ò" or c == "ö" or c == "ô" or c == "Ó" or c == "Ò" or c == "Ö" or c == "Ô":
            resultado = resultado + "o"
        elif c == "ú" or c == "ù" or c == "ü" or c == "û" or c == "Ú" or c == "Ù" or c == "Ü" or c == "Û":
            resultado = resultado + "u"
        elif c == "ñ":
            resultado = resultado + "n"
        elif c == "Ñ":
            resultado = resultado + "N"
        elif c == "¿":
            resultado = resultado + "?"
        elif c == "¡":
            resultado = resultado + "!"
        else:
            if len(c.encode("utf-8")) > 1:
                resultado = resultado + "?"
            else:
                resultado = resultado + c
        i = i + 1
    return resultado


def formatear(texto, largo):
    return sinAcentos(texto)[:largo].ljust(largo)


def validarIngresoEntero(x, y, z):
    valido = False
    try:
        valor = int(x)
        if valor >= y and valor <= z:
            valido = True
        else:
            print(f"Por favor, ingrese un valor entre {y} y {z}")
    except ValueError:
        print("Por favor, ingrese un valor entero")
    return valido


def existeNombre(nombre, nroExcluido):
    existe = False
    tam = os.path.getsize(RUTA_CATEGORIAS)
    arLoCategorias.seek(0, 0)
    while arLoCategorias.tell() < tam:
        reg = pickle.load(arLoCategorias)
        if reg.NroCategoria != nroExcluido and \
                reg.NombreCategoria.rstrip().upper() == nombre.strip().upper():
            existe = True
    return existe


def leerCategoriaEnPosicion(pos):
    arLoCategorias.seek(pos, 0)
    reg = pickle.load(arLoCategorias)
    return reg


def grabarCategoriaEnPosicion(pos, reg):
    arLoCategorias.seek(pos, 0)
    pickle.dump(reg, arLoCategorias)
    arLoCategorias.flush()


def grabarCategoria(nro, nombre, pregunta):
    reg = Categoria()
    reg.NroCategoria = nro
    reg.NombreCategoria = formatear(nombre, LARGO_NOMBRE)
    reg.Pregunta = formatear(pregunta, LARGO_PREGUNTA)
    reg.Estado = "A"
    arLoCategorias.seek(0, 2)
    pickle.dump(reg, arLoCategorias)
    arLoCategorias.flush()


# ---------------------------------------------------------------
# C de CRUD - Alta
# ---------------------------------------------------------------
def altaCategoria():
    continuar = input("¿Seguro que va a dar de alta categorías (S/N)?: ").upper()
    while continuar != "S" and continuar != "N":
        print("Por favor, solo S o N")
        continuar = input("¿Seguro que va a dar de alta categorías (S/N)?: ").upper()
    while continuar == "S":
        nombre = input("Ingresar nombre de la categoría (Max. 30 caracteres): ")
        while len(nombre) > LARGO_NOMBRE or nombre.strip() == "":
            print("El nombre no puede estar vacío ni superar los 30 caracteres")
            nombre = input("Ingresar nombre de la categoría (Max. 30 caracteres): ")
        if existeNombre(nombre, 0):
            print("Ya existe una categoría con ese nombre")
        else:
            pregunta = input("Ingresar la pregunta (Max. 200 caracteres): ")
            while len(pregunta) > LARGO_PREGUNTA or pregunta.strip() == "":
                print("La pregunta no puede estar vacía ni superar los 200 caracteres")
                pregunta = input("Ingresar la pregunta (Max. 200 caracteres): ")
            reg = Categoria()
            reg.NroCategoria = cantidadRegistros() + 1
            reg.NombreCategoria = formatear(nombre, LARGO_NOMBRE)
            reg.Pregunta = formatear(pregunta, LARGO_PREGUNTA)
            reg.Estado = "A"
            arLoCategorias.seek(0, 2)
            pickle.dump(reg, arLoCategorias)
            arLoCategorias.flush()
            print("Categoría", reg.NroCategoria, "-", nombre, "dada de alta")
        continuar = input("¿Ingresa otra categoría (S/N)?: ").upper()
        while continuar != "S" and continuar != "N":
            print("Por favor, solo S o N")
            continuar = input("¿Ingresa otra categoría (S/N)?: ").upper()
    input("Presione Enter para continuar...")


# ---------------------------------------------------------------
# R de CRUD - Mostrar una
# ---------------------------------------------------------------
def mostrarCategoria():
    cant = cantidadRegistros()
    if cant == 0:
        print("No hay categorías registradas")
    else:
        entrada = input("Ingresar el número de categoría a mostrar: ")
        while not validarIngresoEntero(entrada, 1, cant):
            entrada = input("Ingresar el número de categoría a mostrar: ")
        nro = int(entrada)
        pos = (nro - 1) * tamanioRegistro()
        reg = leerCategoriaEnPosicion(pos)
        print("Número:   ", reg.NroCategoria)
        print("Nombre:   ", reg.NombreCategoria.rstrip())
        print("Pregunta: ", reg.Pregunta.rstrip())
        print("Estado:   ", reg.Estado)
    input("Presione Enter para continuar...")


# ---------------------------------------------------------------
# R de CRUD - Listar todas
# ---------------------------------------------------------------
def listarCategorias(soloActivas):
    print("NRO | NOMBRE                         | EST | PREGUNTA")
    print("-" * 80)
    tam = os.path.getsize(RUTA_CATEGORIAS)
    arLoCategorias.seek(0, 0)
    while arLoCategorias.tell() < tam:
        reg = pickle.load(arLoCategorias)
        if not soloActivas or reg.Estado == "A":
            print(reg.NroCategoria, "|", reg.NombreCategoria.rstrip(), "|",
                  reg.Estado, "|", reg.Pregunta.rstrip())


# ---------------------------------------------------------------
# U de CRUD - Modificación (solo el nombre)
# ---------------------------------------------------------------
def modificarCategoria():
    cant = cantidadRegistros()
    if cant == 0:
        print("No hay categorías registradas")
    else:
        listarCategorias(True)
        entrada = input("Ingresar el número de categoría a modificar: ")
        while not validarIngresoEntero(entrada, 1, cant):
            entrada = input("Ingresar el número de categoría a modificar: ")
        nro = int(entrada)
        pos = (nro - 1) * tamanioRegistro()
        reg = leerCategoriaEnPosicion(pos)
        if reg.Estado != "A":
            print("La categoría no está Activa, no se puede modificar")
        else:
            nuevo = input("Ingresar el nuevo nombre (Max. 30 caracteres): ")
            while len(nuevo) > LARGO_NOMBRE or nuevo.strip() == "":
                print("El nombre no puede estar vacío ni superar los 30 caracteres")
                nuevo = input("Ingresar el nuevo nombre (Max. 30 caracteres): ")
            if existeNombre(nuevo, nro):
                print("Ya existe otra categoría con ese nombre")
            else:
                reg.NombreCategoria = formatear(nuevo, LARGO_NOMBRE)
                grabarCategoriaEnPosicion(pos, reg)
                print("Categoría", nro, "modificada")
    input("Presione Enter para continuar...")


# ---------------------------------------------------------------
# D de CRUD - Baja lógica
# ---------------------------------------------------------------
def bajaCategoria():
    cant = cantidadRegistros()
    if cant == 0:
        print("No hay categorías registradas")
    else:
        listarCategorias(True)
        entrada = input("Ingresar el número de categoría a dar de baja: ")
        while not validarIngresoEntero(entrada, 1, cant):
            entrada = input("Ingresar el número de categoría a dar de baja: ")
        nro = int(entrada)
        pos = (nro - 1) * tamanioRegistro()
        reg = leerCategoriaEnPosicion(pos)
        if reg.Estado != "A":
            print("La categoría ya está Inactiva")
        else:
            reg.Estado = "I"
            grabarCategoriaEnPosicion(pos, reg)
            print("Categoría", nro, "-", reg.NombreCategoria.rstrip(), "dada de baja")
    input("Presione Enter para continuar...")


# ---------------------------------------------------------------
# CARGA INICIAL (mínimo 3 categorías para la entrega)
# ---------------------------------------------------------------
def cargarCategoriasIniciales():
    grabarCategoria(1, "Edad Famosos", "¿Quién tiene más años?")
    grabarCategoria(2, "Dinero Famosos", "¿Qué famoso es más rico?")
    grabarCategoria(3, "Países", "¿Qué país tiene más habitantes?")
    print("Se cargaron 3 categorías iniciales")


# ---------------------------------------------------------------
# MENÚ
# ---------------------------------------------------------------
def salir():
    print("Bye Bye")


def mostrarMenu():
    os.system("cls" if os.name == "nt" else "clear")
    print("1 - Alta de categoría")
    print("2 - Mostrar una categoría")
    print("3 - Modificar nombre de una categoría")
    print("4 - Baja de categoría (lógica)")
    print("5 - Listar todas las categorías")
    print("0 - Fin del programa")


def ejecutarCase(o):
    if o == 1:
        altaCategoria()
    if o == 2:
        mostrarCategoria()
    if o == 3:
        modificarCategoria()
    if o == 4:
        bajaCategoria()
    if o == 5:
        listarCategorias(False)
        input("Presione Enter para continuar...")
    if o == 0:
        salir()


def menu():
    termino = False
    while not termino:
        mostrarMenu()
        opcion = input("Ingresar opción deseada: ")
        while not validarIngresoEntero(opcion, 0, 5):
            opcion = input("Ingresar opción deseada: ")
        opcion = int(opcion)
        if opcion == 0:
            termino = True
        else:
            ejecutarCase(opcion)


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------
global arLoCategorias

abrirArchivo()
if archivo_vacio():
    cargarCategoriasIniciales()
menu()
cerrarArchivos()
