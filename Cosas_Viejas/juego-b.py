import random

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
    nombre_jugador = input("Ingresá tu nombre")
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
