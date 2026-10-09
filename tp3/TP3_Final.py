import random
import os
import pickle
import getpass

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
RUTA_OPCIONES = CARPETA + "opciones.dat"
RUTA_JUGADORES = CARPETA + "jugadores.dat"
RUTA_JUGADORES_AUX = CARPETA + "jugadores_aux.dat"

LARGO_NOMBRE = 30
LARGO_PREGUNTA = 200
LARGO_OBJETO = 100

MIN_OPCIONES_PARTIDA = 7  # opciones distintas que necesita una partida (2 + 5 nuevas)

CONTRASENA_ADMIN = "admin"  # constante del programa principal (enunciado §F)


# ---------------------------------------------------------------
# REGISTROS
# ---------------------------------------------------------------
class Categoria:
    def __init__(self):
        self.NroCategoria = 0  # int (consecutivo desde 1)
        self.NombreCategoria = " "  # str(30)
        self.Pregunta = " "  # str(200)
        self.Estado = "A"  # A = Activa / I = Inactiva


class Opcion:
    def __init__(self):
        self.NroCategoria = 0  # FK -> Categoria.NroCategoria
        self.NroOpcion = 0  # consecutivo dentro de la categoria
        self.objeto = " "  # str(100)
        self.valor = 0  # int


class Jugador:
    def __init__(self):
        self.nombre = ""  # str(30)
        self.Creditos = 0.0  # float (arranca en 10000)
        self.juegos = [
            [0] * 4 for _ in range(2)
        ]  # matriz 2x4 (fila 0 gano / fila 1 perdio)


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
        if (
            c == "á"
            or c == "à"
            or c == "ä"
            or c == "â"
            or c == "Á"
            or c == "À"
            or c == "Ä"
            or c == "Â"
        ):
            resultado = resultado + "a"
        elif (
            c == "é"
            or c == "è"
            or c == "ë"
            or c == "ê"
            or c == "É"
            or c == "È"
            or c == "Ë"
            or c == "Ê"
        ):
            resultado = resultado + "e"
        elif (
            c == "í"
            or c == "ì"
            or c == "ï"
            or c == "î"
            or c == "Í"
            or c == "Ì"
            or c == "Ï"
            or c == "Î"
        ):
            resultado = resultado + "i"
        elif (
            c == "ó"
            or c == "ò"
            or c == "ö"
            or c == "ô"
            or c == "Ó"
            or c == "Ò"
            or c == "Ö"
            or c == "Ô"
        ):
            resultado = resultado + "o"
        elif (
            c == "ú"
            or c == "ù"
            or c == "ü"
            or c == "û"
            or c == "Ú"
            or c == "Ù"
            or c == "Ü"
            or c == "Û"
        ):
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
    # Deja el texto en ASCII y con largo fijo (rellena con espacios).
    return sinAcentos(texto)[:largo].ljust(largo)


def validarIngresoEntero(x, y, z):
    # Devuelve True si x es un entero entre y y z (inclusive).
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
    # Devuelve el entero de x, o None si no es un numero entero.
    valor = None
    try:
        valor = int(x)
    except ValueError:
        print("Por favor, ingrese un valor entero")
    return valor


def esNumero(texto):
    # Devuelve True si el texto esta formado solo por digitos (sin signos ni espacios).
    resultado = len(texto) > 0
    i = 0
    while i < len(texto) and resultado:
        if texto[i] < "0" or texto[i] > "9":
            resultado = False
        i = i + 1
    return resultado


def validarNombre(name):
    # Valida que el nombre no este vacio ni supere los 30 caracteres.
    while len(name) > 30 or name.strip() == "":
        print("El nombre no puede superar los 30 caracteres.")
        name = input("Ingrese nombre (máximo 30 caracteres): ")
    return name


# ---------------------------------------------------------------
# CRUD JUGADORES
# ---------------------------------------------------------------
def buscarJugador(name):
    # Busca un jugador por nombre (barrido secuencial); devuelve su posicion o -1.
    global arLoJugadores
    buscado = sinAcentos(name).strip().upper()
    tam = os.path.getsize(RUTA_JUGADORES)
    pos = 0
    resultado = -1
    arLoJugadores.seek(0, 0)
    if tam > 0:
        jug = pickle.load(arLoJugadores)
        while arLoJugadores.tell() < tam and jug.nombre.rstrip().upper() != buscado:
            pos = arLoJugadores.tell()
            jug = pickle.load(arLoJugadores)
        if jug.nombre.strip().upper() == buscado:
            resultado = pos
    return resultado


def crearJugador(name):
    # Agrega un jugador nuevo al final con credito inicial de 10000.
    global arLoJugadores
    jug = Jugador()
    jug.nombre = formatear(name.strip(), LARGO_NOMBRE).upper()
    jug.Creditos = 10000.0
    arLoJugadores.seek(0, 2)
    pickle.dump(jug, arLoJugadores)
    arLoJugadores.flush()
    print("Jugador creado ", name)


def tamanioRegistroJugador():
    # Devuelve el tamanio en bytes de un registro de jugador (para acceso directo).
    # ponytail: asume los contadores de la matriz < 256 (pickle codifica el int en 1 byte).
    global arLoJugadores
    arLoJugadores.seek(0, 0)
    pickle.load(arLoJugadores)
    return arLoJugadores.tell()


def cantidadJugadores():
    # Devuelve la cantidad de jugadores registrados.
    tam = os.path.getsize(RUTA_JUGADORES)
    cant = 0
    if tam > 0:
        cant = tam // tamanioRegistroJugador()
    return cant


def leerJugadorEnPosicion(pos):
    # Lee y devuelve el jugador que esta en la posicion 'pos' (acceso directo).
    global arLoJugadores
    arLoJugadores.seek(pos, 0)
    return pickle.load(arLoJugadores)


def grabarJugadorEnPosicion(pos, reg):
    # Regraba un registro de jugador en su posicion.
    global arLoJugadores
    arLoJugadores.seek(pos, 0)
    pickle.dump(reg, arLoJugadores)
    arLoJugadores.flush()


def actualizarJugador(pos, regJugador):
    # Regraba un jugador en su posicion; lo usan los juegos al terminar cada partida (U del CRUD).
    grabarJugadorEnPosicion(pos, regJugador)
    print("Jugador actualizado:", regJugador.nombre.rstrip())


def nombreJuego(col):
    # Devuelve el nombre del juego segun la columna de la matriz (0..3).
    nombre = ""
    if col == 0:
        nombre = "Mayor/Menor"
    elif col == 1:
        nombre = "Numero secreto"
    elif col == 2:
        nombre = "Blackjack"
    elif col == 3:
        nombre = "Par/Impar"
    return nombre


