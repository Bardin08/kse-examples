import random

from utils import *
from solver_core import get_candidates


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
        elif p[1] in secret:
            known.add(p[1])
            print(YELLOW + p[1] + COLOR_END, end="")
        else:
            banned.add(p[1])
            print(p[1], end="")

    return positions, known, banned


def get_input(words: list[str], attempt: int, is_player: bool, args) -> str:
    if is_player:
        guess = input(f"Enter 5-letter word ({attempt}/{ATTEMPTS}): ")

        while len(guess) != 5:
            print(RED + "Invalid user input length" + COLOR_END)
            guess = input(f"Enter 5-letter word ({attempt}/{ATTEMPTS}): ")

        while guess not in words:
            print("Unknown word")
            guess = input(f"Enter 5-letter word ({attempt}/{ATTEMPTS}): ")
    else:
        candidates = get_candidates(args[0], args[1], args[2], args[3])

        guess = random.choice(candidates)
        print(f">>> ({attempt}/{ATTEMPTS}) 5-letter word: {guess}")

    return guess
