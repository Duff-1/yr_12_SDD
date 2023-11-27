#!python
import random
import sys
import os
import pygame
from pygame.locals import * # type: ignore

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

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

class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png("Player-2.png")
        self.rect.top = y
        self.rect.left = x
    
    def update(self):

        #self.rect.colliderect(Wall.rect)

        
        pressed = pygame.key.get_pressed()
        if (pressed[K_RIGHT] or pressed[K_d]) :
            self.rect.move_ip(3,0)
        if (pressed[K_LEFT] or pressed[K_a]) :
            self.rect.move_ip(-3,0)
        if (pressed[K_DOWN] or pressed[K_s]) :
            self.rect.move_ip(0,3)
        if (pressed[K_UP] or pressed[K_w]) :
            self.rect.move_ip(0,-3)
        
        print(self.rect)
        if self.rect.left > WINDOW_WIDTH - 64:
            self.rect.left = WINDOW_WIDTH - 64
        if self.rect.left < 0:
            self.rect.left = 0
        

class Wall(pygame.sprite.Sprite):
    """ A wall segment that will fall down the screen and go back to the top when off the bottom """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png("wall.png")
        self.rect.top = y
        self.rect.left = x

    def update(self):

        self.rect.move_ip(0,1)
        print(self.rect)
        maxmoveleft = -self.rect.left
        maxmoveright = WINDOW_WIDTH -self.rect.left
        movedecide = random.randint(1,3)
        if movedecide == 1:
            move = -64
        elif movedecide == 2:
            move = 0
        else:
            move = 64
        if self.rect.top > WINDOW_HEIGHT:
            self.rect.move_ip(move, -(WINDOW_HEIGHT+64))

class Pickup(pygame.sprite.Sprite):
    """ A wall segment that will fall down the screen and go back to the top when off the bottom """

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png("wall.png")
        self.rect.top = y
        self.rect.left = x

    def update(self):

        self.rect.move_ip(0,1)
        print(self.rect)
        maxmoveleft = -self.rect.left
        maxmoveright = WINDOW_WIDTH -self.rect.left
        movedecide = random.randint(1,3)
        if movedecide == 1:
            move = -64
        elif movedecide == 2:
            move = 0
        else:
            move = 64
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

def collision(walls, players):
    if pygame.sprite.groupcollide(players, players, False, False):
        print('collide')
        
def pickupcollision(pickups, players):
    if pygame.sprite.groupcollide(players, pickups, False, True):
        print('collide')

def createraandompickup():
    return

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Walltest")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))


    startwall1 = 180
    startwall2 = 380
    test_wall1 = Wall(startwall1,-64)
    test_wall2 = Wall(startwall2, -64)
    test_wall3 = Wall(startwall1, -(64*2))
    test_wall4 = Wall(startwall2, -(64*2))
    test_wall5 = Wall(startwall1, -(64*3))
    test_wall6 = Wall(startwall2, -(64*3))
    test_wall7 = Wall(startwall1, -(64*4))
    test_wall8 = Wall(startwall2, -(64*4))
    test_wall9 = Wall(startwall1,-(64*5))
    test_wall10 = Wall(startwall2, -(64*5))
    test_wall11 = Wall(startwall1, -(64*6))
    test_wall12 = Wall(startwall2, -(64*6))
    test_wall13 = Wall(startwall1, -(64*7))
    test_wall14 = Wall(startwall2, -(64*7))
    test_wall15 = Wall(startwall1, -(64*8))
    test_wall16 = Wall(startwall2, -(64*8))
        
    player = Player((WINDOW_WIDTH/2), (WINDOW_HEIGHT/2))
    
    pickup = Pickup((WINDOW_WIDTH/2), (WINDOW_HEIGHT/10))
    
    # our groups of things

    walls = pygame.sprite.RenderPlain(test_wall1, test_wall2, test_wall3, test_wall4, test_wall5, test_wall6, test_wall7, test_wall8,test_wall9, test_wall10, test_wall11, test_wall12, test_wall13, test_wall14, test_wall15, test_wall16) # type: ignore

    players = pygame.sprite.RenderPlain(player) # type: ignore
    
    pickups = pygame.sprite.RenderPlain(pickup) # type: ignore
    
    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()
    # Event loop
    while True:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        collision(walls, players)
        
        pickupcollision(pickups, players)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        players.clear(screen, background)
        players.update()
        players.draw(screen)
        
        pickups.clear(screen, background)
        pickups.update()
        pickups.draw(screen)
        
        walls.clear(screen, background)
        walls.update()
        walls.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()
