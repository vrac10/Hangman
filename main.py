import random
from english_words import english_words_lower_alpha_set

lives = 6.1


def hangmanUpdate(lives_left, bool):
    hangman = \
        [r'''
                  -----------
                  |         |
                  |         |
                  |         O
                  |         |
                  |       / | \
                  |      /  |  \
                  |        / \
                  |       /   \
                  |
                  ''',
         r'''
                  -----------
                  |         |
                  |         |
                  |         O
                  |         |
                  |       / | \
                  |      /  |  \
                  |        /
                  |       /
                  |
                  ''',

         r'''
                  -----------
                  |         |
                  |         |
                  |         O
                  |         |
                  |       / | \
                  |      /  |  \
                  |
                  |
                  |
                  ''',
         r'''
                  -----------
                  |         |
                  |         |
                  |         O
                  |         |
                  |       / |
                  |      /  |
                  |
                  |
                  |
                  ''',
         r'''
                  -----------
                  |         |
                  |         |
                  |         O
                  |         |
                  |         |
                  |         |
                  |
                  |
                  |
                  ''',
         r'''
                  -----------
                  |         |
                  |         |
                  |         O
                  |
                  |
                  |
                  |
                  |
                  |
                  ''',
         r'''
                  -----------
                  |
                  |
                  |
                  |
                  |
                  |
                  |
                  |
                  |
                  '''
         ]

    if lives_left == 6.1:
        lives_left = 6
    elif (lives_left > 0 or lives == 6) and bool == True:
        lives_left -= 1
    print(hangman[lives_left])
    return lives_left


def blankUpdater(index, word, letter, currentWord=''):
    blanks = ""
    if index == "none":

        for i in range(len(word)):
            blanks += '_'

    else:
        temp = list(currentWord)
        temp[index] = letter
        blanks = "".join(temp)

    return blanks


def words(lives_1):
    print("Welcome to Hangman the game!")
    print("Lets start!")
    live = hangmanUpdate(lives_1, False)
    word = str(random.choice(list(english_words_lower_alpha_set)))
    word_list = list(word)

    word1 = blankUpdater("none", word_list, 'no', )
    print(word1)

    while live <= 6 and live != 0:
        global letter_entered
        if word_list.count(None) != len(word):
            letter_entered = input("Guess a letter: ")

        if letter_entered in word_list and word_list.count(None) != len(word):
            word1 = blankUpdater(word_list.index(letter_entered), word_list, letter_entered, word1)
            word_list.insert(word_list.index(letter_entered), None)
            word_list.pop(word_list.index(letter_entered))
            hangmanUpdate(live, False)

            print(word1)

        elif word_list.count(None) == len(word):
            print("You've guessed the word correctly")
            checker = input("Would you like to play again?(Y/N) : ")
            if checker == "Y" or checker == 'y':
                words(lives)
                break
            else:
                print("Thank you!")
                break
        else:
            live = hangmanUpdate(live, True)
            print(word1)


    else:
        print("You lose!")
        print("The word was", word, "!")
        checker = input("Would you like to play again?(Y/N) : ")
        if checker == "Y" or checker == 'y':
            words(lives)
        else:
            print("Thank you!")


words(lives)
