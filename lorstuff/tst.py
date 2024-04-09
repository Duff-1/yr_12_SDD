import random

def test(p):
    page = open(f'{p}.txt','r')
    
    minimum = 0
    maximum = 0
    count = 0

    dicenum = 1
    
    dicevalues = {}
    
    for line in page:
        if line.strip('\n') == 'eod':
            
            dicevalues[f'dice{dicenum}'] = (minimum, maximum, dicetype)
            
            
            minimum = 0
            maximum = 0
            dicetype = ''
            dicenum = dicenum + 1
            
        else:
            try:
                match count:
                    case 0:
                        minimum = int(line.strip('\n'))
                        count = 1
                    case 1:
                        maximum = int(line.strip('\n'))
                        count = 0

            except:
                dicetype = line.strip('\n')
            
    print(dicevalues)
    print()
    return dicevalues

class dice:
    def __init__(self,min,max,bonus,dicetype):
        
        self.min = min
        self.max = max
        self.bonus = bonus        
        self.dicetype = dicetype
        self.base, self.mod, self.dicetype = self.roll()
        
    def roll(self):
        base = random.randint(self.min, self.max)
        mod = self.bonus + base
        
        return base, mod, self.dicetype

class card:
    def __init__(self,page):
        self.pagedice = test(page)
        self.dicelist= []
        
        self.rollpage()
        
    def rollpage(self):
        for i,b in enumerate(self.pagedice):
            minimum, maximum, dicetype = self.pagedice[b]
            self.dicelist.append(dice(minimum, maximum, checkbonus(dicetype), dicetype))
        count = 0
        for d in self.dicelist:
            tem = d.roll()
            base, maodif, dicetype = tem
            count+=1
            print(f'base: {base}\nmodified: {maodif}\ndicetype: {dicetype}')
            print()

class modifiers:
    def __init__(self,s,blu,p,e,blo):
        self.slash = s
        self.blunt = blu
        self.pierce = p
        self.evade = e
        self.block = blo
mods = modifiers(1,2,3,4,5)

def checkbonus(dtype):
    match dtype:
        case 'slash':
            return mods.slash
        case 'blunt':
            return mods.blunt
        case 'pierce':
            return mods.pierce
        case 'evade':
            return mods.evade
        case 'block':
            return mods.block

def main():
    while True:
        temp = input('page name: ')
        ch = input('change modifiers? (y/n)')
        if ch == 'y':
            slash = int(input('slash'))
            pierce = int(input('pierce'))
            blunt = int(input('blunt'))
            evade = int(input('evade'))
            block = int(input('block'))
            mods = modifiers(slash,blunt,pierce,evade,block)
        else:
            print(f'slash {mods.slash}, blunt {mods.blunt}, pierce {mods.pierce}, evade {mods.evade}, block {mods.block}\n')

        current_card = card(temp)
        current_card.rollpage
        
main()