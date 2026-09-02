import random
import os


"""
Nombre de los integrantes del grupo:
- Angel Jose Ayala
- Gabriela Iglesias
- Maximiliano Iván Campos
- Santiago Nicolás Bolzan
"""

"""
VARIABLES GLOBALES
    MAX_JUGADORES:int (cantidad máxima de jugadores admitidos en cada juego)

    mm_nombre_ultimo_jugador:str (nombre del último jugador de Mayor o Menor)
    mm_nombres:list (nombres registrados en Mayor o Menor, máximo 10)
    mm_rachas:list (racha obtenida por cada jugador de Mayor o Menor)
    mm_cantidad_jugadores:int (cantidad de jugadores registrados en Mayor o Menor)

    ns_nombre_ultimo_jugador:str (nombre del último jugador de Número Secreto)
    ns_nombres:list (nombres registrados en Número Secreto, máximo 10)
    ns_jugadas:list (cantidad de partidas jugadas por cada jugador de Número Secreto)
    ns_ganadas:list (cantidad de partidas ganadas por cada jugador de Número Secreto)
    ns_perdidas:list (cantidad de partidas perdidas por cada jugador de Número Secreto)
    ns_cantidad_jugadores:int (cantidad de jugadores registrados en Número Secreto)

    bj_nombre_ultimo_jugador:str (nombre del último jugador de Blackjack)
    bj_jugadores:list (nombres registrados en Blackjack, máximo 10)
    bj_jugadas:list (cantidad de partidas jugadas por cada jugador de Blackjack)
    bj_ganadas:list (cantidad de partidas ganadas por cada jugador de Blackjack)
    bj_perdidas:list (cantidad de partidas perdidas por cada jugador de Blackjack)
    bj_empatadas:list (cantidad de partidas empatadas por cada jugador de Blackjack)
    bj_cantidad_jugadores:int (cantidad de jugadores registrados en Blackjack)

    pi_nombre_ultimo_jugador:str (nombre del último jugador de Par o Impar)
    pi_nombres:list (nombres registrados en Par o Impar, máximo 10)
    pi_jugadas:list (cantidad de partidas jugadas por cada jugador de Par o Impar)
    pi_ganadas:list (cantidad de partidas ganadas por cada jugador de Par o Impar)
    pi_perdidas:list (cantidad de partidas perdidas por cada jugador de Par o Impar)
    pi_creditos:list (crédito disponible de cada jugador de Par o Impar)
    pi_cantidad_jugadores:int (cantidad de jugadores registrados en Par o Impar)
"""

MAX_JUGADORES = 10

mm_nombre_ultimo_jugador = ''
mm_nombres = ["", "", "", "", "", "", "", "", "", ""]
mm_rachas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
mm_cantidad_jugadores = 0

ns_nombre_ultimo_jugador = ""
ns_nombres = ["", "", "", "", "", "", "", "", "", ""]
ns_jugadas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ns_ganadas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ns_perdidas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ns_cantidad_jugadores = 0

bj_nombre_ultimo_jugador = ""
bj_jugadores = ["", "", "", "", "", "", "", "", "", ""]
bj_jugadas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bj_ganadas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bj_perdidas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bj_empatadas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
bj_cantidad_jugadores = 0

pi_nombre_ultimo_jugador = ''
pi_nombres = ["", "", "", "", "", "", "", "", "", ""]
pi_jugadas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pi_ganadas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pi_perdidas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pi_creditos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pi_cantidad_jugadores = 0

def convertir_digitos_a_entero(texto):
    """
    ALGORITMO: Convierte un string de digitos a entero sin usar int().
    Usa slicing para recorrer el string caracter por caracter,
    compara cada caracter contra '0'..'9' para obtener su valor numerico,
    y construye el numero con aritmetica basica (multiplicacion por 10
    y suma). No usa len(), for(), ord(), ni ninguna funcion prohibida.
    """
    resultado = 0
    indice = 0
    while texto[indice:indice+1] != '':
        caracter = texto[indice:indice+1]
        if caracter == '0':
            valor = 0
        elif caracter == '1':
            valor = 1
        elif caracter == '2':
            valor = 2
        elif caracter == '3':
            valor = 3
        elif caracter == '4':
            valor = 4
        elif caracter == '5':
            valor = 5
        elif caracter == '6':
            valor = 6
        elif caracter == '7':
            valor = 7
        elif caracter == '8':
            valor = 8
        elif caracter == '9':
            valor = 9
        else:
            valor = 0
        resultado = resultado * 10 + valor
        indice = indice + 1
    return resultado

ns_convertir_a_entero = convertir_digitos_a_entero
pi_convertir_a_entero = convertir_digitos_a_entero

def buscar_jugador(nombres, cantidad_jugadores, nombre_buscado):
    """
    ALGORITMO: Busqueda secuencial.
    Recorre el arreglo posicion por posicion desde el inicio.
    En cada paso compara el nombre buscado con el nombre en la posicion actual.
    Si coinciden, guarda la posicion y detiene la busqueda.
    Si llega al final sin encontrar, devuelve -1.

    VARIABLES LOCALES
        nombres:list (arreglo de nombres de jugadores en el que se realiza la búsqueda)
        cantidad_jugadores:int (cantidad de posiciones ocupadas en el arreglo de nombres)
        nombre_buscado:str (nombre que se desea localizar dentro del arreglo)
        indice:int (posición utilizada para recorrer secuencialmente el arreglo)
        posicion:int (indica la posicion encontrada, -1 si no se encontro)
    """
    indice = 0
    posicion = -1

    while indice < cantidad_jugadores and posicion == -1:
        if nombres[indice].lower() == nombre_buscado.lower():
            posicion = indice
        else:
            indice = indice + 1

    return posicion

