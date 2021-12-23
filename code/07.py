from utils import readInput

def solve(file):


    lines = readInput(file)
    positions = list(map(lambda s: int(s), lines[0].split(',')))

    fuelCosts = [-1] * (max(positions) + 1)
    acc = 0
    for dist in range(max(positions) + 1):
        acc += dist
        fuelCosts[dist] = acc
    bestPos = float('inf')
    best = float('inf')
    for pos1 in range(min(positions), max(positions) + 1):
        cost = 0
        for pos2 in positions:
            cost += fuelCosts[abs(pos1 - pos2)]
        if cost < best:
            best = cost
            bestPos = pos1
    print(bestPos, best)
    

solve("inputs/7.txt")