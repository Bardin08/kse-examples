VALID_CHARS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F'
]

GIVEN_NUMBER = '328'
TARGET_BASE = 2


def validate_number(input_number: str, nbase: int):
    """
    Validates if all characters in a given expression are valid digits in a specified base.

    This function takes a string expression and a numerical base. It checks if each character in the
    expression is a valid digit for the given base. The valid digits are assumed to be stored in a list
    named `list_remainders`, where the index corresponds to the digit value.

    :param input_number: A string containing the expression to validate. Each character in this string is considered a
                         digit.
    :param nbase: An integer specifying the base of the numbering system. This determines which digits are valid.
                  For example, for base 10, valid digits are 0 through 9.
    :return: A boolean value. Returns True if all characters in the expression are valid digits for the specified base.
             Returns False otherwise.
    """
    results = map(lambda x: x in VALID_CHARS[:nbase], str(input_number))
    return all(results)


def convert_to_base(input_number: int, target_base: int) -> str:
    """
    Converts a given integer from base 10 to a specified target base.

    This function takes an integer (`input_number`) and converts it into a string representing its value in
    the target base (`target_base`). The conversion is performed by repeatedly dividing the input number by
    the target base and collecting the remainders, which represent the digits in the target base system.
    The process is continued until the input number is reduced to zero. The digits are then assembled into
    the final string representation in reverse order, as the first remainder corresponds to the least significant digit.

    :param input_number: The number in base 10 to be converted.
    :param target_base: The target base into which the number will be converted. Must be an integer greater than 1.
    :return: A string representing the `input_number` in the `target_base`. The digits are ordered from the most
     significant to the least significant.
    """
    if input_number == 0:
        return "0"

    digits = []
    current = int(input_number)

    while current > 0:
        remainder = current % target_base
        current //= target_base
        digits.append(str(remainder))

    digits.reverse()
    return "".join(digits)


def convert_to_dec(input_number: str, base: int) -> int:
    """
    Converts a number from a given base to decimal (base 10).

    This function takes a string `input_number`, which represents the number in a base specified by `BASE`, and
    converts it to its decimal (base 10) equivalent. The conversion is performed by iterating over each digit of the
    input number, converting each digit to its decimal value, and then multiplying it by the base raised to the
    power of the digit's position (starting from 0 for the least significant digit). The results for each digit
    are then summed to get the total decimal value.

    :param input_number: A string representing the number in the base specified by `BASE`.
    :param base: The base of the input number. Must be an integer greater than 1.
    :return: An integer representing the decimal (base 10) equivalent of `input_number`.
    """
    cumulative_sum = 0
    for idx, digit in enumerate(reversed(input_number)):
        cumulative_sum += int(digit) * (base ** idx)

    return cumulative_sum


# ---


if validate_number(GIVEN_NUMBER, 10):
    converted_number = convert_to_base(GIVEN_NUMBER, TARGET_BASE)
    restored_number = convert_to_dec(converted_number, TARGET_BASE)

    print(f"The given number {GIVEN_NUMBER} in decimal base equals to {converted_number} in {TARGET_BASE} base")
    print(f"The number {restored_number} was restored to decimal base from {converted_number} in {TARGET_BASE} base")
else:
    print("Invalid given number, or base")