def juego_mayor_menor():
    """
    VARIABLES LOCALES
        mm_nombre_jugador:str (nombre ingresado por el jugador)
        mm_indice_jugador:int (posición del jugador en los arreglos de Mayor o Menor)
        mm_racha:int (cantidad de aciertos consecutivos obtenidos en la partida)
        mm_juego_finalizado:int (control del ciclo principal: 0 activo y 1 finalizado)
        mm_numero_referencia:int (número mostrado como referencia para la comparación)
        mm_numero_comparar:int (nuevo número aleatorio comparado con el de referencia)
        mm_opcion:str (elección ingresada por el jugador: mayor o menor)
        mm_nombre_valido:int (indica si el nombre ingresado no esta vacio)
        mm_salir:int (indica si se debe salir de la funcion sin jugar)
    """
    global mm_nombre_ultimo_jugador, mm_cantidad_jugadores
    

    print("\n================================================\n")
    print("       ♠  MAYOR O MENOR  ♠")
    print("  Adiviná si el siguiente número es mayor o menor\n")
    print("================================================\n")

    # Validacion de nombre sin break: se repite mientras el nombre sea vacio
    mm_nombre_valido = 0
    while mm_nombre_valido == 0:
        mm_nombre_jugador = input("Escribí tu nombre: ").strip()
        if mm_nombre_jugador != "":
            mm_nombre_valido = 1
        else:
            print("\n  ✗ Nombre vacío: Por favor escribí tu nombre\n")

    mm_indice_jugador = buscar_jugador(
        mm_nombres,
        mm_cantidad_jugadores,
        mm_nombre_jugador
    )

    mm_salir = 0

    if mm_indice_jugador == -1:
        if mm_cantidad_jugadores == MAX_JUGADORES:
            print("\n  ✗ No hay cupos para nuevos jugadores.")
            print("  Se alcanzó el límite de 10 jugadores.")
            input("\nPresione la tecla 'Enter' para continuar...")
            mm_salir = 1

        if mm_salir == 0:
            mm_nombres[mm_cantidad_jugadores] = mm_nombre_jugador
            mm_rachas[mm_cantidad_jugadores] = 0

            mm_indice_jugador = mm_cantidad_jugadores
            mm_cantidad_jugadores = mm_cantidad_jugadores + 1

            print(f"\n  ✓ Nuevo jugador registrado: {mm_nombre_jugador}")
    else:
        print(f"\n  ✓ Bienvenido nuevamente, {mm_nombres[mm_indice_jugador]}")

    if mm_salir == 0:
        mm_nombre_ultimo_jugador = mm_nombre_jugador
        print(f"\n| Bienvenido, {mm_nombre_jugador} ♠          |")

        mm_racha = 0
        mm_juego_finalizado = 0
        mm_numero_referencia = random.randint(1, 1000)

        while mm_juego_finalizado == 0:
            print("\n----------------------------------------")
            print(f"  Número de referencia: {mm_numero_referencia}")
            print("----------------------------------------")
            mm_opcion = input('\n  Escribí "mayor" o "menor": ').strip().lower()
            while mm_opcion != "mayor" and mm_opcion != "menor":
                mm_opcion = input('  ✗ Incorrecto. Escribí "mayor" o "menor": ').strip().lower()

            mm_numero_comparar = random.randint(1, 1000)

            if mm_numero_comparar == mm_numero_referencia:
                print(f"\n  Salió nuevamente el número {mm_numero_comparar}.")
                print("  El juego continúa y la racha no cambia.")
            else:
                if mm_opcion == "mayor":
                    if mm_numero_referencia < mm_numero_comparar:
                        mm_racha = mm_racha + 1
                        print("\n  ✓ ¡Acertaste!")
                        mm_numero_referencia = mm_numero_comparar
                    else:
                        print("\n  ✗ Incorrecto. El número era menor.")
                        mm_juego_finalizado = 1
                else:
                    if mm_numero_referencia > mm_numero_comparar:
                        mm_racha = mm_racha + 1
                        print("\n  ✓ ¡Acertaste!")
                        mm_numero_referencia = mm_numero_comparar
                    else:
                        print("\n  ✗ Incorrecto. El número era mayor.")
                        mm_juego_finalizado = 1
        mm_rachas[mm_indice_jugador] = mm_racha
        print("\n================================================")
        print(f"|                                      |")
        print(f"|     ♠  G A M E  O V E R  ♠           |")
        print(f"|                                      |")
        print(f"|     {mm_nombre_jugador}, tu racha fue: {mm_racha}           |")
        print(f"|                                      |")
        print("================================================")
        input("\nPresione la tecla 'Enter' para continuar...")


