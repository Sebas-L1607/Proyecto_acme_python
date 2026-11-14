import json 
lugar_pc = "/Users/sebastianlamus/Documents/Bootcamp/proyecto_python/"
lugar_pacientes =  lugar_pc + "pacientesguardados.json"
lugar_operarios = lugar_pc + "operariosguardado.json"
lugar_consultas = lugar_pc + "consultasguardads.json"

def guarda_datos (datos, ruta):
    
    with open(ruta, "w",encoding="utf-8") as datos_guardados:
        json.dump (datos,datos_guardados)

def cargar (ruta):
    try:
        with open(ruta, "r",encoding="utf-8") as archivo:
            lista_pacientes = json.load (archivo)
        
    except FileNotFoundError:
        lista_pacientes = []

    return lista_pacientes    


