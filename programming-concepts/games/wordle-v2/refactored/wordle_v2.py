from wordle_core import *

words = list(fetch_words(5, 5))
secret_word = random.choice(list(words))
user_attempts = 0

# Implement game mode selection
is_player = False

# Each guess must be a valid 5-letter word.

print(f"SECRET IS: {secret_word}")

known_positions = {}
known_letters = set()
banned_letters = set()

candidates = words

# ---

while user_attempts < ATTEMPTS:
    user_attempts += 1

    stats = (candidates, known_positions, known_letters, banned_letters)
    user_guess = get_input(words, user_attempts, is_player, stats)
    if user_guess == secret_word:
        print(f"You won! {GREEN + user_guess + COLOR_END}")
        exit()

    result = match_letters(secret_word, user_guess, stats)

    print()

if user_attempts > ATTEMPTS:
    print("You lost!")
