import pickle
import os

#se declara la estructura de datos que vamos a utilizar
class Contacto:
    def __init__(self):
        self.codigo = 0
        self.nombreYApellido =""
        self.telefono =""
        self.mail =""
        self.baja =""

#Verifico si el archivo existe, si no existe lo creo
def abrirArchivo():
    global arFiContacto
    global arLoContacto
    arFiContacto = "Contacto.dat"
    if os.path.exists(arFiContacto):
        arLoContacto = open(arFiContacto, "r+b")
    else:
        print (f"El archivo {arFiContacto} No existía y fue creado")
        arLoContacto = open(arFiContacto, "w+b")
    input()

def ordenarContactosPorNombre():
    global arFiContacto
    global arLoContacto
    con1 = Contacto()
    con2 = Contacto()
    arLoContacto.seek(0, 0)
    con1 = pickle.load(arLoContacto)
    tamReg = arLoContacto.tell()
    tamArc = os.path.getsize(arFiContacto)
    cantReg = tamArc // tamReg
    for i in range(cantReg - 1):
        for j in range(i + 1, cantReg):
            arLoContacto.seek(i * tamReg, 0)
            con1 = pickle.load(arLoContacto)
            arLoContacto.seek(j * tamReg, 0)
            con2 = pickle.load(arLoContacto)
            if con1.nombreYApellido > con2.nombreYApellido:
                arLoContacto.seek(i * tamReg, 0)
                pickle.dump(con2, arLoContacto)
                arLoContacto.flush()
                arLoContacto.seek(j * tamReg, 0)
                pickle.dump(con1, arLoContacto)
                arLoContacto.flush()

def crearContacto():
    con = Contacto()
    continuar = str(input("¿Seguro que vas a crear contactos (S/N)?: "))
    continuar = continuar.upper()
    while continuar != "S" and continuar != "N":
        print("Por favor, solo S o N")
        continuar = str(input("¿Seguro que vas a crear contactos (S/N)?: "))
        continuar = continuar.upper()
    while continuar == "S":
        if os.path.getsize(arFiContacto) == 0:
            con.codigo = 1
        else:
            arLoContacto.seek(0, 0)
            con = pickle.load(arLoContacto)
            tamReg = arLoContacto.tell()
            tamArc = os.path.getsize(arFiContacto)
            cantReg = tamArc // tamReg
            con.codigo = cantReg + 1
        # Ingreso y formateo del campon nombreYApellido
        nomYApe = str(input("Ingresar nombre y apellido (Max. 30 caracteres): "))
        while len(nomYApe) > 30:
            print("Solo 30 caracteres")
            nomYApe = str(input("Ingresar nombre y apellido (Max. 30 caracteres): "))
        if len(nomYApe) < 30:
            con.nombreYApellido = nomYApe.ljust(30, " ")
        elif len(nomYApe) == 30:
            con.nombreYApellido = nomYApe

        # Ingreso y formateo del campon telefono
        tel = str(input("Ingresar número de teléfono (Max. 15 caracteres): "))
        while len(tel) > 15:
            print("Solo 15 caracteres")
            tel = str(input("Ingresar número de teléfono (Max. 15 caracteres): "))
        if len(tel) < 15:
            con.telefono = tel.ljust(15, " ")
        elif len(tel) == 15:
            con.telefono = tel

        # Ingreso y formateo del campon mail
        mail = str(input("Ingresar mail (Max. 30 caracteres): "))
        while len(mail) > 30:
            print("Solo 30 caracteres")
            mail = str(input("Ingresar mail (Max. 30 caracteres): "))
        if len(mail) < 30:
            con.mail = mail.ljust(30, " ")
        elif len(mail) == 30:
            con.mail = mail

        con.baja = "N"
        arLoContacto.seek(0, 2)
        u = arLoContacto.tell()
        pickle.dump(con, arLoContacto)
        arLoContacto.flush()
        arLoContacto.seek(u, 0)
        con = pickle.load(arLoContacto)
        print(con.codigo, "    ", con.nombreYApellido, "    ", con.telefono, "    ", con.mail)
        continuar = str(input("¿Ingresas otro contacto (S/N)?: "))
        continuar = continuar.upper()
        while continuar != "S" and continuar != "N":
            print("Por favor, solo S o N")
            continuar = str(input("¿Seguro que vas a crear contactos (S/N)?: "))
            continuar = continuar.upper()

    ordenarContactosPorNombre()
    arLoContacto.flush()
    arLoContacto.seek(0, 0)
    print("Codigo      Nombre y Apellido        Telefono           Mail")
    while arLoContacto.tell() < os.path.getsize(arFiContacto):
        con = pickle.load(arLoContacto)
        print(con.codigo, "    ", con.nombreYApellido, "    ", con.telefono, "    ", con.mail)

def buscarDicoContacto(n):
    global arFiContacto
    global arLoContacto
    arLoContacto.seek(0, 0)
    con = pickle.load(arLoContacto)
    tamReg = arLoContacto.tell()
    tamArc = os.path.getsize(arFiContacto)
    cantReg = tamArc // tamReg
    pri = 0
    ult = cantReg
    med = (ult + pri) // 2
    arLoContacto.seek(med * tamReg, 0)
    p = arLoContacto.tell()
    con = pickle.load(arLoContacto)
    nomyape = con.nombreYApellido.rstrip()
    while nomyape != n and pri < ult:
        if nomyape > n:
            ult = med - 1
        else:
            pri = med + 1
        med = (ult + pri) // 2
        p = med * tamReg
        arLoContacto.seek(med * tamReg, 0)
        con = pickle.load(arLoContacto)
        nomyape = con.nombreYApellido.rstrip()
    if nomyape == n:
        return p
    else:
        return -1