def mostrarJugador(name):
    # Muestra los datos y la matriz de un jugador buscado por nombre (R del CRUD).
    pos = buscarJugador(name)
    if pos == -1:
        print("El jugador no existe")
    else:
        reg = leerJugadorEnPosicion(pos)
        print("Nombre:   ", reg.nombre.rstrip())
        print("Creditos: ", reg.Creditos)
        col = 0
        while col < 4:
            print(
                nombreJuego(col),
                "- Gano:",
                reg.juegos[0][col],
                "Perdio:",
                reg.juegos[1][col],
            )
            col = col + 1
    input("Presione Enter para continuar...")


def copiarJugadoresAux():
    # Copia jugadores.dat a un archivo auxiliar para ordenarlo sin tocar el original.
    global arLoJugadores
    global arLoJugadoresAux
    arLoJugadoresAux = open(RUTA_JUGADORES_AUX, "w+b")
    tam = os.path.getsize(RUTA_JUGADORES)
    arLoJugadores.seek(0, 0)
    while arLoJugadores.tell() < tam:
        reg = pickle.load(arLoJugadores)
        pickle.dump(reg, arLoJugadoresAux)
    arLoJugadoresAux.flush()


def ordenarJugadoresPorCreditos():
    # Muestra los jugadores de mayor a menor por creditos (ordena una copia auxiliar).
    global arLoJugadoresAux
    cant = cantidadJugadores()
    if cant == 0:
        print("No hay jugadores registrados")
    else:
        copiarJugadoresAux()
        tam = tamanioRegistroJugador()
        i = 0
        while i < cant - 1:
            j = i + 1
            while j < cant:
                arLoJugadoresAux.seek(i * tam, 0)
                jug1 = pickle.load(arLoJugadoresAux)
                arLoJugadoresAux.seek(j * tam, 0)
                jug2 = pickle.load(arLoJugadoresAux)
                if jug1.Creditos < jug2.Creditos:
                    arLoJugadoresAux.seek(i * tam, 0)
                    pickle.dump(jug2, arLoJugadoresAux)
                    arLoJugadoresAux.seek(j * tam, 0)
                    pickle.dump(jug1, arLoJugadoresAux)
                j = j + 1
            i = i + 1
        arLoJugadoresAux.flush()
        print("JUGADOR                        | CREDITOS")
        print("-" * 50)
        arLoJugadoresAux.seek(0, 0)
        while arLoJugadoresAux.tell() < cant * tam:
            reg = pickle.load(arLoJugadoresAux)
            print(reg.nombre.rstrip(), "|", reg.Creditos)
        arLoJugadoresAux.close()
        os.remove(RUTA_JUGADORES_AUX)
    input("Presione Enter para continuar...")


def reportePartidasJugador(name):
    # Muestra a que juegos jugo un jugador, victorias/derrotas por juego y creditos (reporte b).
    pos = buscarJugador(name)
    if pos == -1:
        print("El jugador no existe")
    else:
        reg = leerJugadorEnPosicion(pos)
        print("Jugador:", reg.nombre.rstrip())
        col = 0
        while col < 4:
            gano = reg.juegos[0][col]
            perdio = reg.juegos[1][col]
            if gano + perdio > 0:
                print(nombreJuego(col), "- Gano:", gano, "Perdio:", perdio)
            col = col + 1
        print("Creditos disponibles:", reg.Creditos)
    input("Presione Enter para continuar...")


# ---------------------------------------------------------------
# ACCESO A CATEGORIAS (capa compartida por los CRUD y el juego Menor-Mayor)
# ---------------------------------------------------------------
def tamanioRegistroCategoria():
    # Devuelve el tamanio en bytes de un registro de categoria (para acceso directo).
    # ponytail: tamanio fijo asume NroCategoria < 256 (pickle codifica el int en 1 byte).
    global arLoCategorias
    arLoCategorias.seek(0, 0)
    pickle.load(arLoCategorias)
    return arLoCategorias.tell()


def cantidadCategorias():
    # Devuelve la cantidad total de categorias del archivo.
    tam = os.path.getsize(RUTA_CATEGORIAS)
    cant = 0
    if tam > 0:
        cant = tam // tamanioRegistroCategoria()
    return cant


def leerCategoria(nro):
    # Lee y devuelve la categoria numero 'nro' (acceso directo: pos = (nro-1)*tamReg).
    global arLoCategorias
    pos = (nro - 1) * tamanioRegistroCategoria()
    arLoCategorias.seek(pos, 0)
    return pickle.load(arLoCategorias)


def grabarCategoriaEnPosicion(pos, reg):
    # Regraba un registro de categoria en su posicion (modificacion / baja).
    global arLoCategorias
    arLoCategorias.seek(pos, 0)
    pickle.dump(reg, arLoCategorias)
    arLoCategorias.flush()


def grabarCategoria(nro, nombre, pregunta):
    # Agrega una categoria nueva al final (la usa la carga inicial de datos).
    global arLoCategorias
    reg = Categoria()
    reg.NroCategoria = nro
    reg.NombreCategoria = formatear(nombre, LARGO_NOMBRE)
    reg.Pregunta = formatear(pregunta, LARGO_PREGUNTA)
    reg.Estado = "A"
    arLoCategorias.seek(0, 2)
    pickle.dump(reg, arLoCategorias)
    arLoCategorias.flush()


def existeNombre(nombre, nroExcluido):
    # Devuelve True si ya hay una categoria con ese nombre (ignora mayusculas).
    global arLoCategorias
    existe = False
    tam = os.path.getsize(RUTA_CATEGORIAS)
    arLoCategorias.seek(0, 0)
    while arLoCategorias.tell() < tam:
        reg = pickle.load(arLoCategorias)
        if (
            reg.NroCategoria != nroExcluido
            and reg.NombreCategoria.rstrip().upper() == nombre.strip().upper()
        ):
            existe = True
    return existe


def categoriaActiva(nro):
    # Devuelve True si la categoria 'nro' existe y esta Activa ("A").
    activa = False
    if nro >= 1 and nro <= cantidadCategorias():
        reg = leerCategoria(nro)
        if reg.Estado == "A":
            activa = True
    return activa


def cantidadCategoriasActivas():
    # Cuenta cuantas categorias estan Activas ("A").
    global arLoCategorias
    cant = 0
    tam = os.path.getsize(RUTA_CATEGORIAS)
    arLoCategorias.seek(0, 0)
    while arLoCategorias.tell() < tam:
        reg = pickle.load(arLoCategorias)
        if reg.Estado == "A":
            cant = cant + 1
    return cant


