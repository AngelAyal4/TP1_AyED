import pickle
import os


# ---------------------------------------------------------------
# RUTA DE LOS ARCHIVOS
# Si existe c:\tp3\ se usa esa carpeta (enunciado).
# Si no existe (por ejemplo al probar en Linux), es portable:
# los .dat se crean junto a este .py.
# ---------------------------------------------------------------
CARPETA = "c:\\tp3\\"
if not os.path.exists(CARPETA):
    CARPETA = os.path.dirname(__file__) + os.sep

RUTA_CATEGORIAS = CARPETA + "categorias.dat"
RUTA_OPCIONES = CARPETA + "opciones.dat"

LARGO_NOMBRE = 30
LARGO_PREGUNTA = 200
LARGO_OBJETO = 100


# ---------------------------------------------------------------
# REGISTROS
# ---------------------------------------------------------------
class Categoria:
    def __init__(self):
        self.NroCategoria = 0                       # int (consecutivo desde 1)
        self.NombreCategoria = " "                  # str(30)
        self.Pregunta = " "                         # str(200)
        self.Estado = "A"                           # A = Activa / I = Inactiva


class Opcion:
    def __init__(self):
        self.NroCategoria = 0                       # FK -> Categoria.NroCategoria
        self.NroOpcion = 0                          # consecutivo dentro de la categoría
        self.objeto = " "                           # str(100)
        self.valor = 0                              # int


# ---------------------------------------------------------------
# ARCHIVOS (handles persistentes)
# ---------------------------------------------------------------
def abrirArchivos():
    global arLoCategorias
    global arLoOpciones
    arLoCategorias = abrirUno(RUTA_CATEGORIAS)
    arLoOpciones = abrirUno(RUTA_OPCIONES)


def abrirUno(ruta):
    if os.path.exists(ruta):
        handle = open(ruta, "r+b")
    else:
        print("El archivo " + ruta + " NO existía y fue creado")
        handle = open(ruta, "w+b")
    return handle


def cerrarArchivos():
    arLoCategorias.close()
    arLoOpciones.close()


def archivoVacio(ruta):
    tam = os.path.getsize(ruta) if os.path.exists(ruta) else 0
    return tam == 0


# ---------------------------------------------------------------
# VALIDACIONES Y FORMATEO
# ---------------------------------------------------------------
def sinAcentos(texto):
    # Normaliza a ASCII (ver categoriasOC.py): evita que los acentos
    # cambien el tamaño serializado del registro.
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


def validarEntero(x):
    valor = None
    try:
        valor = int(x)
    except ValueError:
        print("Por favor, ingrese un valor entero")
    return valor


# Devuelve True si el texto esta formado solo por digitos (sin signos ni espacios).
def esNumero(texto):
    resultado = len(texto) > 0
    i = 0
    while i < len(texto) and resultado:
        if texto[i] < "0" or texto[i] > "9":
            resultado = False
        i = i + 1
    return resultado


# ---------------------------------------------------------------
# ACCESO A CATEGORIAS (para relacionar Opciones -> Categoria)
# ---------------------------------------------------------------
# Devuelve el tamaño en bytes de un registro de categoria (para acceso directo).
def tamanioRegistroCategoria():
    arLoCategorias.seek(0, 0)
    pickle.load(arLoCategorias)
    return arLoCategorias.tell()

# Devuelve la cantidad total de categorias del archivo.
def cantidadCategorias():
    tam = os.path.getsize(RUTA_CATEGORIAS)
    cant = 0
    if tam > 0:
        cant = tam // tamanioRegistroCategoria()
    return cant


# Lee y devuelve la categoria numero 'nro' (acceso directo: pos = (nro-1)*tamReg).
def leerCategoria(nro):
    pos = (nro - 1) * tamanioRegistroCategoria()
    arLoCategorias.seek(pos, 0)
    return pickle.load(arLoCategorias)


