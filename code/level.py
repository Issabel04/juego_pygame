import pygame
from player import Player
from overlay import Overlay

from generic import Tree
from generic import Generic
from generic import Water 
from generic import WildFlower

from support import import_folder
from settings import *
from pytmx.util_pygame import load_pygame


class Level():
  def __init__(self):

# Se crea la superficie de nuestra pantalla
    self.display_surface = pygame.display.get_surface()

# Creamos un grupo con todos los sprites del nivel    
    self.all_sprites = CameraGroup()
    self.collision_sprites = pygame.sprite.Group()
    self.tree_sprites = pygame.sprite.Group()

    # Configuramos el jugador
    self.setup()
    
    # Creamos un overlay específico para cada jugador
    self.overlay = Overlay(self.player)
  
  def setup(self):
   
    tmx_data = load_pygame('./data/map.tmx')

    # Configuración de la casa
    for layer in ['HouseFloor', 'HouseFurnitureBottom']:
    # Recorremos todo el archivo map_tmx y obtenemos el layer que buscamos  
      for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
        # Por cada elemento dentro del layer, creamos un objeto de tipo Generic
    # Los datos que tendrá este objeto vendrán directamente del ciclo for
        Generic(pos=(x * TILE_SIZE, y * TILE_SIZE), surf=surf, groups = self.all_sprites, z= LAYER['house bottom'])
      
    # Importamos los gráficos de la casa superior
      for layer in ['HouseWalls', 'HouseFurnitureTop']:   
        for x, y, surf in tmx_data.get_layer_by_name(layer).tiles():
          Generic(pos=(x * TILE_SIZE, y * TILE_SIZE), surf=surf, groups = [self.all_sprites], z= LAYER['house top'])
      
    # Importamos los gráficos de la barda
      for x,y, surf in tmx_data.get_layer_by_name('Fence').tiles():
        Generic(pos=(x * TILE_SIZE, y * TILE_SIZE), surf=surf, groups = [self.all_sprites])

    # Importamos los gráficos del agua
      water_frames = import_folder('./graphics/water')
      for x, y, surf in tmx_data.get_layer_by_name('Water'):
        Water(pos=(x * TILE_SIZE, y * TILE_SIZE), frames=water_frames, groups = [self.all_sprites], z= LAYER['water'])
    
    # Importamos los gráficos de las plantas
      for obj in tmx_data.get_layer_by_name('Decoration'):
        WildFlower(pos=(obj.x, obj.y), surf=obj.image, groups = [self.all_sprites, self.collision_sprites], z= LAYER['main'])
    
    # Importamos los gráficos de los árboles
      for obj in tmx_data.get_layer_by_name('Trees'):
        Tree(pos=(obj.x, obj.y), surf=obj.image, groups = [self.all_sprites, self.collision_sprites, self.tree_sprites], z= LAYER['main'], name=obj.name)

    # Colisiones invisibles
    for x ,y, surf in tmx_data.get_layer_by_name('Collision').tiles():
      Generic(pos=(x * TILE_SIZE, y * TILE_SIZE), surf=pygame.Surface((TILE_SIZE, TILE_SIZE)), groups = [self.collision_sprites])

    for obj in tmx_data.get_layer_by_name('Player'):
      if obj.name == 'Start' : 

     # Creamos nuestro personaje
       self.player = Player(
       pos=(obj.x, obj.y),
       group = self.all_sprites,
       collision_sprites=  self.collision_sprites,
       tree_sprites = self.tree_sprites
       )
   
    terreno = pygame.image.load('./graphics/world/ground.png').convert_alpha()
    
    Generic(pos=(0,0), surf = terreno, groups = self.all_sprites, z=LAYER['ground'])
    
    

  def run(self, dt):
    self.display_surface.fill('black')

# Se dibujan nuestros sprites en toda la superficie de la pantalla
    self.all_sprites.customize_draw(self.player)

# Actualizamos esos sprites
    self.all_sprites.update(dt)

    # Mostra el overlay
    self.overlay.display()

class CameraGroup(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
    self.display_surface = pygame.display.get_surface()
    self.offset = pygame.math.Vector2()

  def customize_draw(self, player):
    self.offset.x = player.rect.centerx - VENTANA_LARGO / 2
    self.offset.y = player.rect.centery - VENTANA_ANCHO / 2
    for layer in LAYER.values():
      for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
       if sprite.z == layer:
         offset_rect = sprite.rect.copy()
         offset_rect.center -= self.offset
      
         self.display_surface.blit(sprite.image, offset_rect)

         if sprite == player:
         
          keys = pygame.key.get_pressed()   
          
          pygame.draw.rect(self.display_surface, 'purple', offset_rect, 5)
          
          hitbox_rect = player.hitbox.copy()
          hitbox_rect.center = offset_rect.center
          pygame.draw.rect(self.display_surface, 'black', hitbox_rect, 5)
          
          target_pos = offset_rect.center + OFFSET_HERRAMIENTAS[player.status.split('_')[0]]
          pygame.draw.circle(self.display_surface, 'brown',target_pos, 5)