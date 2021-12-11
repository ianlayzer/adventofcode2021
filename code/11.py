def printGrid(grid):
    for row in grid:
        print("".join([str(i) for i in row]))

def copyGrid(grid):
    return [row.copy() for row in grid]

def isInRange(grid, r, c):
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

def flash(grid, alreadyFlashed, r, c):
    if grid[r][c] <= 9 or (r, c) in alreadyFlashed:
        return
    # print("Flash: " + str((r,c)))
    alreadyFlashed.add((r, c))
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if isInRange(grid, i, j):
                grid[i][j] += 1
                flash(grid, alreadyFlashed, i, j)

def isSynced(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                return False
    return True
def simulate(grid, numSteps):
    flashCount = 0
    flashed = set()
    sync = False
    step = 0
    while not sync:
        step += 1
        # increase every energy level
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += 1
        # flash
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                flash(grid, flashed, i, j)
                            
        # any octupus that flashed should be set to 0
        for r, c in flashed:
            grid[r][c] = 0
        flashCount += len(flashed)
        flashed = set()
        sync = isSynced(grid)

    return step

def solve(file):
    grid = [[int(s) for s in list(l.strip())] for l in open(file).readlines()]
    step = simulate(grid, 100)
    print(step)

solve("inputs/11.txt")