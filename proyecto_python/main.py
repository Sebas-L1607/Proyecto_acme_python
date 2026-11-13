import login
import intentos
import menu 



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
     
