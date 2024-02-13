import random

MINE = 'X'
SPACE = '0'
GAME_FIELD_SIZE = 4

MINES_LIVES = {
    6: 3,
    4: 2,
    1: 1
}


def print_game_field(field):
    print("\n".join([" ".join(row) for row in field]))


def get_game_field():
    return [
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-']
    ]


def get_mines_amount() -> int:
    amount = input("Enter mines amount: ")
    while not amount.isdigit():
        print("Mines amount is not valid")
        amount = input("Enter mines amount: ")
    return int(amount)


def get_lives_amount():
    amount = 0
    for key, value in MINES_LIVES.items():
        if key >= mines_amount:
            amount = value
    return amount


def get_mines_positions():
    positions = set()
    while len(positions) < mines_amount:
        positions.add(
            (
                random.randint(0, GAME_FIELD_SIZE - 1),
                random.randint(0, GAME_FIELD_SIZE - 1)
            ))
    return positions


def do_step(lives_left, cells_left, mines):
    move_x, move_y = map(int, input(f"Enter row and col split by space ({lives_left}❤️)").split())
    move_x -= 1
    move_y -= 1
    if (move_x, move_y) in mines:
        game_field[move_x][move_y] = MINE
        mines.remove((move_x, move_y))
        lives_left -= 1
    else:
        game_field[move_x][move_y] = SPACE
        cells_left -= 1
    print("\n".join([" ".join(row) for row in game_field]))
    return lives_left, cells_left


while True:
    game_field = get_game_field()
    print_game_field(game_field)

    mines_amount = get_mines_amount()
    lives = get_lives_amount()
    print(f"Mines: {mines_amount}, Lives: {lives}")

    mines_positions = get_mines_positions()
    print(f"Mines positions: {mines_positions}")

    safe_moves = GAME_FIELD_SIZE ** 2 - mines_amount

    while not (lives <= 0 or safe_moves <= 0):
        lives, safe_moves = do_step(lives, safe_moves, mines_positions)

    if lives > 0:
        print("You win! 👏")
    else:
        print("You lose 💔")

    if not input("Play again? (y/Y): ") in ['y', 'Y']:
        break

print("Thanks for playing. Exiting..")
