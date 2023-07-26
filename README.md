# Hangman Game Implementation

This is a simple Hangman game implemented in Python. The game randomly selects a word from a list of words, and the player's task is to guess the word by suggesting letters one by one. The player has a limited number of chances to guess the word correctly.

## Requirements
- Python 3.x (Python 3.6 or higher recommended)
- nltk (Natural Language Toolkit) library. You can install it using `pip install nltk`.

## How to Play
1. Run the Python script and the game will start by asking you to enter the maximum and minimum number of letters that the secret word should have.
2. After entering the valid values for the word length, the game will filter the list of words and randomly select a word for you to guess.
3. You will be informed about the number of chances you have to guess the word.
4. Enter a letter as your guess.
5. If the letter is present in the word, you will receive an encouraging message and the guessed letter's position in the word will be revealed.
6. If the letter is not present in the word, your chances will decrease, and you will be informed accordingly.
7. Continue guessing letters until you either guess the whole word correctly or run out of chances.

## Rules
- The secret word to guess will be represented by dashes, and each dash corresponds to a letter in the word.
- You can only enter one letter at a time as your guess.
- The game will not consider repeated guesses for the same letter.
- The number of chances you have depends on the length of the secret word. Longer words provide more chances.

## Encouragements
Throughout the game, you will receive encouraging messages whenever you guess a correct letter.

## Winning and Losing
- If you correctly guess all the letters in the word before running out of chances, you win the game.
- If you use all the available chances without guessing the word, you lose the game, and the secret word will be revealed.

Have fun playing Hangman! Feel free to modify the code and add new features to enhance the game further. Enjoy!
