

#set count to 0, so that it exists.
count = 0


# the loop rewperesents your game running, each pass through is one "tick" (like fps yk)
looping = True
while looping:
    
    #this just rewperesents you click ing on the charachter
    a = input('go')
    
    #converation 1 happens, the character says stuff, count increses
    if count == 0:
        print("coveration 1")
        count = 1
    
    #since the count incresed, the character now says something different
    if count == 1:
        print("coveration 2")
        count = 2

    #and finally they talk a third time and the charachter resets the count so you can have the first converation again
    if count == 2:
        print("coveration 3")
        count = 0


