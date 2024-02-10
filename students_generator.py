import random


def generate_student_name():
    first_names = ["John", "Jane", "Emily", "Chris", "Alex", "Michael", "Emma", "Olivia",
                   "James", "Isabella", "Sophia", "Amelia", "Lucas", "Charlotte", "Aiden","Mia",
                   "Ethan", "Harper", "Mason", "Ella", "Ava", "William", "Sophie", "Benjamin", "Zoe"
                   "Liam", "Lily", "Noah", "Grace", "Oliver", "Chloe", "Elijah", "Aria", "Logan",
                   "Avery", "Alexander", "Evelyn", "Jacob", "Abigail", "Daniel", "Nora", "Matthew",
                   "Scarlett", "David", "Madison", "Joseph", "Layla", "Jackson", "Riley", "Samuel"]

    last_names = ["Doe", "Smith", "Davis", "Brown", "Johnson", "Wilson", "Moore", "Taylor",
                  "Anderson", "Thomas", "Jackson", "Martin", "Lee", "Hall", "Young", "King",
                  "Wright", "Lopez", "Hill", "Scott", "Adams", "James", "Turner", "Green",
                  "Evans", "Baker", "Harris", "Robinson", "Clark", "Lewis", "Walker", "Parker",
                  "Cook", "Edwards", "Morris", "Rivera", "Cooper", "Morgan", "Peterson", "Cooper",
                  "Reed", "Bailey", "Bell", "Gonzalez", "Carter", "Phillips", "Mitchell", "Ross",
                  "Reyes", "Stewart", "Morales", "Murphy", "Sanchez", "Foster", "Clark"]

    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    return name


def generate_students_inserts(num_students_per_group, group_names):
    base_command = "INSERT INTO students (student_name, group_id) VALUES\n\t"
    inserts = []

    for group_id, group_name in enumerate(group_names, start=1):
        group_inserts = [f"('{generate_student_name()}', {group_id})" for _ in range(num_students_per_group)]
        # Iterate over group_inserts in chunks of up to 15
        chunk_size = 15
        for i in range(0, len(group_inserts), chunk_size):
            chunk = group_inserts[i:i + chunk_size]
            chunk_command = ", ".join(chunk)
            # Add a comma after each chunk except the last chunk of the last group
            if not (i + chunk_size >= len(group_inserts) and group_id == len(group_names)):
                chunk_command += ","
            inserts.append(chunk_command)
        # Add an empty line separator between groups, except after the last group
        if group_id != len(group_names):
            inserts.append("")

    # Joining group inserts with a newline and tab, ensuring proper SQL syntax
    formatted_inserts = "\n\t".join(inserts)
    command = base_command + formatted_inserts
    if command.endswith(","):
        command = command[:-1]  # Remove the trailing comma if present
    command += ";"
    return command

num_students_per_group = 500
group_names = ['CS101', 'CS102', 'CS103', 'CS104', 'CS105']  # Define your group names here

insert_command = generate_students_inserts(num_students_per_group, group_names)

print(insert_command)
print("Done!")

### Output to be saved in a file
# with open('students_inserts.txt', 'w') as file:
#     print(insert_command, file=file)
#     print("Output written to students_inserts.txt")