# Devuelve True si la categoria 'nro' existe y esta Activa ("A").
def categoriaActiva(nro):
    activa = False
    if nro >= 1 and nro <= cantidadCategorias():
        reg = leerCategoria(nro)
        if reg.Estado == "A":
            activa = True
    return activa


# Cuenta cuantas categorias estan Activas ("A").
def cantidadCategoriasActivas():
    cant = 0
    tam = os.path.getsize(RUTA_CATEGORIAS)
    arLoCategorias.seek(0, 0)
    while arLoCategorias.tell() < tam:
        reg = pickle.load(arLoCategorias)
        if reg.Estado == "A":
            cant = cant + 1
    return cant


# Muestra numero, nombre y pregunta de todas las categorias Activas.
def listarCategoriasActivas():
    print("NRO | NOMBRE                         | PREGUNTA")
    print("-" * 80)
    tam = os.path.getsize(RUTA_CATEGORIAS)
    arLoCategorias.seek(0, 0)
    while arLoCategorias.tell() < tam:
        reg = pickle.load(arLoCategorias)
        if reg.Estado == "A":
            print(reg.NroCategoria, "|", reg.NombreCategoria.rstrip(), "|",
                  reg.Pregunta.rstrip())


# Pide por teclado un numero de categoria valido y Activo; devuelve ese numero.
def pedirCategoriaActiva(mensaje):
    nro = 0
    ingresar = True
    while ingresar:
        entrada = input(mensaje).strip()
        if not esNumero(entrada):
            print("Solo se permiten numeros")
        elif validarIngresoEntero(entrada, 1, cantidadCategorias()):
            nro = int(entrada)
            if categoriaActiva(nro):
                ingresar = False
            else:
                print("La categoría no está Activa, elija otra")
    return nro


# ---------------------------------------------------------------
# ACCESO A OPCIONES
# ---------------------------------------------------------------
# Cuenta cuantas opciones pertenecen a la categoria 'nroCategoria' (barrido secuencial).
def contarOpcionesDe(nroCategoria):
    cant = 0
    tam = os.path.getsize(RUTA_OPCIONES)
    arLoOpciones.seek(0, 0)
    while arLoOpciones.tell() < tam:
        reg = pickle.load(arLoOpciones)
        if reg.NroCategoria == nroCategoria:
            cant = cant + 1
    return cant


# Agrega una opcion al final con NroOpcion = (cantidad de esa categoria + 1); devuelve ese NroOpcion.
def grabarOpcion(nroCategoria, objeto, valor):
    reg = Opcion()
    reg.NroCategoria = nroCategoria
    reg.NroOpcion = contarOpcionesDe(nroCategoria) + 1
    reg.objeto = formatear(objeto, LARGO_OBJETO)
    reg.valor = valor
    arLoOpciones.seek(0, 2)
    pickle.dump(reg, arLoOpciones)
    arLoOpciones.flush()
    return reg.NroOpcion


# Agrega una categoria nueva al final (la usa la carga inicial de datos).
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
# ALTA DE OPCION
# ---------------------------------------------------------------
# Pide categoria activa, objeto y valor; graba una opcion nueva (Alta).
def altaOpcion():
    if cantidadCategoriasActivas() == 0:
        print("Antes de registrar opciones debe dar de alta categorías activas")
    else:
        listarCategoriasActivas()
        nro = pedirCategoriaActiva("Ingresar el número de categoría: ")
        objeto = input("Ingresar el objeto (Max. 100 caracteres): ")
        while len(objeto) > LARGO_OBJETO or objeto.strip() == "":
            print("El objeto no puede estar vacío ni superar los 100 caracteres")
            objeto = input("Ingresar el objeto (Max. 100 caracteres): ")
        valor = validarEntero(input("Ingresar el valor (número entero): "))
        while valor is None:
            valor = validarEntero(input("Ingresar el valor (número entero): "))
        nroOpcion = grabarOpcion(nro, objeto, valor)
        print("Opción", nroOpcion, "de la categoría", nro, "-", objeto, "dada de alta")
    input("Presione Enter para continuar...")


