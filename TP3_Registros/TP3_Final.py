class Categorias:
    def __init__(self):
        self.nroCategoria = 0
        self.nombreCategoria ="" #hasta 30 caracteres
        self.pregunta ="" #hasta 200 caracteres
        self.estado =""#A-I Activo, I Inactivo

class Opciones:
    def __init__(self):
        self.nroCategoria = 0
        self.nroOpcion =0
        self.objeto =""
        self.mail =""

class Jugadores:
    def __init__(self):
        self.nombre = "" #hasta 50 caracteres
        self.Creditos =0
        self.juegos= [],[]

def abrirArchivos():
#Verifico si el archivo existe, si no existe lo creo
    def abrirArchivoCategoria():
        global arFiCategorias
        global arLoCategorias
        arFiCategorias = "Categorias.dat"
        if os.path.exists(arFiCategorias):
            arLoCategorias = open(arFiCategorias, "r+b")
        else:
            print (f"El archivo {arFiCategorias} No existía y fue creado")
            arLoCategorias = open(arFiCategorias, "w+b")
        input()

    def abrirArchivoOpciones():
        global arFiOpciones
        global arLoOpciones
        arFiOpciones = "Opciones.dat"
        if os.path.exists(arFiOpciones):
            arLoOpciones = open(arFiOpciones, "r+b")
        else:
            print (f"El archivo {arFiOpciones} No existía y fue creado")
            arLoOpciones = open(arFiOpciones, "w+b")
        input()

    def abrirArchivoJugadores():
        global arFiJugadores
        global arLoJugadores
        arFiJugadores = "Jugadores.dat"
        if os.path.exists(arFiJugadores):
            arLoJugadores = open(arFiJugadores, "r+b")
        else:
            print (f"El archivo {arFiJugadores} No existía y fue creado")
            arLoJugadores = open(arFiJugadores, "w+b")
        input()

def cerrarArchivos():
    global arLoCategorias
    global arLoOpciones
    global arLoJugadores
    arLoCategorias.close()
    arLoOpciones.close()
    arLoJugadores.close()

def menuPrincipal():
    
def mostrar_advertencia():
    """
    VARIABLES LOCALES
        cartel:str (texto multilínea que contiene la advertencia inicial)
    """
    os.system('cls' if os.name == 'nt' else 'clear')
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
    os.system('cls' if os.name == 'nt' else 'clear')

#Declaracion de variables globales
global arFiCategorias
global arLoCategorias
global arFiOpciones
global arLoOpciones
global arFiJugadores
global arLoJugadores

mostrar_advertencia()
abrirArchivos()
menuPrincipal()
cerrarArchivos()