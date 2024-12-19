from collections import defaultdict
import re
from functools import cmp_to_key, lru_cache

test = "testInput/"
real = "input/"
day = "12.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    visited = set()
    tot = 0
    areas = defaultdict(list)
    perims = defaultdict(list)
    N = len(a)
    M = len(a[0])
    dirs = [(0,1),(0,-1),(-1,0),(1,0)]

    def explorePlot(i,j):
        q = {(i,j)}
        while len(q) != 0:
            loc = q.pop()
            if loc not in visited:
                adj = 4
                i,j = loc
                for dir in dirs:
                    if 0 <= i + dir[0] < N and 0<= j+dir[1] < M and a[i+dir[0]][j+dir[1]] == a[i][j]:
                        adj -= 1
                        q.add((i+dir[0], j+dir[1]))
                areas[a[i][j]][-1] += 1
                perims[a[i][j]][-1] += adj
                visited.add(loc)

    for i in range(N):
        for j in range(M):
            if (i,j) not in visited:
                areas[a[i][j]].append(0)
                perims[a[i][j]].append(0)
                explorePlot(i,j)
            
    # print(areas)
    # print(perims)
    for plotType in areas.keys():
        for i in range(len(areas[plotType])):
            tot += perims[plotType][i] *  areas[plotType][i]

    return tot

def part2(a):
    visited = set()
    tot = 0
    areas = defaultdict(list)
    sides = defaultdict(list)
    N = len(a)
    M = len(a[0])
    dirs = [(0,1),(0,-1),(-1,0),(1,0)]

    def explorePlot(i,j):
        q = {(i,j)}
        vSides = defaultdict(set)
        while len(q) != 0:
            loc = q.pop()
            if loc not in visited:
                i,j = loc
                # adjs = []
                for dir in dirs:
                    if 0 <= i + dir[0] < N and 0<= j+dir[1] < M and a[i+dir[0]][j+dir[1]] == a[i][j]:
                        q.add((i+dir[0], j+dir[1]))
                    else:
                        vSides[dir].add((i,j))  
                areas[a[i][j]][-1] += 1
                visited.add(loc)
        s = 0  

        for dir in dirs:
            perimiter = vSides[dir]
            while len(perimiter) != 0:
                s += 1
                adjs = {perimiter.pop()}
                movement = dir[0] != 0 # Used to differ between if we're looking for a horz or vertical side
                while len(adjs) != 0:
                        v = adjs.pop()
                        adj1 = (v[0], v[1] - 1) if movement else (v[0]-1, v[1])
                        adj2 = (v[0], v[1] + 1) if movement else (v[0]+1, v[1])
                        for adj in [adj1, adj2]:
                            if adj in perimiter:
                                perimiter.remove(adj)
                                adjs.add(adj)
        sides[a[i][j]][-1] = s
        
    #
    #xx
    #  x
    for i in range(N):
        for j in range(M):
            if (i,j) not in visited:
                areas[a[i][j]].append(0)
                sides[a[i][j]].append(0)
                explorePlot(i,j)
            
    # print("areas:", areas)
    # print("sides:", sides)
    for plotType in areas.keys():
        for i in range(len(areas[plotType])):
            tot += sides[plotType][i] *  areas[plotType][i]

    return tot

testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))