import pacientes
import intentos
import operarios

def menu_sistema (usuario_actual):
    lista_pacientes = intentos.cargar(intentos.lugar_pacientes)
    lista_operarios = intentos.cargar(intentos.lugar_operarios)
    while True: 
        print("Selecciona una opcion: \n")
        print("1. Registrar un operario")
        print ("2. Registrar un paciente")
        print("3. Diagnosticar un paciente")
        print ("4. Contultar historia clinica")
        print ("5. Cerrar sesión\n")

        seleccion = (input())

        match seleccion:
            case "1":
                operarios.registrar_operario(lista_operarios)
                intentos.guarda_datos(lista_operarios, intentos.lugar_operarios)
            case "2": 
                pacientes.registrar_pacientes(lista_pacientes)
                intentos.guarda_datos(lista_pacientes, intentos.lugar_pacientes)
            case "3": 
                print ("Registrar3")
            case "4":
                print ("Registrar4")
            case "5": 
                print ("Has cerrado sesión")
                return
            case _:
                print ("Opcion no valida")


