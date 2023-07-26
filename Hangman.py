'''Hangman Game Implementation'''

import nltk  # Natural Language ToolKit (to download it: 'pip install nltk')
import random
from time import sleep

# Download words from nltk module
nltk.download('words')  # Use this line only once and then delete it

# Store the words in words_list
words_list = nltk.corpus.words.words()

# Greeting:
print('Welcome to the Hangman game !\n')
sleep(0.75)


def main(words_list):
    ''' Round's whole steps '''

    # Ask the user for the maximum number of letters in the secret_word
    while True:
        try:
            maximum = int(input('Enter the maximum number of letters ' +
                                'that the word should have : '))
            if maximum < 3:
                raise ValueError
            break
        except ValueError:
            print('\nEnter a valid number bigger or equal to 3.\n')

    # Ask the user for the minimum number of letters in the secret_word
    while True:
        try:
            minimum = int(input('Enter the minimum number of letters ' +
                                'that the word should have : '))
            if minimum > maximum or minimum < 3:
                raise IndexError
            break
        except ValueError:
            print('\nEnter a valid number.\n')
        except IndexError:
            print('\nThe minmum number cannnot exceed the',
                  f'maximum ({maximum}), or be less than 3.\n')

    # Filter words_list to have only words that fit to the user's choices
    words_list = [word for word in words_list
                  if minimum <= len(word) <= maximum]

    # Pick a random word to guess
    secret_word = random.choice(words_list).upper()

    # Set and Initialize needed elements for the game
    length = len(secret_word)
    if length > 6:
        chances = length + 4
    else:
        chances = length + 3

    attempt = []  # List of 0's (letter not found) and 1's (found)

    already_tried = ''  # String to store the already entered letters

    # Initialize attempt list to 0's
    for i in range(length):
        attempt.append(0)

    # Encouragements Expressions
    bravos = ['Nice', 'Keep Going', 'You get closer', 'Well Done',
              'You\'re the best', 'Bravo']

    # Announce a rule:
    sleep(0.75)
    print('\nYour chances will only decrease if you enter a wrong letter.\n')
    sleep(0.75)

    # The game's main process
    while True:
        sleep(0.75)

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
                # Uppercase letter to ensure compatibility
                letter = letter.upper()

                if letter in already_tried:
                    print('\nYou have already used this letter.',
                          'Try a new one.\n')
                    continue
                already_tried += letter  # Update the already tried letters
                break
            print('\nInvalid Input.\n')

        # Search the letter matches in the word and
        # update the attempt list if any
        for i in range(length):
            if letter == secret_word[i]:
                attempt[i] = 1

        # If all letters are found, congrats and end the game
        if 0 not in attempt:
            sleep(0.75)
            print('\n\t', secret_word, '!\n')
            print('You Won ! Yeaaah !')
            sleep(1)
            break

        # Decrease the remaining chances if the letter
        # is not in the secret_word
        if letter not in secret_word:
            print(f'\nThere is no "{letter.upper()}" in the secret word.\n')
            chances -= 1
        else:
            print('\n{} !\n'.format(random.choice(bravos)))

        # If chances are all consumed, end the game by a loss
        if chances == 0:
            sleep(0.75)
            print('\nSorry... You lost.\n')
            sleep(0.75)
            print('The word was :', secret_word)
            break

    sleep(1)

    # Ask for a new game:
    while True:
        try:
            restart = int(input('Another game?\n' +
                                '\t1: Yes / 0: No\n\t\tChoice: '))
            if restart == 1:
                print()
                sleep(1)
                main(words_list)
                break
            elif restart == 0:
                print('\nSee You Soon for a new Hangman round !')
                break
            else:
                raise ValueError
        except ValueError:
            print('\nInvalid Command\n')


# Run the Game
main(words_list)
