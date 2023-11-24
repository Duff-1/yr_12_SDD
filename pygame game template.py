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
    x = 3
    y = 5
    z = 3
    v = 2
    x, y, z, v = summation(x, y, z, v)
    print(f"x (after): {x}, y: {y}, z: {z}, v:{v}")
    looping = True

    while looping :
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
    
main()
summation(3,5,3,2)