def juego_numero_secreto():
    """
    VARIABLES LOCALES
        ns_nombre_jugador:str (nombre ingresado por el jugador)
        ns_indice_jugador:int (posición del jugador en los arreglos de Número Secreto)
        NS_MAX_INTENTOS:int (cantidad máxima de intentos permitidos)
        NS_RANGO_MIN:int (límite inferior del número secreto)
        NS_RANGO_MAX:int (límite superior del número secreto)
        ns_numero_secreto:int (número aleatorio que debe adivinar el jugador)
        ns_intentos_usados:int (cantidad de intentos realizados por el jugador)
        ns_intentos_restantes:int (cantidad de intentos disponibles antes de cada jugada)
        ns_adivino:bool (indica si el jugador acertó el número secreto)
        ns_entrada_valida:bool (indica si el valor ingresado pasó las validaciones)
        ns_entrada_texto:str (entrada del usuario antes de convertirla a número)
        ns_es_numero:int (indica si la entrada contiene unicamente digitos)
        ns_intento_actual:int (número ingresado por el jugador en el intento actual)
        ns_nombre_valido:int (indica si el nombre ingresado no esta vacio)
        ns_salir:int (indica si se debe salir de la funcion sin jugar)
        ns_indice_digito:int (posicion para recorrer cada caracter de la entrada)
        ns_caracter:str (caracter actual siendo evaluado)
        ns_solo_digitos:int (bandera: 1 si todos los caracteres son digitos)
    """
    global ns_nombre_ultimo_jugador, ns_cantidad_jugadores

    print("\n================================================\n")
    print("     ♠  NÚMERO SECRETO  ♠")
    print("  Tenés 6 intentos para adivinar el número\n")
    print("================================================\n")

    # Validacion de nombre sin break
    ns_nombre_valido = 0
    while ns_nombre_valido == 0:
        ns_nombre_jugador = input("Escribí tu nombre: ").strip()
        if ns_nombre_jugador != "":
            ns_nombre_valido = 1
        else:
            print("\n  ✗ Nombre vacío: Por favor escribí tu nombre\n")

    ns_indice_jugador = buscar_jugador(
        ns_nombres,
        ns_cantidad_jugadores,
        ns_nombre_jugador
    )

    ns_salir = 0

    if ns_indice_jugador == -1:
        if ns_cantidad_jugadores == MAX_JUGADORES:
            print("\n  ✗ No hay cupos para nuevos jugadores.")
            print("  Se alcanzó el límite de 10 jugadores.")
            input("\nPresione la tecla 'Enter' para continuar...")
            ns_salir = 1

        if ns_salir == 0:
            ns_nombres[ns_cantidad_jugadores] = ns_nombre_jugador
            ns_jugadas[ns_cantidad_jugadores] = 0
            ns_ganadas[ns_cantidad_jugadores] = 0
            ns_perdidas[ns_cantidad_jugadores] = 0

            ns_indice_jugador = ns_cantidad_jugadores
            ns_cantidad_jugadores = ns_cantidad_jugadores + 1

            print(f"\n  ✓ Nuevo jugador registrado: {ns_nombre_jugador}")
    else:
        print(f"\n  ✓ Bienvenido nuevamente, {ns_nombres[ns_indice_jugador]}")

    if ns_salir == 0:
        print(f"\n| Bienvenido, {ns_nombre_jugador} ♠          |")

        NS_MAX_INTENTOS = 6
        NS_RANGO_MAX = 100
        NS_RANGO_MIN = 1
        ns_numero_secreto = random.randint(NS_RANGO_MIN, NS_RANGO_MAX)
        ns_intentos_usados = 0
        ns_adivino = False

        print(f"\n  Pensé un número del {NS_RANGO_MIN} al {NS_RANGO_MAX}")

        while ns_intentos_usados < NS_MAX_INTENTOS and not ns_adivino:
            print("----------------------------------------")
            ns_intentos_restantes = NS_MAX_INTENTOS - ns_intentos_usados
            print(f"  Te quedan {ns_intentos_restantes} intento(s)")

            ns_entrada_valida = False
            ns_intento_actual = 0
            while not ns_entrada_valida:
                ns_entrada_texto = input("  Ingresá tu número: ").strip()

                # Validacion de digitos sin isdigit(), len() ni for():
                # Se verifica que el string no este vacio y se recorre cada
                # caracter mediante while indexado.
                ns_solo_digitos = 0
                if ns_entrada_texto != "":
                    ns_solo_digitos = 1
                    ns_indice_digito = 0
                    while ns_indice_digito < 10 and ns_solo_digitos == 1:
                        ns_caracter = ns_entrada_texto[ns_indice_digito]
                        if ns_caracter < '0' or ns_caracter > '9':
                            ns_solo_digitos = 0
                        ns_indice_digito = ns_indice_digito + 1

                if ns_solo_digitos == 0:
                    print("  ✗ Solo números enteros positivos")
                else:
                    ns_intento_actual = ns_convertir_a_entero(ns_entrada_texto)
                    if ns_intento_actual < NS_RANGO_MIN or ns_intento_actual > NS_RANGO_MAX:
                        print(f"  ✗ El número debe estar entre {NS_RANGO_MIN} y {NS_RANGO_MAX}")
                    else:
                        ns_entrada_valida = True

            if ns_intento_actual == ns_numero_secreto:
                ns_adivino = True
                print(f"\n  ✓ ¡Acertaste! El número era {ns_numero_secreto}")
            elif ns_intento_actual < ns_numero_secreto:
                print("  El número secreto es mayor. Intentá de nuevo")
            else:
                print("  El número secreto es menor. Intentá de nuevo")

            ns_intentos_usados = ns_intentos_usados + 1

        print("\n================================================")
        print(f"|                                      |")
        print(f"|     ♠  G A M E  O V E R  ♠           |")
        print(f"|                                      |")
        if ns_adivino:
            print(f"|     {ns_nombre_jugador}, lo adivinaste en {ns_intentos_usados} intentos!   |")
        else:
            print(f"|     El número era: {ns_numero_secreto}                    |")
        print(f"|                                      |")
        print("================================================")

        ns_jugadas[ns_indice_jugador] = ns_jugadas[ns_indice_jugador] + 1

        if ns_adivino:
            ns_ganadas[ns_indice_jugador] = ns_ganadas[ns_indice_jugador] + 1
        else:
            ns_perdidas[ns_indice_jugador] = ns_perdidas[ns_indice_jugador] + 1

        ns_nombre_ultimo_jugador = ns_nombre_jugador
        input("\nPresione la tecla 'Enter' para continuar...")


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
    global bj_nombre_ultimo_jugador, bj_cantidad_jugadores
    BJ_PALOS = ["♠", "♥", "♦", "♣"]
    BJ_RANGOS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    print("\n================================================\n")
    print("       ♠  BLACKJACK - EL 21  ♠")
    print("  El objetivo es sumar 21 sin pasarte\n")
    print("================================================\n")

    # Validacion de nombre sin break
    bj_nombre_valido = 0
    while bj_nombre_valido == 0:
        bj_nombre_jugador = input("Escribí tu nombre: ").strip()
        if bj_nombre_jugador != "":
            bj_nombre_valido = 1
        else:
            print("\n  ✗ Nombre vacío: Por favor escribí tu nombre\n")

    bj_indice_jugador = buscar_jugador(
        bj_jugadores,
        bj_cantidad_jugadores,
        bj_nombre_jugador
    )

    bj_salir = 0

    if bj_indice_jugador == -1:
        if bj_cantidad_jugadores == MAX_JUGADORES:
            print("\n  ✗ No hay cupos para nuevos jugadores.")
            print("  Se alcanzó el límite de 10 jugadores.")
            input("\nPresione la tecla 'Enter' para continuar...")
            bj_salir = 1

        if bj_salir == 0:
            bj_jugadores[bj_cantidad_jugadores] = bj_nombre_jugador
            bj_jugadas[bj_cantidad_jugadores] = 0
            bj_ganadas[bj_cantidad_jugadores] = 0
            bj_perdidas[bj_cantidad_jugadores] = 0
            bj_empatadas[bj_cantidad_jugadores] = 0

            bj_indice_jugador = bj_cantidad_jugadores
            bj_cantidad_jugadores = bj_cantidad_jugadores + 1

            print(f"\n  ✓ Nuevo jugador registrado: {bj_nombre_jugador}")
    else:
        print(f"\n  ✓ Bienvenido nuevamente, {bj_jugadores[bj_indice_jugador]}")

    if bj_salir == 0:
        print(f"\n| Bienvenido, {bj_nombre_jugador} ♠          |")
        bj_nombre_ultimo_jugador = bj_nombre_jugador

        bj_jugar_otra = "S"
        while bj_jugar_otra == "S":
            bj_mazo = [
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None
            ]

            bj_indice_mazo = 0
            bj_indice_palo = 0

            while bj_indice_palo < 4:
                bj_indice_rango = 0

                while bj_indice_rango < 13:
                    # Carta representada como lista [rango, palo] en vez de tupla
                    bj_mazo[bj_indice_mazo] = [
                        BJ_RANGOS[bj_indice_rango],
                        BJ_PALOS[bj_indice_palo]
                    ]

                    bj_indice_mazo = bj_indice_mazo + 1
                    bj_indice_rango = bj_indice_rango + 1

                bj_indice_palo = bj_indice_palo + 1

            # ALGORITMO: Barajado Fisher-Yates (reemplazo de random.shuffle)
            # Recorre el mazo desde la ultima posicion hasta la primera.
            # En cada paso elige una posicion aleatoria entre 0 y la actual
            # e intercambia las dos cartas. Esto garantiza una permutacion
            # uniforme sin necesidad de la funcion shuffle().
            bj_i = 51
            while bj_i > 0:
                bj_j = random.randint(0, bj_i)
                bj_aux = bj_mazo[bj_i]
                bj_mazo[bj_i] = bj_mazo[bj_j]
                bj_mazo[bj_j] = bj_aux
                bj_i = bj_i - 1

            bj_indice_carta = 0

            bj_cartas_jugador = [
                None, None, None, None, None,
                None, None, None, None, None, None
            ]

            bj_cartas_banca = [
                None, None, None, None, None,
                None, None, None, None, None, None
            ]

            bj_cantidad_cartas_jugador = 0
            bj_cantidad_cartas_banca = 0
            bj_puntos_jugador = 0
            bj_puntos_banca = 0

            print("\n================================================")
            print("          NUEVA PARTIDA")
            print("================================================\n")

            bj_cartas_jugador[bj_cantidad_cartas_jugador] = bj_mazo[bj_indice_carta]
            bj_cantidad_cartas_jugador = bj_cantidad_cartas_jugador + 1
            bj_indice_carta = bj_indice_carta + 1

            bj_cartas_banca[bj_cantidad_cartas_banca] = bj_mazo[bj_indice_carta]
            bj_cantidad_cartas_banca = bj_cantidad_cartas_banca + 1
            bj_indice_carta = bj_indice_carta + 1

            bj_cartas_jugador[bj_cantidad_cartas_jugador] = bj_mazo[bj_indice_carta]
            bj_cantidad_cartas_jugador = bj_cantidad_cartas_jugador + 1
            bj_indice_carta = bj_indice_carta + 1

            bj_cartas_banca[bj_cantidad_cartas_banca] = bj_mazo[bj_indice_carta]
            bj_cantidad_cartas_banca = bj_cantidad_cartas_banca + 1
            bj_indice_carta = bj_indice_carta + 1

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
            bj_puntos_jugador = bj_calcular_puntos(bj_cartas_jugador, bj_cantidad_cartas_jugador)
            print(f"\n  Tu puntuación: {bj_puntos_jugador}")

            if bj_puntos_jugador == 21:
                print("  ♠ ¡BLACKJACK! Sumaste 21 con las dos cartas.")
                bj_puntos_banca = bj_calcular_puntos(bj_cartas_banca, bj_cantidad_cartas_banca)
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
                    bj_jugar_otra = input("\n¿Querés jugar otra partida? (S/N): ").strip().upper()
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
                        bj_opcion = input('\n  "Pedir" otra carta o "Plantarte": ').strip().upper()
                        if bj_opcion != "PEDIR" and bj_opcion != "PLANTARSE":
                            print('  ✗ Opción inválida. Escribí "Pedir" o "Plantarse".')

                    if bj_opcion == "PEDIR":
                        bj_cartas_jugador[bj_cantidad_cartas_jugador] = bj_mazo[bj_indice_carta]

                        bj_carta_nueva = bj_cartas_jugador[bj_cantidad_cartas_jugador]

                        bj_cantidad_cartas_jugador = bj_cantidad_cartas_jugador + 1
                        bj_indice_carta = bj_indice_carta + 1

                        print(f"\n  Sacaste: [{bj_carta_nueva[0]}{bj_carta_nueva[1]}]")
                        print("  Tu mano:")
                        bj_indice = 0

                        while bj_indice < bj_cantidad_cartas_jugador:
                            bj_carta = bj_cartas_jugador[bj_indice]
                            print(f"    [{bj_carta[0]}{bj_carta[1]}]")
                            bj_indice = bj_indice + 1
                        bj_puntos_jugador = bj_calcular_puntos(bj_cartas_jugador, bj_cantidad_cartas_jugador)
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
                    bj_puntos_banca = bj_calcular_puntos(bj_cartas_banca, bj_cantidad_cartas_banca)
                    print(f"  Puntuación Banca: {bj_puntos_banca}")

                    while bj_puntos_banca <= 16:
                        bj_cartas_banca[bj_cantidad_cartas_banca] = bj_mazo[bj_indice_carta]

                        bj_carta_nueva = bj_cartas_banca[bj_cantidad_cartas_banca]

                        bj_cantidad_cartas_banca = bj_cantidad_cartas_banca + 1
                        bj_indice_carta = bj_indice_carta + 1

                        print(f"\n  La banca pide carta: [{bj_carta_nueva[0]}{bj_carta_nueva[1]}]")
                        bj_puntos_banca = bj_calcular_puntos(bj_cartas_banca, bj_cantidad_cartas_banca)
                        print(f"  Puntuación Banca: {bj_puntos_banca}")

                    print("\n----------------------------------------")
                    if bj_puntos_banca > 21:
                        print("\n  >>> ¡GANASTE! La banca se pasó de 21. <<<")
                        bj_ganadas[bj_indice_jugador] = bj_ganadas[bj_indice_jugador] + 1
                    elif bj_puntos_jugador > bj_puntos_banca:
                        print(f"\n  >>> ¡GANASTE! Vos: {bj_puntos_jugador} | Banca: {bj_puntos_banca} <<<")
                        bj_ganadas[bj_indice_jugador] = bj_ganadas[bj_indice_jugador] + 1
                    elif bj_puntos_jugador < bj_puntos_banca:
                        print(f"\n  >>> PERDISTE. Vos: {bj_puntos_jugador} | Banca: {bj_puntos_banca} <<<")
                        bj_perdidas[bj_indice_jugador] = bj_perdidas[bj_indice_jugador] + 1
                    else:
                        #Empate a 21: si la banca tiene blackjack natural (2 cartas) y el jugador no, gana la banca
                        bj_banca_blackjack = (
                            bj_cantidad_cartas_banca == 2
                            and bj_puntos_banca == 21
                        )

                        bj_jugador_blackjack = (
                            bj_cantidad_cartas_jugador == 2
                            and bj_puntos_jugador == 21
                        )
                        if bj_banca_blackjack and not bj_jugador_blackjack:
                            print("\n  >>> PERDISTE. La banca tiene Blackjack natural. <<<")
                            bj_perdidas[bj_indice_jugador] = bj_perdidas[bj_indice_jugador] + 1
                        else:
                            print(f"\n  >>> EMPATE. Ambos con {bj_puntos_jugador} puntos <<<")
                            bj_empatadas[bj_indice_jugador] = bj_empatadas[bj_indice_jugador] + 1
                else:
                    bj_perdidas[bj_indice_jugador] = bj_perdidas[bj_indice_jugador] + 1
                    bj_puntos_banca = bj_calcular_puntos(bj_cartas_banca, bj_cantidad_cartas_banca)
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
                    bj_jugar_otra = input("\n¿Querés jugar otra partida? (S/N): ").strip().upper()
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



