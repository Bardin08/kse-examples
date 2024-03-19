GIVEN_NUMBER = 328
BASE = 5

digits = []
current = GIVEN_NUMBER
while current != 0:
    reminder = int(current % BASE)
    current = (current - reminder) / BASE
    digits.append(str(reminder))

print("".join(digits))

# ---

cumulative_sum = 0
for idx, digit in enumerate(reversed(digits)):
    cumulative_sum += int(digit) * (BASE ** idx)

print(cumulative_sum)
