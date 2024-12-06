import random
grid_size = 7
grid = [['~' for _ in range(grid_size)] for _ in range(grid_size)]

ship_row = random.randint(0, grid_size - 1)
ship_col = random.randint(0, grid_size - 1)

print("Welcome to Sea Battle!")
attempts = 7
for turn in range(attempts):
    print("\nTurn", turn + 1)
    # Display the grid
    for row in grid:
        print(' '.join(row))

    try:
        guess_row = int(input(f"Guess row (0-{grid_size - 1}): "))
        guess_col = int(input(f"Guess column (0-{grid_size - 1}): "))
    except ValueError:
        print("Please enter valid numbers!")
        continue

    if guess_row == ship_row and guess_col == ship_col:
        print("You hit the ship! You win!")
        grid[guess_row][guess_col] = 'X'
        break
    elif 0 <= guess_row < grid_size and 0 <= guess_col < grid_size:
        if grid[guess_row][guess_col] == 'O':
            print("You already guessed this spot. Try again.")
        else:
            print("Miss!")
            grid[guess_row][guess_col] = 'O'
    else:
        print("Out of bounds! Try again.")

    if turn == attempts - 1:
        print("\nGame Over! The ship was at:", ship_row, ship_col)

print("\nFinal grid:")
for row in grid:
    print(' '.join(row))
