import os.path
import pickle
import os
import os.path

class Contacto:
    def __init__(self):
        self.codigo = 0
        self.nombreYApellido = ""
        self.telefono = ""
        self.mail = ""
        self.baja = ""


def abrirArchivo():
    global arFiContacto
    global arLoContacto
    arFiContacto = "contacto.dat"
    if os.path.exists(arFiContacto):
        arLoContacto = open(arFiContacto, "r+b")
    else:
        print("El archivo " + arFiContacto + " NO existía y fue creado")
        arLoContacto = open(arFiContacto, "w+b")


def validarIngresoEntero(x, y, z):
    try:
        valor = int(x)
        if valor >= y and valor <= z:
            return True
        else:
            print(f"Por favor, ingrese un valor entre {y} y {z}")
            return False
    except ValueError:
        print(f"Por favor, ingrese un valor entero")
        return False


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
                arLoContacto.flush
                arLoContacto.seek(j * tamReg, 0)
                pickle.dump(con1, arLoContacto)
                arLoContacto.flush

# R de CRUD
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

# C de CRUD
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
            nomYApe = str(input("Ingresar número de teléfono (Max. 15 caracteres): "))
        if len(tel) < 15:
            con.telefono = tel.ljust(15, " ")
        elif len(tel) == 15:
            con.telefono = tel

        # Ingreso y formateo del campo mail
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
        print("Codigo        Nombre y Apellido          Telefono          Mail")
        while arLoContacto.tell() < os.path.getsize(arFiContacto):
            con = pickle.load(arLoContacto)
            print(con.codigo, "    ", con.nombreYApellido, "    ", con.telefono, "    ", con.mail)

# R de CRUD
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

# U de CRUD
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
            atributo = int(input("Ingrear el númemero del daro a modificar: "))
            while not validarIngresoEntero(atributo, 1, 3):
                print("Un número entre 1 y 3")
                atributo = int(input("Ingrear el númemero del daro a modificar: "))
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
                print("2- Telefono: ", con.telefono)
                print("3- Mail: ", con.mail)
            elif atributo == 2:
                # Ingreso y formateo del campon telefono
                tel = str(input("Ingresar número de teléfono (Max. 15 caracteres): "))
                while len(tel) > 15:
                    print("Solo 15 caracteres")
                    nomYApe = str(input("Ingresar número de teléfono (Max. 15 caracteres): "))
                if len(tel) < 15:
                    con.telefono = tel.ljust(15, " ")
                elif len(tel) == 15:
                    con.telefono = tel
                print("Los nuevos datos del contacto son: ")
                print("1- Nombre: ", con.nombreYApellido)
                print("2- Telefono: ", con.telefono)
                print("3- Mail: ", con.mail)
            elif atributo == 3:
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

# D de CRUD
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
            arLoContacto.flush
            print("El contacto: ", con.nombreYApellido, " fue dado de baja")
        else:
            print("El contacto ya está eliminado")
    else:
        print("El contacto no fue encontrado")
    input()

# R de CRUD
def mostrarLibreta():
    global arFiContacto
    global arLoContacto
    con = Contacto()
    arLoContacto.seek(0, 0)
    print("Codigo    Nombre y Apellido            Telefono       Mail                     ")
    print("_______________________________________________________________________________")
    while arLoContacto.tell() < os.path.getsize(arFiContacto):
        con = pickle.load(arLoContacto)
        if con.baja == "N":
            print(con.codigo, "    ", con.nombreYApellido, con.telefono, con.mail)
    input()

def salir():
    print("Bye Bye")
    input()

def cerrarArchivos():
    arLoContacto.close()

def ejecutarCase(o):
    if o == 1:
        crearContacto()
    if o == 2:
        mostrarContacto()
    if o == 3:
        modificarContacto()
    if o == 4:
        eliminarContacto()
    if o == 5:
        mostrarLibreta()
    if o == 0:
        salir()


def mostrarMenu():
    os.system("cls")
    print("1- Alta")
    print("2 – Mostrar un contacto")
    print("3 – Modificar datos un contacto")
    print("4 – Eliminar contacto (Baja lógica")
    print("5 - Mostrar toda la libreta de contactos")
    print("0 – Fin del programa")


def menu():
    mostrarMenu()
    opcion = input("Ingresar opción deseada: ")
    while not validarIngresoEntero(opcion, 0, 5):
        opcion = input("Ingresar opción deseada: ")
    opcion = int(opcion)
    ejecutarCase(opcion)
    while opcion != 0:
        mostrarMenu()
        opcion = input("Ingresar opción deseada: ")
        while not validarIngresoEntero(opcion, 0, 5):
            opcion = input("Ingresar opción deseada: ")
        opcion = int(opcion)
        ejecutarCase(opcion)



# Acá comienza el programa principal
global arFiContacto
global arLoContacto

abrirArchivo()
menu()
cerrarArchivos()