def bj_calcular_puntos(bj_cartas, bj_cantidad_cartas):
    """
    VARIABLES LOCALES
        bj_cartas:list (arreglo que contiene las cartas de la mano a evaluar)
        bj_cantidad_cartas:int (cantidad de posiciones ocupadas en la mano)
        bj_total:int (suma acumulada de los valores de las cartas)
        bj_cantidad_ases:int (cantidad de ases contados inicialmente con valor 11)
        bj_indice:int (posición utilizada para recorrer la mano)
        bj_rango:str (rango de la carta evaluada en la posición actual)
    """
    bj_total = 0
    bj_cantidad_ases = 0
    bj_indice = 0

    while bj_indice < bj_cantidad_cartas:
        bj_rango = bj_cartas[bj_indice][0]

        if bj_rango == "A":
            bj_total = bj_total + 11
            bj_cantidad_ases = bj_cantidad_ases + 1
        elif bj_rango == "J" or bj_rango == "Q" or bj_rango == "K":
            bj_total = bj_total + 10
        else:
            # bj_rango es un string '2'..'9' o '10'; convertir sin int()
            bj_total = bj_total + convertir_digitos_a_entero(bj_rango)

        bj_indice = bj_indice + 1

    while bj_total > 21 and bj_cantidad_ases > 0:
        bj_total = bj_total - 10
        bj_cantidad_ases = bj_cantidad_ases - 1

    return bj_total


