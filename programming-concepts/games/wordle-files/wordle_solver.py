# The program selects a random 5-letter word from a predefined list of words.
import random
from datetime import datetime

from utils import (save_stats, fetch_words)


def get_metadata(*args):
    return {
        'known_positions': args[0],
        'known_letters': list(args[1]),
        'banned_letters': list(args[2]),
        'candidates': {**args[3]}
    }


def get_candidates(all_words, known_positions, known, banned) -> list[str]:
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

        for letter, letter_indexes in known_positions.items():
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


def game_iteration(words_list) -> bool:
    guesses = []

    known_positions = {}
    known_letters = set()
    banned_letters = set()

    user_attempts = 0
    candidates = words_list
    candidates_status = {}
    secret_word = random.choice(words_list)

    print(f"SECRET IS: {secret_word}")

    while user_attempts < ATTEMPTS:
        user_attempts += 1

        candidates = get_candidates(candidates, known_positions, known_letters, banned_letters)
        candidates_status[user_attempts] = candidates

        user_guess = random.choice(candidates)
        print(f">>> ({user_attempts}/{ATTEMPTS}) 5-letter word: {user_guess}")

        guesses.append(user_guess)

        if user_guess == secret_word:
            print(f"You won! {GREEN + user_guess + COLOR_END}")
            metadata = get_metadata(
                known_positions,
                known_letters,
                banned_letters,
                candidates_status)

            save_stats(
                metadata,
                date=str(datetime.utcnow()),
                target_word=secret_word,
                guesses=guesses,
                attempts=user_attempts,
                outcome="win",
            )
            return True

        pairs = zip(secret_word, user_guess)

        # After each guess, the program provides feedback:
        #     Green for letters that are correct and in the right position.
        #     Yellow for letters that are in the word but in the wrong position.
        #     Gray for letters not in the word.
        for idx, p in enumerate(pairs):
            if p[0] == p[1]:
                if known_positions.__contains__(p[1]):
                    known_positions[p[1]].append(idx)
                else:
                    known_positions[p[1]] = [idx]

                print(GREEN + p[1] + COLOR_END, end="")
            elif p[1] in secret_word:
                known_letters.add(p[1])
                print(YELLOW + p[1] + COLOR_END, end="")
            else:
                banned_letters.add(p[1])
                print(p[1], end="")

        print()

    metadata = get_metadata(known_positions, known_letters, banned_letters, candidates_status)
    save_stats(
        metadata,
        date=str(datetime.utcnow()),
        target_word=secret_word,
        guesses=guesses,
        attempts=user_attempts,
        outcome="lose"
    )
    return False


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
COLOR_END = '\033[0m'

# Players have six attempts to guess the correct word.
ATTEMPTS = 6

words = list(fetch_words(5, 5))

# ---
GAMES_AMOUNT = 1000
games = 0
wins = 0

while games < GAMES_AMOUNT:
    games += 1
    isWin = game_iteration(words)
    if isWin:
        wins += 1

print(f"Games: {games} ({wins}). Win-rate: {wins / games * 100}%")
