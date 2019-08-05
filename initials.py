##This function was written as an exercise for the Python track of the SheCodes.
##It takes input from the user and stores it in three separate variables.
##It takes in name, first name and year of birth.
##The function calculates the user's age, based on the current year.
##This version lets the user set the current year at the beginning.
##The user's initials are taken from first and last name first letter.

def initials():
    curr_year = int(input("Set current year: "))
    ##The user can set current year
    name = input("Name: ")
    ##user types their last name
    first_name = input("First name: ")
    ##user types their first name
    initials = first_name[0]+name[0]
    ##character composed of the first letter of variable name and first letter
    ##of first name letters and creates a single variable
    yob = int(input("Year of birth: "))
    ##user enters their year of birth
    ##It's important to be an integer for the calculations
    age = int(curr_year-yob)
    ##The age is calculated accordingly
    print("Your initials are ", initials, " and you are ", age, " years old.")
    ##It prints the user's initials and age.
    
