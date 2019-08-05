##This function was written as an exercise for the Python track of SheCodes.
##The function works with the random library
##The function chooses a random integer from zero to 36
##And it stores this number as a variable
##Then it asks the user to choose a number from 0 to 36.
##The function then compares both numbers
##If they are equal, the function returns a message saying the user won.
##If the numbers aren't equal, it returns a message saying the user lost.

def roulette():
    import random as r
    ##random is a python library
    ##here I chose to "rename" it to r
    ##since it will be easier to recall it whenever I needed.
    number = r.randint(0, 37)
    ##the computer chooses a random integer number from 0 to 36
    lucky_number = int(input("Choose a number from 0 to 36: "))
    ##The user enters their chosen number
    if number == lucky_number:
    ##this conditional compares both variabbles
    ##It's important to pay attention to the double equal sign
    ##This is used for comparing two values, variables, etc...
        return("You won!")
    ##If the numbers are equal, the user won and a message appear.
    else:
        return("No! You lost.")
    ##If the numbers are different, the user lost and a correspondent message appears
    
