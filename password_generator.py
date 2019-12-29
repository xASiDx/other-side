'''Password generator

Generates a random password of the set length'''

import random
import string
#using my 'input_validation' module
import input_validation

def symb_generator():
    '''Symbol generator

    Generates a random printable symbol, excluding  \t\n\r\x0b\x0c'''
    return string.printable[random.randint(0,len(string.printable)-7)]

def pwd_generator(pwd_length):
    '''Password generator

    Generates a string of random printable symbols of the defined length'''
    pwd = ''
    for i in range(pwd_length):
        pwd += symb_generator()
    return pwd

def pwd_check(pwd, min_length=8, upper_case_symb=1, lower_case_symb=1, number=1):
    '''Password checker

    Checks if a password meets certain requirments'''
    #initialize counters
    upper_case_symb_cnt = 0
    lower_case_symb_cnt = 0
    num_cnt = 0
    #checking if current symbol in password...
    for symb in pwd:
        #is an upper case symbol
        if symb in string.ascii_uppercase:
            #then increment corresponding counter
            upper_case_symb_cnt += 1
        #is a lower case symbol
        elif symb in string.ascii_lowercase:
            #then increment corresponding counter
            lower_case_symb_cnt += 1
        #is a number
        elif symb in string.digits:
            #then increment corresponding counter
            num_cnt += 1
    #if counter are not lower than required
    if (len(pwd) >= min_length) and (upper_case_symb_cnt >= upper_case_symb) and (lower_case_symb_cnt >= lower_case_symb) \
and (num_cnt >= number):
        #then return True
        return True
    else:
        #else return False
        return False

#we ask user to set password length (cannot be lower than 3)
required_length = input_validation.int_input_validation("Input password length (should be longer than 3) - ", 3)
#initialize iteration counter
count = 0
while True:
    #we generate user defined length passwords...
    my_pass = pwd_generator(required_length)
    #and count iterations...
    count += 1
    #until the password meets requirments
    if pwd_check(my_pass,required_length):
        break
print("Password: {}".format(my_pass))
print("Generated in {} iterations".format(count))