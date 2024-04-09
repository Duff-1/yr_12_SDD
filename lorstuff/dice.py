import random, tst

class dice:
    def __init__(self,min,max,bonus):
        
        self.min = min
        self.max = max
        self.bonus = bonus        
        
        self.base, self.mod = self.roll()
        
    def roll(self):
        base = random.randint(self.min, self.max)
        mod = self.bonus + base
        print(f'{base}, {mod}')
        
        return base, mod
        

class card:
    def __init__(self):
        self.pagedice = tst.test('page')
        self.dicelist= []
        
        self.rollpage()
        
    def rollpage(self):
        for i,(minimum, maximum, dicetype) in enumerate(self.pagedice):
            self.dicelist.append(dice(minimum, maximum, checkbonus(dicetype)))
        
        for d in self.dicelist:
            tem = d.roll()
            print(tem)
            
def checkbonus(dtype):
    match dtype:
        case 'slash':
            return 1
        case 'blunt':
            return 2
        case 'pierce':
            return 3
        case 'evade':
            return 4
        case 'block':
            return 5
    
def main():
    l = card
    l.rollpage

main()