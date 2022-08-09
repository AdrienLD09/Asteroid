#importing librarys
import pygame
from pygame.locals import*
from Asteroid import*
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

numlevel = 8
level = 1
asteroidCount = 4
#defining main 
def main():
  global Level
  global numlevel
#  while Level == numlevel:
    