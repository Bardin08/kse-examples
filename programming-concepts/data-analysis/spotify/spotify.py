import csv


def get_records(filtering, cols):
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


TRACK_NAME_INDEX = 1
IS_TRACK_EXPLICIT_INDEX = 2

# Explicit songs: Find amount of explicit songs
explicit_songs = get_records(lambda x: x[IS_TRACK_EXPLICIT_INDEX] == 'True', (TRACK_NAME_INDEX,))
print("Explicit songs amount: " + str(len(explicit_songs)))

# The most popular year: Find the year when the most songs were released
TRACK_RELEASE_YEAR_INDEX = 3

release_years_distribution = {}
release_years = get_records(lambda x: x[TRACK_RELEASE_YEAR_INDEX] != ' ' or None, (TRACK_RELEASE_YEAR_INDEX,))
for release_date in release_years:
    year = str(release_date[0][0:4])
    release_years_distribution[year] = release_years_distribution[year] + 1 if release_years_distribution.__contains__(
        year) else 1

ordered_years = sorted(release_years_distribution.items(), key=lambda x: x[1], reverse=True)
top_year, songs_released = ordered_years[0]

print(f"The most popular year was {top_year}. {songs_released} songs were released!")
# The most popular word in songs names: Find the most popular word in songs names
# Top Three Genres: Identify the three genres that occur most frequently in the dataset.
