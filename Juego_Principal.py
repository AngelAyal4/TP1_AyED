import random
import sys
import os


"""
VARIABLES GLOBALES (para el reporte. Declarar en el archivo principal)
    nombre:str (nombre del último jugador del juego B)
    b_veces_jugado:int (cantidad total de partidas jugadas)
    b_veces_ganado:int (cantidad de partidas ganadas)
    b_veces_perdido:int (cantidad de partidas perdidas)
"""

nombre = ''
racha = 0
a = 0
nreferencia = 0
ncomparar = 0
opcion = ''

def juego_mayor_menor():
    
    global nombre, racha, a, nreferencia, ncomparar, opcion
    
    racha = 0
    a = 0
    nombre = input("Cual es tu nombre? ")
    # Este sera nuestro numero de referencia
    nreferencia = random.randint(1, 1000)
    # Este while funcionara mientras no cometamos errores al adivinar mayor o menor
    while a == 0:
        print(nreferencia)
        # Este es el numero con el cual compararemos el de referencia
        ncomparar = random.randint(1, 1000)
        # En este while nos aseguramos de que el numero de que nreferencia y ncomparar nunca sean iguales. Así evitamos que el usuario pierda injustamente por falta de una opcion valida.
        while ncomparar == nreferencia:
            ncomparar = random.randint(1, 1000)
        # El siguiente comentario sirve para probar el programa, este nos muestra la respuesta correcta.
        # print("Pista!!  ", ncomparar)
        opcion = input("Mayor o menor? ").lower()
        # Con este while validamos el input del usuario.
        while opcion != "mayor" and opcion != "menor":
            opcion = input("Incorrecto, por favor indique, mayor o menor? ").lower()
        # Analizamos si la opcion del usuario fue correcta o incorrecta. Sumamos al contador si este acerto, cerramos el while cambiando el valor de a si se equivocó.
        if opcion == "mayor":
            if nreferencia < ncomparar:
                racha = racha + 1
                nreferencia = ncomparar
            else:
                a = 1
        else:
            if nreferencia > ncomparar:
                racha = racha + 1
                nreferencia = ncomparar
            else:
                a = 1

    print("Game Over", nombre)
    print("Aciertos:", racha)

"""
VARIABLES GLOBALES (para el reporte. Declarar en el archivo principal)
    b_nombre_jugador:str (nombre del último jugador del juego B)
    b_veces_jugado:int (cantidad total de partidas jugadas)
    b_veces_ganado:int (cantidad de partidas ganadas)
    b_veces_perdido:int (cantidad de partidas perdidas)
"""

#INICIALIZO VARIABLES GLOBALES
b_nombre_jugador = ""
b_veces_jugado = 0
b_veces_ganado = 0
b_veces_perdido = 0


