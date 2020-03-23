"""
A Maze is given as N*N binary matrix of blocks where source block is the upper left most block
i.e., maze[0][0] and destination block is lower rightmost block i.e., maze[N-1][N-1].
A rat starts from source and has to reach the destination.
The rat can move only in two directions: forward and down.
In the maze matrix, 0 means the block is a dead end and 1 means the block can be used in the path
from source to destination. Note that this is a simple version of the typical Maze problem.
For example, a more complex version can be that the rat can move in 4 directions and a more
complex version can be with a limited number of moves.
"""

n = 4


def print_board(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()


def is_safe(maze, x, y):
    if 0 <= x < n and 0 <= y < n and maze[x][y] == 1:
        return True
    return False


def solve_maze_util(maze, x, y, solution):
    # if reached end point return True
    if x == n - 1 and y == n - 1:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y):
        solution[x][y] = 1

        # check for right direction
        if solve_maze_util(maze, x + 1, y, solution):
            return True

        if solve_maze_util(maze, x, y + 1, solution):
            return True

        solution[x][y] = 0
        return False
    else:
        return False


def solve_maze(maze):
    solution = [[0 for i in range(n)] for i in range(n)]
    if not solve_maze_util(maze, 0, 0, solution):
        print("no solution")
    print_board(solution)


board = [[1, 0, 0, 0],
         [1, 1, 0, 1],
         [0, 1, 0, 0],
         [1, 1, 1, 1]]

solve_maze(board)
