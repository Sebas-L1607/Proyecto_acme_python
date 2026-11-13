import Validaciones


def crear_operarios ():
    tipo_operario = Validaciones.seleccion_operario ()
    identificacion_operario = Validaciones.validar_identificacion_operario ()
    nombre_operario = Validaciones.validar_nombre_operario ()
    apellido_operario = Validaciones.validar_apellido_operario ()
    telefono_operario = Validaciones.validar_telefono_operario ()
    email_operario = Validaciones.validar_email_operario ()
    contrasena = Validaciones.validar_contrasena_operario ()
    direccion_operario = Validaciones.validar_direccion_operario ()

    operario_creado = {
        "Tipo operario" : tipo_operario,
        "ID operario" : identificacion_operario,
        "Nombre": nombre_operario,
        "Apellido" : apellido_operario,
        "Telefono" : telefono_operario,
        "Email" : email_operario,
        "Contraseña" : contrasena,
        "Direccion" : direccion_operario}

    return operario_creado

def registrar_operario (lista_operarios):

    nuevo_operario = crear_operarios()
    clave = nuevo_operario["Email"]
    if buscar_operario (lista_operarios,clave) is None:
        lista_operarios.append(nuevo_operario)
    else: 
        print("El operario ya esta registrado")
    return lista_operarios

def buscar_operario (lista_operarios, email_operario):
    for operario in lista_operarios:
        if operario["Email"] == email_operario:
            return operario
    return None