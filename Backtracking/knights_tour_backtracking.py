"""

The knight is placed on the first block of an empty board and,
moving according to the rules of chess,
must visit each square exactly once.

till n = 6 it will give quick response
but after 6 it will take so much computation
power.


"""

n = 8


def print_board(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()


def get_fresh_board():
    return [[-1 for i in range(n)] for i in range(n)]


def is_safe_to_place_knight(x, y, arr):
    if 0 < x < n and 0 < y < n and arr[x][y] == -1:
        return True
    return False


def mov_kt_util(arr, x, y, mov_x, mov_y, pos):

    if pos == n**n :
        return True

    for i in range(n):
        new_x = x + mov_x[i]
        new_y = y + mov_y[i]

        if is_safe_to_place_knight(new_x, new_y, arr):
            arr[new_x][new_y] = pos
            if pos == 50:
                print_board(arr)
                print()
            if mov_kt_util(arr, new_x, new_y, mov_x, mov_y, pos+1):
                return True
            arr[new_x][new_y] = -1
    return False


def execute_knight_tour_backtracking():
    board = get_fresh_board()
    position = 1
    mov_x = [2, 1, -1, -2, -2, -2, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[0][0] = 0
    if not mov_kt_util(board, 0, 0, mov_x, mov_y, position):
        print("solution does not exist")
    else:
        print_board(board)


execute_knight_tour_backtracking()