def juego_par_o_impar():
    """
    VARIABLES LOCALES
        pi_juego_activo:bool (indica si el jugador continúa dentro del juego)
        pi_nombre_jugador:str (nombre ingresado por el jugador)
        pi_indice_jugador:int (posición del jugador en los arreglos de Par o Impar)
        pi_apuesta_valida:bool (indica si el monto de la apuesta pasó las validaciones)
        pi_entrada_apuesta:str (monto ingresado antes de convertirlo a número)
        pi_apuesta:int (cantidad de crédito apostada en la ronda)
        pi_tipo_apuesta:str (opción elegida por el jugador: par o impar)
        pi_dado_1:int (resultado aleatorio del primer dado)
        pi_dado_2:int (resultado aleatorio del segundo dado)
        pi_suma_dados:int (suma de los resultados de ambos dados)
        pi_paridad:str (clasificación de la suma como Par o Impar)
        pi_opcion_usuario:str (opción para seguir jugando o salir)
        pi_nombre_valido:int (indica si el nombre ingresado no esta vacio)
        pi_salir:int (indica si se debe salir de la funcion sin jugar)
        pi_solo_digitos:int (bandera: 1 si todos los caracteres son digitos)
        pi_indice_digito:int (posicion para recorrer cada caracter de la entrada)
        pi_caracter:str (caracter actual siendo evaluado)
    """
    global pi_nombre_ultimo_jugador, pi_cantidad_jugadores
    pi_juego_activo = True

    print("\n================================================\n")
    print ("  ♠ Juego: Dados ♠")
    print ("  Adiviná si la suma de los dados será par o impar\n")
    print("================================================\n")

    # Validacion de nombre sin break
    pi_nombre_valido = 0
    while pi_nombre_valido == 0:
        pi_nombre_jugador = input("Escribe tu nombre: ").strip()
        if pi_nombre_jugador != "":
            pi_nombre_valido = 1
        else:
            print("\n  ✗ Nombre vacío: Por favor escribe tu nombre\n")

    pi_indice_jugador = buscar_jugador(
        pi_nombres,
        pi_cantidad_jugadores,
        pi_nombre_jugador
    )

    pi_salir = 0

    if pi_indice_jugador == -1:
        if pi_cantidad_jugadores == MAX_JUGADORES:
            print("\n  ✗ No hay cupos para nuevos jugadores.")
            print("  Se alcanzó el límite de 10 jugadores.")
            input("\nPresione la tecla 'Enter' para continuar...")
            pi_salir = 1

        if pi_salir == 0:
            pi_nombres[pi_cantidad_jugadores] = pi_nombre_jugador
            pi_jugadas[pi_cantidad_jugadores] = 0
            pi_ganadas[pi_cantidad_jugadores] = 0
            pi_perdidas[pi_cantidad_jugadores] = 0
            pi_creditos[pi_cantidad_jugadores] = 1000

            pi_indice_jugador = pi_cantidad_jugadores
            pi_cantidad_jugadores = pi_cantidad_jugadores + 1

            print(f"\n  ✓ Nuevo jugador registrado: {pi_nombre_jugador}")
    else:
        print(f"\n  ✓ Bienvenido nuevamente, {pi_nombres[pi_indice_jugador]}")

    if pi_salir == 0:
        pi_nombre_ultimo_jugador = pi_nombre_jugador
        print(f"\n| Bienvenido, {pi_nombre_jugador} ♠          |")
        while pi_juego_activo:
            if pi_creditos[pi_indice_jugador] == 0:
                print("\n  ✗ Te quedaste sin crédito.")
                print("  No podés continuar jugando.")
                pi_juego_activo = False
            else:
                print(f"\nCrédito disponible: ${pi_creditos[pi_indice_jugador]}")

                pi_apuesta_valida = False

                while pi_apuesta_valida == False:
                    pi_entrada_apuesta = input("Ingresá el monto de la apuesta: $").strip()

                    # Validacion de digitos sin isdigit(), len() ni for():
                    # Se verifica que el string no este vacio y se recorre cada
                    # caracter mediante while indexado.
                    pi_solo_digitos = 0
                    if pi_entrada_apuesta != "":
                        pi_solo_digitos = 1
                        pi_indice_digito = 0
                        while pi_indice_digito < 10 and pi_solo_digitos == 1:
                            pi_caracter = pi_entrada_apuesta[pi_indice_digito]
                            if pi_caracter < '0' or pi_caracter > '9':
                                pi_solo_digitos = 0
                            pi_indice_digito = pi_indice_digito + 1

                    if pi_solo_digitos == 0:
                        print("  ✗ La apuesta debe ser un número entero.")
                    else:
                        pi_apuesta = pi_convertir_a_entero(pi_entrada_apuesta)

                        if pi_apuesta <= 0:
                            print("  ✗ La apuesta debe ser mayor que cero.")
                        elif pi_apuesta > pi_creditos[pi_indice_jugador]:
                            print("  ✗ No podés apostar más de tu crédito.")
                        else:
                            pi_apuesta_valida = True
                pi_tipo_apuesta = input("\nApuestas por: 1) Par | 2) Impar\n> ")
                while pi_tipo_apuesta != "1" and pi_tipo_apuesta != "2":
                    print("\n  ✗ Opción inválida. Ingresá 1 para Par o 2 para Impar.\n")
                    pi_tipo_apuesta = input("\nApuestas por: 1) Par | 2) Impar\n> ")
                if pi_tipo_apuesta == "1":
                    print("\nApostaste por Par ✓\n")
                else:
                    print("\nApostaste por Impar ✓\n")
                pi_dado_1 = random.randint(1,6)
                pi_dado_2 = random.randint(1,6)
                pi_suma_dados = pi_dado_1 + pi_dado_2
                if pi_suma_dados % 2 == 0:
                    pi_paridad = "Par"
                else:
                    pi_paridad = "Impar"
                print("  ~ Tirando dados ⚀⚁⚂⚃⚄⚅ ~")
                print("  ─────────────────")
                if pi_paridad == "Par":
                    print(f"  Resultado: {pi_suma_dados}  →  PAR ♠")
                else: 
                    print(f"  Resultado: {pi_suma_dados}  →  IMPAR ♠")
                print("  ─────────────────")
                pi_jugadas[pi_indice_jugador] = pi_jugadas[pi_indice_jugador] + 1

                if (
                    (pi_paridad == "Par" and pi_tipo_apuesta == "1")
                    or
                    (pi_paridad == "Impar" and pi_tipo_apuesta == "2")
                ):
                    pi_ganadas[pi_indice_jugador] = pi_ganadas[pi_indice_jugador] + 1

                    pi_creditos[pi_indice_jugador] = (
                        pi_creditos[pi_indice_jugador] + pi_apuesta
                    )

                    print(f"\nGanaste ${pi_apuesta} ✓")
                else:
                    pi_perdidas[pi_indice_jugador] = pi_perdidas[pi_indice_jugador] + 1

                    pi_creditos[pi_indice_jugador] = (
                        pi_creditos[pi_indice_jugador] - pi_apuesta
                    )

                    print(f"\nPerdiste ${pi_apuesta} ✗")
                print("\n+--------------------------------+")
                print(f"  Jugador: {pi_nombres[pi_indice_jugador]}")
                print(f"  Jugadas: {pi_jugadas[pi_indice_jugador]}")
                print(f"  Ganadas: {pi_ganadas[pi_indice_jugador]}")
                print(f"  Perdidas: {pi_perdidas[pi_indice_jugador]}")
                print(f"  Crédito: ${pi_creditos[pi_indice_jugador]}")
                print("+--------------------------------+")
                pi_opcion_usuario = (input("\nElige una opción: 1) Seguir jugando 2) Salir \n> "))
                while pi_opcion_usuario != "1" and pi_opcion_usuario != "2":
                    print("\n✗ Opción inválida. Presiona tecla 1 para jugar o tecla 2 para salir.\n")
                    pi_opcion_usuario = (input("\nElige una opción: 1) Seguir jugando 2) Salir \n> "))
                if pi_opcion_usuario == "2":
                    print("+----------------------------+")
                    print("|                            |")
                    print("|   ♠  G A M E  O V E R  ♠   |")
                    print("|                            |")
                    print("+----------------------------+")
                    pi_juego_activo = False
                    print("\nSaliendo al menú principal...")

        


