import json 
lugar_pacientes = "/Users/sebastianlamus/Documents/Bootcamp/proyecto_python/" + "pacientesguardados.json"
lugar_operarios = "/Users/sebastianlamus/Documents/Bootcamp/proyecto_python/" + "operariosguardado.json"

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

