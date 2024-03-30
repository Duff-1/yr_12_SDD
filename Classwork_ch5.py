import pygame, sys, random
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
BARCOLOUR = (50, 50, 200)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')




 
looping = True


values = []


# The main game loop
def getvalues(values):
    print ('') # Just to space things out
    nextValue = int(input('Please enter the next number : '))
    values.append(nextValue)
    return values

def drawbars(BARCOLOUR, WINDOW_HEIGHT, WINDOW, values, barWidth, heightUnit, counter):
    while counter < len(values) :
            barX = counter * barWidth
            barHeight = heightUnit * values[counter]
            barY = WINDOW_HEIGHT - barHeight
   	 
            bar = pygame.Rect(barX, barY, barWidth, barHeight)
            
            pygame.draw.rect(WINDOW, BARCOLOUR, bar)
            counter = counter + 1

def setparamaters(WINDOW_WIDTH, WINDOW_HEIGHT, values):
    barWidth = int(WINDOW_WIDTH / len(values))
    newArray = values.copy()
    newArray.sort()
    largestValue = newArray[-1]
    
    heightUnit = int(WINDOW_HEIGHT / largestValue)
    return barWidth,heightUnit

while looping :
	# Get inputs
    for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()
    
    values = getvalues(values)
    
	# Processing
	# This section will be built out later
    print (values)
    


    # Render elements of the game
    WINDOW.fill(BACKGROUND)
    
    barWidth,heightUnit = setparamaters(WINDOW_WIDTH, WINDOW_HEIGHT, values)
    
    counter = 0

    drawbars(BARCOLOUR, WINDOW_HEIGHT, WINDOW, values, barWidth, heightUnit, counter)
    
    pygame.display.update()
    fpsClock.tick(FPS)
