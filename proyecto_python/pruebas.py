import pacientes  # Importa las funciones del módulo de pacientes.
import intentos
import operarios



lista_operarios = intentos.cargar(intentos.lugar_operarios)

operarios.registrar_operario(lista_operarios)

intentos.guarda_datos(lista_operarios,intentos.lugar_operarios)

"""
lista_pacientes = intentos.cargar(intentos.lugar_pacientes) 

pacientes.registrar_pacientes(lista_pacientes)  # Solicita y registra el primer paciente.
intentos.guarda_datos (lista_pacientes,intentos.lugar_pacientes)
"""