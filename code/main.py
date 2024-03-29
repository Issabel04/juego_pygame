import pygame, sys # Importamos pygame y sys
from level import Level

from settings import *

# Creamos una clase la cual contendrá nuestro juego
class Game: 
    
# Creamos un método constructivo para inicializar nuestros parámetros    
    def __init__(self):
        pygame.init() # Inicializamos pygame
        self.screen = pygame.display.set_mode((VENTANA_LARGO, VENTANA_ANCHO))  # Le decimos a pygame que tendrá una ventana de 128x128
        pygame.display.set_caption(NOMBRE_VIDEOJUEGO)       
       
        self.clock = pygame.time.Clock() # Creamos un reloj interno
        self.level = Level()
    
    def ejecutar(self):
        while True:
    # Este ciclo recorre cada pulsación que haga el usuario
            for evento in pygame.event.get():
        # Si la pulsación coincide con el evento QUIT
                if evento.type == pygame.QUIT:
        # Le decimos que finalice        
                    pygame.quit()
        # Cerramos la ventana que nos genere        
                    sys.exit()

            dt = self.clock.tick() / 1250
            pygame.display.update()

            self.level.run(dt)
            
# Se crea una instancia de Game
game = Game()
# Ejecutamos el método "ejecutar"    
game.ejecutar()
