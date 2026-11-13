import Validaciones


def crear_paciente():
    identificacion_paciente = Validaciones.validar_identificacion_paciente ()
    nombre_paciente = Validaciones.validar_nombre_paciente ()
    apellido_paciente = Validaciones.validar_apellido_paciente ()
    telefono_paciente = Validaciones.validar_telefono_paciente ()
    email_paciente = Validaciones.validar_email_paciente ()
    direccion_paciente = Validaciones.validar_direccion_paciente ()
    genero = Validaciones.validar_genero ()
    estado_civil = Validaciones.validar_estado_civil ()

    paciente_creado = {
        "ID paciente" :identificacion_paciente,
        "Nombre":nombre_paciente,
        "Apellido":apellido_paciente,
        "Telefono":telefono_paciente,
        "Email":email_paciente,
        "Direccion":direccion_paciente,
        "Genero":genero,
        "Estado civil":estado_civil}
    return paciente_creado
        

def registrar_pacientes(lista_pacientes):

    nuevo_paciente = crear_paciente()
    clave = nuevo_paciente["ID paciente"]
    if buscar_paciente (lista_pacientes,clave) is None:
        lista_pacientes.append(nuevo_paciente)
    else: 
        print("El paciente ya esta registrado")
    return lista_pacientes




def buscar_paciente (lista_pacientes, identificacion_paciente):
    for paciente in lista_pacientes:
        if paciente["ID paciente"] == identificacion_paciente:
            return paciente
    return None


