import pygame

# Creamos una clase de Timer (temporizador)
class Timer:
    def __init__(self, duracion, funcion=None):
      self.duracion = duracion # Establece la duración del timer
      self.funcion = funcion # Recibe la función a ejecutarse después

      self.tiempo_inicio = 0
      self.activo = False

    def activate(self):  
      self.activo = True
      self.tiempo_inicio = pygame.time.get_ticks()
    
    def deactivate(self):
      self.activo = False
      self.tiempo_inicio = 0

    def update(self):
      tiempo_de_ejecucion = pygame.time.get_ticks()
      
      if tiempo_de_ejecucion - self.tiempo_inicio >= self.duracion:
       self.deactivate()
      if self.funcion:
         self.funcion()