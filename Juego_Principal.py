import random
import sys
import os


"""
Nombre de los integrantes del grupo:
- Angel Jose Ayala
- Gabriela Iglesias
- Maximiliano Iván Campos
- Santiago Nicolás Bolzan

VARIABLES GLOBALES (para el reporte. Declarar en el archivo principal)
    nombre:str (nombre del último jugador del juego Mayor o Menor)
    racha:int (cantidad de aciertos consecutivos del último jugador)
"""

nombre = ''
racha = 0
a = 0
nreferencia = 0
ncomparar = 0
opcion = ''

def juego_mayor_menor():
    """
    VARIABLES LOCALES
        nombre_jugador:str (nombre ingresado por el jugador)
        nreferencia:int (número de referencia actual)
        ncomparar:int (número a comparar con la referencia)
        opcion:str (opción ingresada: mayor / menor)
        a:int (controla el bucle principal, 0=juego activo, 1=game over)
        racha:int (cantidad de aciertos consecutivos)
    """
    global nombre, racha, a, nreferencia, ncomparar, opcion

    print("\n================================================\n")
    print("       ♠  MAYOR O MENOR  ♠")
    print("  Adiviná si el siguiente número es mayor o menor\n")
    print("================================================\n")

    while True:
        nombre_jugador = input("Escribí tu nombre: ").strip()
        if nombre_jugador != "":
            break
        print("\n  ✗ Nombre vacío: Por favor escribí tu nombre\n")
    nombre = nombre_jugador
    print(f"\n| Bienvenido, {nombre_jugador} ♠          |")

    racha = 0
    a = 0
    nreferencia = random.randint(1, 1000)

    while a == 0:
        print("\n----------------------------------------")
        print(f"  Número de referencia: {nreferencia}")
        print("----------------------------------------")
        opcion = input('\n  Escribí "mayor" o "menor": ').strip().lower()
        while opcion != "mayor" and opcion != "menor":
            opcion = input('  ✗ Incorrecto. Escribí "mayor" o "menor": ').strip().lower()

        ncomparar = random.randint(1, 1000)
        while ncomparar == nreferencia:
            ncomparar = random.randint(1, 1000)

        if opcion == "mayor":
            if nreferencia < ncomparar:
                racha = racha + 1
                print("\n  ✓ ¡Acertaste!")
                nreferencia = ncomparar
            else:
                print("\n  ✗ Incorrecto. El número era menor.")
                a = 1
        else:
            if nreferencia > ncomparar:
                racha = racha + 1
                print("\n  ✓ ¡Acertaste!")
                nreferencia = ncomparar
            else:
                print("\n  ✗ Incorrecto. El número era mayor.")
                a = 1

    print("\n================================================")
    print(f"|                                      |")
    print(f"|     ♠  G A M E  O V E R  ♠           |")
    print(f"|                                      |")
    print(f"|     {nombre_jugador}, tu racha fue: {racha}           |")
    print(f"|                                      |")
    print("================================================")
    input("\nPresione la tecla 'Enter' para continuar...")

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

    print("\n================================================\n")
    print("     ♠  NÚMERO SECRETO  ♠")
    print("  Tenés 6 intentos para adivinar el número\n")
    print("================================================\n")

    while True:
        nombre_jugador = input("Escribí tu nombre: ").strip()
        if nombre_jugador != "":
            break
        print("\n  ✗ Nombre vacío: Por favor escribí tu nombre\n")
    print(f"\n| Bienvenido, {nombre_jugador} ♠          |")

    MAX_INTENTOS = 6
    RANGO_MAX = 100
    RANGO_MIN = 1
    numero_secreto = random.randint(RANGO_MIN, RANGO_MAX)
    intentos_usados = 0
    adivino = False

    print(f"\n  Pensé un número del {RANGO_MIN} al {RANGO_MAX}")

    while intentos_usados < MAX_INTENTOS and not adivino:
        print("----------------------------------------")
        intentos_restantes = MAX_INTENTOS - intentos_usados
        print(f"  Te quedan {intentos_restantes} intento(s)")

        entrada_valida = False
        while not entrada_valida:
            entrada_texto = input("  Ingresá tu número: ").strip()
            es_numero = len(entrada_texto) > 0
            indice = 0
            while indice < len(entrada_texto):
                caracter = entrada_texto[indice]
                if caracter < "0" or caracter > "9":
                    es_numero = False
                indice = indice + 1

            if not es_numero:
                print("  ✗ Solo números enteros positivos")
            else:
                intento_actual = int(entrada_texto)
                if intento_actual < RANGO_MIN or intento_actual > RANGO_MAX:
                    print(f"  ✗ El número debe estar entre {RANGO_MIN} y {RANGO_MAX}")
                else:
                    entrada_valida = True

        if intento_actual == numero_secreto:
            adivino = True
            print(f"\n  ✓ ¡Acertaste! El número era {numero_secreto}")
        elif intento_actual < numero_secreto:
            print("  El número secreto es mayor. Intentá de nuevo")
        else:
            print("  El número secreto es menor. Intentá de nuevo")

        intentos_usados = intentos_usados + 1

    print("\n================================================")
    print(f"|                                      |")
    print(f"|     ♠  G A M E  O V E R  ♠           |")
    print(f"|                                      |")
    if adivino:
        print(f"|     {nombre_jugador}, lo adivinaste en {intentos_usados} intentos!   |")
    else:
        print(f"|     El número era: {numero_secreto}                    |")
    print(f"|                                      |")
    print("================================================")

    if adivino:
        b_veces_ganado = b_veces_ganado + 1
    else:
        b_veces_perdido = b_veces_perdido + 1
    b_nombre_jugador = nombre_jugador
    b_veces_jugado = b_veces_jugado + 1
    input("\nPresione la tecla 'Enter' para continuar...")

