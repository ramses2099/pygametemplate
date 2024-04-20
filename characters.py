import pygame
from settings import *

class NPC(pygame.sprite.Sprite):
    def __init__(self, game, scene, groups, pos, name):
      super().__init__(groups)
      
      self.game = game
      self.scene = scene
      self.name = name
      self.image = pygame.Surface((TITLESIZE, TITLESIZE*1.5))
      self.image.fill(COLORS['green'])
      self.rect = self.image.get_frect(topleft = pos)
      self.speed = 60
      self.force = 2000
      self.acc = vec()
      self.vel = vec()
      self.fric = -15
      
    def physics(self, dt):
        # direcction x
        self.acc.x += self.vel.x * self.fric
        self.vel.x += self.acc.x * dt
        self.rect.centerx += self.vel.x * dt + (self.vel.x/2) * dt
        
        # direcction y
        self.acc.y += self.vel.y * self.fric
        self.vel.y += self.acc.y * dt
        self.rect.centery += self.vel.y * dt + (self.vel.y/2) * dt
        
        if self.vel.magnitude() >= self.speed:
            self.vel = self.vel.normalize() * self.speed

    def update(self, dt):
        self.physics()
    
class Player(NPC):
     def __init__(self, game, scene, groups, pos, name):
      super().__init__(game, scene, groups, pos, name)
    
     def movement(self):
         if INPUTS['left']:
             self.acc.x =-self.force
         elif INPUTS['right']:
             self.acc.x = self.force
         else:
             self.acc.x = 0
        
         if INPUTS['up']:
             self.acc.y =-self.force
         elif INPUTS['down']:
             self.acc.y = self.force
         else:
             self.acc.y = 0
             
     def update(self, dt):
         self.physics(dt)
         self.movement()