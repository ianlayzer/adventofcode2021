def readInput(filePath):
    with open(filePath) as f:
        return list(map(lambda l: l.strip(), f.readlines()))