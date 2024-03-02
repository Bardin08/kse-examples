import csv


# [1, 2, [3, [4, [5]]]] -> [1, 2, 3, 4, 5]
def flat(input_list):
    def flat_internal(flatten_list, elem):
        if not (isinstance(elem, list) or isinstance(elem, tuple)):
            flatten_list.append(elem)
            return

        for it in elem:
            if not (isinstance(it, list) or isinstance(it, tuple)):
                flatten_list.append(it)
            else:
                flat_internal(flatten_list, it)

    res = []

    for i in input_list:
        flat_internal(res, i)

    return res


def get_records(filtering=lambda x: True, cols=()):
    rows = []
    with open("spotify.csv", mode="r", encoding="utf8") as file:
        reader = csv.reader(file)

        for idx, line in enumerate(reader):
            if idx != 0 and filtering(line):
                row = []
                for col in cols:
                    row.append(line[col])
                row = tuple(row)
                rows.append(row)

        file.close()

    return rows


def clear_name(token):
    return token.replace('(', '').replace(')', '').replace('&', '').replace('-', '')


def is_word(token):
    try:
        if token == '' or int(token):
            return False
    except ValueError:
        return True


TRACK_NAME_INDEX = 1
IS_TRACK_EXPLICIT_INDEX = 2
TRACK_RELEASE_YEAR_INDEX = 3
GENRE_INDEX = 4

# Explicit songs: Find amount of explicit songs
explicit_songs = get_records(lambda x: x[IS_TRACK_EXPLICIT_INDEX] == 'True', (TRACK_NAME_INDEX,))
print("1. Explicit songs amount: " + str(len(explicit_songs)))

# The most popular year: Find the year when the most songs were released
years_distribution = {}
release_years = get_records(lambda x: x[TRACK_RELEASE_YEAR_INDEX] != ' ' or None, (TRACK_RELEASE_YEAR_INDEX,))
for release_date in release_years:
    year = str(release_date[0][0:4])
    years_distribution[year] = years_distribution[year] + 1 if years_distribution.__contains__(year) else 1

ordered_years = sorted(years_distribution.items(), key=lambda x: x[1], reverse=True)
top_year, songs_released = ordered_years[0]

print(f"2. The most popular year was {top_year}. {songs_released} songs were released!")

# The most popular word in songs names: Find the most popular word in songs names
selected_records = get_records(cols=(TRACK_NAME_INDEX,))
names = [rec[0] for rec in selected_records]

words = flat([clear_name(name).split(' ') for name in names])
words = list(filter(lambda x: is_word(x), words))

words_distribution = {}
for word in words:
    words_distribution[word] = words_distribution[word] + 1 if words_distribution.__contains__(word) else 1

ordered_words = sorted(words_distribution.items(), key=lambda x: x[1], reverse=True)
_, words_number = ordered_words[0]

print("3. Most popular words in names:")
current = -1
for w in ordered_words:
    current_word, words_amount = w
    if words_amount < words_number:
        break
    print(f"\t- {current_word}: {words_amount}")

# Top Three Genres: Identify the three genres that occur most frequently in the dataset.
selected_records = flat(get_records(cols=(GENRE_INDEX,)))
genres = [item for sublist in [eval(lst) for lst in selected_records] for item in sublist]

genres_distribution = {}
for g in genres:
    genres_distribution[g] = genres_distribution[g] + 1 if genres_distribution.__contains__(g) else 1

ordered_genres = sorted(genres_distribution.items(), key=lambda x: x[1], reverse=True)

print("4. Three most popular genres:")
for g in ordered_genres[:3]:
    genre, amount = g
    print(f"\t- {genre}: {amount}")
