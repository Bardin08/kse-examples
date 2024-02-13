# The program selects a random 5-letter word from a predefined list of words.
import random

words = {
    "table", "apple", "grape", "brick", "clock",
    "chair", "plane", "glass", "house", "train",
    "beach", "grass", "sheep", "light", "sound",
    "water", "bread", "sugar", "smile", "world"
}

# Players have six attempts to guess the correct word.
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
COLOR_END = '\033[0m'

ATTEMPTS = 6

secret_word = random.choice(list(words))
user_attempts = 0

# Each guess must be a valid 5-letter word.

print(f"SECRET IS: {secret_word}")

# ---

while user_attempts < ATTEMPTS:
    user_attempts += 1

    user_guess = input(f"Enter 5-letter word ({user_attempts}/{ATTEMPTS}): ")

    while len(user_guess) != 5:
        print(RED + "Invalid user input length" + COLOR_END)
        user_guess = input(f"Enter 5-letter word ({user_attempts}/{ATTEMPTS}): ")

    if user_guess not in words:
        print("Unknown word")
        exit()

    if user_guess == secret_word:
        print(f"You won! {GREEN + user_guess + COLOR_END}")
        exit()

    pairs = zip(secret_word, user_guess)

    # After each guess, the program provides feedback:
    #     Green for letters that are correct and in the right position.
    #     Yellow for letters that are in the word but in the wrong position.
    #     Gray for letters not in the word.
    for p in pairs:
        if p[0] == p[1]:
            print(GREEN + p[1] + COLOR_END, end="")
        elif p[1] in secret_word:
            print(YELLOW + p[1] + COLOR_END, end="")
        else:
            print(p[1], end="")

    print()
