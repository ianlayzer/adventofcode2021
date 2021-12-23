def findMostCommonValue(readings, bit):
    zeroes = 0
    ones = 0
    for reading in readings:
        if reading[bit] == '0':
            zeroes += 1
        elif reading[bit] == '1':
            ones += 1
        else:
            print("Invalid bit.")
    return '0' if zeroes > ones else '1'

with open('inputs/3/full.txt') as f:
    lines = f.readlines()
    readings = [list(l.strip()) for l in lines]
    length = len(readings[0])
    ones = [0] * length
    zeroes = [0] * length

    gammaArray = [0] * length
    epsilonArray = [0] * length
    for i in range(length):
        mostCommon = findMostCommonValue(readings, i)
        if mostCommon == '0':
            gammaArray[i] = '0'
            epsilonArray[i] = '1'
        else:
            gammaArray[i] = '1'
            epsilonArray[i] = '0'
    print(gammaArray)
    print(epsilonArray)

    gamma = int("".join(gammaArray), 2)
    epsilon = int("".join(epsilonArray), 2)
    print("gamma: " + str(gamma))
    print("epsilon: " + str(epsilon))
    print("gamma * epsilon: " + str(gamma * epsilon))

    # find oxygen generator rating
    currentBit = 0
    candidates = readings
    while len(candidates) > 1:
        mostCommon = findMostCommonValue(candidates, currentBit)
        candidates = list(filter(lambda c: c[currentBit] == mostCommon, candidates))
        currentBit += 1
    oxygenRating = int("".join(candidates[0]), 2)

    # find scrubber rating
    currentBit = 0
    candidates = readings
    while len(candidates) > 1:
        mostCommon = findMostCommonValue(candidates, currentBit)
        candidates = list(filter(lambda c: c[currentBit] != mostCommon, candidates))
        currentBit += 1
    scrubberRating = int("".join(candidates[0]), 2)

    lifeSupportRating = oxygenRating * scrubberRating

    print("oxygen rating: " + str(oxygenRating))
    print("scrubber rating: " + str(scrubberRating))
    print("life support rating: " + str(lifeSupportRating))

    
    
    
    