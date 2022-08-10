#importing librarys
import pygame
from pygame.locals import* 
#class setup
class ShipClass(pygame.sprite.Sprite):
  def __init__(self,position):
    super().__init__()
    self.image = pygame.image.load("ship.png")
    self.image = pygame.transform.smoothscale(self.image,(40,40))
    self.rect = self.image.get_rect()
    self.rect.center = position
    self.speed = pygame.math.Vector2(0,0)
  def movement(self):
    self.rect.move_ip(self.speed)