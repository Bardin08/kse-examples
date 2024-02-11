import random

# Configuration
NUM_STUDENTS = 2501

NUM_SUBJECTS = 5
MIN_MARKS_PER_SUBJECT = 150
MAX_MARKS_PER_SUBJECT = 150
DEFAULT_CHUNK_SIZE = 10000


def generate_marks_inserts():
    with open('../scripts/insert_marks.sql', 'w') as file:
        file.write("INSERT INTO marks (student_id, subject_id, mark) VALUES\n\t")

        chunk_size = MIN_MARKS_PER_SUBJECT if DEFAULT_CHUNK_SIZE >= MIN_MARKS_PER_SUBJECT else DEFAULT_CHUNK_SIZE
        for student_id in range(1, NUM_STUDENTS + 1):
            for subject_id in range(1, NUM_SUBJECTS + 1):
                num_marks = random.randint(MIN_MARKS_PER_SUBJECT, MAX_MARKS_PER_SUBJECT)

                marks = []
                for _ in range(num_marks):  # Generate each mark
                    mark = random.randint(45, 100)  # Assuming marks range from 60 to 100
                    marks.append(f"({student_id}, {subject_id}, {mark})")

                    if len(marks) >= chunk_size:
                        row = ", ".join(marks) + ",\n\t"
                        file.write(row)
                        file.flush()
                        print(f"Flushed! +{MIN_MARKS_PER_SUBJECT} records")

                        marks.clear()

        file.flush()
        file.write('(1, 1, 100);')


generate_marks_inserts()
print("Done!")