# ---------------------------------------------------------------
# CONSULTA DE OPCIONES
# ---------------------------------------------------------------
# Muestra la pregunta y todas las opciones con su valor de una categoria (Consulta).
def consultaOpciones():
    if cantidadCategoriasActivas() == 0:
        print("No hay categorías activas")
    else:
        listarCategoriasActivas()
        nro = pedirCategoriaActiva("Ingresar el número de categoría a consultar: ")
        reg = leerCategoria(nro)
        print("Pregunta:", reg.Pregunta.rstrip())
        print("NRO | OBJETO                                   | VALOR")
        print("-" * 80)
        hay = False
        tam = os.path.getsize(RUTA_OPCIONES)
        arLoOpciones.seek(0, 0)
        while arLoOpciones.tell() < tam:
            op = pickle.load(arLoOpciones)
            if op.NroCategoria == nro:
                print(op.NroOpcion, "|", op.objeto.rstrip(), "|", op.valor)
                hay = True
        if not hay:
            print("La categoría no tiene opciones cargadas")
    input("Presione Enter para continuar...")


# ---------------------------------------------------------------
# CARGA INICIAL (mínimo para la entrega, sin listas)
# ---------------------------------------------------------------
# Carga 3 categorias de ejemplo (solo si categorias.dat esta vacio).
def cargarCategoriasIniciales():
    grabarCategoria(1, "Edad Famosos", "¿Quién tiene más años?")
    grabarCategoria(2, "Dinero Famosos", "¿Qué famoso es más rico?")
    grabarCategoria(3, "Países", "¿Qué país tiene más habitantes?")
    print("Se cargaron 3 categorías iniciales")


# Carga 9 opciones de ejemplo (3 por categoria; solo si opciones.dat esta vacio).
def cargarOpcionesIniciales():
    grabarOpcion(1, "Tom Cruise", 62)
    grabarOpcion(1, "Lionel Messi", 37)
    grabarOpcion(1, "Cristiano Ronaldo", 39)
    grabarOpcion(2, "Lionel Messi", 600)
    grabarOpcion(2, "Cristiano Ronaldo", 800)
    grabarOpcion(2, "Elon Musk", 400)
    grabarOpcion(3, "Argentina", 46000000)
    grabarOpcion(3, "Brasil", 215000000)
    grabarOpcion(3, "China", 1400000000)
    print("Se cargaron 9 opciones iniciales")


# ---------------------------------------------------------------
# MENÚ
# ---------------------------------------------------------------
# Limpia la pantalla y muestra las opciones del menu.
def mostrarMenu():
    os.system("cls" if os.name == "nt" else "clear")
    print("1 - Alta de opción")
    print("2 - Consulta de opciones")
    print("3 - Volver")
    print("0 - Fin del programa")


# Despacha la opcion elegida a la funcion correspondiente.
def ejecutarCase(o):
    if o == 1:
        altaOpcion()
    if o == 2:
        consultaOpciones()
    if o == 3:
        print("Volviendo...")


# Bucle principal del menu hasta que el usuario elige salir.
def menu():
    termino = False
    while not termino:
        mostrarMenu()
        opcion = input("Ingresar opción deseada: ")
        while not validarIngresoEntero(opcion, 0, 3):
            opcion = input("Ingresar opción deseada: ")
        opcion = int(opcion)
        if opcion == 0 or opcion == 3:
            termino = True
        else:
            ejecutarCase(opcion)


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------
global arLoCategorias
global arLoOpciones

abrirArchivos()
if archivoVacio(RUTA_CATEGORIAS):
    cargarCategoriasIniciales()
if archivoVacio(RUTA_OPCIONES):
    cargarOpcionesIniciales()
menu()
cerrarArchivos()
