#importing librarys
import pygame, sys
from pygame.locals import*
from Asteroid import*
from Ship import*
#initializing/setup
pygame.init()

screen_info = pygame.display.Info()
width = int(screen_info.current_w)
height = int(screen_info.current_h)
size = (width,height)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
color = (30,0,30)
screen.fill(color)
#variables
numlevel = 8
Level = 1
asteroidCount = 4
player = ShipClass((20,200))

#defining main 
def main():
  global Level
  global numlevel
  while Level <= numlevel:
    clock.tick(60) 
    #input
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
          player.speed[0] = 10
        if event.key == pygame.K_LEFT:
          player.speed[0] = -10
        if event.key == pygame.K_DOWN:
          player.speed[1] = 10
        if event.key == pygame.K_UP:
          player.speed[1] = -10
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
          player.speed[0] = 0
        if event.key == pygame.K_LEFT:
          player.speed[0] = 0
        if event.key == pygame.K_UP:
          player.speed[1] = 0
        if event.key == pygame.K_DOWN:
          player.speed[1] = 0
        
    


    player.movement()     
    screen.fill(color)
    screen.blit(player.image,player.rect)
    pygame.display.flip()
#mainloop
if __name__ == "__main__":
  main()
