import math

def summulti():
    n = float(input('n '))
    r = float(input('r '))
    a = float(input('a '))
    count = 1
    sum = a
    
    while n > count:
        #sand = [a]
        a = a * r
        sum = sum + a
        count = count + 1
        print(f'count: {count}')
        print(f'n: {a}')
        print(f'sum: {sum}')

def sumplus():
    n = float(input('n '))
    r = float(input('r '))
    a = float(input('a '))
    count = 1
    sum = a
    
    while n > count:
        #sand = [a]
        a = a + r
        sum = sum + a
        count = count + 1
        print(f'count: {count}')
        print(f'n: {a}')
        print(f'sum: {sum}')

def sumpat():
    n = float(input('n '))
    x = float(input('(base value add)x '))
    r = float(input('(add to x)r '))
    a = float(input('(start)a '))
    count = 1
    sum = a
    
    while n > count:
        #sand = [a]
        a = a + 2 * (a - 2)
        x = x + r
        sum = sum + a
        count = count + 1
        print(f'count: {count}')
        print(f'n: {a}')
        print(f'sum: {sum}')
        
def main():
    u = input('(m) for sum (multiplication), (a) for sum (addition), (p) for sum (pattern)')
    if u == 'm':
        summulti()
    elif u == 'a':
        sumplus()
    else:
        sumpat()

main()