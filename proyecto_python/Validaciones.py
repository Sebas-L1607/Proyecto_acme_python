##OPERARIOS
##OPERARIOS
##OPERARIOS
##OPERARIOS

def seleccion_operario():
    operario = ("")
    while True:
        print ("Seleccione el operario: ")
        print ("1. Medico")
        print ("2. Personal Administrativo")
        print ("3. Administrador\n")

        try: 
            seleccion = int(input())
        except ValueError:
            print ("\nFavor de digitar el numero de uno de las tres opciones.\n")
            continue

        match seleccion:
            case 1: 
                operario = ("Medico")
                return operario
            case 2: 
                operario = ("Personal Administrativo")
                return operario
            case 3:
                operario = ("Administrador")
                return operario
            case _:
                print ("\nEl numero seleccionado no esta dentro de las opciones, elija entre 1 a 3.\n")
                continue


def validar_identificacion_operario (): 
    while True: 
        id_operario = (input("\nIngrese el numero de identificacion del operario: \n"))

        if id_operario.isdecimal():
            return id_operario
        else: 
            print ("\nLa identificacion solo pueden ser numeros enteros positivos y el 0.\n")
            continue
            


def validar_nombre_operario ():
    while True: 
        nombre_operario = input ("\nIngrese el nombre del operario:\n\n").strip()
        nombreoperario = nombre_operario
        nombre_operario = nombre_operario.replace(" ","")
        if nombre_operario.isalpha():
            nombre_operario = nombreoperario
            return nombre_operario
        else: 
            print ("\nEl nombre del operario no puede estar vacio o contener numeros, solo puede tener letras\n")


def validar_apellido_operario ():
    while True: 
        apellido_operario = input ("\nIngrese el apellido del operario:\n\n").strip()
        apellidooperario = apellido_operario
        apellido_operario = apellido_operario.replace(" ","")
        if apellido_operario.isalpha():
            apellido_operario = apellidooperario

            return apellido_operario
        else: 
            print ("\nEl apellido del operario no puede estar vacio o contener numeros, solo puede tener letras\n")


def validar_telefono_operario (): 
    while True: 
        telefono_operario = (input("\nIngrese el numero de telefono del operario: \n"))
        if telefono_operario.isdecimal():
            return telefono_operario
        else: 
            print ("El teléfono debe contener únicamente dígitos del 0 al 9")
            continue



def validar_email_operario ():
    while True: 
        email_operario = input("Digite el correo corporativo del operario: ").lower().strip()
        conteo = email_operario.count("@")

        if email_operario.find(" ") >=0: 
            print ("\nVerifique nuevamente el correo digitado, tiene espacios internos \n")
            continue
        
        if conteo != 1 or email_operario[0] == "@":
            print ("\nVerifique nuevamente el correo digitado. Recuerde que tiene que el correo tiene que ser del dominio @acmeclinic.com \n")
            continue

        if email_operario.endswith("@acmeclinic.com"):
            return email_operario
        else: 
            print ("\nVerifique nuevamente el correo digitado. Recuerde que tiene que el correo tiene que ser del dominio @acmeclinic.com \n")
            continue


def validar_direccion_operario ():
    while True: 
        direccion_operario = input("Digite la direccion del operario: ")
        if direccion_operario == "" or direccion_operario.isspace():
            print("La direccion no puede estar vacia, favor de digitarla nuevamente")
            continue
        
        return direccion_operario


def validar_contrasena_operario (): 
    while True: 
        contrasena_operario = input("Digite la contraseña: ")
        if contrasena_operario.isspace() or contrasena_operario == "":
            print("La contraseña no puede estar vacia.")
            continue

        if contrasena_operario.find (" ") != -1: 
            print ("La contraseña no puede tener espacios internos.")
            continue

        while True: 
            confirmacion_contrasena = input ("\nConfirmación contraseña. Digite nuevamente la contraseña: \n\n")

            if contrasena_operario == confirmacion_contrasena : 
                return contrasena_operario
            else: 
                print ("Las contraseñas no coinciden, favor de digitarla nuevamente")
                continue



