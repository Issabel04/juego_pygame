import pygame
from settings import *

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z= LAYER['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z

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

class Tree(Generic):
   def __init__(self, pos, surf, groups, z, name):
      super().__init__(pos=pos, surf=surf, groups=groups, z=z,)