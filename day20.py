test = "testInput/"
real = "input/"
day = "20.txt"
from collections import *
from functools import *
import heapq

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def dijkstra(racetrack, N, M, start, end):
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    d = {}
    p = {}
    for i in range(N):
        for j in range(M):
            d[(i,j)] = 99999999999999
    
    
    heap = []
    d[start] = 0
    heapq.heappush(heap, (d[start], start))
            
    steps = 0
    while len(heap) != 0:
        dist, pos = heapq.heappop(heap)
        if dist > d[pos]:
            continue
        if pos == end:
            break
    
        for nDir in dirs:
            i = pos[0]+nDir[0]
            j = pos[1]+nDir[1] 
            if 0 <= i < N and 0 <= j < M and racetrack[i][j] != "#":
                newDist = dist + 1
                if newDist < d[(i,j)]:
                    d[(i,j)] = newDist
                    p[(i,j)] = pos
                    heapq.heappush(heap, (newDist, (i,j)))
        steps+=1
    return d, p

def part1(a):
    tot = 0
    racetrack = []
    N = len(a)
    M = len(a[0])
    start = (0,0)
    end = (0,0)
    for i in range(N):
        row = []
        for j in range(M):
            row.append(a[i][j])
            if a[i][j] == "S":
                start = (i,j)
            if a[i][j] == "E":
                end = (i,j)
        racetrack.append(row)
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    
    def calcNewPos(pos, dir):
        return (pos[0]+dir[0], pos[1]+dir[1])
    
    def isInBounds(pos):
        return 0 <= pos[0] < N and 0 <= pos[1] < M
        
    d, path = dijkstra(racetrack, N, M, start, end)
    def savings(start, cheat):
        return d[cheat[-1]] - d[start] + 2
    
    seenCheats = set()
    
    def findCheats(pos):
        cheatsForPos = Counter()
        for d1 in dirs:
            np1 = calcNewPos(pos, d1)
            if isInBounds(np1) and racetrack[np1[0]][np1[1]] == "#":
                for d2 in dirs:
                    np2 = calcNewPos(np1, d2)
                    if isInBounds(np2):
                        if racetrack[np2[0]][np2[1]] != "#" and np2 != pos and (np1,np2) not in seenCheats:
                            s = savings(pos, (np1, np2)) * -1
                            if s > 0:
                                cheatsForPos[s] += 1
                            seenCheats.add((np1, np2))
                                    
        return cheatsForPos

    scores = Counter()
    
    for pos in path.keys():
        scores.update(findCheats(pos))
           
    tot = 0
    return sum([scores[v] for v in scores if v > 99])

def part2(a, limit):
    tot = 0
    
    racetrack = []
    N = len(a)
    M = len(a[0])
    start = (0,0)
    end = (0,0)
    for i in range(N):
        row = []
        for j in range(M):
            row.append(a[i][j])
            if a[i][j] == "S":
                start = (i,j)
            if a[i][j] == "E":
                end = (i,j)
        racetrack.append(row)    
    
    d, path = dijkstra(racetrack, N, M, start, end)
    
    def savings(start, end, cheatLen):
        return d[end] - d[start] + cheatLen

    def dist(p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    
    def findCheats(start):
        cheatsForPos = Counter()
        
        for i in range(N):
            for j in range(M):
                if racetrack[i][j] != "#":
                    d = dist(start, (i,j))
                    if d <= 20:
                        s = savings(start, (i,j), d) * -1
                        if s > limit:
                            cheatsForPos[s] += 1
                
        return cheatsForPos

    scores = Counter()
    
    for pos in path.keys():
        scores.update(findCheats(pos))
    
    return sum([scores[v] for v in scores])


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput, 49))
print(part2(input, 99))