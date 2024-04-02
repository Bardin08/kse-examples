# Console colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
COLOR_END = '\033[0m'

# Players have six attempts to guess the correct word
ATTEMPTS = 6


def fetch_words(min_letters=0, max_letters=20):
    result = []
    file = open("words.txt")
    for word in file.read().split('\n'):
        if min_letters <= len(word) <= max_letters:
            result.append(word)
    return result
