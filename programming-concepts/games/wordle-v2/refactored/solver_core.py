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
