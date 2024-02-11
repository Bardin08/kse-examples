import random

# configuration
STUDENTS_PER_GROUP = 500
GROUP_NUMBERS = 5

FIRST_NAMES = ["John", "Jane", "Emily", "Chris", "Alex", "Michael", "Emma", "Olivia",
               "James", "Isabella", "Sophia", "Amelia", "Lucas", "Charlotte", "Aiden", "Mia",
               "Ethan", "Harper", "Mason", "Ella", "Ava", "William", "Sophie", "Benjamin", "Zoe",
               "Liam", "Lily", "Noah", "Grace", "Oliver", "Chloe", "Elijah", "Aria", "Logan",
               "Avery", "Alexander", "Evelyn", "Jacob", "Abigail", "Daniel", "Nora", "Matthew",
               "Scarlett", "David", "Madison", "Joseph", "Layla", "Jackson", "Riley", "Samuel"]

LAST_NAMES = ["Doe", "Smith", "Davis", "Brown", "Johnson", "Wilson", "Moore", "Taylor",
              "Anderson", "Thomas", "Jackson", "Martin", "Lee", "Hall", "Young", "King",
              "Wright", "Lopez", "Hill", "Scott", "Adams", "James", "Turner", "Green",
              "Evans", "Baker", "Harris", "Robinson", "Clark", "Lewis", "Walker", "Parker",
              "Cook", "Edwards", "Morris", "Rivera", "Cooper", "Morgan", "Peterson", "Cooper",
              "Reed", "Bailey", "Bell", "Gonzalez", "Carter", "Phillips", "Mitchell", "Ross",
              "Reyes", "Stewart", "Morales", "Murphy", "Sanchez", "Foster", "Clark"]

DEFAULT_CHUNK_SIZE = 10000


def generate_student_name():
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"


def generate_students_inserts():
    with open(f'scripts/insert_students.sql', 'w') as file:
        file.write("INSERT INTO students (student_name, group_id) VALUES\n\t")

        chunk_size = STUDENTS_PER_GROUP if DEFAULT_CHUNK_SIZE >= STUDENTS_PER_GROUP else DEFAULT_CHUNK_SIZE
        for group_id in range(1, GROUP_NUMBERS + 1):
            students = []
            for student in range(STUDENTS_PER_GROUP):
                students.append(f"('{generate_student_name()}', {group_id})")

                if len(students) >= chunk_size:
                    row = ", ".join(students) + ",\n\t"
                    file.write(row)
                    file.flush()
                    print(f"Flushed! +{chunk_size} records")

                    students.clear()

        file.flush()
        file.write(f"('{generate_student_name()}', 1);")  # add record to the first group to avoid trailing-comma


generate_students_inserts()
print("Done!")
