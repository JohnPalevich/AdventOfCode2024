test = "testInput/"
real = "input/"
day = "16.txt"
from collections import Counter
import networkx as nx
import heapq
from heapq import _siftdown

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = 0
    N = len(a)
    M = len(a[0])
    s = (0,0)
    e = (0,0)
    p = {}
    d = {}
    heap = []
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    for i in range(N):
        for j in range(M):
            if a[i][j] == "E":
                e = (i,j)
            for dir in dirs:
                d[((i,j), dir)] = 99999999999999
                p[((i,j), dir)] = None
            if a[i][j] == "S":
                s = (i,j)
                d[((i,j), dirs[1])] = 0
                heapq.heappush(heap, (d[((i,j), dirs[1])], (i,j), dirs[1]))
            
    steps = 0
    while len(heap) != 0:
        dist, pos, dir = heapq.heappop(heap)
        if dist > d[(pos, dir)]:
            continue
        if pos == e:
            break
    
        # print(pos, steps, d[(pos,dir)], end=", ")
        for nDir in dirs:
            i = pos[0]+nDir[0]
            j = pos[1]+nDir[1]
            
            if a[i][j] != "#" and not (dir[0]+nDir[0] == 0 and dir[1]+nDir[1] == 0):
                newDist = dist + 1 if dir == nDir else dist + 1001
                if newDist < d[((i,j), nDir)]:
                    d[((i,j), nDir)] = newDist
                    p[((i,j), nDir)] = pos
                    heapq.heappush(heap, (newDist, (i,j), nDir))
        steps+=1
    return min([d[(e,dir)] for dir in dirs])

def part2(a):
    tot = 0
    
    def doPart1(a):
        N = len(a)
        M = len(a[0])
        s = (0,0)
        e = (0,0)
        p = {}
        d = {}
        heap = []
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        for i in range(N):
            for j in range(M):
                if a[i][j] == "E":
                    e = (i,j)
                for dir in dirs:
                    d[((i,j), dir)] = 99999999999999
                    p[((i,j), dir)] = None
                if a[i][j] == "S":
                    s = (i,j)
                    d[((i,j), dirs[1])] = 0
                    heapq.heappush(heap, (d[((i,j), dirs[1])], (i,j), dirs[1]))
        if s == (0,0) or e==(0,0):
            return 999999999, 0,0
                
        steps = 0
        fD = 0
        while len(heap) != 0:
            dist, pos, dir = heapq.heappop(heap)
            if dist > d[(pos, dir)]:
                continue
            if pos == e:
                fD = dir
                break
            
            # print(pos, steps, d[(pos,dir)], end=", ")
            for nDir in dirs:
                i = pos[0]+nDir[0]
                j = pos[1]+nDir[1]
                
                if a[i][j] != "#" and not (dir[0]+nDir[0] == 0 and dir[1]+nDir[1] == 0):
                    newDist = dist + 1 if dir == nDir else dist + 1001
                    if newDist < d[((i,j), nDir)]:
                        p[((i,j), nDir)] = (pos, dir)
                        d[((i,j), nDir)] = newDist
                        heapq.heappush(heap, (newDist, (i,j), nDir))
            steps+=1
        if fD == 0:
            return 999999999, 0, 0
        return d[(e,fD)], p, (e,fD)
    
    bestDist, p, e = doPart1(a)
    tilesInPath = set()
    while e != None:
        tilesInPath.add(e[0])
        if e not in p.keys():
            break
        e = p[e]
    
    for tile in tilesInPath.copy():
        a[tile[0]] = a[tile[0]][:tile[1]]+"#"+a[tile[0]][tile[1]+1:]
        nDist, p, e = doPart1(a)
        a[tile[0]] = a[tile[0]][:tile[1]]+"."+a[tile[0]][tile[1]+1:]
        if nDist != bestDist:
            continue
        else: 
            while e != None:
                tilesInPath.add(e[0])
                if e not in p.keys():
                    break
                e = p[e]

    return len(tilesInPath)


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))