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
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 800

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Game')

def update():
    fpsClock.tick(FPS)
    WINDOW.fill(BACKGROUND)
    createArc(200,60,9.8)
    pygame.display.flip()

def createArc(total_velocity, angle, gravity):
    #processing
    yVelcoity = math.sin(math.radians(angle))*total_velocity
    xVelocity = math.cos(math.radians(angle))*total_velocity
    time = math.sqrt((2*yVelcoity)/gravity)
    xEnd = (xVelocity*time)
    xPoint = (xEnd,WINDOW_HEIGHT)
    yMax = (yVelcoity*(time/2))-((gravity*(time*time))/2)
    yPoint = ((xEnd/2),WINDOW_HEIGHT-yMax)


    #display points
    pygame.draw.circle(WINDOW,BLUE,(0,WINDOW_HEIGHT),5,3) #start
    pygame.draw.circle(WINDOW,BLUE,yPoint,5,3) #max height
    pygame.draw.circle(WINDOW,BLUE,xPoint,5,3) #end



    
    
def main():
    looping = True

    while looping :
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
        update()


    
main()