def listarCategorias(soloActivas):
    # Muestra numero, nombre, estado y pregunta de las categorias (todas o solo activas).
    global arLoCategorias
    print("NRO | NOMBRE                         | EST | PREGUNTA")
    print("-" * 80)
    tam = os.path.getsize(RUTA_CATEGORIAS)
    arLoCategorias.seek(0, 0)
    while arLoCategorias.tell() < tam:
        reg = pickle.load(arLoCategorias)
        if not soloActivas or reg.Estado == "A":
            print(
                reg.NroCategoria,
                "|",
                reg.NombreCategoria.rstrip(),
                "|",
                reg.Estado,
                "|",
                reg.Pregunta.rstrip(),
            )


def pedirCategoriaActiva(mensaje):
    # Pide por teclado un numero de categoria valido y Activo; devuelve ese numero.
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
# CRUD CATEGORIAS
# ---------------------------------------------------------------
def altaCategoria():
    # Pide nombre (valida duplicado) y pregunta; graba la categoria con Nro consecutivo (Alta).
    global arLoCategorias
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
            reg.NroCategoria = cantidadCategorias() + 1
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


def mostrarCategoria():
    # Muestra una sola categoria (por numero).
    cant = cantidadCategorias()
    if cant == 0:
        print("No hay categorías registradas")
    else:
        entrada = input("Ingresar el número de categoría a mostrar: ")
        while not validarIngresoEntero(entrada, 1, cant):
            entrada = input("Ingresar el número de categoría a mostrar: ")
        nro = int(entrada)
        reg = leerCategoria(nro)
        print("Número:   ", reg.NroCategoria)
        print("Nombre:   ", reg.NombreCategoria.rstrip())
        print("Pregunta: ", reg.Pregunta.rstrip())
        print("Estado:   ", reg.Estado)
    input("Presione Enter para continuar...")


def modificarCategoria():
    # Lista las activas, valida estado "A" y modifica solo el nombre (Modificacion).
    cant = cantidadCategorias()
    if cant == 0:
        print("No hay categorías registradas")
    else:
        listarCategorias(True)
        entrada = input("Ingresar el número de categoría a modificar: ")
        while not validarIngresoEntero(entrada, 1, cant):
            entrada = input("Ingresar el número de categoría a modificar: ")
        nro = int(entrada)
        pos = (nro - 1) * tamanioRegistroCategoria()
        reg = leerCategoria(nro)
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


def bajaCategoria():
    # Lista las activas, valida estado "A" y las pasa a Inactiva "I" (Baja logica).
    cant = cantidadCategorias()
    if cant == 0:
        print("No hay categorías registradas")
    else:
        listarCategorias(True)
        entrada = input("Ingresar el número de categoría a dar de baja: ")
        while not validarIngresoEntero(entrada, 1, cant):
            entrada = input("Ingresar el número de categoría a dar de baja: ")
        nro = int(entrada)
        pos = (nro - 1) * tamanioRegistroCategoria()
        reg = leerCategoria(nro)
        if reg.Estado != "A":
            print("La categoría ya está Inactiva")
        else:
            reg.Estado = "I"
            grabarCategoriaEnPosicion(pos, reg)
            print("Categoría", nro, "-", reg.NombreCategoria.rstrip(), "dada de baja")
    input("Presione Enter para continuar...")


# ---------------------------------------------------------------
# CRUD OPCIONES
# ---------------------------------------------------------------
def contarOpcionesDe(nroCategoria):
    # Cuenta cuantas opciones pertenecen a la categoria 'nroCategoria' (barrido secuencial).
    global arLoOpciones
    cant = 0
    tam = os.path.getsize(RUTA_OPCIONES)
    arLoOpciones.seek(0, 0)
    while arLoOpciones.tell() < tam:
        reg = pickle.load(arLoOpciones)
        if reg.NroCategoria == nroCategoria:
            cant = cant + 1
    return cant


def leerOpcionKDe(nroCategoria, k):
    # Devuelve la k-esima opcion (1..N) de la categoria (barrido secuencial).
    global arLoOpciones
    encontrada = Opcion()
    tam = os.path.getsize(RUTA_OPCIONES)
    visto = 0
    arLoOpciones.seek(0, 0)
    while arLoOpciones.tell() < tam:
        reg = pickle.load(arLoOpciones)
        if reg.NroCategoria == nroCategoria:
            visto = visto + 1
            if visto == k:
                encontrada = reg
    return encontrada


def grabarOpcion(nroCategoria, objeto, valor):
    # Agrega una opcion al final con NroOpcion = (cantidad de esa categoria + 1).
    global arLoOpciones
    reg = Opcion()
    reg.NroCategoria = nroCategoria
    reg.NroOpcion = contarOpcionesDe(nroCategoria) + 1
    reg.objeto = formatear(objeto, LARGO_OBJETO)
    reg.valor = valor
    arLoOpciones.seek(0, 2)
    pickle.dump(reg, arLoOpciones)
    arLoOpciones.flush()
    return reg.NroOpcion


def altaOpcion():
    # Pide categoria activa, objeto y valor; graba una opcion nueva (Alta).
    if cantidadCategoriasActivas() == 0:
        print("Antes de registrar opciones debe dar de alta categorías activas")
    else:
        listarCategorias(True)
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


def consultaOpciones():
    # Muestra la pregunta y todas las opciones con su valor de una categoria (Consulta).
    global arLoOpciones
    if cantidadCategoriasActivas() == 0:
        print("No hay categorías activas")
    else:
        listarCategorias(True)
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
# ADMINISTRACION (opcion F del menu principal)
# ---------------------------------------------------------------
def pedirContrasena():
    # Pide la contrasena oculta (getpass); da 3 intentos. Devuelve True si es correcta.
    ok = False
    intentos = 0
    while intentos < 3 and not ok:
        clave = getpass.getpass("Ingresar contraseña de administrador: ")
        if clave == CONTRASENA_ADMIN:
            ok = True
        else:
            intentos = intentos + 1
            if intentos < 3:
                print("Contraseña incorrecta. Intentos restantes:", 3 - intentos)
    if not ok:
        print(
            "Superó los 3 intentos de ingresar contraseña, salga e intente nuevamente"
        )
    return ok


def mostrarMenuAdmin():
    # Limpia la pantalla y muestra el submenu de administracion.
    os.system("cls" if os.name == "nt" else "clear")
    print("1 - Administrar Categorías")
    print("2 - Administrar Opciones")
    print("3 - Volver")


