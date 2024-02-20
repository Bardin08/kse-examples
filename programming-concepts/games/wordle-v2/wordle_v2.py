import random


def fetch_words(min_letters=0, max_letters=20):
    result = []
    file = open("words.txt")
    for word in file.read().split('\n'):
        if min_letters <= len(word) <= max_letters:
            result.append(word)
    return result


def get_candidates(all_words, positions, known, banned) -> list[str]:
    matched_words = []

    for candidate in all_words:
        is_matched = True
        for letter in banned:
            if letter in candidate:
                is_matched = False
                break

        if is_matched:
            matched_words.append(candidate)

    for candidate in matched_words:
        for letter in known:
            if letter not in candidate:
                matched_words.remove(candidate)
                break

    for candidate in matched_words:
        is_matched = True

        for letter, letter_indexes in positions.items():
            if letter not in candidate:
                is_matched = False
                break

            for index in letter_indexes:
                if candidate[index] != letter:
                    is_matched = False
                    break

            if not is_matched:
                break

        if not is_matched:
            matched_words.remove(candidate)

    print(matched_words)

    return matched_words if len(matched_words) > 0 else all_words


def match_letters(secret, attempt_word, args):
    pairs = zip(secret, attempt_word)

    positions = args[1]
    known = args[2]
    banned = args[3]

    # After each guess, the program provides feedback:
    #     Green for letters that are correct and in the right position.
    #     Yellow for letters that are in the word but in the wrong position.
    #     Gray for letters not in the word.
    for idx, p in enumerate(pairs):
        if p[0] == p[1]:
            if positions.__contains__(p[1]):
                positions[p[1]].append(idx)
            else:
                positions[p[1]] = [idx]

            print(GREEN + p[1] + COLOR_END, end="")
        elif p[1] in secret_word:
            known.add(p[1])
            print(YELLOW + p[1] + COLOR_END, end="")
        else:
            banned.add(p[1])
            print(p[1], end="")

    return positions, known, banned


def get_input(is_player: bool, args) -> str:
    if is_player:
        guess = input(f"Enter 5-letter word ({user_attempts}/{ATTEMPTS}): ")

        while len(guess) != 5:
            print(RED + "Invalid user input length" + COLOR_END)
            guess = input(f"Enter 5-letter word ({user_attempts}/{ATTEMPTS}): ")

        while guess not in words:
            print("Unknown word")
            guess = input(f"Enter 5-letter word ({user_attempts}/{ATTEMPTS}): ")
    else:
        candidates = get_candidates(args[0], args[1], args[2], args[3])

        guess = random.choice(candidates)
        print(f">>> ({user_attempts}/{ATTEMPTS}) 5-letter word: {guess}")

    return guess


# Players have six attempts to guess the correct word.
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
COLOR_END = '\033[0m'

ATTEMPTS = 6

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
    user_guess = get_input(is_player, stats)
    if user_guess == secret_word:
        print(f"You won! {GREEN + user_guess + COLOR_END}")
        exit()

    result = match_letters(secret_word, user_guess, stats)

    print()

if user_attempts > ATTEMPTS:
    print("You lost!")
