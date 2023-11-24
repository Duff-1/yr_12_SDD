import time

chars = 'ABCDEFGH'
loop = range(1, len(chars) + 1)

for idx in loop:
    print(chars[:idx], end='\r') # <-- end with carriage return
    time.sleep(.5)