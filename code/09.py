
def isInRange(r, c, heightMap):
    numRows = len(heightMap)
    numCols = len(heightMap[0])
    return r >= 0 and r < numRows and c >= 0 and c < numCols

def getNeighbors(r, c, heightMap):
    candidates = []
    if isInRange(r+1, c, heightMap):
        candidates.append((r+1, c))
    if isInRange(r-1, c, heightMap):
        candidates.append((r-1, c))
    if isInRange(r, c+1, heightMap):
        candidates.append((r, c+1))
    if isInRange(r, c-1, heightMap):
        candidates.append((r, c-1))
    return candidates

def findLowestPoints(heightMap):
    numRows = len(heightMap)
    numCols = len(heightMap[0])
    lowPoints = []
    for i in range(numRows):
        for j in range(numCols):
            curr = heightMap[i][j]
            neighbors = getNeighbors(i, j, heightMap)
            isLowPoint = True
            for r, c in neighbors:
                if curr >= heightMap[r][c]:
                    isLowPoint = False
            if isLowPoint:
                lowPoints.append((curr, i, j))
    return lowPoints

def exploreBasin(heightMap, row, col, alreadyInBasin):
    def exploreHelper(r, c, prev, visited):
        if (r,c) in visited or (r,c) in alreadyInBasin:
            return
        if not isInRange(r, c, heightMap):
            return
        if heightMap[r][c] == 9:
            return
        visited.add((r, c))
        currHeight = heightMap[r][c]
        neighbors = getNeighbors(r, c, heightMap)
        for nr, nc in neighbors:
            if currHeight > heightMap[nr][nc] and not (nr, nc) in visited:
                visited.remove((r, c))
                return
        for nr, nc in neighbors:
            if currHeight < heightMap[nr][nc]:
                exploreHelper(nr, nc, currHeight, visited)
    
    visited = set()
    exploreHelper(row, col, 0, visited)
    return visited

def solve(file):
    heightMap = [[int(s) for s in list(l.strip())] for l in open(file).readlines()]
    # printGrid(heightMap)
    lowPoints = findLowestPoints(heightMap)
    basinSizes = []
    alreadyInBasin = set()
    for _, r, c in lowPoints:
        basin = exploreBasin(heightMap, r, c, alreadyInBasin)
        alreadyInBasin.update(basin)
        print(sorted(list(basin)))
        basinSizes.append(len(basin))
    basinSizes = sorted(basinSizes, reverse=True)
    print(basinSizes)
    score = 1
    for size in basinSizes[:3]:
        score *= size
    print(score)
    

def printGrid(grid):
    for row in grid:
        print(row)
solve("inputs/09/full.txt")