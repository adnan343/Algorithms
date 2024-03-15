def DFS(grid, row, column):
    if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]) or grid[row][column] == '#' or grid[row][column] == 'X':
        return 0

    d= 0
    if grid[row][column] == 'D':
        d = 1
    grid[row][column] = 'X'

    d += DFS(grid, row - 1, column)
    d += DFS(grid, row + 1, column)
    d += DFS(grid, row, column - 1)
    d += DFS(grid, row, column + 1)

    return d

def max_diamonds(grid):
    max_d = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == '.':
                max_d = max(max_d, DFS(grid, row, column))

    return max_d

with open("input6.txt", "r") as file:
    outfile= open("output6.txt","w")

    temp = file.readline().strip().split(' ')
    R = int(temp[0])
    H = int(temp[1])
    grid = []

    for x in range(R):
        row = file.readline().strip()
        grid.append(list(row))

    max_d =max_diamonds(grid)

    with open("output6.txt", "w") as file1:
        file1.write(f'{max_d}')
