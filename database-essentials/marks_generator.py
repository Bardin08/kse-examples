import random


def generate_marks_inserts(num_students, num_subjects, min_marks_per_subject, max_marks_per_subject):
    base_command = "INSERT INTO marks (student_id, subject_id, mark) VALUES\n\t"
    inserts = list(list())
    for student_id in range(1, num_students + 1):
        inserts.append([])

        for subject_id in range(1, num_subjects + 1):
            num_marks = random.randint(min_marks_per_subject,
                                       max_marks_per_subject)  # Determine the number of marks for this subject
            for _ in range(num_marks):  # Generate each mark
                mark = random.randint(60, 100)  # Assuming marks range from 60 to 100
                inserts[student_id - 1].append(f"({student_id}, {subject_id}, {mark})")

    rows = []
    for student_marks in inserts:
        row = ", ".join(student_marks)
        rows.append(row)

    formatted_inserts = ",\n\t".join(rows)
    command = base_command + formatted_inserts + ";"
    return command


# Example usage
num_students = 25
num_subjects = 5
min_marks_per_subject = 15  # Minimum number of marks per subject
max_marks_per_subject = 20  # Maximum number of marks per subject to match the example formatting

insert_command = generate_marks_inserts(num_students, num_subjects, min_marks_per_subject, max_marks_per_subject)
print(insert_command)
