import random

#UNICO USUARIO PERMITIDO
usuarios_login = {
    "julboter@gmail.com": "123"
}


# LOGIN

def login():

    intentos = 0

    while intentos < 3:

        correo = input("Ingrese correo: ")
        password = input("Ingrese contraseña: ")

        if correo in usuarios_login and usuarios_login[correo] == password:

            print("Login exitoso")
            return True

        else:

            intentos = intentos + 1
            restantes = 3 - intentos
            print("Credenciales incorrectas. Intentos restantes:", restantes)

    print("Cuenta bloqueada")
    return False



# GENERAR CONSUMOS ENTRE 100 Y 500 ALEATORIO 

def generar_consumos():

    lista = []

    for i in range(500):

        numero = random.randint(100,500)

        lista.append(numero)

    return lista



# CALCULAR PROMEDIO

def calcular_promedio(lista):

    suma = sum(lista)

    cantidad = len(lista)

    promedio = suma / cantidad

    return promedio


# LISTA USUARIOS SERVICIO

usuarios_servicio = []



# CREAR USUARIOS INICIALES , CREA 10 USUARIOS DE MANERA ALEATORIA

def crear_usuarios():

    for i in range(10):

        usuario = {}

        usuario["id"] = i + 1
        usuario["nombre"] = "usuario" + str(i+1)
        usuario["documento"] = 1000 + i
        usuario["estrato"] = random.randint(1,6)
        usuario["consumoEnergetico"] = generar_consumos()
        usuario["estado"] = "ACTIVO"

        usuarios_servicio.append(usuario)



# CONSULTAR USUARIOS

def consultar_usuarios():

    for usuario in usuarios_servicio:

        promedio = calcular_promedio(usuario["consumoEnergetico"])

        print(
            "ID:", usuario["id"],
            "Nombre:", usuario["nombre"],
            "Estrato:", usuario["estrato"],
            "Promedio:", round(promedio,2),
            "Estado:", usuario["estado"]
        )



# AÑADIR USUARIO APPEND 

def añadir_usuario():

    usuario = {}

    usuario["id"] = int(input("Ingrese id: "))
    usuario["nombre"] = input("Ingrese nombre: ")
    usuario["documento"] = input("Ingrese documento: ")
    usuario["estrato"] = int(input("Ingrese estrato (1-6): "))
    usuario["consumoEnergetico"] = generar_consumos()
    usuario["estado"] = "ACTIVO"

    usuarios_servicio.append(usuario)

    print("Usuario añadido")



# ELIMINAR USUARIO REMOVE 

def eliminar_usuario():

    id_buscar = int(input("Ingrese id del usuario a eliminar: "))

    for usuario in usuarios_servicio:

        if usuario["id"] == id_buscar:

            usuarios_servicio.remove(usuario)

            print("Usuario eliminado")

            return

    print("Usuario no encontrado")



# ORDENAR USUARIOS POR CONSUMO

def obtener_promedio(usuario):
    """Devuelve el promedio de consumo de un usuario"""
    return calcular_promedio(usuario["consumoEnergetico"])

def ordenar_por_consumo():
    usuarios_servicio.sort(key=obtener_promedio)
    print("\nUsuarios ordenados por consumo promedio\n")
    consultar_usuarios()



# MENU , EL MENU SE CREO CON CHAT GPT 

def menu():

    opcion = "0"

    while opcion != "6":

        print("\n------ MENU ------")
        print("1. Consultar usuarios")
        print("2. Añadir usuario")
        print("3. Eliminar usuario")
        print("4. Ordenar usuarios por consumo")
        print("5. Calcular promedio de un usuario")
        print("6. Salir")

        opcion = input("Seleccione opcion: ")

        if opcion == "1":

            consultar_usuarios()

        elif opcion == "2":

            añadir_usuario()

        elif opcion == "3":

            eliminar_usuario()

        elif opcion == "4":

            ordenar_por_consumo()

        elif opcion == "5":

            id_buscar = int(input("Ingrese id del usuario: "))

            for usuario in usuarios_servicio:

                if usuario["id"] == id_buscar:

                    promedio = calcular_promedio(usuario["consumoEnergetico"])

                    print("Promedio de consumo:", round(promedio,2))

                    break

        elif opcion == "6":

            print("Programa finalizado")

        else:

            print("Opcion invalida")



# PROGRAMA PRINCIPAL CHAT GPT EL MENU 

acceso = login()

if acceso == True:

    crear_usuarios()

    menu()