def menuAdmin():
    # Pide la contrasena y, si es correcta, muestra el submenu de administracion.
    if pedirContrasena():
        termino = False
        while not termino:
            mostrarMenuAdmin()
            opcion = input("Ingresar opción deseada: ")
            while not validarIngresoEntero(opcion, 1, 3):
                opcion = input("Ingresar opción deseada: ")
            opcion = int(opcion)
            if opcion == 1:
                menuAdminCategorias()
            if opcion == 2:
                menuAdminOpciones()
            if opcion == 3:
                termino = True


def mostrarMenuAdminCategorias():
    # Limpia la pantalla y muestra el submenu de categorias (enunciado §F).
    os.system("cls" if os.name == "nt" else "clear")
    print("1 - Alta")
    print("2 - Modificación")
    print("3 - Baja")
    print("4 - Volver")


def menuAdminCategorias():
    # Submenu iterativo de categorias: Alta / Modificacion / Baja / Volver.
    termino = False
    while not termino:
        mostrarMenuAdminCategorias()
        opcion = input("Ingresar opción deseada: ")
        while not validarIngresoEntero(opcion, 1, 4):
            opcion = input("Ingresar opción deseada: ")
        opcion = int(opcion)
        if opcion == 1:
            altaCategoria()
        if opcion == 2:
            modificarCategoria()
        if opcion == 3:
            bajaCategoria()
        if opcion == 4:
            termino = True


def mostrarMenuAdminOpciones():
    # Limpia la pantalla y muestra el submenu de opciones (enunciado §F).
    os.system("cls" if os.name == "nt" else "clear")
    print("1 - Alta")
    print("2 - Consulta")
    print("3 - Volver")


def menuAdminOpciones():
    # Submenu iterativo de opciones: Alta / Consulta / Volver.
    termino = False
    while not termino:
        mostrarMenuAdminOpciones()
        opcion = input("Ingresar opción deseada: ")
        while not validarIngresoEntero(opcion, 1, 3):
            opcion = input("Ingresar opción deseada: ")
        opcion = int(opcion)
        if opcion == 1:
            altaOpcion()
        if opcion == 2:
            consultaOpciones()
        if opcion == 3:
            termino = True


# ---------------------------------------------------------------
# JUEGOS
# ---------------------------------------------------------------

# ---------------------------------------------------------------
# JUEGO 1: MAYOR O MENOR
# ---------------------------------------------------------------


def yaUsado(usados, cantUsados, nroOpcion):
    # Devuelve True si 'nroOpcion' ya esta en el arreglo de opciones usadas.
    usado = False
    i = 0
    while i < cantUsados:
        if usados[i] == nroOpcion:
            usado = True
        i = i + 1
    return usado


def sortearOpcionNoUsada(nroCategoria, usados, cantUsados, valorEvitar):
    # Sortea una opcion de la categoria que no se haya usado ni empate con 'valorEvitar'.
    # ponytail: si la categoria tuviera muchos valores repetidos podria quedar en loop;
    # el dato actual tiene valores distintos por categoria.
    cant = contarOpcionesDe(nroCategoria)
    opcion = Opcion()
    repetida = True
    while repetida:
        k = random.randint(1, cant)
        opcion = leerOpcionKDe(nroCategoria, k)
        repetida = (
            yaUsado(usados, cantUsados, opcion.NroOpcion) or opcion.valor == valorEvitar
        )
    return opcion


