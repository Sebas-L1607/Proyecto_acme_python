import login
import intentos
import menu 
import operarios

datos_admin = {
        "Tipo operario" : "Administrador",
        "ID operario" : "0000",
        "Nombre": "Admin",
        "Apellido" : "Administrador", 
        "Telefono" : "555 000111",
        "Email" : "admin@acmeclinic.com", 
        "Contraseña" : "123456",
        "Direccion" : "Cl 185 # 26 - 85"}

lista_admin = intentos.cargar(intentos.lugar_operarios)

if len(lista_admin) == 0:
    lista_admin.append(datos_admin)
    intentos.guarda_datos(lista_admin,intentos.lugar_operarios)


while True: 
    print ("1. Iniciar sesión")
    print ("2. Salir\n\n")

    seleccion = input ("Elija la accion que quiere realizar: \n\n")

    if seleccion == "1": 
        operarios = intentos.cargar (intentos.lugar_operarios)
        usuario_actual = login.iniciar_sesion(operarios)
        if usuario_actual is None:
            print("\nVerifique sus credenciales\n")
        else: 
            print ("Bienvenido", usuario_actual["Nombre"])
            menu.menu_sistema (usuario_actual)

    elif seleccion== "2":
        print ("\nHasta luego :) ")
        break
    else: 
        print ("\nOpcion no valida\n")
     
