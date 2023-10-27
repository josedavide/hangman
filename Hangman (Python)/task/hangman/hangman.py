import random
import string

CHOICES = 8
PLAY = "play"
RESULTS = "results"
EXIT = "exit"
ACTIONS = (PLAY, RESULTS, EXIT)
def get_letter_indexes_in_word(word, letters):
    word_indexes = set()

    for letter in letters:
        for index, character in enumerate(word):
            if character == letter:
                word_indexes.add(index)

    return word_indexes


def show_word_characters(word, word_indexes):
    word_to_show = ""
    for index, character in enumerate(word):
        word_to_show += character if index in word_indexes else "-"

    return word_to_show


def request_user_input(suggested_word):
    print()
    print(suggested_word)
    user_input = input("Input a letter: ")
    if len(user_input) != 1:
        print("Please, input a single letter.")
        return request_user_input(suggested_word)
    elif user_input not in string.ascii_lowercase:
        print("Please, enter a lowercase letter from the English alphabet.")
        return request_user_input(suggested_word)

    return user_input


def play():
    words = ("python", "java", "swift", "javascript")
    solution = random.choice(words)
    user_letters = set()

    word_indexes = get_letter_indexes_in_word(solution, user_letters)

    attempts = CHOICES
    word_found = False
    while attempts > 0 and not word_found:
        suggested_word = show_word_characters(solution, word_indexes)
        user_input = request_user_input(suggested_word)

        repeated_input = user_input in user_letters
        user_letters.update(set(user_input))
        word_indexes = get_letter_indexes_in_word(solution, user_letters)
        suggested_word = show_word_characters(solution, word_indexes)

        if suggested_word in words:
            word_found = True
        elif repeated_input:
            print("You've already guessed this letter.")
        elif user_input not in solution:
            attempts -= 1
            print(f"That letter doesn't appear in the word.  # {attempts} ")

    if word_found:
        suggested_word = show_word_characters(solution, word_indexes)
        print(f"You guessed the word {suggested_word}!")
        print("You survived!")
        return 1
    else:
        print("You lost!")
        return 0

def show_menu():
    res = input(f'Type "{PLAY}" to play the game, "{RESULTS}" to show the scoreboard, and "{EXIT}" to quit:')
    if res not in ACTIONS:
        return show_menu()
    else:
        return res


print("H A N G M A N  # 8 attempts")

played = 0
won = 0
lost = played - won
to_exit = False

while not to_exit:
    action = show_menu()
    if action == PLAY:
        played += 1
        won += play()
    elif action == RESULTS:
        print(f"You won: {won} times.")
        print(f"You lost: {played - won} times.")
    elif action == EXIT:
        to_exit = True
