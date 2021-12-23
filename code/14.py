from collections import defaultdict

def pairInsertion(template, rules, numSteps):
    currPolymer = template
    lastScore = 0
    for i in range(numSteps):
        nextPolymer = ""
        justAdded = False
        for j in range(len(currPolymer)-1):
            currPair = currPolymer[j:j+2]
            if currPair in rules:
                if not justAdded:
                    nextPolymer += currPair[0]
                nextPolymer += rules[currPair]
                nextPolymer += currPair[1]
                justAdded = True
            else:
                justAdded = False
        currPolymer = nextPolymer
        score = getScore(currPolymer)
        r = score / lastScore if lastScore > 0 else 0
        print(f"After step {i+1}: {currPolymer}")
        lastScore = score
    return currPolymer

def makeRules(ruleLines):
    rules = {}
    for line in ruleLines:
        split = line.split(" -> ")
        pair = split[0]
        insertion = split[1]
        rules[pair] = insertion
    return rules

def getScore(polymer):
    counts = defaultdict(int)
    for c in polymer:
        counts[c] += 1
    return max(counts.values()) - min(counts.values())

def solve(file):
    lines = [l.strip() for l in open(file).readlines()]
    template = lines[0]
    rules = makeRules(lines[2:])
    polymer = pairInsertion(template, rules, 5)
    score = getScore(polymer)
    print(score)

def addCounts(counts1, counts2):
    for c in counts2:
        if c in counts1:
            counts1[c] += counts2[c]
        else:
            counts1[c] = counts2[c]

def solveFast(file):
    lines = [l.strip() for l in open(file).readlines()]
    template = lines[0]
    rules = makeRules(lines[2:])
    cache = {}
    def recursive(pair, numSteps):
        if (pair, numSteps) in cache:
            return cache[(pair, numSteps)]
        if not pair in rules or numSteps == 0:
            if pair[0] == pair[1]:
                return {pair[0]: 2}
            else:
                return {pair[0]: 1, pair[1]: 1}
        insertion = rules[pair]
        result = {}
        recLeft = recursive(pair[0] + insertion, numSteps - 1)
        recRight = recursive(insertion + pair[1], numSteps - 1)
        addCounts(result, recLeft)
        addCounts(result, recRight)
        result[insertion] -= 1
        cache[(pair, numSteps)] = result
        return result
    
    totalCounts = {}
    for i in range(len(template) - 1):
        pair = template[i:i+2]
        pairCounts = recursive(pair, 40)
        addCounts(totalCounts, pairCounts)
    
    for i in range(1, len(template) - 1):
        totalCounts[template[i]] -= 1
    score = max(totalCounts.values()) - min(totalCounts.values())
    print(f"Score: {score}")     

solveFast("inputs/14.txt")
