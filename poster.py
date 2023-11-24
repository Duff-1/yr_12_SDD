
def getinputs():
    nholes = int(input('number of holes: '))
    yhole = []
    xhole = []
    for i in range(nholes):
        xhole.append(input('x value of hole'))
        yhole.append(input('y value of hole'))
    print(f'x values: {xhole}')
    print(f"y values: {yhole}")

def processing():
    
    for i in range(nholes):
        if xhole[i] > highestx:
            highestx = xhole[i]
        if xhole[i] < lowestx:
            lowestx = xhole[i]
        if yhole[i] > highesty:
            highesty = yhole[i]
        if yhole[i] < lowesty:
            lowesty = yhole[i]




def main():
    nholes = int(input('number of holes: '))
    yhole = []
    xhole = []
    highestx = 0
    highesty = 0
    lowestx = 10000
    lowesty = 10000
    for i in range(nholes):
        xhole.append(input('x value of hole'))
        yhole.append(input('y value of hole'))
    print(f'x values: {xhole}')
    print(f"y values: {yhole}")
    
    for i in range(nholes):
        if int(xhole[i]) > int(highestx):
            highestx = int(xhole[i])
        if int(xhole[i]) < int(lowestx):
            lowestx = int(xhole[i])
        if int(yhole[i]) > int(highesty):
            highesty = int(yhole[i])
        if int(yhole[i]) < int(lowesty):
            lowesty = int(yhole[i])
    point1 = highestx - lowestx
    point2 = highesty - lowesty
    p = point1 * point2 
    print(p)
    
main()