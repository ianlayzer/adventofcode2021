from collections import defaultdict

class DigitSignals:
    def __init__(self, signals):
        self.signals = ["".join(sorted(s)) for s in signals]
        self.signalsByLength = defaultdict(list)
        self.wires = ["?"] * 7
        self.numberMap = {}
        self.signalsToNumbers = {}
        self.solve()

    def solve(self):
        for signal in self.signals:
            self.signalsByLength[len(signal)].append(signal)
            if len(signal) == 2:
                self.numberMap[1] = signal
            elif len(signal) == 3:
                self.numberMap[7] = signal
            elif len(signal) == 4:
                self.numberMap[4] = signal
            elif len(signal) == 7:
                self.numberMap[8] = signal
        # use 1 and 7 to find top wire
        top = list(filter(lambda c: c not in self.numberMap[1], self.numberMap[7]))[0]
        self.wires[0] = top
        # 3 has length 5 and has all the wires of 7
        for signal in self.signalsByLength[5]:
            isPossible = True
            for c in self.numberMap[7]:
                if c not in signal:
                    isPossible = False
            if isPossible:
                self.numberMap[3] = signal
                break
        # 9 is only 6 character number that has all of 4 characters
        for signal in self.signalsByLength[6]:
            signalSet = set(signal)
            isPossible = True
            for c in self.numberMap[4]:
                if c not in signalSet:
                    isPossible = False
            if isPossible:
                self.numberMap[9] = signal
                break
        # 0 has one character difference from 9 and has both of 1
        for signal in self.signalsByLength[6]:
            signalSet = set(signal)
            differences = 0
            for c in self.numberMap[9]:
                if c not in signalSet:
                    differences += 1
            if differences == 1:
                isPossible = True
                for c in self.numberMap[1]:
                    if c not in signalSet:
                        isPossible = False
                if isPossible:
                    self.numberMap[0] = signal
        # 6 is last remaining 6 char
        for signal in self.signalsByLength[6]:
            if signal not in self.numberMap.values():
                self.numberMap[6] = signal
        # 5 is 6 without 1 character
        sixSet = set(self.numberMap[6])
        for signal in self.signalsByLength[5]:
            if signal == self.numberMap[3]:
                continue
            isPossible = True
            for c in signal:
                if c not in sixSet:
                    isPossible = False
            if isPossible:
                self.numberMap[5] = signal
                break
        matched = set(self.numberMap.values())
        unmatched = list(filter(lambda s: s not in matched, self.signals))
        for signal in unmatched:
            if len(signal) == 5:
                self.numberMap[2] = signal

        # reverse number map
        for number, signal in self.numberMap.items():
            self.signalsToNumbers[signal] = str(number)

    def translate(self, signals):
        sortedSignals = ["".join(sorted(s)) for s in signals]
        return int("".join([self.signalsToNumbers[s] for s in sortedSignals]))        

def solveDisplay(signals, outputs):
    digit = DigitSignals(signals)
    num = digit.translate(outputs)
    return num

def solve(file):
    lines = [l.strip().split(" | ") for l in open(file).readlines()]
    total = 0
    for signals, outputs in lines:
        num = solveDisplay(signals.split(), outputs.split())
        print(num)
        total += num
    print("total: " + str(total))
    



solve("inputs/08/full.txt")