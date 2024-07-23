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
        
def squareall(term,n):
    for i in range(1,n):
        term = term*term
    return term

def f(x,gradient):
    y = -gradient*(squareall(scaledx(x), 2)) - (WINDOW_HEIGHT/2)
    print(y)
    x = scaledx(x)
    #y = scaledy(y)
    return y



def drawline(x,gradient):
    for x in range(WINDOW_WIDTH):
        y = f(x,gradient)
        pygame.draw.circle(WINDOW, BLUE, (x,y), 1)
    
    for x in range(0,WINDOW_WIDTH,10):
        y = f(x,gradient)
        pygame.draw.circle(WINDOW, RED, (x,y), 3)




def text_display(text,position):
    text_render = FONT.render(text, True, (0,0,0))
    WINDOW.blit(text_render, position)

class store:
    scale = None

class point:
    def __init__(self,x,y):
        self.real_x = x
        self.real_y = y
        self.scale = store.scale
        self.x = scaledx(x)
        self.y= scaledy(y)
        self.update()

    def showval(self):
        mx,my = pygame.mouse.get_pos()
        if mx < self.real_x+10 and mx > self.real_x-10:
            text_display(f"{self.x}",(self.real_x,self.real_y)) if self.real_x != WINDOW_HEIGHT/2 else None
        if my < self.real_y+10 and my > self.real_y-10:
            text_display(f"{self.y}",(self.real_x,self.real_y)) if self.real_y != WINDOW_WIDTH/2 else None

    def update(self):
        self.showval()
        self.scale = store.scale
        self.x = scaledx(self.real_x)
        self.y = scaledy(self.real_y)
        pygame.draw.circle(WINDOW,BLUE,(self.real_x,self.real_y),3,0)

def scaledy(value):
    try:
        scaledvalue = -(value-WINDOW_HEIGHT/2)/store.scale
    except:
        scaledvalue = 0
    return scaledvalue

def scaledx(value):
    try:
        scaledvalue = (value-WINDOW_WIDTH/2)/store.scale
    except:
        scaledvalue = 0
    return scaledvalue

def unscalex(value):
    unscaled = value*store.scale+(WINDOW_WIDTH/2)
    return unscaled

def unscaley(value):
    unscaled = -(value*store.scale+(WINDOW_WIDTH/2))
    return unscaled

def main():
    store.scale = 30
    x = 0
    gradient = 2
    looping = True
    points = []
    for x in range(0,WINDOW_WIDTH,20):
        points.append(point(x,WINDOW_HEIGHT/2))
    for y in range(0,WINDOW_HEIGHT,20):
        points.append(point(WINDOW_WIDTH/2,y))

    while looping :
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    store.scale -= 1 if store.scale > 0 else 0
                elif event.y == -1:
                    store.scale += 1 if store.scale < 100000 else 0


        WINDOW.fill(BACKGROUND)

        pygame.draw.line(WINDOW,(BLUE),(0,WINDOW_HEIGHT/2),(WINDOW_WIDTH,WINDOW_HEIGHT/2),1)
        pygame.draw.line(WINDOW,(BLUE),(WINDOW_WIDTH/2,0),(WINDOW_WIDTH/2,WINDOW_HEIGHT),1)
        for dot in points:
            dot.update() 
    
        # mouse_pos = pygame.mouse.get_pos()
        # mouse_x, mouse_y = mouse_pos
        # text = f'    graph_y = {round((WINDOW_HEIGHT - f(mouse_x,gradient)),3)}'
        # text2 = f'    graph_x = {mouse_x}'
        # position = (mouse_x,mouse_y) if mouse_x < (2*WINDOW_WIDTH/3) else (mouse_x-(WINDOW_WIDTH/3),mouse_y)
        # position2 = (mouse_x,mouse_y+40)if mouse_x < (2*WINDOW_WIDTH/3) else (mouse_x-(WINDOW_WIDTH/3),mouse_y+40)
        # position3 = (mouse_x,mouse_y+80)if mouse_x < (2*WINDOW_WIDTH/3) else (mouse_x-(WINDOW_WIDTH/3),mouse_y+80)
        
        
        # A = drawlines(gradient, start=0, stop=mouse_x, partitions=10)
        # print(A)
                
        drawline(x,gradient)
        
        # text_display(text,position)
        # text_display(text2,position2)
        # text_display(text3,position3)
        
        fpsClock.tick(FPS)
        pygame.display.flip()

main()
