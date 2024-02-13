# Game Mechanics:
#   The program selects a random word from a predefined list. ✅
#   The word is displayed as a series of underscores, representing each letter. ✅
#   Players guess one letter at a time. ✅
#   If the guessed letter is in the word, reveal its position(s). ✅
#   If the guess is incorrect, add a part to the hangman drawing. ✅
#   Players continue until they guess the word or the hangman drawing is complete. ✅

import random

words = ['apple', 'house', 'dog', 'cat',
         'book', 'pen', 'sun', 'moon',
         'tree', 'river', 'mountain', 'ocean',
         'coffee', 'friend', 'happy', 'sad',
         'travel', 'music', 'family', 'green']

secret_word: str = random.choice(words)
print(secret_word)

MAX_ATTEMPTS = 8
user_attempts = 0

guesses = ['_' for _ in range(len(secret_word))]

while user_attempts < MAX_ATTEMPTS:
    print(" ".join(guesses))

    while True:
        guess_letter = input(f"Enter single letter ({user_attempts + 1}/{MAX_ATTEMPTS}): ")

        if len(guess_letter) > 1 or 0:
            print("Invalid length")
            continue

        if not guess_letter.isalpha():
            print("Letter required")
            continue

        print(guess_letter)
        break

    if guess_letter in secret_word:
        zipped = list(zip(guess_letter * len(secret_word), secret_word))

        for idx, value in enumerate(zipped):
            if value[0] == value[1]:
                guesses[idx] = guess_letter
    else:
        print("Letter not appears in the secret word")
        user_attempts += 1
        continue

    if not guesses.__contains__('_'):
        print("You won!")
        break

if user_attempts == MAX_ATTEMPTS:
    print("You Lose!")