def reporte_ordenar_indices(valores, cantidad, descendente):
    """
    ALGORITMO: Ordenamiento por seleccion.
    Se construye un arreglo auxiliar de indices. En cada paso se busca
    el mayor (o menor) valor entre las posiciones restantes y se coloca
    en la siguiente posicion del arreglo de indices. Al final se devuelve
    el arreglo de indices ordenado, sin modificar el arreglo original.

    VARIABLES LOCALES
        valores:list (arreglo cuyos valores determinan el orden de las posiciones)
        cantidad:int (cantidad de posiciones ocupadas que deben ordenarse)
        descendente:bool (indica si el orden debe ser de mayor a menor)
        indices:list (arreglo auxiliar con las posiciones de los jugadores)
        indice:int (posición utilizada para inicializar el arreglo de índices)
        posicion:int (posición que se está ordenando mediante selección)
        posicion_elegida:int (posición del menor o mayor valor encontrado)
        comparacion:int (posición utilizada para comparar los valores restantes)
        valor_comparado:int (valor correspondiente a la posición que se compara)
        valor_elegido:int (valor correspondiente a la posición seleccionada)
        auxiliar:int (variable temporal utilizada para intercambiar dos índices)
    """
    indices = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    indice = 0

    while indice < cantidad:
        indices[indice] = indice
        indice = indice + 1

    posicion = 0
    while posicion < cantidad - 1:
        posicion_elegida = posicion
        comparacion = posicion + 1

        while comparacion < cantidad:
            valor_comparado = valores[indices[comparacion]]
            valor_elegido = valores[indices[posicion_elegida]]

            if descendente:
                if valor_comparado > valor_elegido:
                    posicion_elegida = comparacion
            else:
                if valor_comparado < valor_elegido:
                    posicion_elegida = comparacion

            comparacion = comparacion + 1

        auxiliar = indices[posicion]
        indices[posicion] = indices[posicion_elegida]
        indices[posicion_elegida] = auxiliar
        posicion = posicion + 1

    return indices


