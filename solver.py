import math
def getSize(grid):
    num = 0
    for x in grid:
        num += 1
    return num

def is_valid_move(grid, row, col, number):
    for x in range(getSize(grid)):
        if grid[row][x] == number:
            return False
    for x in range(getSize(grid)):
        if grid[x][col] == number:
            return False

    root = math.sqrt(getSize(grid))

    corner_row = row - row % int(root)
    corner_col = col - col % int(root)

    for x in range(int(root)):
        for y in range(int(root)):
            if grid[corner_row + x][corner_col + y] == number:
                return False

    return True

def solve(grid, row, col):
    if col == getSize(grid):
        if row == getSize(grid)-1:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)

    for num in range(1, getSize(grid)+1):

        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            if solve(grid, row, col + 1):
                return True

        grid[row][col] = 0

    return False

def solved(grid):
    if solve(grid, 0, 0):
        print("Solved Sudoku:")
        for i in range(getSize(grid)):
            for j in range(getSize(grid)):
                print(grid[i][j], end=" ")
            print()
    else:
        print("No Solution For This Sudoku")

grid = [[1, 0, 3, 0],
        [0, 2, 0, 4],
        [4, 0, 2, 0],
        [0, 3, 0, 1]]
grid2 = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]]

solved(grid)
solved(grid2)

