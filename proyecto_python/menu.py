import pacientes
import intentos
import operarios
import consultar
import historia_clinica

def menu_sistema (usuario_actual):
    lista_pacientes = intentos.cargar(intentos.lugar_pacientes)
    lista_operarios = intentos.cargar(intentos.lugar_operarios)
    lista_consultas = intentos.cargar(intentos.lugar_consultas)
    while True: 
        print("Selecciona una opcion: \n")
        print("1. Registrar un operario")
        print ("2. Registrar un paciente")
        print("3. Diagnosticar un paciente")
        print ("4. Consultar historia clínica")
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
                nueva_consulta = consultar.registrar_consulta(lista_pacientes, usuario_actual)
                if nueva_consulta is not None:
                    lista_consultas.append(nueva_consulta)
                    intentos.guarda_datos(lista_consultas,intentos.lugar_consultas)
            case "4":
                historia_clinica.mostrar_clinica(lista_pacientes, lista_consultas)
            case "5": 
                print ("Has cerrado sesión")
                return
            case _:
                print ("Opcion no valida")


