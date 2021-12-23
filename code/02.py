with open ('inputs/02/full.txt') as f:
    lines = f.readlines()
    aim = 0
    depth = 0
    horizontal = 0
    for line in lines:
        split = line.split(" ")
        action = split[0]
        num = int(split[1].strip())
        if action == "forward":
            horizontal += num
            depth += aim * num
        elif action == "down":
            aim += num
        elif action == "up":
            aim -= num
    
    print("Depth: " + str(depth))
    print("Horizontal: " + str(horizontal))
    print(depth * horizontal)