def juegoMayorMenor():
    # Juego del menor-mayor: apuesta, 6 rondas de aciertos y actualiza al jugador (opcion A).
    """
    VARIABLES LOCALES
        mm_nombre:str (nombre ingresado por el jugador)
        mm_pos:int (posicion del jugador en jugadores.dat)
        mm_reg:Jugador (registro del jugador: creditos y matriz de juegos)
        mm_puede_jugar:bool (False si no tiene creditos para apostar)
        mm_apuesta:int (creditos apostados en la partida)
        mm_apuesta_valida:bool (control del ciclo de apuesta)
        mm_entrada:str (apuesta ingresada por teclado)
        mm_nro:int (numero de la categoria elegida)
        mm_cat:Categoria (categoria elegida, para mostrar su pregunta)
        mm_usados:[int]*8 (arreglo fijo con los NroOpcion ya sorteados)
        mm_cant_usados:int (cuantos NroOpcion hay en mm_usados)
        mm_op_uno:Opcion (opcion que se muestra como 1)
        mm_op_dos:Opcion (opcion que se muestra como 2)
        mm_op_correcta:Opcion (opcion de mayor valor, pasa de ronda)
        mm_opcion:str (1 o 2, eleccion de la ronda)
        mm_eligio_correcta:bool (True si eligio la opcion de mayor valor)
        mm_puntos:int (aciertos acumulados)
        mm_ronda:int (ronda actual, 1..6)
        mm_gano:bool (True si acerto 4 o mas)
    """
    global arLoCategorias
    global arLoOpciones
    global arLoJugadores

    print("\n================================================\n")
    print("    ♠  BIENVENIDOS AL JUEGO DEL MENOR-MAYOR  ♠")
    print("\n================================================\n")

    mm_nombre = input("Escribí tu nombre: ")
    mm_nombre = validarNombre(mm_nombre)
    mm_pos = buscarJugador(mm_nombre)
    if mm_pos == -1:
        crearJugador(mm_nombre)
        mm_pos = buscarJugador(mm_nombre)
    mm_reg = leerJugadorEnPosicion(mm_pos)

    mm_puede_jugar = True
    mm_apuesta = 0
    if mm_reg.Creditos < 1:
        print(f"\n  ✗ {mm_nombre}, no tenés créditos para apostar.")
        input("  Presione la tecla 'Enter' para continuar...")
        mm_puede_jugar = False
    else:
        print(f"\n  Créditos disponibles: ${int(mm_reg.Creditos)}")
        mm_apuesta_valida = False
        while not mm_apuesta_valida:
            mm_entrada = input("  Ingresá el monto de la apuesta: $").strip()
            if not esNumero(mm_entrada):
                print("  ✗ La apuesta debe ser un número entero.")
            elif validarIngresoEntero(mm_entrada, 1, int(mm_reg.Creditos)):
                mm_apuesta = int(mm_entrada)
                mm_apuesta_valida = True

    if mm_puede_jugar:
        listarCategorias(True)
        mm_nro = pedirCategoriaActiva("Ingresar el número de categoría: ")
        while contarOpcionesDe(mm_nro) < MIN_OPCIONES_PARTIDA:
            print(
                f"  ✗ Esa categoría no tiene opciones suficientes (mínimo {MIN_OPCIONES_PARTIDA})."
            )
            mm_nro = pedirCategoriaActiva("Ingresar el número de categoría: ")
        mm_cat = leerCategoria(mm_nro)
        print("\n  Pregunta:", mm_cat.Pregunta.rstrip())

        mm_usados = [0] * 8
        mm_cant_usados = 0
        mm_op_uno = sortearOpcionNoUsada(mm_nro, mm_usados, mm_cant_usados, None)
        mm_usados[mm_cant_usados] = mm_op_uno.NroOpcion
        mm_cant_usados = mm_cant_usados + 1
        mm_op_dos = sortearOpcionNoUsada(
            mm_nro, mm_usados, mm_cant_usados, mm_op_uno.valor
        )
        mm_usados[mm_cant_usados] = mm_op_dos.NroOpcion
        mm_cant_usados = mm_cant_usados + 1

        mm_puntos = 0
        mm_ronda = 1
        while mm_ronda <= 6:
            # Orden de presentacion aleatorio (si no, la opcion correcta quedaria siempre primera)
            if random.randint(0, 1) == 0:
                mm_op_uno, mm_op_dos = mm_op_dos, mm_op_uno
            print("\n----------------------------------------")
            print(f"  Ronda {mm_ronda} de 6   |   Puntos: {mm_puntos}")
            print("----------------------------------------")
            print(f"  1. {mm_op_uno.objeto.rstrip()}")
            print(f"  2. {mm_op_dos.objeto.rstrip()}")
            mm_opcion = input("  ¿Cuál tiene mayor valor? (1/2): ").strip()
            while mm_opcion != "1" and mm_opcion != "2":
                print("  ✗ Ingresá 1 o 2.")
                mm_opcion = input("  ¿Cuál tiene mayor valor? (1/2): ").strip()

            if mm_op_uno.valor > mm_op_dos.valor:
                mm_op_correcta = mm_op_uno
                mm_eligio_correcta = mm_opcion == "1"
            else:
                mm_op_correcta = mm_op_dos
                mm_eligio_correcta = mm_opcion == "2"

            print(
                f"\n  {mm_op_uno.objeto.rstrip()} {mm_op_uno.valor} / "
                f"{mm_op_dos.objeto.rstrip()} {mm_op_dos.valor}"
            )
            if mm_eligio_correcta:
                mm_puntos = mm_puntos + 1
                print("  ✓ ¡Acertaste!")
            else:
                print("  ✗ Incorrecto.")
            input("  Presione la tecla 'Enter' para continuar...")

            mm_ronda = mm_ronda + 1
            if mm_ronda <= 6:
                mm_op_uno = mm_op_correcta
                mm_op_dos = sortearOpcionNoUsada(
                    mm_nro, mm_usados, mm_cant_usados, mm_op_correcta.valor
                )
                mm_usados[mm_cant_usados] = mm_op_dos.NroOpcion
                mm_cant_usados = mm_cant_usados + 1

        mm_gano = mm_puntos >= 4
        if mm_gano:
            mm_reg.Creditos = mm_reg.Creditos + mm_apuesta
            mm_reg.juegos[0][0] = mm_reg.juegos[0][0] + 1
        else:
            mm_reg.Creditos = mm_reg.Creditos - mm_apuesta
            mm_reg.juegos[1][0] = mm_reg.juegos[1][0] + 1
        actualizarJugador(mm_pos, mm_reg)

        print("\n================================================")
        print("           ♠  G A M E  O V E R  ♠")
        print(f"  Jugador: {mm_nombre}")
        print(f"  Puntos:  {mm_puntos} de 6")
        if mm_gano:
            print("  Resultado: GANASTE ✓")
        else:
            print("  Resultado: PERDISTE ✗")
        print(f"  Créditos: ${int(mm_reg.Creditos)}")
        print("================================================")
        input("\nPresione la tecla 'Enter' para continuar...")


# ---------------------------------------------------------------
# JUEGO 2: NUMERO SECRETO
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# JUEGO 3: BLACKJACK
# ---------------------------------------------------------------
def bj_sacar_carta(bj_cartas_usadas):
    bj_id_carta = random.randint(0, 51)

    while bj_cartas_usadas[bj_id_carta]:
        bj_id_carta = random.randint(0, 51)

    bj_cartas_usadas[bj_id_carta] = True

    return bj_id_carta

def bj_calcular_puntos(bj_cartas, bj_cantidad_cartas):
    bj_puntos = 0
    bj_ases = 0
    bj_indice = 0

    while bj_indice < bj_cantidad_cartas:
        bj_rango = bj_cartas[bj_indice] % 13

        if bj_rango == 12:
            bj_puntos = bj_puntos + 11
            bj_ases = bj_ases + 1
        elif bj_rango >= 9:
            bj_puntos = bj_puntos + 10
        else:
            bj_puntos = bj_puntos + bj_rango + 2

        bj_indice = bj_indice + 1

    while bj_puntos > 21 and bj_ases > 0:
        bj_puntos = bj_puntos - 10
        bj_ases = bj_ases - 1

    return bj_puntos

