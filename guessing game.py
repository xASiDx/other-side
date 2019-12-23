import random
'''Guessing game

Allows user to set a range, initializes a random number in that range and lets user to guess it'''

def guess_random(max_val):
    '''Guess a number

    Allows to play to Guess a Number from 1 to max_val'''
    #initializing a random number
    x = random.randint(1, max_val)
    guess_count = 0
    flag = True
    while flag:
        #player makes a guess
        our_guess = int(input_validation("Enter a number from 1 to {} ".format(max_val), high_limit=max_val))
        #player won the game
        if our_guess == x:
            flag = False
            print("Yep, that's it!")
        #the guess is too high
        elif our_guess > x:
            print("Nope, too high. Try again.")            
        #the guess is too low
        else:
            print("Nope, too low. Try again.")
        guess_count += 1
    #the game is over
    else:
        print("The guessing game is over. You guessed in {} attempts".format(guess_count))
        
def input_validation(message, low_limit=1, high_limit=65536):
    '''User input validation
    
    The function checks if user input meets set requirements'''
    user_input = 0
    #we ask user to enter an integer number between low_limit and high_limit
    #until he enters correctly
    while True:
        user_input = input(message)
        if user_input.isdecimal() and (int(user_input) in range(low_limit,high_limit+1)):
            return user_input
        else:
            print("Incorrect input!")
        
keep_playing = True
#check if the player wants to play the game one more time
while keep_playing:
    #the game begins
    print("Let's play a guessing game\n")
    #the player enters upper limit 
    choose_your_destiny = int(input_validation\
    ("Set difficulty - enter the highest possible number (from 1 to whatever) "))
    #guessing happens
    guess_random(choose_your_destiny)
    while True:
        #we ask if the player wants to play one more time
        choise = input("Play again? y/n\n").casefold()
        #and change the variable accordingly, if he doesn't
        if choise == "n":
            keep_playing = False
            break
        elif choise == "y":
            print("All right, all right!")
            break
        else:
            print("Incorrect input!")