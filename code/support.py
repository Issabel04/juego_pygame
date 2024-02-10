from os import walk


def import_folder(ruta_completa):
    
    lista_de_superficies = []

    for carpeta in walk(ruta_completa): 
        print(carpeta)

    return lista_de_superficies