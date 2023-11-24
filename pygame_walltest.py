#!python

import sys
import os
import pygame
from pygame.locals import *

def load_png(name):
    """ Load image and return image object"""
    #fullname = os.path.join("data", name)
    try:
        image = pygame.image.load(name)
        if image.get_alpha is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {name}")
        raise SystemExit
    return image, image.get_rect()

class Wall(pygame.sprite.Sprite):
    """ A wall segment that will fall down the screen and remove itself when off the bottom """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png("wall.png")
        self.rect.top = y
        self.rect.left = x

    def update(self):
        self.rect.move_ip(0,1)
    
def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Basic Pong")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    test_wall = Wall(10,-10)

    # our groups of things
    walls = pygame.sprite.RenderPlain(test_wall)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()

    # Event loop
    while True:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)



        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        walls.clear(screen, background)
        walls.update()
        walls.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
