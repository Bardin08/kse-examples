import random


def fetch_words(min_letters=0, max_letters=20):
    result = []
    with open("words.txt") as file:
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

    return matched_words if len(matched_words) > 0 else all_words


def match_letters(secret, attempt_word, args):
    pairs = zip(secret, attempt_word)

    positions = args[1]
    known = args[2]
    banned = args[3]

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
            print("Invalid user input length")
            guess = input(f"Enter 5-letter word ({user_attempts}/{ATTEMPTS}): ")

        while guess not in words:
            print("Unknown word")
            guess = input(f"Enter 5-letter word ({user_attempts}/{ATTEMPTS}): ")
    else:
        candidates = get_candidates(args[0], args[1], args[2], args[3])

        guess = random.choice(candidates)
        print(f">>> ({user_attempts}/{ATTEMPTS}) 5-letter word: {guess}")

    return guess


def match_letters(secret, attempt_word, args):
    positions = args[1]
    known = args[2]
    banned = args[3]

    for idx, letter in enumerate(attempt_word):
        if letter == secret[idx]:
            if letter in positions:
                positions[letter].append(idx)
            else:
                positions[letter] = [idx]
        elif letter in secret:
            known.add(letter)
        else:
            banned.add(letter)

    for idx, letter in enumerate(attempt_word):
        if letter == secret[idx]:
            print(GREEN + letter + COLOR_END, end="")
        elif letter in secret:
            print(YELLOW + letter + COLOR_END, end="")
        else:
            print(RED + letter + COLOR_END, end="")

    return positions, known, banned


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
COLOR_END = '\033[0m'

ATTEMPTS = 6
words = list(fetch_words(5, 5))
secret_word = random.choice(words)
user_attempts = 0

print(f"SECRET IS: {secret_word}")

known_positions = {}
known_letters = set()
banned_letters = set()

candidates = words

is_player = input("Do you want to play as the guesser (player)? (y/n): ").lower() == 'y'

while user_attempts < ATTEMPTS:
    user_attempts += 1

    stats = (candidates, known_positions, known_letters, banned_letters)
    user_guess = get_input(is_player, stats)
    if user_guess == secret_word:
        print(f"You won! {GREEN + user_guess + COLOR_END}")
        exit()

    result = match_letters(secret_word, user_guess, stats)

    print()

if user_attempts >= ATTEMPTS:
    print("You lost!")