#PACIENTES   
#PACIENTES   
#PACIENTES
#PACIENTES   
#PACIENTES   
#PACIENTES   
#PACIENTES       


def validar_identificacion_paciente (): 
    while True: 
        id_paciente = (input("\nIngrese el numero de identificacion del paciente: \n"))
        if id_paciente.isdecimal(): 
            return id_paciente
        else:
            print ("\nLa identificacion solo pueden ser numeros enteros positivos y el 0.\n")

       
    


def validar_nombre_paciente ():
    while True: 
        nombre_paciente = input ("\nIngrese el nombre del paciente:\n\n").strip()
        nombrepaciente = nombre_paciente
        nombre_paciente = nombre_paciente.replace(" ","")
        if nombre_paciente.isalpha():
            nombre_paciente = nombrepaciente
            return nombre_paciente
        else: 
            print ("\nEl nombre del paciente no puede estar vacio o contener numeros, solo puede tener letras\n")

def validar_apellido_paciente ():
    while True: 
        apellido_paciente = input ("\nIngrese el apellido del paciente:\n\n").strip()
        apellidopaciente = apellido_paciente
        apellido_paciente = apellido_paciente.replace(" ","")
        if apellido_paciente.isalpha():
            apellido_paciente = apellidopaciente

            return apellido_paciente
        else: 
            print ("\nEl apellido del paciente no puede estar vacio o contener numeros, solo puede tener letras\n")

def validar_telefono_paciente(): 
    while True: 
        telefono_paciente = (input("\nIngrese el numero de telefono del paciente: \n"))
        if telefono_paciente.isdecimal():
            return telefono_paciente
        else: 
            print ("El teléfono debe contener únicamente dígitos del 0 al 9")
            continue

def validar_direccion_paciente ():
    while True: 
        direccion_paciente = input("\nDigite la direccion del paciente: \n\n")
        if direccion_paciente == "" or direccion_paciente.isspace():
            print("La direccion no puede estar vacia, favor de digitarla nuevamente")
            continue
        
        return direccion_paciente

def validar_email_paciente ():
    while True:
        email_paciente = input("\nDigite el email del paciente: \n\n").strip()
        conteo = email_paciente.count ("@")

        if email_paciente.find(" ") >=0: 
            print ("\nVerifique nuevamente el correo digitado, tiene espacios internos  \n")
            continue

        if conteo >=2 or conteo <1 or email_paciente[0] == "@" or email_paciente[-1]=="@":
            print ("\nEste no es un correo valido, favor de ingresar un correo valido")
            continue
        else:
            return email_paciente


def validar_genero ():
    while True:
        print ("Seleccione el genero del paciente:")
        print ("1. Masculino")
        print ("2. Femenino\n")
        
        try: 
            seleccion = int(input())
            
        except ValueError:
            print ("\nFavor de digitar el numero de uno de las dos opciones.\n")
            continue

        match seleccion:
            case 1: 
                genero = ("Masculino")
                return genero
            case 2: 
                genero = ("Femenino")
                return genero
            case _:
                print ("\nEl numero seleccionado no esta dentro de las opciones, elija entre 1 o 2.\n")
                continue

def validar_estado_civil ():
        while True:
            print ("Seleccione el estado civil:")
            print ("1. Soltero")
            print ("2. Casado\n")
            
            try: 
                seleccion = int(input())
                
            except ValueError:
                print ("\nFavor de digitar el numero de uno de las dos opciones.\n")
                continue

            match seleccion:
                case 1: 
                    estado_civil = ("Soltero")
                    return estado_civil
                case 2: 
                    estado_civil = ("Casado")
                    return estado_civil
                case _:
                    print ("\nEl numero seleccionado no esta dentro de las opciones, elija entre 1 o 2.\n")
                    continue

