import random


def create_board(size, num_mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mines = set()

    while len(mines) < num_mines:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        mines.add((row, col))
        board[row][col] = 'X'

    return board

def count_adjacent_mines(board, row, col):
    count = 0
    size = len(board)

    for i in range(max(0, row - 1), min(row + 2, size)):
        for j in range(max(0, col - 1), min(col + 2, size)):
            if board[i][j] == 'X':
                count += 1

    return count

def reveal_cell(board, revealed, row, col):
    if revealed[row][col]:
        return

    revealed[row][col] = True

    if board[row][col] == 'X':
        return

    if count_adjacent_mines(board, row, col) == 0:
        size = len(board)
        for i in range(max(0, row - 1), min(row + 2, size)):
            for j in range(max(0, col - 1), min(col + 2, size)):
                reveal_cell(board, revealed, i, j)

def print_board(board, revealed):
    size = len(board)

    print('   ' + ' '.join(str(i) for i in range(size)))
    print('  +' + '-' * (2 * size - 1) + '+')

    for i in range(size):
        print(f'{i} |', end='')
        for j in range(size):
            if revealed[i][j]:
                if board[i][j] == 'X':
                    print('X', end=' ')
                else:
                    count = count_adjacent_mines(board, i, j)
                    print(count if count > 0 else ' ', end=' ')
            else:
                print('.', end=' ')
        print('|')

    print('  +' + '-' * (2 * size - 1) + '+')

def play_minesweeper(size, num_mines):
    board = create_board(size, num_mines)
    revealed = [[False for _ in range(size)] for _ in range(size)]

    while True:
        print_board(board, revealed)
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))

        if row < 0 or row >= size or col < 0 or col >= size:
            print("Out of range! Please try again.")
            continue

        if board[row][col] == 'X':
            print("Game over! You hit a mine.")
            break

        reveal_cell(board, revealed, row, col)

        if all(all(revealed[i][j] or board[i][j] == 'X' for j in range(size)) for i in range(size)):
            print("Congratulations! You won!")
            break

play_minesweeper(5, 5)
