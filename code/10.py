openToClose = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">"
}
closeToOpen = {
    "]": "[",
    "}": "{",
    ")": "(",
    ">": "<"
}

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

autoScores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def check(line):
    stack = []
    for c in line:
        if c in openToClose:
            stack.append(c)
        elif not len(stack):
            return c
        elif stack.pop() != closeToOpen[c]:
            return c
    return None

def complete(line):
    score = 0
    stack = []
    for c in line:
        if c in openToClose:
            stack.append(c)
        else:
            stack.pop()
    stack = list(reversed(stack))
    for c in stack:
        score = score * 5 + autoScores[openToClose[c]]

    return score

def solve(file):
    lines = [l.strip() for l in open(file).readlines()]
    scores = []
    for line in lines:
        err = check(line)
        if not err:
            scores.append(complete(line))
    mid = len(scores) // 2
    scores = sorted(scores)
    print(scores[mid])
    
solve("inputs/10.txt")