import pygame
from settings import *
from random import randint
from timer import Timer
from random import choice, randint


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z= LAYER['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate((- self.rect.width * 0.2, - self.rect.height * 0.75))

class Water(Generic):
    def __init__(self, pos, frames, groups, z):

# Configuración para la animación del agua
        self.frames = frames
        self.frame_index = 0
# Con ésto heredamos las funciones de Generic y las modificamos
        super().__init__(pos = pos, surf = self.frames[self.frame_index], groups = groups, z=z)

    def animate(self, dt):
      self.frame_index += 5 * dt
      if self.frame_index >= len(self.frames):
         self.frame_index = 0

      self.image = self.frames[int(self.frame_index)]
    
    def update(self, dt):
      self.animate(dt)

class WildFlower(Generic):
   def __init__(self, pos, surf, groups, z):
     super().__init__(pos=pos, surf=surf, groups=groups, z=z)
     self.hitbox = self.rect.copy().inflate((-20,  - self.rect.height * 0.90))
class Tree(Generic):
  def __init__(self, pos, surf, groups, z, name):
      super().__init__(pos=pos, surf=surf, groups=groups, z=z,)

      # Las manzanas del árbol
      self.health = 5
      self.alive = True

      # Creamos el atributo para tener la imagen del árbol talado
      ruta_talado = f'./graphics/stumps/{"small" if name == "Small" else "large"}.png'
      self.superficie_talado = pygame.image.load(ruta_talado).convert_alpha()
      self.invul_time = Timer(200)


      # Creamos los métodos para poner manzanas en los árboles
      self.apple_surf = pygame.image.load('./graphics/fruit/apple.png')
      self.apple_pos = APPLE_POS[name]
      self.apple_sprites = pygame.sprite.Group()
      self.create_fruit()

  def create_fruit(self):
    for pos in self.apple_pos:
      if randint(0,10) < 2: 
        x = pos[0] + self.rect.left
        y = pos[1] + self.rect.top
        Generic(
           pos=(x,y),
           surf = self.apple_surf,
           groups = [self.apple_sprites, self.groups()[0]],
           z= LAYER['fruit']
           )

  def damage(self):
     self.health =- 1
     print('Se le hizo daño al árbol')

     if len(self.apple_sprites.sprites()) > 0:
        random_apple = choice(self.apple_sprites.sprites())
        random_apple.kill()


         
