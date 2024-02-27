import csv
import datetime
import json


def json_to_csv_raw():
    try:
        with open("logs.json", "r") as json_file:
            with open("logs.csv", "a") as csv_file:
                log_json = json_file.readline()
                log = json.loads(log_json)

                writer = csv.DictWriter(csv_file, fieldnames=log.keys(), delimiter='\t')
                writer.writeheader()

                json_file.seek(0)
                for line in json_file.readlines():
                    if line == '\n':
                        continue

                    log = json.loads(line)
                    writer.writerow(log)

    except FileNotFoundError:
        print("JSON file not exists")


def get_log_object(record):
    return {
        'date': datetime.datetime.strptime(record['date'], "%Y-%m-%d %H:%M:%S.%f"),
        'target_word': record['target_word'],
        'guesses': json.loads(record['guesses'].replace("'", '"')),
        'attempts': int(record['attempts']),
        'outcome': record['outcome'],
        'metadata': eval(record['metadata'])  # Using eval as it's a complex nested dict; be cautious with eval!
    }


def map_to_normalized_log(old_log):
    log = {**old_log}
    metadata = log["metadata"]
    del log["metadata"]

    for k, v in metadata.items():
        if k == 'candidates':
            for ck, cv in v.items():
                log["metadata_" + "candidates_" + str(ck)] = cv

            continue

        log["metadata_" + str(k)] = v

    return log


def clean_csv_1():
    try:
        with open("logs.csv", "r") as raw_file:
            with open("logs_cleared.csv", "w") as cleaned_file:
                keys = ["date", "target_word", "guesses", "attempts", "outcome", "metadata"]
                reader = csv.DictReader(raw_file, fieldnames=keys, delimiter='\t')

                keys_new = ["date",
                            "target_word",
                            "guesses",
                            "attempts",
                            "outcome",
                            "metadata_known_positions",
                            "metadata_known_letters",
                            "metadata_banned_letters",
                            "metadata_candidates_1",
                            "metadata_candidates_2",
                            "metadata_candidates_3",
                            "metadata_candidates_4",
                            "metadata_candidates_5",
                            "metadata_candidates_6"
                            ]
                writer = csv.DictWriter(cleaned_file, fieldnames=keys_new, delimiter='\t')
                writer.writeheader()

                for idx, line in enumerate(reader):
                    if idx == 0:
                        continue

                    log = get_log_object(line)
                    normalized_log = map_to_normalized_log(log)
                    writer.writerow(normalized_log)

    except FileNotFoundError:
        print("JSON file not exists")


clean_csv_1()
