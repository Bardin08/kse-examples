import random


def generate_marks_inserts(num_students, num_subjects, min_marks_per_subject, max_marks_per_subject):
    with open('example.sql', 'w') as file:
        file.write("INSERT INTO marks (student_id, subject_id, mark) VALUES\n\t")

        for student_id in range(1, num_students + 1):

            for subject_id in range(1, num_subjects + 1):
                num_marks = random.randint(min_marks_per_subject,
                                           max_marks_per_subject)  # Determine the number of marks for this subject
                marks = []
                for _ in range(num_marks):  # Generate each mark
                    mark = random.randint(60, 100)  # Assuming marks range from 60 to 100
                    marks.append(f"({student_id}, {subject_id}, {mark})")

                    if len(marks) > min_marks_per_subject:
                        row = ", ".join(marks) + ",\n\t"
                        file.write(row)
                        file.flush()
                        print(f"Flushed! +{min_marks_per_subject} records")

                        marks.clear()

        file.flush()
        file.write('(1, 1, 100);')


# Example usage
num_students = 25
num_subjects = 5
min_marks_per_subject = 15  # Minimum number of marks per subject
max_marks_per_subject = 20  # Maximum number of marks per subject to match the example formatting

insert_command = generate_marks_inserts(num_students, num_subjects, min_marks_per_subject, max_marks_per_subject)
print(insert_command)
