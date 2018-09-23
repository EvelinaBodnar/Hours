# Problem Set 2, hangman.py
# Name:Evelina Bodnar
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import re

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    if (re.match(r"^[a-z]{1,10}$", secret_word)):
        return secret_word
    else:
        return False

    setsecret_word = set(secret_word)
    setletters_guessed = set(letters_guessed)

    if setsecret_word == setletters_guessed:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    letters_guessed = ""
    for i in secret_word:
        if i in letters_guessed:
            letters_guessed += i
        else:
            letters_guessed += " _ "

    return letters_guessed


def get_available_letters(letters_guessed):
    all_letters = set('abcdefghijklmnopqrstuvwxyz')
    letters_guessed = list(all_letters - set(letters_guessed))
    sorted(letters_guessed)
    return letters_guessed


def hangman(secret_word):
    all_letters = set('abcdefghijklmnopqrstuvwxyz')
    guesses = 6
    warning = 3

    letters_guessed = []
    print('Guess word that have', len(secret_word), 'letters')
    print('_ ' * len(secret_word))

    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print('You have', guesses, 'guesses')
        print('You have', warning, 'warning')
        print('Avaliable latters ', get_available_letters(letters_guessed))
        letter = input('Try to guess letter ')
        if len(letter) != 1:
            if warning > 0:
                warning -= 1

            if warning == 0:
                guesses -= 1
            print('Please,write something another')
        if letter in letters_guessed:
            warning -= 1
            print('You have written this letter')

        if letter in secret_word:
            print('Yes,we have this letter')
            letters_guessed.append(letter)

        if letter == "*" and with_hints:
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        if not letter in all_letters and warning > 0:
            warning -= 1
            print("Try another. You have ", warning, "warnings left")

    else:
        print("Sorry , but no")
        if letter in set(["a", "e", "i", "o", "u"]):
            guesses -= 2
        letters_guessed.append(letter)
        guesses -= 1
    print("________________________")

    if (guesses == 0):
        print(secret_word)
        print("You lose !")
    else:
        print(secret_word)
        print("Congratulaion , you have :", str(guesses * len(set(secret_word))), " scores")

    pass


def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")
    letters_set = set(my_word)
    if len(other_word) != len(my_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] != other_word[i] and my_word[i] != "_" and my_word[i] == '_' and other_word[i] != '_' and \
                other_word[i] in letters_set:
            return False

    return True


def show_possible_matches(my_word):
    result = "Posible words are: "
    for i in wordlist:
        if match_with_gaps(my_word, i):
            result += i + " "
    if len(result) == len("Posible words : "):
        return "No matches found"
    return result


def hangman_with_hints(secret_word):
    global with_hints
    WithHints = True
    print("Game with hints")
    hangman(secret_word)
    pass


WithHints = False
if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
    letters_tried = []
    hint = input('To run game without hints print 1. To run game with hints print 2. ')

    if hint == '1':
        hangman(secret_word)

    if hint == '2':
        hangman_with_hints(secret_word)