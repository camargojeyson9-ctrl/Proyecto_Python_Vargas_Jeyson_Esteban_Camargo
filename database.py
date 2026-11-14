# Importo el modulo para trabajar en archivos json.
import json

# Creo funcion para leer datos de archivo existente, en caso que no exista con el try salvamos que el programa falle y guarda una lista vacia.
def leer_datos(nombre_archivo):
    try:
        with open(nombre_archivo,"r",encoding="utf-8") as archivo:
            return json.load(archivo)

    except FileNotFoundError:
        return []

# Creo la funcion para generar los archivos json de las funcionalidades del programa. 
def guardar_datos(nombre_archivo,datos):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos,archivo)
