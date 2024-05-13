import pygame, sys, math, random
from pygame.locals import *
pygame.init()
pygame.font.init()

# Aspects
BACKGROUND = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FONT = pygame.font.SysFont('Arial', 20)


# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Game')


def summation(x,y,z,v):
    x = x
    for i in y:
        if v == 1:
            x = x + z
        if v == 2:
            x = x * z
        if v == 3:
            x = x / z
    return x,y,z,v
    
def main():
    looping = True

    while looping :
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

        WINDOW.fill(BACKGROUND)
        strips(0,0.000000055,0.000000055)



        fpsClock.tick(FPS)
        pygame.display.flip()


def strips(source1,source2,wavelength):
    for point in range(1,WINDOW_WIDTH):
        pd = abs(source1*point-source2*point)
        if pd%(wavelength/2) == 0:
            pygame.draw.line(WINDOW,RED,(point,0),(point,WINDOW_HEIGHT),3)
        if pd%wavelength == 0:
            pygame.draw.line(WINDOW,BLUE,(point,0),(point,WINDOW_HEIGHT),3)

#def strips2(screen_dist,slit_sep,wavelength):
#    pointdiff = 
#    for point in range(1,WINDOW_WIDTH/2):
        



main()