def juego_numero_secreto():
    """
    VARIABLES LOCALES 
        MAX_INTENTOS:int (cantidad máxima de intentos permitidos)
        RANGO_MIN:int (límite inferior del número secreto)
        RANGO_MAX:int (límite superior del número secreto)
        nombre_jugador:str (nombre ingresado por el jugador)
        numero_secreto:int (número aleatorio generado por el programa)
        intento_actual:int (número ingresado por el jugador en cada turno)
        intentos_usados:int (contador de intentos realizados)
        adivino:bool (True si el jugador acertó el número)
        entrada_texto:str (entrada cruda del usuario antes de validar)
        entrada_valida:bool (True cuando la entrada pasa todas las validaciones)
        es_numero:bool (True si todos los caracteres del texto son dígitos)
        indice:int (posición actual al recorrer la cadena de entrada)
        caracter:str (carácter individual analizado en la validación)
        intentos_restantes:int (intentos que le quedan al jugador en cada turno)
    """
    global b_nombre_jugador, b_veces_jugado, b_veces_ganado, b_veces_perdido

    #CONSTANTES
    MAX_INTENTOS = 6
    RANGO_MAX = 100
    RANGO_MIN = 1

    #INICIALIZACIÓN DE VARIABLES LOCALES
    nombre_jugador = ""
    numero_secreto = 0
    intento_actual = 0
    intentos_usados = 0
    adivino = False
    entrada_texto = ""
    entrada_valida = False
    es_numero = False
    indice = 0
    caracter = ""
    intentos_restantes = 0

    #PANTALLA DE BIENVENIDA
    print("Bienvenido al juego B Número secreto. Tenes 6 intentos para adivinar")

    #INGRESO NOMBRE DEL USUARIO
    nombre_jugador = input("Ingresá tu nombre: ")
    while nombre_jugador == "":
        print("Por favor ingresá tu nombre")
        nombre_jugador = input("Ingresá tu nombre")

    #GENERAR NÚMERO SECRETO
    numero_secreto = random.randint(RANGO_MIN, RANGO_MAX)
    intentos_usados = 0
    adivino = False
    print(f"{nombre_jugador}, pensé un número del {RANGO_MIN} al {RANGO_MAX}")

    #BUCLE PRINCIPAL DEL JUEGO
    while intentos_usados < MAX_INTENTOS and not adivino:
        intentos_restantes = MAX_INTENTOS - intentos_usados
        print(f"Te quedan {intentos_restantes} intento(s)")

        #VALIDACIÓN DEL NUMERO INGRESADO
        entrada_valida = False
        while not entrada_valida:
            entrada_texto = input("Ingresá tu número:")
            #VERIFICO QUE TODOS LOS CARACTERES SEAN DIGITOS
            es_numero = len(entrada_texto) > 0
            indice = 0
            while indice < len(entrada_texto):
                caracter = entrada_texto[indice]
                if caracter < "0" or caracter > "9":
                    es_numero = False
                indice = indice + 1

            if not es_numero:
                print("Ingresá solo números enteros positivos")
            else:
                intento_actual = int(entrada_texto)
                if intento_actual < RANGO_MIN or intento_actual > RANGO_MAX:
                    print(f"El número debe estar entre {RANGO_MIN} y {RANGO_MAX}")
                else:
                    entrada_valida = True

        #EVALUAR EL INTENTO
        if intento_actual == numero_secreto:
            adivino = True
        elif intento_actual < numero_secreto:
            print("El número secreto es mayor. Intentá de nuevo")
        else:
            print("El número secreto es menor. Intentá de nuevo")

        intentos_usados = intentos_usados + 1
        print()

    #RESULTADO FINAL
    if adivino:
        print(f"Felicitaciones {nombre_jugador}. Adivinaste el número secreto {numero_secreto} en {intentos_usados} intento(s)")
        b_veces_ganado = b_veces_ganado + 1
    else:
        print(f"Se acabaron los intentos {nombre_jugador}. El número secreto era: {numero_secreto}")
        b_veces_perdido = b_veces_perdido + 1

    #ACTUALIZACIÓN ESTADISTICAS
    b_nombre_jugador = nombre_jugador
    b_veces_jugado = b_veces_jugado + 1
    input("Presioná Enter para volver al menú")


def juego_blackjack():
        print("Juego en construcción...")
        input("\nPresione la tecla 'Enter' para continuar...")
        #os.system('cls' if os.name == 'nt' else 'clear')
    

nombreJugadorDados = ''
vecesJugadoDados = 0
vecesGanadoDados = 0
vecesPerdidoDados = 0
    