def mostrarContacto():
    global arFiContacto
    global arLoContacto
    con = Contacto()
    nya = str(input("Ingresar el nombre o apellido del contacto a buscar: "))
    pos = buscarDicoContacto(nya)
    if pos != -1:
        arLoContacto.seek(pos, 0)
        con = pickle.load(arLoContacto)
        print("Nombre: ", con.nombreYApellido)
        print("Telefono: ", con.telefono)
    else:
        print("El contacto no fue encontrado")
    input()

def modificarContacto():
    global arFiContacto
    global arLoContacto
    con = Contacto()
    nya = str(input("Ingresar el nombre o apellido del contacto a buscar: "))
    pos = buscarDicoContacto(nya)
    if pos != -1:
        arLoContacto.seek(pos, 0)
        con = pickle.load(arLoContacto)
        if con.baja == "N":
            print("1- Nombre: ", con.nombreYApellido)
            print("2- Telefono: ", con.telefono)
            print("3- Mail: ", con.mail)
            atributo = int(input("Ingresar el númemero del daro a modificar: "))
            while not validarIngresoEntero(atributo, 1, 3):
                print("Un número entre 1 y 3")
                atributo = int(input("Ingresar el númemero del daro a modificar: "))
            if atributo == 1:
                nomYApe = str(input("Ingresar nombre y apellido (Max. 30 caracteres): "))
                while len(nomYApe) > 30:
                    print("Solo 30 caracteres")
                    nomYApe = str(input("Ingresar nombre y apellido (Max. 30 caracteres): "))
                if len(nomYApe) < 30:
                    con.nombreYApellido = nomYApe.ljust(30, " ")
                elif len(nomYApe) == 30:
                    con.nombreYApellido = nomYApe
                print("Los nuevos datos del contacto son: ")
                print("1- Nombre: ", con.nombreYApellido)
                mail = str(input("Ingresar mail (Max. 30 caracteres): "))
                while len(mail) > 30:
                    print("Solo 30 caracteres")
                    mail = str(input("Ingresar mail (Max. 30 caracteres): "))
                if len(mail) < 30:
                    con.mail = mail.ljust(30, " ")
                elif len(mail) == 30:
                    con.mail = mail
                print("Los nuevos datos del contacto son: ")
                print("1- Nombre: ", con.nombreYApellido)
                print("2- Telefono: ", con.telefono)
                print("3- Mail: ", con.mail)
            arLoContacto.seek(pos, 0)
            pickle.dump(con, arLoContacto)
            arLoContacto.flush()
        else:
            print("El contacto está eliminado")
    else:
        print("El contacto no fue encontrado")
    input()

def eliminarContacto():
    global arFiContacto
    global arLoContacto
    con = Contacto()
    nya = str(input("Ingresar el nombre o apellido del contacto a buscar: "))
    pos = buscarDicoContacto(nya)
    if pos != -1:
        arLoContacto.seek(pos, 0)
        con = pickle.load(arLoContacto)
        if con.baja == "N":
            con.baja = "S"
            arLoContacto.seek(pos, 0)
            pickle.dump(con, arLoContacto)
            arLoContacto.flush()
            print("El contacto: ", con.nombreYApellido, " fue dado de baja")
        else:
            print("El contacto ya está eliminado")
    else:
        print("El contacto no fue encontrado")
    input()

def mostrarLibreta():
    global arFiContacto
    global arLoContacto
    con = Contacto()
    arLoContacto.seek(0, 0)
    print("Codigo      Nombre y Apellido        Telefono           Mail")
    while arLoContacto.tell() < os.path.getsize(arFiContacto):
        con = pickle.load(arLoContacto)
        if con.baja == "N":
            print(con.codigo, "    ", con.nombreYApellido, "    ", con.telefono, "    ", con.mail)

def salir():
    global arFiContacto
    global arLoContacto
    cerrarArchivos()
    print("Saliendo del programa...")
    input()

#cierra el archivo de contactos
def cerrarArchivos():
    arLoContacto.close()

def mostrarMenu():
    os.system("clear" if os.name == "posix" else "cls")
    print("1. Agregar contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Modificar contacto")
    print("5. Eliminar contacto")
    print("6. Mostrar libreta")
    print("0. Salir")

def validarIngresoEntero(x, y, z):
    try:
        valor = int(x)
        if y <= valor <= z:
            return True
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")
            return False
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return False

def ejecutarCase(o):
    if o == 1:
        crearContacto()
    elif o == 2:
        mostrarLibreta()
    elif o == 3:
        mostrarContacto()
    elif o == 4:
        modificarContacto()
    elif o == 5:
        eliminarContacto()
    elif o == 6:
        mostrarLibreta()
    elif o == 0:
        print("Saliendo del programa...")
        salir()
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")

def menu():
    mostrarMenu()
    opcion = input("Ingrese una opción: ")
    while not validarIngresoEntero(opcion, 0, 6):
        opcion = input("Ingrese la opción deseada: ")
    opcion = int(opcion)
    ejecutarCase(opcion)
    while opcion != 0:
        mostrarMenu()
        opcion = input("Ingrese una opción: ")
        while not validarIngresoEntero(opcion, 0, 6):
            opcion = input("Ingrese la opción deseada: ")
        opcion = int(opcion)
        ejecutarCase(opcion)
    input()

#Aca comienza nuestro programa principal
global arFiContacto
global arLoContacto 

abrirArchivo()
menu()
cerrarArchivos()