"""
VARIABLES GLOBALES (para el reporte. Declarar en el archivo principal)
    bj_nombre_jugador:str (nombre del último jugador del juego C)
    bj_veces_jugado:int (cantidad total de partidas jugadas)
    bj_veces_ganado:int (cantidad de partidas ganadas por el jugador)
    bj_veces_perdido:int (cantidad de partidas perdidas por el jugador)
    bj_veces_empatado:int (cantidad de partidas empatadas)
    bj_jugadores:list (lista de nombres registrados, máximo 10)
"""

#INICIALIZO VARIABLES GLOBALES DE BLACKJACK
bj_nombre_jugador = ""
bj_veces_jugado = 0
bj_veces_ganado = 0
bj_veces_perdido = 0
bj_veces_empatado = 0
bj_jugadores = []


def juego_blackjack():
    """
    VARIABLES LOCALES
        PALOS:list (lista de los 4 palos de la baraja inglesa)
        RANGOS:list (lista de las 13 cartas de cada palo)
        mazo:list (mazo de 52 cartas, cada carta es una tupla (rango, palo))
        indice_carta:int (índice de la carta a sacar dentro del mazo)
        cartas_jugador:list (cartas en mano del jugador)
        cartas_banca:list (cartas en mano de la banca)
        puntos_jugador:int (suma de puntos del jugador)
        puntos_banca:int (suma de puntos de la banca)
        nombre_jugador:str (nombre ingresado por el jugador)
        nombre_existe:bool (True si el nombre ya está registrado)
        opcion:str (opción ingresada por el jugador: Pedir / Plantarse)
        jugar_otra:str (S/N para jugar otra partida)
        banca_blackjack:bool (True si la banca tiene blackjack natural)
        jugador_blackjack:bool (True si el jugador tiene blackjack natural)
    """
    global bj_nombre_jugador, bj_veces_jugado, bj_veces_ganado
    global bj_veces_perdido, bj_veces_empatado, bj_jugadores

    PALOS = ["♠", "♥", "♦", "♣"]
    RANGOS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    print("\n================================================\n")
    print("       ♠  BLACKJACK - EL 21  ♠")
    print("  El objetivo es sumar 21 sin pasarte\n")
    print("================================================\n")

    while True:
        nombre_jugador = input("Escribí tu nombre: ").strip()
        if nombre_jugador != "":
            break
        print("\n  ✗ Nombre vacío: Por favor escribí tu nombre\n")

    nombre_existe = False
    for nombre_registrado in bj_jugadores:
        if nombre_registrado.lower() == nombre_jugador.lower():
            nombre_existe = True
            break

    if not nombre_existe:
        if len(bj_jugadores) >= 10:
            print("\n  ✗ No hay cupos para un nuevo jugador. Límite de 10 alcanzado.")
            print("  Volvé al menú principal.")
            input("\nPresione la tecla 'Enter' para continuar...")
            return
        else:
            bj_jugadores.append(nombre_jugador)
            print(f"\n  ✓ Nuevo jugador registrado: {nombre_jugador}")
    else:
        print(f"\n  ✓ Bienvenido de nuevo, {nombre_jugador}")

    print(f"\n| Bienvenido, {nombre_jugador} ♠          |")
    bj_nombre_jugador = nombre_jugador

    jugar_otra = "S"
    while jugar_otra == "S":
        mazo = []
        for palo in PALOS:
            for rango in RANGOS:
                mazo.append((rango, palo))
        random.shuffle(mazo)
        indice_carta = 0

        cartas_jugador = []
        cartas_banca = []
        puntos_jugador = 0
        puntos_banca = 0

        print("\n================================================")
        print("          NUEVA PARTIDA")
        print("================================================\n")

        cartas_jugador.append(mazo[indice_carta])
        indice_carta = indice_carta + 1
        cartas_banca.append(mazo[indice_carta])
        indice_carta = indice_carta + 1
        cartas_jugador.append(mazo[indice_carta])
        indice_carta = indice_carta + 1
        cartas_banca.append(mazo[indice_carta])
        indice_carta = indice_carta + 1

        print("  Cartas de la Banca:")
        for carta in cartas_banca:
            print(f"    [{carta[0]}{carta[1]}]")

        print("\n  Cartas de", nombre_jugador + ":")
        for carta in cartas_jugador:
            print(f"    [{carta[0]}{carta[1]}]")

        puntos_jugador = _calcular_puntos(cartas_jugador)
        print(f"\n  Tu puntuación: {puntos_jugador}")

        if puntos_jugador == 21:
            print("  ♠ ¡BLACKJACK! Sumaste 21 con las dos cartas.")
            puntos_banca = _calcular_puntos(cartas_banca)
            print(f"\n  Puntuación Banca: {puntos_banca}")
            if puntos_banca != 21:
                print("\n  >>> ¡GANASTE! <<<")
                bj_veces_ganado = bj_veces_ganado + 1
            else:
                print("\n  >>> EMPATE (ambos con Blackjack) <<<")
                bj_veces_empatado = bj_veces_empatado + 1
            bj_veces_jugado = bj_veces_jugado + 1
            print("\n----------------------------------------")
            print("  ESTADÍSTICAS DE BLACKJACK:")
            print(f"    Partidas jugadas: {bj_veces_jugado}")
            print(f"    Ganadas: {bj_veces_ganado}")
            print(f"    Perdidas: {bj_veces_perdido}")
            print(f"    Empatadas: {bj_veces_empatado}")
            print("----------------------------------------")
            jugar_otra = ""
            while jugar_otra != "S" and jugar_otra != "N":
                jugar_otra = input("\n¿Querés jugar otra partida? (S/N): ").strip().upper()
                if jugar_otra != "S" and jugar_otra != "N":
                    print("  ✗ Opción inválida. Ingresá S o N.")
            if jugar_otra == "S":
                print("\n  ✓ Comenzando nueva partida...")
            else:
                print("\n  Volviendo al menú principal...")
            continue

        turno_activo = True
        while turno_activo:
            opcion = ""
            while opcion != "PEDIR" and opcion != "PLANTARSE":
                opcion = input('\n  "Pedir" otra carta o "Plantarte": ').strip().upper()
                if opcion != "PEDIR" and opcion != "PLANTARSE":
                    print('  ✗ Opción inválida. Escribí "Pedir" o "Plantarse".')

            if opcion == "PEDIR":
                cartas_jugador.append(mazo[indice_carta])
                indice_carta = indice_carta + 1
                print(f"\n  Sacaste: [{cartas_jugador[-1][0]}{cartas_jugador[-1][1]}]")
                print("  Tu mano:")
                for carta in cartas_jugador:
                    print(f"    [{carta[0]}{carta[1]}]")
                puntos_jugador = _calcular_puntos(cartas_jugador)
                print(f"\n  Tu puntuación: {puntos_jugador}")

                if puntos_jugador > 21:
                    print("\n  ✗ ¡Te pasaste de 21! Perdiste automáticamente.")
                    turno_activo = False
                elif puntos_jugador == 21:
                    print("\n  ♠ ¡Llegaste a 21! Pasás el turno a la banca.")
                    turno_activo = False
            else:
                print(f"\n  Te plantaste con {puntos_jugador} puntos.")
                turno_activo = False

        if puntos_jugador <= 21:
            print("\n----------------------------------------")
            print("  Turno de la Banca:")
            print("  Cartas de la Banca:")
            for carta in cartas_banca:
                print(f"    [{carta[0]}{carta[1]}]")
            puntos_banca = _calcular_puntos(cartas_banca)
            print(f"  Puntuación Banca: {puntos_banca}")

            while puntos_banca <= 16:
                cartas_banca.append(mazo[indice_carta])
                indice_carta = indice_carta + 1
                print(f"\n  La banca pide carta: [{cartas_banca[-1][0]}{cartas_banca[-1][1]}]")
                puntos_banca = _calcular_puntos(cartas_banca)
                print(f"  Puntuación Banca: {puntos_banca}")

            print("\n----------------------------------------")
            if puntos_banca > 21:
                print("\n  >>> ¡GANASTE! La banca se pasó de 21. <<<")
                bj_veces_ganado = bj_veces_ganado + 1
            elif puntos_jugador > puntos_banca:
                print(f"\n  >>> ¡GANASTE! Vos: {puntos_jugador} | Banca: {puntos_banca} <<<")
                bj_veces_ganado = bj_veces_ganado + 1
            elif puntos_jugador < puntos_banca:
                print(f"\n  >>> PERDISTE. Vos: {puntos_jugador} | Banca: {puntos_banca} <<<")
                bj_veces_perdido = bj_veces_perdido + 1
            else:
                #Empate a 21: si la banca tiene blackjack natural (2 cartas) y el jugador no, gana la banca
                banca_blackjack = (len(cartas_banca) == 2 and puntos_banca == 21)
                jugador_blackjack = (len(cartas_jugador) == 2 and puntos_jugador == 21)
                if banca_blackjack and not jugador_blackjack:
                    print("\n  >>> PERDISTE. La banca tiene Blackjack natural. <<<")
                    bj_veces_perdido = bj_veces_perdido + 1
                else:
                    print(f"\n  >>> EMPATE. Ambos con {puntos_jugador} puntos <<<")
                    bj_veces_empatado = bj_veces_empatado + 1
        else:
            bj_veces_perdido = bj_veces_perdido + 1
            puntos_banca = _calcular_puntos(cartas_banca)
            print(f"\n  Puntuación Banca (no necesitó jugar): {puntos_banca}")

        bj_veces_jugado = bj_veces_jugado + 1
        print("\n----------------------------------------")
        print("  ESTADÍSTICAS DE BLACKJACK:")
        print(f"    Partidas jugadas: {bj_veces_jugado}")
        print(f"    Ganadas: {bj_veces_ganado}")
        print(f"    Perdidas: {bj_veces_perdido}")
        print(f"    Empatadas: {bj_veces_empatado}")
        print("----------------------------------------")

        jugar_otra = ""
        while jugar_otra != "S" and jugar_otra != "N":
            jugar_otra = input("\n¿Querés jugar otra partida? (S/N): ").strip().upper()
            if jugar_otra != "S" and jugar_otra != "N":
                print("  ✗ Opción inválida. Ingresá S o N.")

        if jugar_otra == "S":
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


