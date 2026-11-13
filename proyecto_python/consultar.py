import pacientes

def registrar_consulta (lista_pacientes, usuario_actual):
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
            if diagnostico.isspace():
                print ("No puede dejar esta sección vacia.")
                continue
            else:
                break
    else: 
        print ("El paciente no esta registrado.")
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

        if dosis == ""
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

    