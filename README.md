# TP1_AyED

VARIABLES GLOBALES
    a_nombre, b_nombre_jugador, d_nombre_jugador:str
    a_racha, a_racha_max, a_veces_jugado, b_veces_jugado, b_veces_ganado, b_veces_perdido, d_veces_jugado, d_veces_ganado, d_veces_perdido :int

    a_nombre:str (nombre del último jugador del juego A)
    a_racha:int (racha de la partida)
    a_racha_max:int (racha maxima de todas las partidas)
    a_veces_jugado:int (cantidad total de partidas jugadas)
    b_nombre_jugador:str (nombre del último jugador del juego B)
    b_veces_jugado:int (cantidad total de partidas jugadas)
    b_veces_ganado:int (cantidad de partidas ganadas)
    b_veces_perdido:int (cantidad de partidas perdidas)
    nombre_jugador_dados: str (nombre del jugador)
    veces_jugado_dados: int (cantidad de veces jugado, solo cuenta al iniciar)
    veces_ganado_dados: int (veces que el usuario acierta si es par o impar)
    veces_perdido_dados: int (veces que el usuario no acierta)
"""

"""Variables Locales Juego Mayor-Menor:
    a, nreferencia, ncomparar:int
    opcion:str
    
    a:int (corta el while al cambiar a 1)
    nreferencia:int (numero mostrado en pantalla, se debe adivinar si el siguiente es mayor o menor)
    ncomparar:int (nreferenca se compara con este)
    opcion:string (puede valer mayor o menor, es la opcion elegida por el usuario)

    """

    Variables locales juego B:
        MAX_INTENTOS, RANGO_MIN, RANGO_MAX, numero_secreto, intento_actual, intentos_usados, indice, intentos_restantes:int
        adivino, entrada_valida, es_numero:bool

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




    """
    Variables locales juego D:
        dado1, dado2, suma_dados:int
        juego_activo:bool
        tipo_de_apuesta, opcion_usuario, paridad:str

    """

# ─────────────────────────────────────
# Nombre del módulo: Juego Dados
# Variables:
#   juego_activo : bool (booleano para el bucle principal)
#   tipo_de_apuesta: str (elección del usuario si es par o impar)
#   opcion_usuario : str (opción de seguir jugando o salir)
#   dado1: int (número aleatorio del dado 1)
#   dado2: int (número aleatorio del dado 1)
#   suma_dados: int (suma de los dados)
#   paridad: str (resultado de la suma de dados si es par o impar)
# ─────────────────────────────────────