def juego_blackjack():
    """
    VARIABLES LOCALES
        BJ_PALOS:list (arreglo con los cuatro palos de la baraja inglesa)
        BJ_RANGOS:list (arreglo con los trece rangos de las cartas)
        bj_nombre_jugador:str (nombre ingresado por el jugador)
        bj_indice_jugador:int (posición del jugador en los arreglos de Blackjack)
        bj_jugar_otra:str (respuesta S o N para iniciar otra partida)
        bj_mazo:list (arreglo fijo que representa las 52 cartas del mazo)
        bj_indice_mazo:int (posición utilizada para cargar las cartas en el mazo)
        bj_indice_palo:int (posición utilizada para recorrer los palos)
        bj_indice_rango:int (posición utilizada para recorrer los rangos)
        bj_indice_carta:int (posición de la próxima carta que se extrae del mazo)
        bj_cartas_jugador:list (arreglo fijo con las cartas de la mano del jugador)
        bj_cartas_banca:list (arreglo fijo con las cartas de la mano de la banca)
        bj_cantidad_cartas_jugador:int (cantidad de cartas ocupadas en la mano del jugador)
        bj_cantidad_cartas_banca:int (cantidad de cartas ocupadas en la mano de la banca)
        bj_puntos_jugador:int (puntuación total de la mano del jugador)
        bj_puntos_banca:int (puntuación total de la mano de la banca)
        bj_indice:int (posición utilizada para recorrer las manos de cartas)
        bj_carta:list (carta actual mostrada durante el recorrido de una mano)
        bj_carta_nueva:list (última carta entregada al jugador o a la banca)
        bj_partida_inicial_finalizada:bool (indica si la partida terminó con el reparto inicial)
        bj_turno_activo:bool (indica si el jugador continúa tomando decisiones)
        bj_opcion:str (elección del jugador: pedir o plantarse)
        bj_banca_blackjack:bool (indica si la banca tiene Blackjack natural)
        bj_jugador_blackjack:bool (indica si el jugador tiene Blackjack natural)
        bj_nombre_valido:int (indica si el nombre ingresado no esta vacio)
        bj_salir:int (indica si se debe salir de la funcion sin jugar)
        bj_i:int (posicion para el barajado Fisher-Yates)
        bj_j:int (posicion aleatoria para intercambio en Fisher-Yates)
        bj_aux:list (variable temporal para intercambiar dos cartas)
    """

    BJ_PALOS = ["♠", "♥", "♦", "♣"]
    BJ_RANGOS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    print("\n================================================\n")
    print("       ♠  BLACKJACK - EL 21  ♠")
    print("  El objetivo es sumar 21 sin pasarte\n")
    print("================================================\n")

    bj_nombre_jugador = input("Escribí tu nombre: ")
    bj_nombre_jugador = validarNombre(bj_nombre_jugador)

    bj_pos = buscarJugador(bj_nombre_jugador)

    if bj_pos == -1:
        crearJugador(bj_nombre_jugador)
        bj_pos = buscarJugador(bj_nombre_jugador)

    bj_reg = leerJugadorEnPosicion(bj_pos)
    bj_nombre_jugador = bj_reg.nombre.strip()

    print(f"\n| Bienvenido, {bj_nombre_jugador} ♠          |")

    bj_jugar_otra = "S"
    while bj_jugar_otra == "S":
        bj_cartas_usadas = [False] * 52

        bj_cartas_jugador = [0] * 11
        bj_cartas_banca = [0] * 11

        bj_cantidad_cartas_jugador = 0
        bj_cantidad_cartas_banca = 0

        bj_puntos_jugador = 0
        bj_puntos_banca = 0

        print("\n================================================")
        print("          NUEVA PARTIDA")
        print("================================================\n")

        bj_cartas_jugador[bj_cantidad_cartas_jugador] = bj_sacar_carta(bj_cartas_usadas)
        bj_cantidad_cartas_jugador = bj_cantidad_cartas_jugador + 1

        bj_cartas_banca[bj_cantidad_cartas_banca] = bj_sacar_carta(bj_cartas_usadas)
        bj_cantidad_cartas_banca = bj_cantidad_cartas_banca + 1

        bj_cartas_jugador[bj_cantidad_cartas_jugador] = bj_sacar_carta(bj_cartas_usadas)
        bj_cantidad_cartas_jugador = bj_cantidad_cartas_jugador + 1

        bj_cartas_banca[bj_cantidad_cartas_banca] = bj_sacar_carta(bj_cartas_usadas)
        bj_cantidad_cartas_banca = bj_cantidad_cartas_banca + 1

        print("  Cartas de la Banca:")
        bj_indice = 0

        while bj_indice < bj_cantidad_cartas_banca:
            bj_carta = bj_cartas_banca[bj_indice]
            print(f"    [{bj_carta[0]}{bj_carta[1]}]")
            bj_indice = bj_indice + 1

        print("\n  Cartas de", bj_nombre_jugador + ":")
        bj_indice = 0

        while bj_indice < bj_cantidad_cartas_jugador:
            bj_carta = bj_cartas_jugador[bj_indice]
            print(f"    [{bj_carta[0]}{bj_carta[1]}]")
            bj_indice = bj_indice + 1
        bj_puntos_jugador = bj_calcular_puntos(
            bj_cartas_jugador, bj_cantidad_cartas_jugador
        )
        print(f"\n  Tu puntuación: {bj_puntos_jugador}")

        if bj_puntos_jugador == 21:
            print("  ♠ ¡BLACKJACK! Sumaste 21 con las dos cartas.")
            bj_puntos_banca = bj_calcular_puntos(
                bj_cartas_banca, bj_cantidad_cartas_banca
            )
            print(f"\n  Puntuación Banca: {bj_puntos_banca}")
            if bj_puntos_banca != 21:
                print("\n  >>> ¡GANASTE! <<<")
                bj_ganadas[bj_indice_jugador] = bj_ganadas[bj_indice_jugador] + 1
            else:
                print("\n  >>> EMPATE (ambos con Blackjack) <<<")
                bj_empatadas[bj_indice_jugador] = bj_empatadas[bj_indice_jugador] + 1
            bj_jugadas[bj_indice_jugador] = bj_jugadas[bj_indice_jugador] + 1
            print("\n----------------------------------------")
            print("  ESTADÍSTICAS DE BLACKJACK:")
            print(f"    Jugador: {bj_jugadores[bj_indice_jugador]}")
            print(f"    Partidas jugadas: {bj_jugadas[bj_indice_jugador]}")
            print(f"    Ganadas: {bj_ganadas[bj_indice_jugador]}")
            print(f"    Perdidas: {bj_perdidas[bj_indice_jugador]}")
            print(f"    Empatadas: {bj_empatadas[bj_indice_jugador]}")
            print("----------------------------------------")
            bj_jugar_otra = ""
            while bj_jugar_otra != "S" and bj_jugar_otra != "N":
                bj_jugar_otra = (
                    input("\n¿Querés jugar otra partida? (S/N): ").strip().upper()
                )
                if bj_jugar_otra != "S" and bj_jugar_otra != "N":
                    print("  ✗ Opción inválida. Ingresá S o N.")
            if bj_jugar_otra == "S":
                print("\n  ✓ Comenzando nueva partida...")
            else:
                print("\n  Volviendo al menú principal...")
            bj_partida_inicial_finalizada = True
        else:
            bj_partida_inicial_finalizada = False

        if bj_partida_inicial_finalizada == False:
            bj_turno_activo = True
            while bj_turno_activo:
                bj_opcion = ""
                while bj_opcion != "PEDIR" and bj_opcion != "PLANTARSE":
                    bj_opcion = (
                        input('\n  "Pedir" otra carta o "Plantarte": ').strip().upper()
                    )
                    if bj_opcion != "PEDIR" and bj_opcion != "PLANTARSE":
                        print('  ✗ Opción inválida. Escribí "Pedir" o "Plantarse".')

                if bj_opcion == "PEDIR":
                    bj_cartas_jugador[bj_cantidad_cartas_jugador] = bj_sacar_carta(
                        bj_cartas_usadas
                    )

                    bj_carta_nueva = bj_cartas_jugador[bj_cantidad_cartas_jugador]

                    bj_cantidad_cartas_jugador = bj_cantidad_cartas_jugador + 1

                    print(f"\n  Sacaste: [{bj_carta_nueva[0]}{bj_carta_nueva[1]}]")
                    print("  Tu mano:")
                    bj_indice = 0

                    while bj_indice < bj_cantidad_cartas_jugador:
                        bj_carta = bj_cartas_jugador[bj_indice]
                        print(f"    [{bj_carta[0]}{bj_carta[1]}]")
                        bj_indice = bj_indice + 1
                    bj_puntos_jugador = bj_calcular_puntos(
                        bj_cartas_jugador, bj_cantidad_cartas_jugador
                    )
                    print(f"\n  Tu puntuación: {bj_puntos_jugador}")

                    if bj_puntos_jugador > 21:
                        print("\n  ✗ ¡Te pasaste de 21! Perdiste automáticamente.")
                        bj_turno_activo = False
                    elif bj_puntos_jugador == 21:
                        print("\n  ♠ ¡Llegaste a 21! Pasás el turno a la banca.")
                        bj_turno_activo = False
                else:
                    print(f"\n  Te plantaste con {bj_puntos_jugador} puntos.")
                    bj_turno_activo = False

            if bj_puntos_jugador <= 21:
                print("\n----------------------------------------")
                print("  Turno de la Banca:")
                print("  Cartas de la Banca:")
                bj_indice = 0
                while bj_indice < bj_cantidad_cartas_banca:
                    bj_carta = bj_cartas_banca[bj_indice]
                    print(f"    [{bj_carta[0]}{bj_carta[1]}]")
                    bj_indice = bj_indice + 1
                bj_puntos_banca = bj_calcular_puntos(
                    bj_cartas_banca, bj_cantidad_cartas_banca
                )
                print(f"  Puntuación Banca: {bj_puntos_banca}")

                while bj_puntos_banca <= 16:
                    bj_cartas_banca[bj_cantidad_cartas_banca] = bj_sacar_carta(
                        bj_cartas_usadas
                    )

                    bj_carta_nueva = bj_cartas_banca[bj_cantidad_cartas_banca]

                    bj_cantidad_cartas_banca = bj_cantidad_cartas_banca + 1

                    print(
                        f"\n  La banca pide carta: [{bj_carta_nueva[0]}{bj_carta_nueva[1]}]"
                    )
                    bj_puntos_banca = bj_calcular_puntos(
                        bj_cartas_banca, bj_cantidad_cartas_banca
                    )
                    print(f"  Puntuación Banca: {bj_puntos_banca}")

                print("\n----------------------------------------")
                if bj_puntos_banca > 21:
                    print("\n  >>> ¡GANASTE! La banca se pasó de 21. <<<")
                    bj_ganadas[bj_indice_jugador] = bj_ganadas[bj_indice_jugador] + 1
                elif bj_puntos_jugador > bj_puntos_banca:
                    print(
                        f"\n  >>> ¡GANASTE! Vos: {bj_puntos_jugador} | Banca: {bj_puntos_banca} <<<"
                    )
                    bj_ganadas[bj_indice_jugador] = bj_ganadas[bj_indice_jugador] + 1
                elif bj_puntos_jugador < bj_puntos_banca:
                    print(
                        f"\n  >>> PERDISTE. Vos: {bj_puntos_jugador} | Banca: {bj_puntos_banca} <<<"
                    )
                    bj_perdidas[bj_indice_jugador] = bj_perdidas[bj_indice_jugador] + 1
                else:
                    # Empate a 21: si la banca tiene blackjack natural (2 cartas) y el jugador no, gana la banca
                    bj_banca_blackjack = (
                        bj_cantidad_cartas_banca == 2 and bj_puntos_banca == 21
                    )

                    bj_jugador_blackjack = (
                        bj_cantidad_cartas_jugador == 2 and bj_puntos_jugador == 21
                    )
                    if bj_banca_blackjack and not bj_jugador_blackjack:
                        print("\n  >>> PERDISTE. La banca tiene Blackjack natural. <<<")
                        bj_perdidas[bj_indice_jugador] = (
                            bj_perdidas[bj_indice_jugador] + 1
                        )
                    else:
                        print(
                            f"\n  >>> EMPATE. Ambos con {bj_puntos_jugador} puntos <<<"
                        )
                        bj_empatadas[bj_indice_jugador] = (
                            bj_empatadas[bj_indice_jugador] + 1
                        )
            else:
                bj_perdidas[bj_indice_jugador] = bj_perdidas[bj_indice_jugador] + 1
                bj_puntos_banca = bj_calcular_puntos(
                    bj_cartas_banca, bj_cantidad_cartas_banca
                )
                print(f"\n  Puntuación Banca (no necesitó jugar): {bj_puntos_banca}")

            bj_jugadas[bj_indice_jugador] = bj_jugadas[bj_indice_jugador] + 1
            print("\n----------------------------------------")
            print("  ESTADÍSTICAS DE BLACKJACK:")
            print(f"    Jugador: {bj_jugadores[bj_indice_jugador]}")
            print(f"    Partidas jugadas: {bj_jugadas[bj_indice_jugador]}")
            print(f"    Ganadas: {bj_ganadas[bj_indice_jugador]}")
            print(f"    Perdidas: {bj_perdidas[bj_indice_jugador]}")
            print(f"    Empatadas: {bj_empatadas[bj_indice_jugador]}")
            print("----------------------------------------")

            bj_jugar_otra = ""
            while bj_jugar_otra != "S" and bj_jugar_otra != "N":
                bj_jugar_otra = (
                    input("\n¿Querés jugar otra partida? (S/N): ").strip().upper()
                )
                if bj_jugar_otra != "S" and bj_jugar_otra != "N":
                    print("  ✗ Opción inválida. Ingresá S o N.")

            if bj_jugar_otra == "S":
                print("\n  ✓ Comenzando nueva partida...")
            else:
                print("\n================================================")
                print("|                                      |")
                print("|     ♠  G A M E  O V E R  ♠           |")
                print("|                                      |")
                print(f"|     Volviendo al menú principal...    |")
                print("|                                      |")
                print("================================================")

    input("\nPresione la tecla 'Enter' para continuar...")


