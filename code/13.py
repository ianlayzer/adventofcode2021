def getMaxes(coords):
    maxX, maxY = 0, 0
    for x, y in coords:
        maxX = max(maxX, x)
        maxY = max(maxY, y)
    return maxX, maxY

def display(coords):
    maxX, maxY = getMaxes(coords)
    paper = [["."] * (maxX + 1) for _ in range(maxY + 1)]
    for x, y in coords:
        paper[y][x] = "#"
    for i, row in enumerate(paper):
        numStr = str(i)
        if i < 10:
            numStr += " "
        print(numStr + " " + "".join(row))

def fold(x, maxX, fold):
    if x == fold:
        return None
    newMaxX = max(maxX - fold, fold - maxX) - 1
    pastFold = x - fold
    newX = newMaxX - (pastFold - 1)
    return newX

    

def solve(file):
    lines = [l.strip() for l in open(file).readlines()]
    coords = set()
    folds = []
    for line in lines:
        if "fold" in line:
            split = line.split("=")
            axis = split[0][-1]
            num = int(split[1])
            folds.append((axis, num))
        elif len(line) > 0:
            split = line.split(",")
            x, y = int(split[0]), int(split[1])
            coords.add((x, y))
    for fAxis, fNum in folds[:1]:
        maxX, maxY = getMaxes(coords)
        newCoords = set()
        for x, y in coords:
            if fAxis == "x":
                newX = fold(x, maxX, fNum)
                newY = y
            elif fAxis == "y":
                newX = x
                newY = fold(y, maxY, fNum)
            if newX != None and newY != None:
                newCoords.add((newX, newY))
        coords = newCoords
    print(coords)

# solve("inputs/13small.txt")
tests = [1, 3, 5, 11, 13]
print(tests)
print(list(map(lambda t: fold(t, 14, 7), tests)))
