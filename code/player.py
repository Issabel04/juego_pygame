import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        # Se configuran las propiedades de nuestro personaje
        self.image = pygame.Surface((32,64))
        self.image.fill('black')
        
        self.rect = self.image.get_rect(center = pos)
        
        #Configuración para el movimiento
        self.direction = pygame.math.Vector2(self.rect.center)
        
        self.pos = pygame.math.Vector2()

        self.speed = 200
        
        #(x,y)
    
    def input(self):
        
        keys = pygame.key.get_pressed()    
      
        if keys [pygame.K_w]:
            self.direction.y = -1
        
        elif keys[pygame.K_s]:
            self.direction.y = 1
        
        else:
            self.direction.y = 0
        
        if keys[pygame.K_a]:
            self.direction.x = -1
        
        elif keys[pygame.K_d]:
            self.direction.x = 1

        else:
            self.direction.x = 0

        print(self.direction)
    
    def move(self, dt):
        self.pos += self.direction * self.speed * dt    
        self.rect.center = self.pos
    
    def update(self, dt):
        self.input()
        self.move(dt)