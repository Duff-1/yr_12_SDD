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
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

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
        strips(0,0.000050,0.000050)

        #version2(0.000630,0,0.000050,2)

        fpsClock.tick(FPS)
        pygame.display.flip()


def strips(source1,source2,wavelength):
    for point in range(1,int(WINDOW_WIDTH/2)):
        pd = abs(source1*point-source2*point)
        if pd%wavelength == 0:
            pygame.draw.line(WINDOW,BLUE,(point+(WINDOW_WIDTH/2),0),(point+(WINDOW_WIDTH/2),WINDOW_HEIGHT),1)
            pygame.draw.line(WINDOW,BLUE,((WINDOW_WIDTH/2)-point,0),((WINDOW_WIDTH/2)-point,WINDOW_HEIGHT),1)
        else:
            pygame.draw.line(WINDOW,RED,(point+(WINDOW_WIDTH/2),0),(point+(WINDOW_WIDTH/2),WINDOW_HEIGHT),1)
            pygame.draw.line(WINDOW,RED,((WINDOW_WIDTH/2)-point,0),((WINDOW_WIDTH/2)-point,WINDOW_HEIGHT),1)
    
def version2(wavelength,source1,source2,screen_dist):
    fringe1_sep = ((wavelength*screen_dist)/(abs(source1-source2)))/1000
    theta = math.degrees(math.atan2(fringe1_sep,2))
    dist_true = 0
    i = 0
    while dist_true < WINDOW_WIDTH:
        i+=1
        dist_true = i*wavelength/math.sin(math.radians(theta))
        print
        print(dist_true)

        pygame.draw.line(WINDOW,RED,(dist_true,0),(dist_true,WINDOW_HEIGHT),1)


        
        



main()
