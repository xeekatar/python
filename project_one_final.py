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
##3 Hours
##Help From: Dad

DEBUG = False

def create_blanks(secret_word):
    '''creates blanks '_' for secret word'''
    blanks = len(secret_word)*'_ '
    return blanks
    
def check_guess(guess, secret_word):
    '''checks if the guess is correct, valid, or incorrect'''
    if guess in secret_word:
        return 'Good guess!'
    if guess.isnumeric():
        return 'Really a number?'
    else:
        return 'Bad guess!'

def track_progress(guess, secret_word, progress):
    '''replaced blanks with correct letters is guessed'''
    x = 0
    new_progress = ''
    for i in secret_word:
        if i == guess:
            new_progress += i
            x += 2
        else:
            if progress[x] == '_':
                new_progress += '_ '
                x += 2 
            else:
                new_progress += progress[x]
                x += 1
    progress = new_progress
    return progress

def rem_letters(remaining_letters, guess):
    '''displays remaining letters'''
    remaining_letters = remaining_letters.replace(guess, '')
    return remaining_letters

wrong_guesses = 0
remaining_letters = all_letters # gets the remianing letters ready for the loop
progress = create_blanks(secret_word) # gets the blanks ready for the loop
guess = ''

print()
print()
print()
print(' +--------------------------------------------------------+')
print(' | Welcome to the Politically Correct Word Guessing Game! |')
print(' +--------------------------------------------------------+')
print()
print('   I am thinking of a random word')
print()
print(progress) # prints only blanks



while wrong_guesses < 8: # runs until 8 wrong guesses
    if DEBUG == True:
        print(secret_word)
        print(wrong_guesses)
    print()
    print('Wrong guesses:',wrong_guesses) # prints ammount of incorrect guesses
    remaining_letters = rem_letters(remaining_letters, guess) # prints all the remaining letters
    guess = input('Guess a letter! ' + '(' + remaining_letters + ')' + ' :: ' ) 
    print(check_guess(guess, secret_word)) # checks if the guess is correct or incorrect
    status = check_guess(guess, secret_word)
    if status == 'Bad guess!': # if the guess is wrong it adds one to wrong_guesses
        wrong_guesses += 1   
    progress = track_progress(guess, secret_word, progress) # prints the word with any guessed letters filled in
    print(progress)
    print()
    if progress == secret_word: # win statment
        print('Congradulations you have won the Politically Correct Word Guessing Game!')
        print('You had',wrong_guesses,'wrong guess(es)')
        break
if wrong_guesses == 8: # lose statment
    print('You Lost! The word was',secret_word)
    print('Oh well, better luck next time')

