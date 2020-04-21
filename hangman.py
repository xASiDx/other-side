"""Hangman"""

import random
import os

def words_from_file(file_path, file_name):
    """Get words from a file"""
    full_path = os.path.join(file_path, file_name)
    result = {}
    with open(full_path, "r", encoding="utf-8") as read_file:
        for line in read_file:
            result[line[:line.find(":")]] = list(set(line[line.find(":")+1:].\
                replace(" ", "").replace("\n", "").split(",")))
    return result

def random_word(words):
    """Get a random word"""
    category = random.choice(list(words.keys()))
    word = random.choice(words[category])
    return category, word

def propose_letter():
    """Get a letter from the player"""
    letter = input("\nВведите букву: ")
    return letter.lower()

def print_word(word, guessed_letters=None, show_word=False):
    """Print guessed letters of the word"""
    output = []
    for letter in word:
        if show_word or (guessed_letters and (letter in guessed_letters)):
            output.append(letter)
        else:
            output.append("_")
    print("\n" + " ".join(output))
    if guessed_letters:
        print(guessed_letters)
    if not show_word:
        return check_if_guessed("".join(output))

def check_letter(word, letter):
    """Check if a letter is in the word"""
    if letter in word:
        print("\nIt's in")
        return 0
    else:
        print("\nIt's NOT in")
        return 1

def check_if_guessed(word):
    """Check if whole word has been guessed already"""
    if word.find("_") < 0:
        print("\nУра!")
        return True

def check_error_counter(error_counter, max_error_number, word):
    """Check if max error count is reached"""
    print("\n{} попыток осталось".format(max_error_number - error_counter))
    if error_counter == max_error_number:
        print("\nКранты, чувак! Это же")
        print_word(word, show_word=True)
        return True

def guessing(word, max_error_number):
    guessed_letters = []
    error_counter = 0
    while True:
        """Need to check validity of user input"""
        guessed_letters.insert(0, propose_letter())
        error_counter += check_letter(word, guessed_letters[0])
        """Need to separate checking if the word has been guessed and
        printing the word
        """
        if print_word(word, guessed_letters):
            break
        if check_error_counter(error_counter, max_error_number, word):
            break


#file_path = os.getcwd()
file_path = ""
file_name = "hangman_words_rus.txt"
words = words_from_file(file_path, file_name)
max_error_number = 6
while True:
    category, word = random_word(words)
    print('\n\n\nУгадайте слово из категории "{}"'.format(category))
    print_word(word)
    guessing(word, max_error_number)
    if input("\nPress 'Enter' to continue, type 'не' to exit: ") == "не":
        break
