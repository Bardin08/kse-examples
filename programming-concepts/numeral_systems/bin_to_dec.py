GIVEN_NUMBER = 328
BASE = 5

# 9A7x16 ->
# 7*16^0 + A*16^1 + 9*16^2 ->
# 7+160+2304 ->
# 2471x10

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