# ---------------------------------------------------------------
# JUEGO 4: DADOS (PAR O IMPAR)
# ---------------------------------------------------------------


def enConstruccion():
    # Stub para los juegos y el reporte que todavia no estan implementados.
    print("Función en construcción, vuelva pronto")
    input("Presione Enter para continuar...")


# ---------------------------------------------------------------
# ABRIR Y CERRAR ARCHIVOS
# ---------------------------------------------------------------
def abrirUno(ruta):
    # Abre (o crea) un archivo binario y devuelve su handle.
    if os.path.exists(ruta):
        handle = open(ruta, "r+b")
    else:
        print("El archivo " + ruta + " NO existía y fue creado")
        handle = open(ruta, "w+b")
    return handle


def abrirArchivos():
    # Abre los 3 archivos del sistema y guarda sus handles en variables globales.
    global arLoCategorias
    global arLoOpciones
    global arLoJugadores
    arLoCategorias = abrirUno(RUTA_CATEGORIAS)
    arLoOpciones = abrirUno(RUTA_OPCIONES)
    arLoJugadores = abrirUno(RUTA_JUGADORES)


def cerrarArchivos():
    # Cierra los 3 archivos del sistema.
    global arLoCategorias
    global arLoOpciones
    global arLoJugadores
    arLoCategorias.close()
    arLoOpciones.close()
    arLoJugadores.close()


