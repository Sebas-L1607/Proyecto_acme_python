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
                    print ("No puede dejar esta sección vacia.\n")
                    continue
                else: 
                    break
            while True:  
                diagnostico = input("\nDigite el diagnóstico del paciente: \n\n").strip()
                if diagnostico == "":
                    print ("No puede dejar esta sección vacia.\n")
                    continue
                else:
                    break
            medicamentos = []
            while True:
                medicamentos.append(crear_medicamento())
                while True:
                    decision = input ("Hay que recetar otro medicamento? SI/NO\n\n").lower().strip()

                    if decision == "si" or decision == "no":
                        break
                    else:
                        print("Responda Si o No\n")
                        continue
                if decision == "si":
                    continue
                else: 
                    break

            while True:  
                fecha = input("Ingrese la fecha de la consulta (DD/MM/AAAA):\n").strip() 

                if fecha == "":  
                    print("No puede dejar esta sección vacía.")  
                    continue

                if len(fecha) != 10:  
                    print("La fecha debe tener el formato DD/MM/AAAA.")  
                    continue  

                if fecha[2] != "/" or fecha[5] != "/":  
                    print("Debe separar el día, mes y año con /.")  
                    continue 

                dia = fecha[:2]  
                mes = fecha[3:5]  
                anio = fecha[6:]  

                if not dia.isdecimal() or not mes.isdecimal() or not anio.isdecimal(): 
                    print("El día, mes y año deben contener únicamente números.") 
                    continue 

                if not 1 <= int(dia) <= 31: 
                    print("El día debe estar entre 01 y 31.")  
                    continue 

                if not 1 <= int(mes) <= 12: 
                    print("El mes debe estar entre 01 y 12.")  
                    continue  

                if int(anio) == 0:
                    print("El año debe ser mayor que cero.") 
                    continue 

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
        medicamento = input("Digite el nombre del medicamento:\n").strip()
        if medicamento == "":
            print("No puede dejar vacia esta seccion\n")
            continue
        else: 
            break

    while True:
        try:
            cantidad = int(input("Digite la cantidad del medicamento:\n"))
        except ValueError:
            print ("Las cantidades solo pueden ser numeros enteros.\n")
            continue

        if cantidad <=0:
            print("Las cantidades no pueden ser menores o igual a cero\n")
        else: 
            break

    while True: 
        dosis = input("Digite la dosis a recomendar: \n").strip()

        if dosis == "":
            print("No puede dejar esta seccion vacia\n")
            continue
        else: 
            break 

    while True:
        try:
            dias = int(input("Digite los dias del tratamiento: \n"))
        except ValueError:
            print ("Los dias solo pueden ser numeros enteros.\n")
            continue

        if dias <=0:
            print("Los dias no pueden ser menores o igual a cero\n")
        else: 
            break

    receta = {
        "Medicamento": medicamento,
        "Cantidad": cantidad,
        "Dosis": dosis,
        "Dias": dias}

    return receta

    