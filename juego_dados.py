import random

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

    '''
    ############################################################################################
    NOTA PARA ANGEL (QUITAR LUEGO DE IMPLEMENTAR)
    
    # Agregar estas variables antes de esta función, son las globales que sirven para el reporte
    
    vecesJugadoDados = 0
    vecesPerdidoDados = 0
    vecesGanadoDados = 0

    # Importar esta librería al principio del archivo principal

    import random
    ############################################################################################
    '''

    global nombreJugador
    global vecesJugadoDados
    global vecesGanadoDados
    global vecesPerdidoDados
    juegoActivo = True


    print("\n================================================\n")
    print ("  ♠ Juego: Dados ♠")
    print ("  Adiviná si la suma de los dados será par o impar\n")
    print("================================================\n")
    vecesJugadoDados = vecesJugadoDados + 1
    nombreJugador = input("Escribe tu nombre: ")
    while nombreJugador == "":
        print("\n  ✗ Nombre vacío: Por favor escribe tu nombre\n")
        nombreJugador = input("Escribe tu nombre: ")
    print(f"\n| Bienvenido, {nombreJugador} ♠          |")
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
        pi_jugadas[indice_jugador] = pi_jugadas[indice_jugador] + 1

        if (
            (paridad == "Par" and tipoDeApuesta == "1")
            or
            (paridad == "Impar" and tipoDeApuesta == "2")
        ):
            pi_ganadas[indice_jugador] = pi_ganadas[indice_jugador] + 1

            pi_creditos[indice_jugador] = (
                pi_creditos[indice_jugador] + apuesta
            )

            print(f"\nGanaste ${apuesta} ✓")
        else:
            pi_perdidas[indice_jugador] = pi_perdidas[indice_jugador] + 1

            pi_creditos[indice_jugador] = (
                pi_creditos[indice_jugador] - apuesta
            )

            print(f"\nPerdiste ${apuesta} ✗")
        print("\n+--------------------------------+")
        print(f"  Jugador: {pi_nombres[indice_jugador]}")
        print(f"  Jugadas: {pi_jugadas[indice_jugador]}")
        print(f"  Ganadas: {pi_ganadas[indice_jugador]}")
        print(f"  Perdidas: {pi_perdidas[indice_jugador]}")
        print(f"  Crédito: ${pi_creditos[indice_jugador]}")
        print("+--------------------------------+")
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
            
    