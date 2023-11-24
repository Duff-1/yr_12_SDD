import random, time, keyboard, os, curses

#stdscr = curses.initscr()

#player location
def playerlocation(baseline):
    player_loc = 0
    for i in range(len(baseline)):
        if(baseline[i])=="*":
        #print(i,"player location")
            player_loc = i
            
    return player_loc


#wall locations
def walllocation(line1):
    wall_loc1 = 0
    wall_loc2 = 0
    for i in range(len(line1)):
        if(line1[i])=="I" and wall_loc1 == 0:
        #print(i,"wall1")
            wall_loc1 = i
        if(line1[i])=="I" and wall_loc1 != 0:
        #print(i,"wall2")
            wall_loc2 = i

            
    return wall_loc1, wall_loc2

#display things  
def showscreen(screen):
    for i in range(len(screen)):
        print("".join(screen[i]))

    #clear screen
    os.system("cls")

#movement
def movement(baseline, player_loc):
    if keyboard.is_pressed('q'):
        baseline[player_loc] = ' '
        player_loc -= 1
        baseline[player_loc] = '*'

    elif keyboard.is_pressed('e'):
        baseline[player_loc] = ' '
        player_loc += 1
        baseline[player_loc] = '*'
    return baseline

# scrolling and generation
def scroll(screen):
    
    screen[10] = screen[9]
    screen[9] = screen[8]
    screen[8] = screen[7]
    screen[7] = screen[6]
    screen[6] = screen[5]
    screen[5] = screen[4]
    screen[4] = screen[3]
    screen[3] = screen[2]
    screen[2] = screen[1]
    screen[1] = screen[0]
    screen[0] = generate_newline(screen[0], screen)
        
    return screen

            
        
########################bad
def generate_newline(line1,screen):
    wall1, wall2 = walllocation(line1)
    if wall1 == 0:
        shift = random.randint(0,1)
    elif wall2 == len(screen) -1:
        shift = random.randint(-1,0)
    else:
        shift = random.randint(-1,1)
    
    line1[wall1] = ' '
    wall1 = wall1 + shift
    line1[wall1] = 'I'
    
    line1[wall2] = ' '
    wall2 = wall2 + shift
    line1[wall2] = 'I'
    
    return line1
    
    
    
    
    

def main():
    
    #init variables
    
    line1 = [' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ']
    line2 = [' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ']
    line3 = [' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ']
    line4 = [' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ']
    line5 = [' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ']
    line6 = [' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ']
    line7 = [' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ']
    line8 = [' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ']
    line9 = [' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ']
    line10 = [' ',' ',' ',' ','I',' ',' ',' ',' ',' ',' ',' ','I',' ',' ',' ',' ']

    baseline = [' ',' ',' ',' ','I',' ',' ',' ','*',' ',' ',' ','I',' ',' ',' ',' ']

    screen = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,baseline]
    
    on = True
    while on:
        screen = scroll(screen)
        screen[10] = baseline
        player_loc = playerlocation(baseline)
        baseline = movement(baseline, player_loc)
        showscreen(screen)

main()