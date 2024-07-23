import pygame, sys, math, random
from pygame.locals import * # type: ignore
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
WINDOW_HEIGHT =600
WINDOW_WIDTH =600

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Game')

#class trapezoid:
#    def __init__(self, x, y):
        
def squareall(term,n):
    for i in range(1,n):
        term = term*term
    return term

def f(x,gradient):
    #y = WINDOW_HEIGHT - 0.004*(WINDOW_HEIGHT - (2.6*gradient)*x) * (x+2*gradient)
    #y = 0.001 * gradient*(squareall(((x)-WINDOW_WIDTH/2), 2)) - WINDOW_HEIGHT
    y = 0.001 * gradient*(squareall(((x)-WINDOW_WIDTH/2), 2)) - WINDOW_HEIGHT
    y = -y
    return y


def draw_trapezoid_side(x, gradient):
    ypoint = f(x,gradient)
    pygame.draw.line(WINDOW, RED, (x, WINDOW_HEIGHT), (x, ypoint), 1)


def drawline(x,gradient):
    for x in range(WINDOW_WIDTH):
        y = f(x,gradient)
        pygame.draw.circle(WINDOW, BLUE, (x,y), 1)

def drawlines(gradient, start, stop, partitions):
    x = start
    middle_sum = 0
    xpoints = []
    while x < stop:
        draw_trapezoid_side(x, gradient)
        
        xpoints.append(x)
        
        x+=(stop-start)/partitions
        
        
    
    temp = xpoints[0]
    
    for value in xpoints:
        if value != xpoints[-1] and value != xpoints[0]:
            middle_sum += (WINDOW_HEIGHT - f(value,gradient))
    
    for value in xpoints:
        pygame.draw.line(WINDOW, RED, (value, f(value,gradient)), (temp, f(temp,gradient)), 1)
        temp = value
    A = ((stop-start)/((partitions-1)*2)) * ((WINDOW_HEIGHT - f(start,gradient)) + (WINDOW_HEIGHT -f(stop,gradient)) + 2*(middle_sum)) #not working
    return A


def text_display(text,position):
    text_render = FONT.render(text, True, (0,0,0))
    WINDOW.blit(text_render, position)


def main():

    x = 0
    #gradient = 0.3852
    gradient = 2
    pygame.time.wait(1000)
    looping = True

    while looping :
        try:
            for event in pygame.event.get() :
                if event.type == QUIT :
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_q:
                    gradient -= 0.01

                if event.type == KEYDOWN and event.key == K_e:
                    gradient += 0.01
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_x, mouse_y = mouse_pos
            text = f'    graph_y = {round((WINDOW_HEIGHT - f(mouse_x,gradient)),3)}'
            text2 = f'    graph_x = {mouse_x}'
            position = (mouse_x,mouse_y) if mouse_x < (2*WINDOW_WIDTH/3) else (mouse_x-(WINDOW_WIDTH/3),mouse_y)
            position2 = (mouse_x,mouse_y+40)if mouse_x < (2*WINDOW_WIDTH/3) else (mouse_x-(WINDOW_WIDTH/3),mouse_y+40)
            position3 = (mouse_x,mouse_y+80)if mouse_x < (2*WINDOW_WIDTH/3) else (mouse_x-(WINDOW_WIDTH/3),mouse_y+80)
            
            WINDOW.fill(BACKGROUND)
            A = drawlines(gradient, start=0, stop=mouse_x, partitions=1000)
            print(A)
            
            text3 = f'    graph_area = {A}'
            
            drawline(x,gradient)
            
            text_display(text,position)
            text_display(text2,position2)
            text_display(text3,position3)
            
            fpsClock.tick(FPS)
            pygame.display.flip()
        except:
            pass

main()
