##This function was written as an exercise for the SheCodes' Python track.
##The first function works with Python's random library.



def roulette():
	import random as r ##I import the random library.
	##I chose 'import ... as ...' because in Python you have to
	##call the library before you call its specific function.
	##Then, importing random as r makes the whole job easier.
	number = r.randint(0, 37) ##A random integer between 0 and 37 is chosen
	return(number) ##The function returns the number randomly chosen
    ##by the function.




def choose():
	number = roulette() ##It uses the previous function in order to choose
	##a random integer
	chosen = int(input("Choose a number between 0 and 36:\n"))
	##asks for the input of the user
	if chosen > number:
            ##compares the number given by the user to the random number.
            ##The user lost.
		print("You lost! The number you chose is greater than the number the computer chose.")
	elif chosen < number:
            ##The user lost.
		print("You lost. The number you chose is lesser than the number the computer chose.")
	else:
            ##The user wins.
		print("You won! The numbers are equal.")
	return(number)##That line is totally optional.
    ##You can choose not to show the random number.

		
