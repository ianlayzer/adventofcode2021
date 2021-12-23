from collections import defaultdict

def createAdjList(edges):
    adj = defaultdict(list)
    for edge in edges:
        src, dst = edge.split("-")
        adj[src].append(dst)
        if src != "start" and dst != "end":
            adj[dst].append(src)
    return adj

def findNumPaths(adj):
    paths = 0
    def pathsHelper(curr, visited):
        nonlocal paths
        if curr == "end":
            paths += 1
            return
        if curr.islower() and not smallCaves and visited[curr] >= 1:
            return
        if curr.islower() and visited[curr] >= 2:
            return
        visited[curr] += 1
        if curr.islower() and visited[curr] == 2:
            smallCaves = False
        for neighbor in adj[curr]:
            pathsHelper(neighbor, visited)
        if visited[curr] == 2:
            smallCaves = True
        visited[curr] -= 1

    pathsHelper("start", defaultdict(int))
    return paths

def solve(file):
    edges = [l.strip() for l in open(file).readlines()]
    adj = createAdjList(edges)
    numPaths = findNumPaths(adj)
    print(f"Number of paths: {numPaths}")

solve("inputs/12small2.txt")