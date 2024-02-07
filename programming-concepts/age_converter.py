from datetime import datetime

DATE_FORMAT = '%m.%d.%Y'
HOURS_MULTIPLIER = 24
MINUTES_MULTIPLIER = 24 * 60
SECONDS_MULTIPLIER = 24 * 60 * 60

birth_date = input(f"Please, enter your birthdate int the following format {DATE_FORMAT}: ")
date_chunks = list(map(int, birth_date.split('.')))

while ((date_chunks[0] < 0 or date_chunks[0] > 12) or
       (date_chunks[1] < 0 or date_chunks[1] > 31) or
       (date_chunks[2] < 1900 or date_chunks[2] > 2024)):
    print("Invalid date")
    birth_date = input(f"Please, enter your birthdate int the following format {DATE_FORMAT}: ")
    date_chunks = list(map(int, birth_date.split('.')))

age = (datetime.today() - datetime.strptime(birth_date, DATE_FORMAT))

print(f"Your age is: \n"
      f"{age.days} days or\n"
      f"{age.days * HOURS_MULTIPLIER} hours or \n"
      f"{age.days * MINUTES_MULTIPLIER} minutes or \n"
      f"{age.days * SECONDS_MULTIPLIER} seconds")
