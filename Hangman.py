'''Hangman Game Implementation'''

import nltk # Natural Language ToolKit (to download it: 'pip install nltk')
import random
from time import sleep

# Download words from nltk module and 
# nltk.download('words') (Use this line only once and then delete it)

# Store the words in words_list
words_list = nltk.corpus.words.words()

# Greeting:
print('Welcome to this hard Hangman game !\n')
sleep(0.5)

#Ask the user for the maximum number of letters in the secret_word
while True:
    try:
        print('Enter the maximum number of letters the word would have : ',\
                end='')
        maximum = int(input(''))
        if maximum < 3:
            raise ValueError
        break
    except ValueError:
        print('\nEnter a valid number bigger or equal to 3.\n')
#Ask the user for the minimum number of letters in the secret_word
while True:
    try:
        print('Enter the minimum number of letters the word would have : ',\
                end='')
        minimum = int(input(''))
        if minimum > maximum or minimum < 3:
            raise IndexError
        break
    except ValueError:
        print('\nEnter a valid number.\n')
    except IndexError:
        print(f'\nThe minmum number cannot exceed the maximum ({maximum}),',\
                'or be less than 3.\n')

# Filter words_list to have only words that fit to the user's choices
words_list = [word for word in words_list if minimum <= len(word) <= maximum]

# Pick a random word to guess
secret_word = random.choice(words_list).upper()

# Set and Initialize needed elements for the game
length = len(secret_word)
if length > 6:
    chances = length + 4
else:
    chances = length + 3

attempt = [] # List of 0's (letter not found) and 1's (found)\
        # following the secret_word indexes

already_tried = '' # String to store the already entered letters

# Initialize attempt list to 0's
for i in range(length):
    attempt.append(0)

# Encouragements Expressions
bravos = ['Nice', 'Keep Going', 'You get closer', 'Well Done',\
        'You\'re the best', 'Bravo']

# Announce a rule:
sleep(0.5)
print('\nYour chances will only decrease if you enter a wrong letter.\n')
sleep(0.5)
# The game's process
while True:
    sleep(0.5)

    # Print the number of the remaining chances
    print('You have', end=' ')
    if chances > 1:
        print(chances, 'chances', end=' ')
    else:
        print('only one chance', end=' ')
    print('left to guess the word.\n')

    # Print the current progression
    for i in range(length):
        if attempt[i] == 0:
            print('-', end='')
        else:
            print(secret_word[i], end='')
    print('\n')

    # Prompt the user for a new valid letter
    while True:
        letter = input('Enter a letter: ')
        if letter.isalpha() and len(letter) == 1:
            letter = letter.upper() # Uppercase letter to ensure compatibility
            if letter in already_tried:
                print('\nYou have already used this letter. Try a new one.\n')
                continue
            already_tried += letter # Update the already tried letters
            break
        print('\nInvalid Input.\n')

    # Search the letter matches in the word and update the attempt list if any
    for i in range(length):
        if letter == secret_word[i]:
            attempt[i] = 1

    # If all letters are found, congrats and end the game
    if 0 not in attempt:
        sleep(0.5)
        print('\n\t', secret_word, '!\n')
        print('You Won ! Yeaaah !')
        sleep(1)
        break

    # Decrease the remaining chances if the letter is not in the secret_word
    if letter not in secret_word:
        print(f'\nThere is no "{letter.upper()}" in the secret word.\n')
        chances -= 1
    else:
        print('\n{} !\n'.format(random.choice(bravos)))

    # If chances are all consumed, end the game by a loss
    if chances == 0:
        sleep(0.5)
        print('\nSorry... You lost.\n')
        sleep(0.5)
        print('The word was :', secret_word)
        break
