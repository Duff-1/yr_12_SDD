#!python

import sys
import os
import time
import random
import pygame
from pygame.locals import * # type: ignore
pygame.font.init()
font = pygame.font.SysFont('Arial', 20)


    
window_width = 640
window_height = 480

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Asteroid valley")

# player control variables
player_move_speed = 3

# wall control variables
fall_rate = 4
starting_top = -64
current_left = [50, 500]
block_size = 64
wall_jitter = 0.5

#creates a cache of images to reference
image_cache = {}

def load_png(name, label):
    """ Load image into cache and return it """
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
    #return image, image.get_rect()
    image_cache[label] = image
    return image

class Wall(pygame.sprite.Sprite):
    """ A wall segment that will fall down the screen. When it reaches the bottom it will
    simply move itself to the top at the a new x offset """

    def __init__(self, side, left=None, top=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = image_cache['wall']
        self.rect = self.image.get_rect()
        self.side = side
        top = self.initial_top(top)
        left = self.initial_left(left)
        self.rect.update(left, top, self.rect.width, self.rect.height)

    def jitter(self):
        return self.rect.width * wall_jitter
    
    #returns initial top as long as top does not exist
    def initial_top(self, top):
        return starting_top if top is None else top
    
    def initial_left(self, left):
        # dont let wall0 and wall1 overlap each other (or leave no space between themselves) (this shouldn't work, but it does so I'm leaving it in)
        wall_dist = current_left[1] - current_left[0]
        if left is not None:
            return left
        elif self.side == 'left':
            if wall_dist >= block_size*2.5:
                current_left[0] = current_left[0] + self.jitter() * (1 if random.random() < 0.5 else -1)
            else:
                current_left[0] = current_left[0] - self.jitter()
            # make sure we dont go past the left edge of the screen
            if current_left[0] < 0:
                current_left[0] = 0
            return current_left[0]
        else:
            if wall_dist >= block_size*2.5:
                current_left[1] = current_left[1] + self.jitter() * (1 if random.random() < 0.5 else -1)
            else:
                current_left[1] = current_left[1] + self.jitter()
            # make sure we don't go more than 1 wall width away from the right of the screen
            if current_left[1] > window_width-block_size:
                current_left[1] = window_width-block_size
            return current_left[1]

    def update(self):
        self.rect.move_ip(0, fall_rate)
        if self.rect.top >= window_height:
            self.rect.update( self.initial_left(None), self.initial_top(None), self.rect.width, self.rect.height )

class Ship(pygame.sprite.Sprite):
    """ A movable player character """
    def __init__(self, left, top):
        pygame.sprite.Sprite.__init__(self)
        self.speed = player_move_speed
        self.next_move = [0,0]
        self.state = 'still'
        self.image = image_cache['player']
        self.rect = self.image.get_rect()
        self.rect.update(left, top, self.rect.width, self.rect.height)
    
    def update(self):
        if self.state == 'move_right':
            self.rect.move_ip( self.speed, 0 )
        elif self.state == 'move_left':
            self.rect.move_ip( -self.speed, 0 )

    #states for movement l/r
    def move_left(self):
        self.state = "move_left"
    
    def move_right(self):
        self.state = "move_right"
    
    def stop(self):
        self.state = "still"

def titlescreen():
    
    #Background processing
    game_background = pygame.image.load('titlescreen.png').convert_alpha()
    game_background = pygame.transform.scale(game_background, (window_width, window_height))
    
    #init variables:
    button_play = button(screen, (200, 300), "Play")
    looping = True
    clock = pygame.time.Clock()
    while looping :
        clock.tick(60)
        # Get inputs
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

            # Check if mouse click 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.collidepoint(pygame.mouse.get_pos()):
                    main()
        #button+bg creation
        screen.blit(game_background, (0, 0))
        button_play = button(screen, (200, 300), "Play")
        
        pygame.display.update()

def displayScore(currentScore): # Displays the current score
    score = font.render("Score: " + str(int(currentScore/30)), True, (255, 255, 255))
    if currentScore <= 1000:
        screen.blit(score, (20, 10))
    else:
        screen.blit(score, (10, 10))

def button(window, position, text): # Creates a button
    buttonFont = pygame.font.SysFont("Arial", 50)
    text_render = buttonFont.render(text, 1, (255, 0, 0)) # type: ignore
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(window, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(window, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(window, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(window, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(window, (100, 100, 100), (x, y, w , h))
    return window.blit(text_render, (x, y))
 
def main():
    # Initialise screen
    pygame.init()
    
    # initialise the screen so we can load images
    global window_height
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Asteroid feild")
    
    # cache images
    i = load_png('wall.png', 'wall')
    block_size = i.get_rect().width
    i = load_png('player.png', 'player')
    player_size = i.get_rect().width
    
    #Background processing
    game_background = pygame.image.load('game_background.png').convert_alpha()
    game_background = pygame.transform.scale(game_background, (window_width, window_height))
    
    
    # resize window height to a multiple of wall block_size
    window_height = block_size * round(window_height/block_size)
    screen = pygame.display.set_mode((window_width, window_height))
    
    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # our groups of things
    walls = pygame.sprite.RenderPlain()

    player = Ship(250, window_height-1.5*block_size)
    players = pygame.sprite.RenderPlain(player)  # type: ignore

    current_score = 1
    # create our blocks from the bottom up
    for top in range(window_height, -block_size, (-block_size)):
        walls.add( Wall('left', None, top) )
        walls.add( Wall('right', None, top) )

    

    # Blit everything to the screen
    screen.blit(game_background, (0, 0))
    walls.draw(screen)
    pygame.display.flip()

    # Initialise clock
    clock = pygame.time.Clock()

    # Event loop
    playing = True
    while playing:
        # Make sure game doesn't run at more than 60 frames per second
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_LEFT:
                player.move_left()
            elif event.type == KEYDOWN and event.key == K_RIGHT:
                player.move_right()
            elif event.type == KEYUP and event.key in [K_LEFT, K_RIGHT]:
                player.stop()

        screen.blit(game_background, (0, 0))
        walls.clear(screen, background)
        players.clear(screen, background)
        walls.update()
        players.update()
        walls.draw(screen)
        players.draw(screen)
        displayScore(current_score)
        current_score += 1
        # do collision detect/death here
        if pygame.sprite.spritecollide( player, walls, 0 ): # type: ignore
            playing = False

        pygame.display.flip()

    # Game over!!!
    font = pygame.font.Font(None, 64)
    font.set_bold(True)
    game_over = font.render("GAME OVER!", True, (250,0,0))
    pos = game_over.get_rect( centerx=background.get_width()/2, centery=background.get_height()/2 )
    screen.blit( game_over, pos )
    scoredisplay = font.render(f'SCORE: {str(int(current_score/30))}', True, (250,0,0))
    pos2 = scoredisplay.get_rect( centerx=background.get_width()/2, centery=(background.get_height()/2 -64) )
    screen.blit( scoredisplay, pos2 )
    pygame.display.flip()
    time.sleep(5)


titlescreen()
