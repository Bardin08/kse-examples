# Check win condition
# 1. Collect all rows + cols + diagonals
# 2. Convert each of them to sets
# Check the following condition
#   - A single item in the set, and it's not a '_' - we have a winner
game_board = \
    [
        ['x', 'o', 'x'],
        ['_', 'x', '_'],
        ['_', 'o', '_'],
    ]

cols = [list(c) for c in zip(game_board[0], game_board[1], game_board[2])]

diagonals = [[], []]

SIZE = 3

# d1 -> idx_r == idx_c
# d2 -> idx_r + idx_c == size - 1, where size is a game field's side length
for idx_r, r in enumerate(game_board):
    for idx_c, c in enumerate(r):
        if idx_r == idx_c:
            diagonals[0].append(game_board[idx_r][idx_c])

        if idx_r + idx_c == SIZE - 1:
            diagonals[1].append(game_board[idx_r][idx_c])

for it in diagonals:
    print(it)

all_vectors = \
    [
        *game_board,
        *cols,
        *diagonals
    ]

for it in all_vectors:
    print(it)

# --- Leaderboard ---

# add record to leaderboard
# show leaderboard

leaderboard = \
    [
        {
            "Player": "Vlad_1",
            "Wins": 15,
            "Loses": 10,
            "Draws": 20
        },
        {
            "Player": "Vlad_2",
            "Wins": 10,
            "Loses": 10,
            "Draws": 20
        }
    ]

with open('leaderboard.txt', 'w') as f:
    f.write(str(leaderboard))

with open('leaderboard.txt', 'r') as f:
    for line in f.readlines():
        print(line)
