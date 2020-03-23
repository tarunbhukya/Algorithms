"""
place all the 8 queens in such a way that
no queen kills another queen
"""

n = 8


def print_board(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()


def is_safe(board, x, y):
    # check for all columns till y
    for j in range(y):
        if board[x][j] == 1:
            return False

    # check for left upper diagonal
    j = y - 1
    i = x - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1


    # check for left lower diagonal
    i = x+1
    j = y-1
    while i < n and j >= 0 and i >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1

    return True


def is_queen_problem_solved(board, x, y, queens_placed):
    if queens_placed == n:
        return True
    else:
       # for all the rows
       for i in range(n):
           if is_safe(board, i, y):
                board[i][y] = 1
                queens_placed = queens_placed + 1
                if is_queen_problem_solved(board, x, y+1, queens_placed):
                    return True
                else:
                    board[i][y] = 0
                    queens_placed = queens_placed - 1


    return False


board = [[0 for i in range(n)] for i in range(n)]
queens_placed = 0

if is_queen_problem_solved(board, 0, 0, queens_placed):
    print_board(board)
else:
    print("No Solution")
