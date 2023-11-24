
#testing_doc

#def snailracetest():
    # snail race test:

    #import random, time
    #def snailrace():
    #  
    #  guess = input('bet on snail (1)(2)(3): ')
    #  
    #  snail1 = ['1','@']
    #  snail2 = ['2','@']
    #  snail3 = ['3','@']
    #  
    #  race = True
    #  x = 1
    #  while race == True:
    #    x1 = random.randint(0,1)
    #    x2 = random.randint(0,1)
    #    x3 = random.randint(0,1)
    #    if x1 == 1:
    #      snail1.insert(1, '_')
    #    if x2 == 1:
    #      snail2.insert(1, '_')
    #    if x3 == 1:
    #      snail3.insert(1, '_')
    #    time.sleep(1)
    #    x = x+1
    #    
    #    print('')
    #    if x == 1:
    #      print(f'{x} second')
    #    else:
    #      print(f'{x} seconds')
    #    print('')
    #    
    #    print(f'{snail1}\n{snail2}\n{snail3}')
    #    
    #    if len(snail1) > 10:
    #      print('snail1 wins!!!')
    #      winner = '1'
    #      break
    #    elif len(snail2) > 10:
    #      print('snail2 wins!!!')
    #      winner = '2'
    #      break
    #    elif len(snail3) > 10:
    #      print('snail3 wins!!!')
    #      winner = '3'
    #      break
    #  if guess == winner:
    #    return 'win'
    #  else:
    #    return 'lose'
    #snailrace()

    #snail1 = ['a','e']
    #snail2 = ['i','o']
    #snail3 = ['u', 'y']
    #
    #print(''.join(snail1))

#from curses import wrapper
#
#def main(stdscr):
#    # Clear screen
#    stdscr.clear()
#
#    # This raises ZeroDivisionError when i == 10.
#    for i in range(0, 11):
#        v = i-20
#        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
#
#    stdscr.refresh()
#    stdscr.getkey()
#
#wrapper(main)

import random
def blackjack():
    deck = build_deck()
    dealer_score = 0
    current_score = 0
    dealer_hand, deck, dealer_score = draw_hand(deck, 2, dealer_score)
    player_hand, deck, current_score = draw_hand(deck, 2, current_score)
    print(current_score)
  
    while current_score < 21:
        draw_q = input('draw a card? (y/n): ')
        if draw_q == 'y':
            player_hand, deck, current_score = draw_card(player_hand, deck, current_score)
        
        else:
            break
        
    if current_score > 21:
        print('lose')
    else:
        print('win')

#processing

def draw_card(player_hand, deck, current_score):
    total_score = current_score
    for draw in range(int(1)):
        selected_card = (random.choice(deck))
        total_score += getvalue(selected_card)
        print('You drew %s.' % (selected_card[0]))
        print(total_score)
        player_hand.append(selected_card)
        deck.remove(selected_card)
    return player_hand, deck, total_score
    
def draw_card_dealer(dealer_hand, deck, current_score):
    total_score = current_score
    for draw in range(int(1)):
        selected_card = (random.choice(deck))
        total_score += getvalue(selected_card)
        print('Dealer drew %s.' % (selected_card[0]))
        print(total_score)
        dealer_hand.append(selected_card)
        deck.remove(selected_card)
    return dealer_hand, deck, total_score
    

def draw_hand(deck, hand_size, current_score):
    
  # The player receives a card into their hand while the same card is removed from the deck.
    player_hand = []
    for draw in range(int(hand_size)):
        selected_card = (random.choice(deck))
        current_score += getvalue(selected_card)
        print('You drew %s.' % (selected_card[0]))
        player_hand.append(selected_card)
        deck.remove(selected_card)
    return player_hand, deck, current_score

def draw_dealer_hand(deck, hand_size, dealer_score):
    
  # The player receives a card into their hand while the same card is removed from the deck.
    dealer_hand = []
    for draw in range(int(hand_size)):
        selected_card = (random.choice(deck))
        dealer_score += getvalue(selected_card)
        print('You drew %s.' % (selected_card[0]))
        dealer_hand.append(selected_card)
        deck.remove(selected_card)
    return dealer_hand, deck, dealer_score

def getvalue(Selected_card):
    score = 0
    
    for i in range(14):
        if i == 1:
            if 'Ace' in Selected_card:
                score = 1
        elif i == 11:
            if 'Jack' in Selected_card:
                score = 10
        elif i == 12:
            if 'Queen' in Selected_card:
                score = 10
        elif i == 13:
            if 'King' in Selected_card:
                score = 10
        else:
            if str(i) in Selected_card:
                score = i
    return score
    
            

        

def build_deck():
    deck = []
    value = 0
    face = ''
    for value in range(13):
        value += 1
        suit_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suit_list:
            if value == 1:
                face = 'Ace'
            elif value == 11:
                face = 'Jack'
            elif value == 12:
                face = 'Queen'
            elif value == 13:
                face = 'King'
            else:
                face = str(value)
            name = 'the %s of %s' % (face, suit)
            # The deck is shuffled only once, when the deck is first built.
            random.shuffle(deck)
            deck.append((name, face, suit, value))
    return deck

blackjack()