# ---------------------------------------------------------------
# CARGA INICIAL (minimo para la entrega, sin listas)
# ---------------------------------------------------------------
def cargarCategoriasIniciales():
    # Carga 3 categorias de ejemplo (solo si categorias.dat esta vacio).
    grabarCategoria(1, "Edad Famosos", "¿Quién tiene más años?")
    grabarCategoria(2, "Dinero Famosos", "¿Qué famoso es más rico?")
    grabarCategoria(3, "Países", "¿Qué país tiene más habitantes?")
    print("Se cargaron 3 categorías iniciales")


def cargarOpcionesIniciales():
    # Carga 9 opciones de ejemplo (3 por categoria; solo si opciones.dat esta vacio).
    grabarOpcion(1, "Tom Cruise", 62)
    grabarOpcion(1, "Lionel Messi", 37)
    grabarOpcion(1, "Cristiano Ronaldo", 39)
    grabarOpcion(2, "Lionel Messi", 600)
    grabarOpcion(2, "Cristiano Ronaldo", 800)
    grabarOpcion(2, "Elon Musk", 400000)
    grabarOpcion(3, "Argentina", 46000000)
    grabarOpcion(3, "Brasil", 215000000)
    grabarOpcion(3, "China", 1400000000)
    print("Se cargaron 9 opciones iniciales")


# ---------------------------------------------------------------
# MENU'S
# ---------------------------------------------------------------
def mostrar_menu():
    # Limpia la pantalla y muestra el menu principal (a-g, enunciado).
    os.system("cls" if os.name == "nt" else "clear")
    print("\n........MENU PRINCIPAL.")
    print("A - Mayor o Menor")
    print("B - Numero Secreto")
    print("C - BlackJack Simple")
    print("D - Dados (Par o Impar)")
    print("E - Reporte")
    print("F - Administracion de Juegos")
    print("G - Salir del programa")


def mostrarMenuReporte():
    # Limpia la pantalla y muestra el submenu de reporte (enunciado §E).
    os.system("cls" if os.name == "nt" else "clear")
    print("a - Jugadores ordenados de mayor a menor por creditos")
    print("b - Juegos jugados por un jugador")
    print("c - Volver")


def menuReporte():
    # Submenu iterativo de reporte: a) por creditos / b) por jugador / c) volver.
    termino = False
    while not termino:
        mostrarMenuReporte()
        opcion = input("Ingrese opcion deseada: ").strip().lower()
        while len(opcion) != 1 or opcion < "a" or opcion > "c":
            opcion = input("Ingrese opcion deseada: ").strip().lower()
        if opcion == "a":
            ordenarJugadoresPorCreditos()
        if opcion == "b":
            nombre = input("Ingrese el nombre del jugador: ")
            reportePartidasJugador(nombre)
        if opcion == "c":
            termino = True


def ejecutar_case(o):
    # Despacha la opcion elegida a la funcion correspondiente.
    if o == "A":
        juegoMayorMenor()
    if o == "B":
        enConstruccion()
    if o == "C":
        enConstruccion()
    if o == "D":
        enConstruccion()
    if o == "E":
        menuReporte()
    if o == "F":
        menuAdmin()
    if o == "G":
        salir()


def salir():
    # Muestra el cartel final del enunciado (§G) y cierra el programa.
    os.system("cls" if os.name == "nt" else "clear")
    print("\n\nGracias por jugar, no apueste y juega por diversión! Hasta la próxima!")
    input("\nPresione la tecla 'Enter' para salir...")
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    # Bucle principal del menu hasta que el usuario elige salir (G).
    mostrar_menu()
    opcion = input("Ingrese opcion deseada: ").strip().upper()
    while opcion not in ["A", "B", "C", "D", "E", "F", "G"]:
        opcion = input("Ingrese opcion deseada: ").strip().upper()
    ejecutar_case(opcion)
    while opcion != "G":
        mostrar_menu()
        opcion = input("Ingrese opcion deseada: ").strip().upper()
        while opcion not in ["A", "B", "C", "D", "E", "F", "G"]:
            opcion = input("Ingrese opcion deseada: ").strip().upper()
        ejecutar_case(opcion)


def mostrar_advertencia():
    # Muestra el cartel inicial de advertencia sobre los juegos de apuesta.
    os.system("cls" if os.name == "nt" else "clear")
    cartel = """
    █████████████████████████████████████████████████████████████████
    █                                                               █
    █                          ¡ATENCIÓN!                           █
    █                                                               █
    █            LOS JUEGOS DE APUESTA ESTÁN PROHIBIDOS             █
    █             PARA MENORES Y SU ABUSO ES ALTAMENTE              █
    █                  PERJUDICIAL PARA LA SALUD.                   █
    █                                                               █
    █████████████████████████████████████████████████████████████████
    """
    print(cartel)
    input("\nPresione la tecla 'Enter' para continuar...")
    os.system("cls" if os.name == "nt" else "clear")


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------
# Declaracion de variables globales
global arLoCategorias
global arLoOpciones
global arLoJugadores

mostrar_advertencia()
abrirArchivos()
if os.path.getsize(RUTA_CATEGORIAS) == 0:
    cargarCategoriasIniciales()
if os.path.getsize(RUTA_OPCIONES) == 0:
    cargarOpcionesIniciales()
menu()
cerrarArchivos()


# Faltan 3 juegos
# Mayor menor if ff gano capaz podemos hacer una funcion para eso