def reporte_mostrar_jugadores_ordenados(nombres, valores, cantidad, titulo, descendente):
    """
    VARIABLES LOCALES
        nombres:list (arreglo de nombres que se mostrará en el reporte)
        valores:list (arreglo de victorias asociado a los nombres)
        cantidad:int (cantidad de jugadores registrados que deben mostrarse)
        titulo:str (título identificador del juego informado)
        descendente:bool (indica el sentido del ordenamiento)
        indices:list (posiciones ordenadas devueltas por el procedimiento de selección)
        posicion:int (posición utilizada para recorrer los índices ordenados)
        indice_jugador:int (posición real del jugador dentro de los arreglos)
    """
    print(f"\n--- {titulo} ---")

    if cantidad == 0:
        print("No hay jugadores registrados.")
    else:
        indices = reporte_ordenar_indices(valores, cantidad, descendente)
        posicion = 0

        while posicion < cantidad:
            indice_jugador = indices[posicion]
            print(f"{nombres[indice_jugador]} - Ganadas: {valores[indice_jugador]}")
            posicion = posicion + 1


def reporte_jugadores_por_victorias():
    """
    VARIABLES LOCALES
        No utiliza variables locales propias; invoca el reporte ordenado de victorias
        para Número Secreto, Blackjack y Par o Impar.
    """
    reporte_mostrar_jugadores_ordenados(
        ns_nombres, ns_ganadas, ns_cantidad_jugadores,
        "NÚMERO SECRETO", True
    )
    reporte_mostrar_jugadores_ordenados(
        bj_jugadores, bj_ganadas, bj_cantidad_jugadores,
        "BLACKJACK", True
    )
    reporte_mostrar_jugadores_ordenados(
        pi_nombres, pi_ganadas, pi_cantidad_jugadores,
        "PAR O IMPAR", True
    )