def juegoDados():
    # ─────────────────────────────────────
    # Nombre del módulo: Juego Dados
    # Variables:
    #   juegoActivo : bool
    #   tipoDeApuesta: str
    #   opcionUsuario : str
    #   dado1: int
    #   dado2: int
    #   sumaDados: int
    #   nombreJugador: str
    #   paridad = str
    #---Variables globales reporte---
    #   vecesJugadoDados: int
    #   vecesGanadoDados: int
    #   vecesPerdidoDados: int
    # ─────────────────────────────────────

    global nombreJugadorDados
    global vecesJugadoDados
    global vecesGanadoDados
    global vecesPerdidoDados
    juegoActivo = True

    print("\n================================================\n")
    print ("  ♠ Juego: Dados ♠")
    print ("  Adiviná si la suma de los dados será par o impar\n")
    print("================================================\n")
    vecesJugadoDados = vecesJugadoDados + 1
    nombreJugadorDados = input("Escribe tu nombre: ")
    while nombreJugadorDados == "":
        print("\n  ✗ Nombre vacío: Por favor escribe tu nombre\n")
        nombreJugadorDados = input("Escribe tu nombre: ")
    print(f"\n| Bienvenido, {nombreJugadorDados} ♠          |")
    while juegoActivo:
        tipoDeApuesta = input("\nApuestas por: 1) Par | 2) Impar\n> ")
        while tipoDeApuesta != "1" and tipoDeApuesta != "2":
            print("\n  ✗ Opción inválida. Ingresá 1 para Par o 2 para Impar.\n")
            tipoDeApuesta = input("\nApuestas por: 1) Par | 2) Impar\n> ")
        if tipoDeApuesta == "1":
            print("\nApostaste por Par ✓\n")
        else:
            print("\nApostaste por Impar ✓\n")
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        sumaDados = dado1 + dado2
        if sumaDados % 2 == 0:
            paridad = "Par"
        else:
            paridad = "Impar"
        print("  ~ Tirando dados ⚀⚁⚂⚃⚄⚅ ~")
        print("  ─────────────────")
        if paridad == "Par":
            print(f"  Resultado: {sumaDados}  →  PAR ♠")
        else: 
            print(f"  Resultado: {sumaDados}  →  IMPAR ♠")
        print("  ─────────────────")
        if (paridad == "Par" and tipoDeApuesta == "1") or (paridad == "Impar" and tipoDeApuesta == "2"):
            vecesGanadoDados = vecesGanadoDados + 1
            print(f"Ganaste ✓\n")
        else:
            vecesPerdidoDados = vecesPerdidoDados + 1
            print(f"\nPerdiste ✗\n")
        print("\n|----------------------------|+")
        print(f"\n|      Ganados: {vecesGanadoDados}")
        print(f"\n|      Perdidos: {vecesPerdidoDados}")
        print("\n|----------------------------+|")
        opcionUsuario = (input("\nElige una opción: 1) Seguir jugando 2) Salir \n> "))
        while opcionUsuario != "1" and opcionUsuario != "2":
            print("\n✗ Opción inválida. Presiona tecla 1 para jugar o tecla 2 para salir.\n")
            opcionUsuario = (input("\nElige una opción: 1) Seguir jugando 2) Salir \n> "))
        if opcionUsuario == "2":
            print("+----------------------------+")
            print("|                            |")
            print("|   ♠  G A M E  O V E R  ♠   |")
            print("|                            |")
            print("+----------------------------+")
            juegoActivo = False
            print("\nSaliendo al menú principal...")
            
    


def reporte():
    print('\n--- REPORTE DEL JUGADOR ---')
    if nombre != '':
        print('Mayor o Menor - Nombre:', nombre, '- Racha:', racha)
    if b_nombre_jugador != '':
        print('Número Secreto - Nombre:', b_nombre_jugador, '- Veces jugado:', b_veces_jugado, '- Ganadas:', b_veces_ganado, '- Perdidas:', b_veces_perdido)
    if nombreJugadorDados != '':
        print('\nDados (Par o Impar) - Nombre:', nombreJugadorDados, '- Veces jugadas:', vecesJugadoDados, '- Ganadas:', vecesGanadoDados, '- Perdidas:', vecesPerdidoDados)
    print('---------------------------')


def main():
    # no se pide nombre en main; se pide en cada juego individual
    opcion = ""
    while opcion != "S":
        print("\n........MENU PRINCIPAL.")
        print("A - Mayor o Menor")
        print("B - Numero Secreto")
        print("C - BlackJack Simple")
        print("D - Dados (Par o Impar)")
        print("E - Reporte")
        print("S - Fin DEL PROGRAMA")
        opcion = input("Ingrese su opcion: ").strip().upper()
        while opcion == "" or (opcion != "A" and opcion != "B" and opcion != "C" and opcion != "D" and opcion != "E" and opcion != "S"):
            opcion = input("Ingreso invalido - reintente: ").strip().upper()

        match opcion:
            case "A":
                os.system('cls' if os.name == 'nt' else 'clear')
                juego_mayor_menor()
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "B":
                os.system('cls' if os.name == 'nt' else 'clear')
                juego_numero_secreto()
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "C":
                os.system('cls' if os.name == 'nt' else 'clear')
                juego_blackjack()
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "D":
                os.system('cls' if os.name == 'nt' else 'clear')
                juegoDados()
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "E":
                os.system('cls' if os.name == 'nt' else 'clear')
                reporte()
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "S":
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\n\nGracias por jugar, no apueste y juega por diversión! Hasta la próxima!')
                input("\nPresione la tecla 'Enter' para salir...")
                os.system('cls' if os.name == 'nt' else 'clear')
                sys.exit()
                
            

def mostrar_advertencia():
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
    
    

mostrar_advertencia()
main()