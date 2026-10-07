import random


def juego1():
    cont = 0
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
                cont = cont + 1
                nreferencia = ncomparar
            else:
                a = 1
        else:
            if nreferencia > ncomparar:
                cont = cont + 1
                nreferencia = ncomparar
            else:
                a = 1

    print("Game Over", nombre)
    print("Aciertos:", cont)


juego1()
