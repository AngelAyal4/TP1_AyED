import pickle
import os
import os.path
import random
 
RUTA_JUGADORES = "C:\\tp3\\jugadores.dat"
CREDITO_INICIAL = 10000.0
 
PAR_IMPAR = 3          # columna de la matriz "juegos" que corresponde a Par/Impar
FILA_GANADAS = 0
FILA_PERDIDAS = 1
 
 
# ----------------------------------------------------------------------
# REGISTRO
# ----------------------------------------------------------------------
class Jugador:
    def __init__(self):
        self.nombre = " " * 30                      # str(30)
        self.creditos = CREDITO_INICIAL             # float
        self.juegos = [[0] * 4 for i in range(2)]   # matriz 2 x 4 de enteros
 
 
# ----------------------------------------------------------------------
# MANEJO DEL ARCHIVO JUGADORES.DAT (acceso directo con pickle)
# ----------------------------------------------------------------------
def buscar_jugador(nombre):
    """Devuelve la posición (en bytes) del jugador en el archivo, o -1 si no existe."""
    pos = -1
    if os.path.exists(RUTA_JUGADORES):
        f = open(RUTA_JUGADORES, "rb")
        tam = os.path.getsize(RUTA_JUGADORES)
        while pos == -1 and f.tell() < tam:
            p = f.tell()
            reg = pickle.load(f)
            if reg.nombre.strip().lower() == nombre.strip().lower():
                pos = p
        f.close()
    return pos
 
 
def alta_jugador(nombre):
    """Agrega un jugador nuevo con crédito inicial al final del archivo y devuelve su posición."""
    reg = Jugador()
    reg.nombre = nombre.strip().ljust(30)[:30]
    f = open(RUTA_JUGADORES, "ab")
    f.seek(0, os.SEEK_END)
    pos = f.tell()
    pickle.dump(reg, f)
    f.flush()
    f.close()
    return pos
 
 
def leer_jugador(pos):
    f = open(RUTA_JUGADORES, "rb")
    f.seek(pos)
    reg = pickle.load(f)
    f.close()
    return reg
 
 
def grabar_jugador(pos, reg):
    """Reescribe el registro en su posición. Devuelve True si se pudo grabar.
    Si el registro nuevo ocupara más bytes que el anterior (un contador que
    pasa de 255), se pisaría al jugador siguiente: en ese caso no se graba."""
    grabado = False
    tam_viejo = len(pickle.dumps(leer_jugador(pos)))
    tam_nuevo = len(pickle.dumps(reg))
    if tam_viejo == tam_nuevo:
        f = open(RUTA_JUGADORES, "r+b")
        f.seek(pos)
        pickle.dump(reg, f)
        f.flush()
        f.close()
        grabado = True
    return grabado
 
 
def obtener_posicion_jugador(nombre):
    """Si el jugador existe devuelve su posición; si no, lo da de alta."""
    pos = buscar_jugador(nombre)
    if pos == -1:
        pos = alta_jugador(nombre)
        print("Jugador nuevo registrado con un crédito inicial de $", CREDITO_INICIAL)
    else:
        print("¡Bienvenido de vuelta,", nombre.strip() + "!")
    return pos
 
 
# ----------------------------------------------------------------------
# ENTRADAS CON VALIDACIÓN
# ----------------------------------------------------------------------
def pedir_nombre():
    nombre = input("Ingrese su nombre de jugador (máx. 30 caracteres): ").strip()
    while nombre == "" or len(nombre) > 30:
        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
        else:
            print("Error: el nombre no puede superar los 30 caracteres.")
        nombre = input("Ingrese su nombre de jugador (máx. 30 caracteres): ").strip()
    return nombre
 
 
def pedir_apuesta(creditos):
    texto = input("¿Cuántos créditos quiere apostar? (disponible: $" + str(creditos) + "): ").strip()
    valida = False
    apuesta = 0
    while not valida:
        if not texto.isdecimal():
            print("Error: ingrese un número entero positivo.")
        else:
            apuesta = int(texto)
            if apuesta <= 0:
                print("Error: la apuesta debe ser mayor a cero.")
            elif apuesta > creditos:
                print("Error: no puede apostar más de lo que tiene ($" + str(creditos) + ").")
            else:
                valida = True
        if not valida:
            texto = input("¿Cuántos créditos quiere apostar? (disponible: $" + str(creditos) + "): ").strip()
    return apuesta
 
 
def pedir_eleccion():
    eleccion = input("¿La suma de los dados será PAR o IMPAR? (P/I): ").strip().upper()
    while eleccion != "P" and eleccion != "I":
        print("Error: ingrese 'P' para par o 'I' para impar.")
        eleccion = input("¿La suma de los dados será PAR o IMPAR? (P/I): ").strip().upper()
    return eleccion
 
 
def preguntar_otra_partida():
    resp = input("¿Quiere jugar otra partida? (S/N): ").strip().upper()
    while resp != "S" and resp != "N":
        print("Error: ingrese 'S' o 'N'.")
        resp = input("¿Quiere jugar otra partida? (S/N): ").strip().upper()
    return resp == "S"
 
 
# ----------------------------------------------------------------------
# JUEGO
# ----------------------------------------------------------------------
def jugar_una_ronda(reg):
    """Juega una ronda y actualiza el registro en memoria. Devuelve True si ganó."""
    apuesta = pedir_apuesta(reg.creditos)
    eleccion = pedir_eleccion()
 
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    es_par = suma % 2 == 0
 
    print("Dados:", dado1, "y", dado2, "-> suma =", suma, "(" + ("PAR" if es_par else "IMPAR") + ")")
 
    gano = (es_par and eleccion == "P") or (not es_par and eleccion == "I")
    if gano:
        reg.creditos = reg.creditos + apuesta
        reg.juegos[FILA_GANADAS][PAR_IMPAR] = reg.juegos[FILA_GANADAS][PAR_IMPAR] + 1
        print("¡GANASTE! Se le suman $" + str(apuesta) + ".")
    else:
        reg.creditos = reg.creditos - apuesta
        reg.juegos[FILA_PERDIDAS][PAR_IMPAR] = reg.juegos[FILA_PERDIDAS][PAR_IMPAR] + 1
        print("LO LAMENTO HAS PERDIDO. Se le restan $" + str(apuesta) + ".")
    print("Crédito actual: $" + str(reg.creditos))
    return gano
 
 
def jugar_par_impar():
    print("=" * 40)
    print("        JUEGO DE PAR O IMPAR")
    print("=" * 40)
    nombre = pedir_nombre()
    pos = obtener_posicion_jugador(nombre)
 
    aciertos = 0       # veces que acertó en esta sesión
    jugadas = 0
    seguir = True
    while seguir:
        reg = leer_jugador(pos)
        if reg.creditos <= 0:
            print("Se quedó sin créditos, ya no puede jugar.")
            seguir = False
        else:
            if jugar_una_ronda(reg):
                aciertos = aciertos + 1
            jugadas = jugadas + 1
            if grabar_jugador(pos, reg):
                if reg.creditos <= 0:
                    print("Se quedó sin créditos, ya no puede jugar.")
                    seguir = False
                else:
                    seguir = preguntar_otra_partida()
            else:
                print("Error: no se pudo actualizar el registro del jugador en el archivo.")
                seguir = False
    print("Aciertos en esta sesión:", aciertos, "de", jugadas, "jugadas.")
    print("Volviendo al menú principal...")
 
 
# Para probarlo solo (en el programa final se llama desde el menú, opción d)
if __name__ == "__main__":
    jugar_par_impar()
 