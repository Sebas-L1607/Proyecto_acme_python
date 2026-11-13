import operarios

def iniciar_sesion (lista_operarios):
    login = input("Ingrese su correo: ").strip().lower()
    contrasena = input("Ingrese su contraseña: ")
    operador = operarios.buscar_operario(lista_operarios,login)
    if operador is not None: 
        if operador["Contraseña"] == contrasena:
            return operador       
    return None

    
    