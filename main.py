import pygame,sys
from settings import *
from level import Level

#Pygame Setup
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()
bg = pygame.image.load("img/bg.jpg")
level = Level()

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # screen.fill(BG_COLOR)
    screen.blit(bg,(0,0))
    level.run()

    # draw logic
    pygame.display.update()
    clock.tick(FPS)