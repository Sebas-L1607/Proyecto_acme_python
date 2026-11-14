import pacientes

def mostrar_clinica (lista_pacientes, lista_consultas):
    identificacion = input ("Digite la identificacion del paciente: \n\n")
    paciente_encontrado = pacientes.buscar_paciente(lista_pacientes, identificacion)
    if paciente_encontrado is None:
        print ("El paciente no esta registrado")
        return  
    else:
        for campo in paciente_encontrado: 
            print (campo, ": ", paciente_encontrado[campo])
            print ()

        numero_consultas = 0
        for historia in lista_consultas: 
            if historia["ID paciente"] == identificacion: 
                print()
                print ("Fecha: ", historia["Fecha"])
                print ("Nombre medico: ", historia["Nombre medico"])
                print ("Sintomas: ", historia["Sintomas"])
                print ("Diagnostico: ", historia["Diagnostico"])
                numero_consultas += 1

                print("Medicamentos Prescritos")
                for prescritos in historia["Medicamentos"]:
                    print ("Medicamento: ", prescritos["Medicamento"])
                    print ("Cantidad: ", prescritos["Cantidad"])
                    print ("Dosis: ", prescritos["Dosis"])
                    print ("Dias: ", prescritos["Dias"])
                    print()

        if numero_consultas == 0:
            print ("El paciente no tiene consultas registradas")

        
        



        