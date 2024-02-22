# Write a Python function to find the maximum of three numbers.

def max_three(in_list):
    return sorted(in_list, reverse=True)[:3]


# Write a Python function to multiply all the numbers in a list.
def multiply_list(in_list):
    res = 1
    return [res * i for i in in_list]


# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def distinct(in_list):
    return list(set(in_list))


# local variables
def multiply_list(list_to_multiply):
    result = 1
    for num in list_to_multiply:
        result *= num

    return result


# postal validation
def validate_postal(postal: str):
    if len(postal) < 6:
        return False, "Too short"

    postal.replace(" ", "")

    if len(postal) != 6:
        return False, "Invalid length, must be 6"

    letters_validation_result = validate_postal_positions(postal, [0, 2, 4], lambda x, i: x.isalpha())
    if not letters_validation_result[0]:
        return letters_validation_result

    digits_validation_result = validate_postal_positions(postal, [1, 3, 5], lambda x, i: x.isdigit())
    if not digits_validation_result[0]:
        return digits_validation_result

    return True,


def validate_postal_positions(postal, positions, predicate):
    for pos in positions:
        if not predicate(postal[pos], pos):
            return False, "Unexpected character"

    return True,


print("Max three: " + str(max_three((1, 2, 2, 2, 2, 2, 2, 2, 2, 3))))
print("Multiply: " + str(multiply_list((1, 2, 2, 2, 2, 2, 2, 2, 2, 3))))
print("Distinct: " + str(distinct((1, 2, 2, 2, 2, 2, 2, 2, 2, 3))))

# postal code validations
print(validate_postal("a2s1f1"))
print(validate_postal("a211f1"))
print(validate_postal("12s1f1"))
print(validate_postal("ads1f1"))
print(validate_postal("as1f1"))
print(validate_postal("a244s1f1"))
print(validate_postal("a244   s1f1"))
print(validate_postal("a244 s1f1"))

raise ValueError("MY TEST EXCEPTION")

try:
    some_input = "hello"
    some_int = int(some_input)
except ValueError:
    print("Not a number")
