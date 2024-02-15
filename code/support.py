from os import walk
import pygame


def import_folder(ruta_completa):
    
    lista_de_superficies = []

    for carpeta in walk(ruta_completa): 
        for image in carpeta[-1]:   
            if ':Zone.Identifier' in image:
                continue
            else:
                ruta_entera = ruta_completa + '/' + image
                superficie_imagen = pygame.image.load(ruta_entera).convert_alpha()
                lista_de_superficies.append(superficie_imagen)
    
    return lista_de_superficies