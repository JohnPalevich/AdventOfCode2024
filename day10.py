from collections import defaultdict
import re
from functools import cmp_to_key

test = "testInput/"
real = "input/"
day = "10.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = 0
    g = []
    N = len(a)
    M = len(a[0])
    trailheads = []
    for i in range(N):
        nl = []
        for j in range(M):
            nl.append(a[i][j])
            if a[i][j] == "0":
                trailheads.append((i, j))
        g.append(nl)
                
    # print(trailheads)
    
    
    def exploreTrail(loc):
        if g[loc[0]][loc[1]] == "9":
            return {loc}
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        t = set()
        for dir in dirs:
            nLoc = (loc[0]+dir[0], loc[1]+dir[1])
            if  0 <= nLoc[0] < N and 0 <= nLoc[1] < M and g[nLoc[0]][nLoc[1]] == ".":
                continue
            elif 0 <= nLoc[0] < N and 0 <= nLoc[1] < M and int(g[nLoc[0]][nLoc[1]]) == (int(g[loc[0]][loc[1]]) + 1):
                t.update(exploreTrail(nLoc))
        return t
        
    
    
    for trailhead in trailheads:
        tot += len(exploreTrail(trailhead))
    
    return tot

def part2(a):
    tot = 0
    g = []
    N = len(a)
    M = len(a[0])
    trailheads = []
    for i in range(N):
        nl = []
        for j in range(M):
            nl.append(a[i][j])
            if a[i][j] == "0":
                trailheads.append((i, j))
        g.append(nl)
                
    # print(trailheads)
    
    
    def exploreTrail(loc):
        if g[loc[0]][loc[1]] == "9":
            return 1
        dirs = [(0,1),(0,-1),(-1,0),(1,0)]
        t = 0
        for dir in dirs:
            nLoc = (loc[0]+dir[0], loc[1]+dir[1])
            if  0 <= nLoc[0] < N and 0 <= nLoc[1] < M and g[nLoc[0]][nLoc[1]] == ".":
                continue
            elif 0 <= nLoc[0] < N and 0 <= nLoc[1] < M and int(g[nLoc[0]][nLoc[1]]) == (int(g[loc[0]][loc[1]]) + 1):
                t += exploreTrail(nLoc)
        return t
        
    
    
    for trailhead in trailheads:
        trails = exploreTrail(trailhead)
        tot += trails
    
    return tot

testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))