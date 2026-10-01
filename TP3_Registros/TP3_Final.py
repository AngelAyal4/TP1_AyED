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