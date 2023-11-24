#testing walls
from ipaddress import v4_int_to_packed
import re
import pygame, sys, math, random, time, os
from pygame.locals import *
pygame.init()
pygame.font.init()

# Aspects
BACKGROUND = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FONT = pygame.font.SysFont('Arial', 20)
BLACK = (0, 0, 0)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 500

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Death valley')

def load_png(name):
    """ Load image and return image object"""
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()


class Wall(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('brick_texture2.png')
        self.area = WINDOW.get_rect()
        self.x = 40
        self.y = WINDOW_HEIGHT + 50
        self.w = 30
        self.h = 50

            
        pass
    
    def wallprint(self):
        wall_hitbox = pygame.Rect(self.x, self.y, self.w, self.h)
        pygame.draw.rect(WINDOW, RED, wall_hitbox)
    
    def wallmove(self, movespeed):
        self.y -= movespeed 


def main():
    wall1 = Wall()
    looping = True
    walls = pygame.sprite.RenderPlain(wall1)
    movespeed = int(input('speed'))
    while looping:
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        wall1.wallmove(movespeed)

        WINDOW.blit(WINDOW, wall1.rect)
        pygame.display.update()
        fpsClock.tick(FPS)
        WINDOW.fill(BACKGROUND)

main()