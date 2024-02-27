import json
import os


def save_stats(metadata: dict, **kwargs):
    # print(kwargs)  # **kwargs -> keyword arguments, *args -> arguments

    log = {**kwargs, 'metadata': metadata}
    try:
        with open("logs.json", mode="a") as file:
            log_str = json.dumps(log)
            file.write(log_str + os.linesep)
    except IOError:
        print("Something went wrong")


def fetch_words(min_letters=0, max_letters=20):
    result = []
    file = open("words.txt")
    for word in file.read().split('\n'):
        if min_letters <= len(word) <= max_letters:
            result.append(word)
    return result
