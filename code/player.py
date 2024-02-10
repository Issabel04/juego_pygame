import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()

        # Se configuran las propiedades de nuestro personaje
        self.image = pygame.Surface((32,64))
        self.image.fill('black')
        
        self.rect = self.image.get_rect(center = pos)
        
        #Configuración para el movimiento
        self.direction = pygame.math.Vector2()
        
        self.pos = pygame.math.Vector2(self.rect.center)

        self.speed = 350
        
        #(x,y)
    
    # Creamos un diccionario con todos los movimientos de nuestro personaje de la carpeta graphics
    def import_assets(self):
         self.animations = {'up':[], 'down': [], 'left':[], 'right':[],
                       'up_idle': [], 'down_idle': [], 'left_idle':[], 'right_idle':[],
                       'up_axe': [], 'down_axe': [], 'left_axe':[], 'right_axe':[],
                       'up_hoe': [], 'down_hoe': [], 'left_hoe':[], 'right_hoe':[],
                       'up_water': [], 'down_water': [], 'left_water':[], 'right_water':[],
                      }
         
         for animation in self.animations.keys():
            ruta_completa = '../graphics/character/' + animation
            self.animations[animation] = import_folder(ruta_completa)

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

    
    def move(self, dt):

    # Se hace la normalización de nuestros vectores de movimiento    
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        #print(self.direction)

       # Movimiento horizontal 
        self.pos.x += self.direction.x * self.speed * dt    
        self.rect.centerx = self.pos.x
        # Movimiento vértical
        self.pos.y += self.direction.y * self.speed * dt    
        self.rect.centery = self.pos.y
    
    def update(self, dt):
        self.input()
        self.move(dt)