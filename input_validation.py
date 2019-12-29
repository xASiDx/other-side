'''Input validation module

Contains some functions that validate user input'''

def int_input_validation(message, low_limit=1, high_limit=65536, error_message="Incorrect input!"):
    '''User input validation

The function checks if user input meets set requirements'''
    user_input = 0
    #we ask user to enter an integer number between low_limit and high_limit
    #until he enters correctly
    while True:
        user_input = input(message)
        #if user input meets the requirments...
        if user_input.isdecimal() and (int(user_input) in range(low_limit,high_limit+1)):
            #we return user input
            return int(user_input)
        else:
            #otherwise we print the error message and continue the loop
            print(error_message)