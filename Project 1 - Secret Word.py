# Secret Word - Helper Code
# (you don't need to understand this helper code)

import random

all_letters = 'abcdefghijklmnopqrstuvwxyz'
WORDLIST_FILENAME = "words.txt"

def load_words():
    """Returns a list of valid words. Words are strings of lowercase letters."""
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist

wordlist = load_words()
print (len(wordlist),"words loaded in a variable called wordlist.")
secret_word = random.choice(wordlist)
print ("A random word has been chosen from wordlist and stored in the string variable secret_word")

# end of helper code. 
# --------------------------------------------------------------------------
##Jimmy Wallace
##9/8/15
##Project One
##Help From: Dad

DEBUG = True

def create_blanks(secret_word):
    '''creates blanks '_' for secret word'''
    blanks = len(secret_word)*'_ '
    return blanks
    
def check_guess(guess, secret_word):
    '''checks if the guess is correct, valid, or incorrect'''
    if guess in secret_word:
        print('Good guess!')
    else:
        print('Bad guess!')

def track_progress(guess, secret_word, progress):
    '''replaced blanks with correct letters is guessed'''
    x = 0
    new_progress = ''
    for i in secret_word:
        if i == guess:
            new_progress += i
        else:
            if progress[x] == '_':
                new_progress += '_ '
            else:
                new_progress += progress[x]
        x += 2
    progress = new_progress
    return progress
    
def rem_letters(all_letters, guess):
    '''displays remaining letters'''
    remaining_letters = remaining_letters.replace(guess, '')
    return remaining_letters

wrong_guesses = 0


print('Welcome to the Politically Correct Word Guessing Game!')
print()
print('I am thinking of a random word')


while wrong_guesses <= 8:
    print(create_blanks(secret_word))
    if DEBUG == True:
        print(secret_word)
    #print('Unused letters:',rem_letters(all_letters, guess))
    guess = input('Guess a letter! : ')
    print(check_guess(guess, secret_word))
    print(track_progress(guess, secret_word, progress))
