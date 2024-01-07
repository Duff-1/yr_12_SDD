#two-thirds average



import os
import math
import numpy as np

class player:
    guesses_array = []
    playerguess = {}
    


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def findvalunder(array, val):
    diff_list = []
    below = False
    for item in array:  
        diff = abs(array[item] - val)
        diff_list.append(diff)
        diff_list.sort()
    
    if diff_list[0] < 1: 
        below = True


    
    return diff_list[0]
    
    

def find_nearest_below_avg(array, value):
    array = np.asarray(array)
    array.sort()
    idx = (np.abs(array - value)).argmin()
    if array[idx] < value:
        return array[idx]
    else:
        arr2 = []
        for num in range(idx,len(array)):
            arr2.append(array[num])
        array = np.asarray(array)
        idx = (np.abs(array - value)).argmin()
        return idx
            
    
    
def normalplay():
    total=0
    name = ' '
    while name != '':
        name = input('name: ')
        
        if name == '':
            break
        
        guess = int(input('guess '))
        
        player.playerguess[name] = guess
        
        os.system('cls')
    
    for item,itemname in enumerate(player.playerguess):
        
        total+=int(player.playerguess[itemname])
        print(f'{itemname} guessed {player.playerguess[itemname]}')
        
        #prep for getting closest
        player.guesses_array.append(player.playerguess[itemname])
    
    print(f'number of guesses: {len(player.playerguess)}')
    print(f'total of all guesses: {total}')
    
    average = total / len(player.playerguess)
    two_thirds_avg = average * (2/3)
    
    print(f'two thirds average: {two_thirds_avg}')
    
    closestguess = find_nearest(player.guesses_array, two_thirds_avg)
    
    print(f'the closest guess was {closestguess}')
    
    for item,itemname in enumerate(player.playerguess):
        if player.playerguess[itemname] == closestguess:
            winner = itemname
    
    print(f'made by{winner}')
        
    
        
        
        
def notoverplay():
    total=0
    name = ' '
    while name != '':
        name = input('name: ')
        
        if name == '':
            break
        
        guess = int(input('guess '))
        
        player.playerguess[name] = guess
        
        os.system('cls')
    
    for item,itemname in enumerate(player.playerguess):
        
        total+=int(player.playerguess[itemname])
        print(f'{itemname} guessed {player.playerguess[itemname]}')
        
        #prep for getting closest
        player.guesses_array.append(player.playerguess[itemname])
    
    print(f'number of guesses: {len(player.playerguess)}')
    print(f'total of all guesses: {total}')
    
    average = total / len(player.playerguess)
    two_thirds_avg = average * (2/3)
    
    print(f'two thirds average: {two_thirds_avg}')
    
    closestguess = find_nearest(player.guesses_array, two_thirds_avg)
    
    print(f'the closest guess was {closestguess}')
    
    for item,itemname in enumerate(player.playerguess):
        if player.playerguess[itemname] == closestguess:
            winner = itemname
    
    print(f'made by{winner}')
    

def main():
    gametype = input('would you ike to play normally? (y), or have the closest answer without going over the average win? (n) ')

    if gametype == 'y':
        normalplay()
    else:
        a = None
main()