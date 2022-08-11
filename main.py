#importing librarys
import pygame, sys, random, pandas as pd
from pygame.locals import*
from Asteroid import AsteroidClass
from Ship import ShipClass
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

df = pd.read_csv("game_info.csv")

#variables
numlevel = df['LevelNum'].max()
Level = df['LevelNum'].min()
LevelData = df.iloc[Level]
asteroids = pygame.sprite.Group()
asteroidCount = LevelData['AsteroidCount']
player = ShipClass((LevelData['PlayerX'], LevelData['PlayerY']))

def win():
  font = pygame.font.SysFont(None,70)
  text = font.render("You Win!!!", True, (255,0,0))
  text_rec = text.get_rect()
  text_rec.center = (width/2, height/2)
  while True:
    screen.fill(color)
    screen.blit(text,text_rec)
    pygame.display.flip()


def init():
  global asteroidCount , LevelData
  global asteroids
  LevelData = df.iloc[Level]
  player.reset ((20,200))
  asteroids.empty()
  asteroidCount += 2
  for i in range(asteroidCount):
    asteroids.add(AsteroidClass((random.randint(50, width - 50),random.randint(50, height - 50)), random.randint(15, 60)))
    

#defining main 
def main():
  global Level, numlevel
  init()
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

    screen.fill(color)
    player.movement() 
    for asteroid in asteroids:
      asteroid.movement()
    get_hit = pygame.sprite.spritecollide(player,asteroids, False)
    asteroids.draw(screen)
    screen.blit(player.image,player.rect)
    pygame.display.flip()

    if player.checkReset(width):
      if Level == numlevel:
        break
      else:
        Level+=1
        init()
    elif get_hit:
      player.reset((LevelData['PlayerX'],LevelData['PlayerY']))
      player.reset((LevelData['PlayerX'],LevelData['PlayerY']))
      #mainloop
  win()
if __name__ == "__main__":
  main()

