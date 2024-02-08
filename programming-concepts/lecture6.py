set_of_tuple = {
    ("key_1", "value_1"),
    ("key_1", "value_1_1"),
    ("key_2", "value_2"),
    ("key_3", "value_3"),
}

dict1 = {}
for tuple_item in set_of_tuple:
    key, value = tuple_item

    if not dict1.__contains__(key):
        dict1[key] = []

    dict1[key].append(value)

print(str(dict1))

# --- take a list of ints and print second greatest

integers = (input("Enter integers splited by whitespace: ")
            .split())
integers = map(int, integers)

set_of_integers = set(integers)
integers = list(sorted(set_of_integers, reverse=True))

second_greatest = integers[1] if len(integers) >= 2 else None
print(second_greatest)

# ---

input_tuple = (1, 2)

reversed_tuple = input_tuple[::-1]

a, b = input_tuple
reversed_tuple1 = (b, a)

print(reversed_tuple)
print(reversed_tuple1)

# ---

given_numbers = [1, 2, 4, 4, 5, 6, 3, 2, 3]  # -> [1, 2, 4, 5, 6, 3]
unique = []

for i in given_numbers:
    if i not in unique:
        unique.append(i)

print(unique)

# ---

dict1 = {"key_1": "value_1", "key_2": "value_2_1"}
dict2 = {"key_2": "value_2_2", "key_3": "value_3"}

merged_dict = {**dict1, **dict2}

print(merged_dict)