def reporte_juegos_por_jugador():
    """
    VARIABLES LOCALES
        nombre_buscado:str (nombre ingresado para consultar sus juegos y estadísticas)
        encontrado:bool (indica si el nombre fue localizado en al menos un juego)
        mm_indice_jugador:int (posición del jugador en Mayor o Menor)
        ns_indice_jugador:int (posición del jugador en Número Secreto)
        bj_indice_jugador:int (posición del jugador en Blackjack)
        pi_indice_jugador:int (posición del jugador en Par o Impar)
    """
    nombre_buscado = input("\nIngresá el nombre del jugador: ").strip()
    encontrado = False

    mm_indice_jugador = buscar_jugador(
        mm_nombres, mm_cantidad_jugadores, nombre_buscado
    )
    if mm_indice_jugador != -1:
        encontrado = True
        print(
            "Mayor o Menor - Racha:",
            mm_rachas[mm_indice_jugador]
        )

    ns_indice_jugador = buscar_jugador(
        ns_nombres, ns_cantidad_jugadores, nombre_buscado
    )
    if ns_indice_jugador != -1:
        encontrado = True
        print(
            "Número Secreto - Jugadas:", ns_jugadas[ns_indice_jugador],
            "- Ganadas:", ns_ganadas[ns_indice_jugador],
            "- Perdidas:", ns_perdidas[ns_indice_jugador]
        )

    bj_indice_jugador = buscar_jugador(
        bj_jugadores, bj_cantidad_jugadores, nombre_buscado
    )
    if bj_indice_jugador != -1:
        encontrado = True
        print(
            "Blackjack - Jugadas:", bj_jugadas[bj_indice_jugador],
            "- Ganadas:", bj_ganadas[bj_indice_jugador],
            "- Perdidas:", bj_perdidas[bj_indice_jugador],
            "- Empatadas:", bj_empatadas[bj_indice_jugador]
        )

    pi_indice_jugador = buscar_jugador(
        pi_nombres, pi_cantidad_jugadores, nombre_buscado
    )
    if pi_indice_jugador != -1:
        encontrado = True
        print(
            "Par o Impar - Jugadas:", pi_jugadas[pi_indice_jugador],
            "- Ganadas:", pi_ganadas[pi_indice_jugador],
            "- Perdidas:", pi_perdidas[pi_indice_jugador],
            "- Crédito: $", pi_creditos[pi_indice_jugador]
        )

    if encontrado == False:
        print("\n✗ No se encontró ese jugador.")


def reporte_creditos_par_impar():
    """
    VARIABLES LOCALES
        indices:list (posiciones de los jugadores ordenadas por crédito ascendente)
        posicion:int (posición utilizada para recorrer el arreglo de índices)
        pi_indice_jugador:int (posición real del jugador en los arreglos de Par o Impar)
    """
    print("\n--- CRÉDITOS DE PAR O IMPAR ---")

    if pi_cantidad_jugadores == 0:
        print("No hay jugadores registrados.")
    else:
        indices = reporte_ordenar_indices(
            pi_creditos, pi_cantidad_jugadores, False
        )
        posicion = 0

        while posicion < pi_cantidad_jugadores:
            pi_indice_jugador = indices[posicion]
            print(
                pi_nombres[pi_indice_jugador],
                "- Crédito: $",
                pi_creditos[pi_indice_jugador]
            )
            posicion = posicion + 1


def reporte_racha_mayor_menor():
    """
    VARIABLES LOCALES
        nombre_buscado:str (nombre ingresado para consultar su racha)
        mm_indice_jugador:int (posición del jugador en los arreglos de Mayor o Menor)
    """
    nombre_buscado = input("\nIngresá el nombre del jugador: ").strip()
    mm_indice_jugador = buscar_jugador(
        mm_nombres, mm_cantidad_jugadores, nombre_buscado
    )

    if mm_indice_jugador == -1:
        print("\n✗ El jugador no participó en Mayor o Menor.")
    else:
        print(
            "\nJugador:", mm_nombres[mm_indice_jugador],
            "- Racha:", mm_rachas[mm_indice_jugador]
        )


def reporte():
    """
    VARIABLES LOCALES
        reporte_opcion:str (opción ingresada dentro del submenú de reportes)
    """
    reporte_opcion = ""

    while reporte_opcion != "E":
        print("\n========== REPORTES ==========")
        print("A - Jugadores ordenados por victorias")
        print("B - Juegos jugados por un jugador")
        print("C - Créditos de Par o Impar")
        print("D - Racha de Mayor o Menor")
        print("E - Volver al menú principal")

        reporte_opcion = input("Ingrese una opción: ").strip().upper()

        if reporte_opcion == "A":
            reporte_jugadores_por_victorias()
        elif reporte_opcion == "B":
            reporte_juegos_por_jugador()
        elif reporte_opcion == "C":
            reporte_creditos_par_impar()
        elif reporte_opcion == "D":
            reporte_racha_mayor_menor()
        elif reporte_opcion == "E":
            print("\nVolviendo al menú principal...")
        else:
            print("\n✗ Opción inválida.")

        if reporte_opcion != "E":
            input("\nPresione la tecla 'Enter' para continuar...")


def main():
    """
    VARIABLES LOCALES
        menu_opcion:str (opción ingresada dentro del menú principal)
        salir_programa:int (indica si se debe terminar el programa)
    """
    # no se pide nombre en main; se pide en cada juego individual
    menu_opcion = ""
    salir_programa = 0
    while menu_opcion != "S" and salir_programa == 0:
        print("\n........MENU PRINCIPAL.")
        print("A - Mayor o Menor")
        print("B - Numero Secreto")
        print("C - BlackJack Simple")
        print("D - Dados (Par o Impar)")
        print("E - Reporte")
        print("S - Fin DEL PROGRAMA")
        menu_opcion = input("Ingrese su opcion: ").strip().upper()
        while menu_opcion == "" or (menu_opcion != "A" and menu_opcion != "B" and menu_opcion != "C" and menu_opcion != "D" and menu_opcion != "E" and menu_opcion != "S"):
            menu_opcion = input("Ingreso invalido - reintente: ").strip().upper()

        match menu_opcion:
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
                juego_par_o_impar()
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
                salir_programa = 1
                
            

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
    
    
mostrar_advertencia()
