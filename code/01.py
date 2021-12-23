

with open('inputs/01/full.txt') as f:
    lines = f.readlines()
    # part 1
    count = 0
    last = None
    for line in lines:
        num = int(line.strip())
        if last and num > last:
            count += 1
        last = num
    print("Part 1: " + str(count))
    # part 2
    prefixSums = [0] * len(lines)
    summ = 0
    for i, line in enumerate(lines):
        num = int(line.strip())
        summ += num
        prefixSums[i] = summ
    count = 0
    last = prefixSums[2]
    for i in range(3, len(prefixSums)):
        window = prefixSums[i] - prefixSums[i-3]
        if last and window > last:
            count += 1
        last = window
    print("Part 2: " + str(count))
    