def _calcular_puntos(cartas):
    """
    Calcula la puntuación de una mano de Blackjack.
    CARTAS NUMÉRICAS (2-10): valen su número.
    FIGURAS (J, Q, K): valen 10.
    AS (A): vale 11, pero si al sumarlo se supera 21, pasa a valer 1.
    """
    total = 0
    cantidad_ases = 0

    for carta in cartas:
        rango = carta[0]
        if rango == "A":
            total = total + 11
            cantidad_ases = cantidad_ases + 1
        elif rango == "J" or rango == "Q" or rango == "K":
            total = total + 10
        else:
            #Cartas numéricas (2 al 10)
            total = total + int(rango)

    #Si nos pasamos de 21 y tenemos Ases, los convertimos de 11 a 1
    while total > 21 and cantidad_ases > 0:
        total = total - 10
        cantidad_ases = cantidad_ases - 1

    return total
    

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
    nombreJugadorDados = input("Escribe tu nombre: ").strip()
    while nombreJugadorDados == "":
        print("\n  ✗ Nombre vacío: Por favor escribe tu nombre\n")
        nombreJugadorDados = input("Escribe tu nombre: ").strip()
    print(f"\n| Bienvenido, {nombreJugadorDados} ♠          |")
    while juegoActivo:
        vecesJugadoDados = vecesJugadoDados + 1
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
    # Verifico si hay al menos un juego jugado (algún nombre registrado)
    hay_registros = (nombre != '' or b_nombre_jugador != '' or
                     bj_nombre_jugador != '' or nombreJugadorDados != '')
    if not hay_registros:
        print('\n--- REPORTE DEL JUGADOR ---')
        print('Aún no hay registros.')
        print('Debes jugar al menos una vez en cualquiera de los juegos')
        print('para que aparezcan tus estadísticas en el reporte.')
        print('---------------------------')
        print('\nVolviendo al menú principal...')
        input("\nPresione la tecla 'Enter' para continuar...")
        return
    print('\n--- REPORTE DEL JUGADOR ---')
    if nombre != '':
        print('Mayor o Menor - Nombre:', nombre, '- Racha:', racha)
    if b_nombre_jugador != '':
        print('Número Secreto - Nombre:', b_nombre_jugador, '- Veces jugado:', b_veces_jugado, '- Ganadas:', b_veces_ganado, '- Perdidas:', b_veces_perdido)
    if bj_nombre_jugador != '':
        print('Blackjack - Nombre:', bj_nombre_jugador, '- Veces jugado:', bj_veces_jugado, '- Ganadas:', bj_veces_ganado, '- Perdidas:', bj_veces_perdido, '- Empatadas:', bj_veces_empatado, '- Jugadores registrados:', len(bj_jugadores))
    if nombreJugadorDados != '':
        print('\nDados (Par o Impar) - Nombre:', nombreJugadorDados, '- Veces jugadas:', vecesJugadoDados, '- Ganadas:', vecesGanadoDados, '- Perdidas:', vecesPerdidoDados)
    print('---------------------------')
    input("\nPresione la tecla 'Enter' para volver al menú...")


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
                break
                
            

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