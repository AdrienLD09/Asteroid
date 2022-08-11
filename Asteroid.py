import pygame, random

class AsteroidClass(pygame.sprite.Sprite):
  def __init__(self, pos, size):
    super().__init__()
    self.image = pygame.image.load("asteroid.png")
    self.image = pygame.transform.smoothscale(self.image,(size,size))
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.speed = pygame.math.Vector2(0,3)
    self.speed.rotate_ip(random.randint(0,360))
def movement(self):
  screen_info = pygame.display.Info()
  self.rect.move_ip(self.speed)
  if self.rect.left <= 0 or self.rect.right >= screen_info.current_w:
    self.speed[0] *= - 1
    self.image = pygame.transform.flip(self.image, True, False)
    self.rect.move_ip(self.speed[0],0)
  if self.rect.bottom <= 0 or self.rect.top >= screen_info.current_h:
    self.speed[1] *= - 1
    self.image = pygame.transform.flip(self.image, False, True)
    self.rect.move_ip(0,self.speed[1])
  