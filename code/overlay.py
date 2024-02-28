import pygame


class Overlay: 
    def __init__(self, player):
      
    # Configuración general
      self.superficie_pantalla = pygame.display.get_surface()
      self.player = player

      ruta_overlay = './graphics/overlay/'
    
    # Mandando a llamar la lista de herramientas en el archivo player
      self.herramientas_superficies = {herramienta:pygame.image.load(f'{ruta_overlay}{herramienta}.png').convert_alpha() for herramienta in player.herramientas}
      self.herramientas_superficies = {semilla:pygame.image.load(f'{ruta_overlay}{semilla}.png').convert_alpha() for semilla in player.semilla}
      