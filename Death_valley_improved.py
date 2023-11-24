import random, asciimatics, math, time, keyboard
from asciimatics.screen import Screen
from random import randint

#attempts_used = 0
#max_attempts = 200

def get_difficulty():
    diff = input('Difficulty: easy (e) normal (n) hard (h) custom (c)')
    if diff == 'e':
        return 30, 0.5
    elif diff == 'n':
        return 20, 0.3
    elif diff == 'h':
        return 10, 0.2
    else:
        print('custom settings')
        dist = int(input('input width: '))
        tickspeed = int(input('time between steps: '))
        return dist, tickspeed

def shiftwalls(wall_to_screen, wall_dist_left, wall_dist_right):
    wts = wall_to_screen
    wdl = wall_dist_left
    wdr = wall_dist_right
    
    d = randint(-1,1)
    if wts + d < 0:
        d = randint(0,1)
    elif wts + d > 20:
        d = randint(-1,0)

    wts += d
    wdl -= d
    wdr += d
    return wts, wdl, wdr

def emptyspace(n):
    x = 1
    if n == 0:
        return
    for i in range(n):
        print(" ", end= '')
        x += 1
    return

def printframe(wall_to_screen, wall_dist_left, wall_dist_right):
    emptyspace(wall_to_screen)
    print('I', end= '')
    emptyspace(wall_dist_left)
    print('*', end= '')
    emptyspace(wall_dist_right)
    print('I', end = '\n')

def move(wall_dist_left, wall_dist_right):

    if keyboard.is_pressed('q'):
        wall_dist_left -= 1
        wall_dist_right += 1
    if keyboard.is_pressed('e'):
        wall_dist_left += 1
        wall_dist_right -= 1
    return wall_dist_left, wall_dist_right

def death(wall_dist_left, wall_dist_right):
    crashed = False
    if wall_dist_left < 1 or wall_dist_right < 1:
        print('you have crashed into the wall')
        time.sleep(0.5)
        print('and disintegrated')
        time.sleep(3)
        crashed = True
        return crashed
    return crashed

def win(crashed):
    if crashed == False:
        print('well done-you have made it')
        time.sleep(0.5)
        print('through death valley')
        time.sleep(3)

def main():

    steps_to_end = int(200)
    width, tickspeed = get_difficulty()

    wall_to_screen = int(10)
    wall_dist_left = int(width/2)
    wall_dist_right = int(width/2)
    
    for i in range(steps_to_end):
        crashed = death(wall_dist_left, wall_dist_right)
        if crashed == True:
            break
        wall_dist_left, wall_dist_right = move(wall_dist_left, wall_dist_right)
        printframe(wall_to_screen, wall_dist_left, wall_dist_right)
        wall_to_screen, wall_dist_left, wall_dist_right = shiftwalls(wall_to_screen, wall_dist_left, wall_dist_right)
        
        time.sleep(tickspeed)
    win(crashed)

main()