NUM_ROWS = 5
NUM_COLS = 5

class Board:
    def __init__(self, id, lines):
        assert(NUM_ROWS == len(lines))
        self.id = id
        self.numMap = {}
        self.marked = set()
        self.rowCounts = [0] * NUM_ROWS
        self.colCounts = [0] * NUM_COLS
        for i in range(NUM_ROWS):
            cols = list(map(lambda s: int(s), lines[i].strip().split()))
            assert(NUM_COLS == len(cols))
            for j in range(NUM_COLS):
                self.numMap[cols[j]] = (i, j)

    def markNumber(self, number):
        if number in self.numMap:
            r, c = self.numMap[number]
            self.rowCounts[r] += 1
            self.colCounts[c] += 1
            self.marked.add(number)
            return self.rowCounts[r] == NUM_COLS or self.colCounts[c] == NUM_ROWS
        else:
            return False

    def getSumUnmarked(self):
        return sum(filter(lambda n: n not in self.marked, self.numMap.keys()))


def playGame():
    with open('inputs/4.txt') as f:
        lines = f.readlines()
        order = list(map(lambda s: int(s), lines[0].strip().split(",")))
        
        boards = []
        for i in range(2, len(lines), NUM_ROWS + 1):
            boards.append(Board(len(boards), lines[i:i+NUM_ROWS]))
        
        # play game
        for number in order:
            completedBoards = set()
            print("Drew " + str(number))
            for board in boards:
                if board.markNumber(number):
                    numSum = board.getSumUnmarked()
                    score = numSum * number
                    if (len(boards)) == 1:
                        print("Last board score: " + str(score))
                        return
                    completedBoards.add(board)
            boards = list(filter(lambda b: b not in completedBoards, boards))
playGame()
            


