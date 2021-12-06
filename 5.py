class LineSegment:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def isDiagonal(self):
        return self.x1 != self.x2 and self.y1 != self.y2

    def getAffectedCoords(self):
        coords = []
        if self.x1 == self.x2:
            for y in range(min(self.y1, self.y2), max(self.y1, self.y2) + 1):
                coords.append((self.x1, y))
        elif self.y1 == self.y2:
            for x in range(min(self.x1, self.x2), max(self.x1, self.x2) + 1):
                coords.append((x, self.y1))
        else:
            if self.x1 < self.x2:
                startX = self.x1
                startY = self.y1
                endX = self.x2
                endY = self.y2
            else:
                startX = self.x2
                startY = self.y2
                endX = self.x1
                endY = self.y1

            diff = endX - startX
            ydir = 1 if endY > startY else -1
            for i in range(diff + 1):
                coords.append((startX + i, startY + i*ydir))
        return coords

    def __repr__(self):
        return "(" + str(self.x1) + "," + str(self.y1) + ") -> (" + str(self.x2) + "," + str(self.y2) + ")"

with open('5input.txt') as f:
    maxX = 0
    maxY = 0
    lines = f.readlines()
    segments = []
    for line in lines:
        split = line.strip().split(" -> ")
        coord1, coord2 = tuple(map(lambda str: str.split(","), split))
        segments.append(LineSegment(int(coord1[0]), int(coord1[1]), int(coord2[0]), int(coord2[1])))
    
    for seg in segments:
        maxX = max(maxX, seg.x1, seg.x2)
        maxY = max(maxY, seg.y1, seg.y2)

    oceanFloor = [[0] * (maxX + 1) for _ in range(maxY + 1)]
    for seg in segments:
        coords = seg.getAffectedCoords()
        for x, y in coords:
            oceanFloor[y][x] += 1

    count = 0
    for row in oceanFloor:
        for col in row:
            if col > 1:
                count += 1
    print("Count: " + str(count))
    
    # for row in oceanFloor:
    #     print("".join(list(map(lambda d: '.' if d == 0 else str(d), row))))