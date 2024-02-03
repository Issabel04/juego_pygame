import pygame

class Level():
  def __init__(self):

# Se crea la superficie de nuestra pantalla
    self.display_surface = pygame.display.get_surface()
# Creamos un grupo con todos los sprites del nivel    
    self.all_sprites = pygame.sprite.Group()
  
  
  def run(self, dt):
    self.display_surface.fill('purple')
# Se dibujan nuestros sprites en toda la superficie de la pantalla
    self.all_sprites.draw(self.display_surface)
# Actualizamos esos sprites
    self.all_sprites.update()