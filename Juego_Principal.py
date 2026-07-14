import random
import sys
import os


"""
Nombre de los integrantes del grupo:
- Angel Jose Ayala
- Gabriela Iglesias
- Maximiliano Iván Campos
- Santiago Nicolás Bolzan

VARIABLES GLOBALES
    a_nombre, b_nombre_jugador, d_nombre_jugador:str
    a_racha, a_racha_max, a_veces_jugado, b_veces_jugado, b_veces_ganado, b_veces_perdido, d_veces_jugado, d_veces_ganado, d_veces_perdido :int

"""
#INICIALIZO VARIABLES GLOBALES
a_nombre = ''
a_racha = 0
a_racha_max = 0
a_veces_jugado = 0


b_nombre_jugador = ""
b_veces_jugado = 0
b_veces_ganado = 0
b_veces_perdido = 0

d_nombre_jugador = ""
d_veces_jugado = 0
d_veces_ganado = 0
d_veces_perdido = 0


def juego1():
    """Variables Locales Juego A:
        a, nreferencia, ncomparar:int
        opcion:str

    """
    global a_nombre, a_racha, a_racha_max, a_veces_jugado
    a_veces_jugado = a_veces_jugado + 1
    a_racha = 0
    a = 0
    a_nombre = input("Cual es tu nombre? ")
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
                a_racha = a_racha + 1
                nreferencia = ncomparar
            else:
                a = 1
        else:
            if nreferencia > ncomparar:
                a_racha = a_racha + 1
                nreferencia = ncomparar
            else:
                a = 1
    if a_racha_max < a_racha:
        a_racha_max = a_racha
    print(a_racha_max)    
    print("Game Over", a_nombre)
    print("Aciertos:", a_racha)
    input("\nPresione la tecla 'Enter' para salir...")


def juego2():
    """
    Variables locales juego B:
        MAX_INTENTOS, RANGO_MIN, RANGO_MAX, numero_secreto, intento_actual, intentos_usados, indice, intentos_restantes:int
        adivino, entrada_valida, es_numero:bool

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


def juego3():
        print("Juego en construcción...")
        input("\nPresione la tecla 'Enter' para continuar...")
        #os.system('cls' if os.name == 'nt' else 'clear')
    

    
def juego4():

    """
    Variables locales juego D:
        dado1, dado2, suma_dados:int
        juego_activo:bool
        tipo_de_apuesta, opcion_usuario, paridad:str

    """

    global d_nombre_jugador
    global d_veces_jugado
    global d_veces_ganado
    global d_veces_perdido
    juego_activo = True
    tipo_de_apuesta = ""
    opcion_usuario = ""
    dado1 = 0
    dado2 = 0
    suma_dados = 0
    paridad = ""

    print("\n================================================\n")
    print ("  ♠ Juego: Dados ♠")
    print ("  Adiviná si la suma de los dados será par o impar\n")
    print("================================================\n")
    # Al iniciar suma a la variable glocal para el reporte
    d_veces_jugado = d_veces_jugado + 1
    # Pido y valido el nombre
    d_nombre_jugador = input("Escribe tu nombre: ")
    while d_nombre_jugador == "":
        print("\n  ✗ Nombre vacío: Por favor escribe tu nombre\n")
        d_nombre_jugador = input("Escribe tu nombre: ")
    print(f"\n| Bienvenido, {d_nombre_jugador} ♠          |")
    # Bucle principal
    while juego_activo:
        # Pido y valido el tipo de juego del usuario
        tipo_de_apuesta = input("\nApuestas por: 1) Par | 2) Impar\n> ")
        while tipo_de_apuesta != "1" and tipo_de_apuesta != "2":
            print("\n  ✗ Opción inválida. Ingresá 1 para Par o 2 para Impar.\n")
            tipo_de_apuesta = input("\nApuestas por: 1) Par | 2) Impar\n> ")
        if tipo_de_apuesta == "1":
            print("\nApostaste por Par ✓\n")
        else:
            print("\nApostaste por Impar ✓\n")
        # Se generan los numeros aleatorios para los dados
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        suma_dados = dado1 + dado2
        # Validamos si el resto es 0 es par
        if suma_dados % 2 == 0:
            paridad = "Par"
        else:
            paridad = "Impar"
        print("  ~ Tirando dados ⚀⚁⚂⚃⚄⚅ ~")
        print("  ─────────────────")
        if paridad == "Par":
            print(f"  Resultado: {suma_dados}  →  PAR ♠")
        else: 
            print(f"  Resultado: {suma_dados}  →  IMPAR ♠")
        print("  ─────────────────")
        # Valido casos ganadores
        if (paridad == "Par" and tipo_de_apuesta == "1") or (paridad == "Impar" and tipo_de_apuesta == "2"):
            # Se suma a la variable global para el reporte
            d_veces_ganado = d_veces_ganado + 1
            print(f"Ganaste ✓\n")
        else:
            # Se suma a la variable global para el reporte
            d_veces_perdido = d_veces_perdido + 1
            print(f"\nPerdiste ✗\n")
        print("\n|----------------------------|+")
        print(f"\n|      Ganados: {d_veces_ganado}")
        print(f"\n|      Perdidos: {d_veces_perdido}")
        print("\n|----------------------------+|")
        # Valido la opción del usuario para seguir jugando o salir
        opcion_usuario = (input("\nElige una opción: 1) Seguir jugando 2) Salir \n> "))
        while opcion_usuario != "1" and opcion_usuario != "2":
            print("\n✗ Opción inválida. Presiona tecla 1 para jugar o tecla 2 para salir.\n")
            opcion_usuario = (input("\nElige una opción: 1) Seguir jugando 2) Salir \n> "))
        if opcion_usuario == "2":
            print("+----------------------------+")
            print("|                            |")
            print("|   ♠  G A M E  O V E R  ♠   |")
            print("|                            |")
            print("+----------------------------+")
            # Al ser False finaliza el bucle principal
            juego_activo = False
            print("\nSaliendo al menú principal...")
            
    


def reporte():
    print('\n--- REPORTE DEL JUGADOR ---')
    if a_nombre != '':
        print('Mayor o Menor - Nombre:', a_nombre, 'Veces jugado: ', a_veces_jugado, '- Mayor racha alcanzada:', a_racha_max)
    if b_nombre_jugador != '':
        print('Número Secreto - Nombre:', b_nombre_jugador, '- Veces jugado:', b_veces_jugado, '- Ganadas:', b_veces_ganado, '- Perdidas:', b_veces_perdido)
    if d_nombre_jugador != '':
        print('Dados (Par o Impar) - Nombre:', d_nombre_jugador, '- Veces jugadas:', d_veces_jugado, '- Ganadas:', d_veces_ganado, '- Perdidas:', d_veces_perdido)
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
        print("F - Fin DEL PROGRAMA")
        opcion = input("Ingrese su opcion: ").strip().upper()
        while opcion == "" or (opcion != "A" and opcion != "B" and opcion != "C" and opcion != "D" and opcion != "E" and opcion != "F"):
            opcion = input("Ingreso invalido - reintente: ").strip().upper()

        match opcion:
            case "A":
                os.system('cls' if os.name == 'nt' else 'clear')
                juego1()
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "B":
                os.system('cls' if os.name == 'nt' else 'clear')
                juego2()
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "C":
                os.system('cls' if os.name == 'nt' else 'clear')
                juego3()
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "D":
                os.system('cls' if os.name == 'nt' else 'clear')
                juego4()
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "E":
                os.system('cls' if os.name == 'nt' else 'clear')
                reporte()
                input("\nPresione la tecla 'Enter' para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')
                
            case "F":
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