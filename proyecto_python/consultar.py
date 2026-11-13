import pacientes


def registrar_consulta (lista_pacientes, usuario_actual):
    verificacion_operario = usuario_actual["Tipo operario"]
    if verificacion_operario == "Medico": 
        identificacion_paciente = input("\nDigite el ID del paciente: \n")
        existe = pacientes.buscar_paciente(lista_pacientes,identificacion_paciente)
        if existe is not None:
            print (existe["Nombre"])
            while True:
                sintomas = input("Digite los sintomas del paciente:\n\n").strip()
                if sintomas == "": 
                    print ("No puede dejar esta sección vacia.")
                    continue
                else: 
                    break
            while True:  
                diagnostico = input("\nDigite el diagnósticos del paciente \n\n").strip()
                if diagnostico == "":
                    print ("No puede dejar esta sección vacia.")
                    continue
                else:
                    break
            medicamentos = []
            while True:
                medicamentos.append(crear_medicamento())
                while True:
                    decision = input ("Hay que recetar otro medicamento? SI/NO").lower().strip()

                    if decision == "si" or decision == "no":
                        break
                    else:
                        print("Responda Si o No")
                        continue
                if decision == "si":
                    continue
                else: 
                    break
            while True:
                fecha = input("Ingrese la fecha de la consulta(DD/MM/AAAA):").strip()

                if fecha == "":
                    print ("No puede dejar esta seccion vacia")
                    continue
                else:
                    break

            nombre_medico = usuario_actual["Nombre"] + " " + usuario_actual["Apellido"]

            consulta_creada = {
                "Fecha":fecha,
                "ID paciente":identificacion_paciente,
                "Nombre medico": nombre_medico,
                "Email medico": usuario_actual["Email"],
                "Sintomas":sintomas,
                "Diagnostico":diagnostico,
                "Medicamentos":medicamentos}

            return consulta_creada
        else: 
            print ("El paciente no esta registrado.")
            return

    else: 
        print("Solo medicos pueden registrar consultas")
        return



def crear_medicamento ():
    while True:
        medicamento = input("Digite el nombre del medicamento:").strip()
        if medicamento == "":
            print("No puede dejar vacia esta seccion")
            continue
        else: 
            break

    while True:
        try:
            cantidad = int(input("Digite la cantidad del medicamento"))
        except ValueError:
            print ("Las cantidades solo pueden ser numeros enteros.")
            continue

        if cantidad <=0:
            print("Las cantidades no pueden ser menores o igual a cero")
        else: 
            break

    while True: 
        dosis = input("Digite la dosis a recomendar: ").strip()

        if dosis == "":
            print("No puede dejar esta seccion vacia")
            continue
        else: 
            break 

    while True:
        try:
            dias = int(input("Digite los dias del tratamient"))
        except ValueError:
            print ("Los dias solo pueden ser numeros enteros.")
            continue

        if dias <=0:
            print("Los dias no pueden ser menores o igual a cero")
        else: 
            break

    receta = {
        "Medicamento": medicamento,
        "Cantidad": cantidad,
        "Dosis": dosis,
        "Dias": dias}

    return receta

    