import random

MINE = 'X'
SPACE = '0'
GAME_FIELD_SIZE = 4

MINES_LIVES = {
    6: 3,
    4: 2,
    1: 1
}

while True:
    game_field = [
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
        ['-', '-', '-', '-'],
    ]

    print("\n".join([" ".join(row) for row in game_field]))

    mines_amount = input("Enter mines amount: ")
    while not mines_amount.isdigit():
        print("Mines amount is not valid")
        mines_amount = input("Enter mines amount: ")
    mines_amount = int(mines_amount)

    lives = 0
    for key, value in MINES_LIVES.items():
        if key >= mines_amount:
            lives = value
    print(f"Mines: {mines_amount}, Lives: {lives}")

    mines_positions = set()
    while len(mines_positions) < mines_amount:
        mines_positions.add(
            (
                random.randint(0, GAME_FIELD_SIZE - 1),
                random.randint(0, GAME_FIELD_SIZE - 1)
            ))
    print(f"Mines positions: {mines_positions}")

    safe_moves = GAME_FIELD_SIZE ** 2 - mines_amount

    while not (lives <= 0 or safe_moves <= 0):
        move_x, move_y = map(int, input(f"Enter row and col split by space ({lives}❤️)").split())

        move_x -= 1
        move_y -= 1

        if (move_x, move_y) in mines_positions:
            game_field[move_x][move_y] = MINE
            mines_positions.remove((move_x, move_y))
            lives -= 1
        else:
            game_field[move_x][move_y] = SPACE
            safe_moves -= 1

        print("\n".join([" ".join(row) for row in game_field]))

    if lives > 0:
        print("You win! 👏")
    else:
        print("You lose 💔")

    if not input("Play again? (y/Y): ") in ['y', 'Y']:
        break

print("Thanks for playing. Exiting..")
