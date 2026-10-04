import random
import os


class Categoria:
    def __init__(self):
        self.nroCategoria = 0
        self.nombreCategoria ="" #hasta 30 caracteres
        self.pregunta ="" #hasta 200 caracteres
        self.estado =""#A-I Activo, I Inactivo

class Opcion:
    def __init__(self):
        self.nroCategoria = 0
        self.nroOpcion =0
        self.objeto =""
        self.mail =""

class Jugador:
    def __init__(self):
        self.nombre = "" #hasta 50 caracteres
        self.Creditos = 10000,0
        self.juegos= [],[]

def buscarJugador(name):
    print("Jugador ya existe en la posicion 1")
    return -1


def crearJugador(name):
    global arFiJugadores, arLoJugadores
    jug = Jugador()
    jug.nombre = nom.ljust(30, " ") 
    jug.creditos = 10000.0 
    jug.juegos = [ \* 4 for \_ in range(2)] # Matriz 2x4 inicializada en 0
    arLoJugadores.seek(0, 2) # Se posiciona al final del archivo 
    pickle.dump(jug, arLoJugadores) 
    arLoJugadores.flush()


    print("Jugador creado " ,name)


def actualizarJugador(pos, regJugador):
    pass

def ordenarJugadoresPorCreditos():
    pass

def reportePartidasJugador(nombre):
    pass

def juegoMayorMenor():
    nombre = input("Ingrese nombre del Jugador: ")
    posicion = buscarJugador(nombre)
    if posicion == -1:
        crearJugador(nombre)
        posicion = 1 ## Cual es la posicion de un jugador recien creado?

    print("El jugador ", nombre, " esta en la posicion ", posicion)





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



def mostrar_menu():
    #os.system("cls" if os.name == "nt" else "clear")
    print("\n........MENU PRINCIPAL.")
    print("A - Mayor o Menor")
    print("B - Numero Secreto")
    print("C - BlackJack Simple")
    print("D - Dados (Par o Impar)")
    print("E - Reporte")
    print("F - Fin del programa")

def ejecutar_case(o):
    if o == "A":
        juegoMayorMenor()
    if o == "B":
        juego_numero_secreto()

    if o == "C":
        juego_blackjack()

    if o == "D":
        juego_par_o_impar()

    if o == "E":
        reporte()

    if o == "F":
        salir()

def salir():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n\nGracias por jugar, no apueste y juega por diversión! Hasta la próxima!')
    input("\nPresione la tecla 'Enter' para salir...")
    os.system('cls' if os.name == 'nt' else 'clear')
    salir_programa = 1
## REVISAR procedimiento Salir!!!!!!!!!



def menu():
    mostrar_menu()
    opcion = input("Ingrese opcion deseada: ").strip().upper()
    while opcion not in ["A", "B", "C", "D", "E", "F"]:
        opcion = input("Ingrese opcion deseada: ").strip().upper()
    ejecutar_case(opcion)
    while opcion != "F":
        mostrar_menu()
        opcion = input("Ingrese opcion deseada: ").strip().upper()
        while opcion not in ["A", "B", "C", "D", "E", "F"]:
                opcion = input("Ingrese opcion deseada: ").strip().upper()
        ejecutar_case(opcion)
    

    
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
menu()
cerrarArchivos()