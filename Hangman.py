import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    # while ' ' or '-' in word:
    word = random.choice(words)
    return word.upper()


def hangman():
    print("testing")
    word = get_valid_word(words)
    word_letters = set(word)    # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letter = set()          # keeps a track of what the users have guessed

    lives = 6

    # getting a input
    while len(word_letters) > 0 and lives > 0:
        # letter used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letter))

        word_list = [letter if letter in used_letter else '-' for letter in word ]
        print('Current word: ', ' '.join(word_list))

        # what current word is (is W - R D)
        user_letter = input("Guess a letter:").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives-1   # takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letter:
            print("You have already used that character. Please try again ")
        else:
            print("Invalid char , please try again")

    # gets here when len(word_letters) == 0 or when lives ==0
    if lives == 0:
        print('You died , your lives are over', word)
    else:
        print('You guessed the word', word, '!!')


hangman()