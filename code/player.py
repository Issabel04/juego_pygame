import pygame
from settings import *
from support import *
from timer import Timer

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites):
        super().__init__(group)

        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0
        # Se configuran las propiedades de nuestro personaje
        self.image = self.animations[self.status][self.frame_index]
        #self.image = pygame.Surface((32,64))
        #self.image.fill('black')
        self.rect = self.image.get_rect(center = pos)
        # Altura en la cual se encuentra mi personaje
        self.z = LAYER['main']
        # Le agregamos un hitbox
        self.hitbox = self.rect.copy().inflate((-126, -70))
        
        self.collision_sprites = collision_sprites

        
        #Configuración para el movimiento
        self.direction = pygame.math.Vector2()
        
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 350

        # Configuración temporizador
        self.timers = {
          'uso herramienta': Timer(600, self.usar_herramienta),
          'cambio herramienta': Timer(600),
          'uso semilla': Timer(600, self.usar_semilla),
          'cambio semilla': Timer(500)
        }

        # Variables para el uso de herramientas
        self.herramientas = ['axe', 'hoe', 'water']
        self.index_herramienta = 0
        self.herramienta_seleccionada = self.herramientas[self.index_herramienta]
        
        for herramienta in range(len(self.herramientas)):
            self.herramientas


        # Variables para el uso de semillas
        self.semillas = ['corn', 'tomato']
        self.index_semillas = 0
        self.semilla_seleccionada = self.semillas[self.index_semillas]

    def usar_herramienta(self):
        print(self.herramienta_seleccionada)

    def usar_semilla(self):
        pass


    
        
       
    
    # Creamos un diccionario con todos los movimientos de nuestro personaje de la carpeta graphics
    def import_assets(self):
        self.animations = {'up':[], 'down': [], 'left':[], 'right':[],
                       'up_idle': [], 'down_idle': [], 'left_idle':[], 'right_idle':[],
                       'up_axe': [], 'down_axe': [], 'left_axe':[], 'right_axe':[],
                       'up_hoe': [], 'down_hoe': [], 'left_hoe':[], 'right_hoe':[],
                       'up_water': [], 'down_water': [], 'left_water':[], 'right_water':[],
                      }
         
        for animation in self.animations.keys():
            ruta_completa = './graphics/character/' + animation
            self.animations[animation] = import_folder(ruta_completa)

    
    def animate(self, dt):  
      self.frame_index += 4 * dt   
      if self.frame_index >= len(self.animations[self.status]):
          self.frame_index = 0
      self.image = self.animations[self.status][int(self.frame_index)]


    
    def input(self):
        
        keys = pygame.key.get_pressed()    
          
        
        if not self.timers['uso herramienta'].activo:         
        
        # Movimiento vértical
            if keys [pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            
            elif keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'

            
            else:
                self.direction.y = 0
            
            # Movimiento horizontal
            if keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'

            
            elif keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'


            else:
                self.direction.x = 0

            # Uso de la herramienta
            #---------------------------------------------------
            if keys[pygame.K_f]:
                self.timers['uso herramienta'].activate()
                self.direction = pygame.math.Vector2()
                self.frame_index = 0
            # Esta línea verifica si la tecla 'e' está siendo presionada y si el temporizador no está activo
            if keys[pygame.K_e] and not self.timers['cambio herramienta'].activo:
                self.timers['cambio herramienta'].activate() #se activa el temporizador si la condición anterior se cumple
                self.index_herramienta = (self.index_herramienta + 1) % len(self.herramientas) #asegura que el índice permanezca dentro de los límites
                self.herramienta_seleccionada = self.herramientas[self.index_herramienta] #se selecciona la herramienta correspondiente en la lista

            # Uso de las semillas
            #------------------------------------------------

            if keys[pygame.K_h]:
             self.timers['uso semilla'].activate()
             self.direction =pygame.math.Vector2()
             self.frame_index = 0
             print(f'Se plantó una semilla de: {self.semilla_seleccionada}')

            if keys[pygame.K_1] and not self.timers['cambio semilla'].activo:
             self.timers['cambio semilla'].activate() 
             self.index_semillas = 0
             self.semilla_seleccionada = self.semillas[self.index_semillas]
             
            
            if keys[pygame.K_2] and not self.timers['cambio semilla'].activo:
             self.timers['cambio semilla'].activate() 
             self.index_semillas = 1
             self.semilla_seleccionada = self.semillas[self.index_semillas]
            

    def actualizar_timers(self):
      for timer in self.timers.values():
        timer.update()    
    
    def collisions(self, direction):
       for sprite in self.collision_sprites.sprites():
        # Detecta si el objeto del sprite tiene un atributo "hitbox"
          if hasattr(sprite, 'hitbox'):
            # Detecta si el sprite tiene una colision
             if sprite.hitbox.colliderect(self.hitbox):
                
                # Verifica los choques entre el eje horizontal
                if direction == 'horizontal':
                    if self.direction.x > 0: # Significa que el usuario se está moviendo hacia la derecha:
                        self.hitbox.right = sprite.hitbox.left
                   
                    elif self.direction.x < 0: # Significa que el usuario se está moviendo hacia la izquierda:
                      self.hitbox.left = sprite.hitbox.right
                
                    self.rect.centerx = self.hitbox.centerx
                    self.pos.x = self.hitbox.centerx
           
           # Verifica los choques en el eje vértical 
                if direction =='vertical':
                    if self.direction.y > 0: # Significa que el usuario se está moviendo hacia la abajo:
                        self.hitbox.bottom = sprite.hitbox.top
                   
                    elif self.direction.y < 0: # Significa que el usuario se está moviendo hacia arriba:
                      self.hitbox.top = sprite.hitbox.bottom
                
                    self.rect.centery = self.hitbox.centery
                    self.pos.y = self.hitbox.centery
   
   
   
   
   
    def get_status(self):
     # Si mi personaje no se está desplazando 
      if self.direction.magnitude() ==  0:
        self.status = self.status.split('_')[0] + '_idle'
      
      
      if self.timers['uso herramienta'].activo:
        self.status = self.status.split('_')[0] + '_' + self.herramienta_seleccionada
        

    
    def move(self, dt):

    # Se hace la normalización de nuestros vectores de movimiento    
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        #print(self.direction)

       # Movimiento horizontal 
        self.pos.x += self.direction.x * self.speed * dt    
        self.rect.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        self.collisions('horizontal')
        
        
        
        # Movimiento vértical
        self.pos.y += self.direction.y * self.speed * dt    
        self.rect.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery
        self.collisions('vertical')
    
    def update(self, dt):
        self.input()
        self.get_status()
        self.actualizar_timers()
        self.move(dt)
        self.animate(dt)
       
        
        