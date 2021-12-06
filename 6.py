def generation(currentGen):
    nextGen = [-1] * len(currentGen)
    for i, fish in enumerate(currentGen):
        if fish == 0:
            nextGen[i] = 6
            nextGen.append(8)
        else:
            nextGen[i] = fish - 1
    return nextGen


def simulate(initialState, days):
    curr = initialState
    print(curr)
    for i in range(days):
        curr = generation(curr)
    return len(curr)

def generationBig(currentGen):
    nextGen = [0] * 9
    nextGen[8] = currentGen[0]
    nextGen[7] = currentGen[8]
    nextGen[6] = currentGen[7] + currentGen[0]
    nextGen[5] = currentGen[6]
    nextGen[4] = currentGen[5]
    nextGen[3] = currentGen[4]
    nextGen[2] = currentGen[3]
    nextGen[1] = currentGen[2]
    nextGen[0] = currentGen[1]
    return nextGen
    

def simBig(initialState, days):
    numFishes = [0] * 9
    for fish in initialState:
        numFishes[fish] += 1
    
    for i in range(days):
        numFishes = generationBig(numFishes)
    return sum(numFishes)
    



def solve(file):
    with open(file) as f:
        data = list(map(lambda s: int(s), f.readline().strip().split(",")))
        print(simBig(data, 256))

solve("6.txt")