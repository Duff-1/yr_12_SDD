#death_valley_pygame_imp
from ipaddress import v4_int_to_packed
import re
import pygame, sys, math, random, time
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


def text_objects(text, font):
	textsurface = font.render(text, True, BLACK)
	return textsurface, textsurface.get_rect()

def button(msg, x, y, w, h, colour1, colour2, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(WINDOW, colour2, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                game()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
    else:
        pygame.draw.rect(WINDOW, colour1, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x+(w/2)), (y+(h/2)))
    WINDOW.blit(textsurf, textrect)
       


def playerhitbox(playerX, playerY, playerW, playerH):
    p_hitbox = pygame.Rect(playerX, playerY, playerW, playerH)
    
    pygame.draw.rect(WINDOW, RED, p_hitbox)
    
    return p_hitbox

def wallhitbox(wallX,wallY,wallW,wallH):
    w_hitbox = pygame.Rect(wallX,wallY,wallW,wallH)
    
    pygame.draw.rect(WINDOW, RED, w_hitbox)
    
    return w_hitbox

def wallcollision(p_hitbox):
    
    if p_hitbox.colliderect(Wall.self.rect) == True:
        print('collide')
        return True
    return False
    

def playermove(playerX, playerY, dead):

    
    if not dead:
        pressed = pygame.key.get_pressed()
        if (pressed[K_RIGHT] or pressed[K_d]) :
            playerX += 3
        if (pressed[K_LEFT] or pressed[K_a]) :
            playerX -= 3
        if (pressed[K_DOWN] or pressed[K_s]) :
            playerY += 3
        if (pressed[K_UP] or pressed[K_w]) :
            playerY -= 3
    return playerX, playerY

def titlescreen():
    title = True
    while title:
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        button('Start', 200, 200 , 80, 30, BLUE, RED, 'play')

                
        pygame.display.update()
        fpsClock.tick(FPS)
        WINDOW.fill(BACKGROUND)
        

def game () :
    looping = True
    playerX, playerY, playerW, playerH = 30, 30, 30, 30

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
    
    walls = pygame.sprite.RenderPlain(test_wall1, test_wall2, test_wall3, test_wall4, test_wall5, test_wall6, test_wall7, test_wall8,test_wall9, test_wall10, test_wall11, test_wall12, test_wall13, test_wall14, test_wall15, test_wall16)
    
    # Fill background
    background = pygame.Surface(WINDOW.get_size())
    background = background.convert()
    background.fill((BACKGROUND))
    
    # Blit everything to the screen
    WINDOW.blit(background, (0, 0))
    pygame.display.flip()
    
    
    # The main game loop
    while looping :
        # Get inputs
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        
        playerX, playerY = playermove(playerX, playerY, False)
        p_hitbox = playerhitbox(playerX, playerY, playerW, playerH)

        walls.clear(WINDOW, background)
        walls.update()
        walls.draw(WINDOW)
        
        wallcollision(p_hitbox)
        pygame.display.update()
        fpsClock.tick(FPS)
        WINDOW.fill(background)

titlescreen()

#walls = []
#walls1 = []
#walls.append(walls1)
#movewall(walls)