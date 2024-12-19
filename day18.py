test = "testInput/"
real = "input/"
day = "18.txt"
from collections import Counter
import networkx as nx
import heapq
from heapq import _siftdown
from functools import cmp_to_key, lru_cache


def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a, size, bytes):
    tot= 0
    grid = [["." for i in range(size+1)] for j in range(size+1)]
    
    start = (0,0)
    end = (size, size)
    
    for i in range(bytes):
        j, i = [int(v) for v in a[i].split(",")]
        grid[i][j] = "#"
    N = size+1
    M = size+1
    d = {}
    heap = []
    for i in range(N):
        for j in range(M):
            d[(i,j)] = 99999999999999
            # p[((i,j), dir)] = None
    
    d[start] = 0
    heapq.heappush(heap, (d[start], start))
            
    steps = 0
    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    while len(heap) != 0:
        dist, pos = heapq.heappop(heap)
        if dist > d[pos]:
            continue
        if pos == end:
            break
    
        # print(pos, steps, d[(pos,dir)], end=", ")
        for nDir in dirs:
            i = pos[0]+nDir[0]
            j = pos[1]+nDir[1]
            
            if 0 <= i < N and 0 <= j < M and grid[i][j] != "#":
                newDist = dist + 1
                if newDist < d[(i,j)]:
                    d[(i,j)] = newDist
                    heapq.heappush(heap, (newDist, (i,j)))
        steps+=1
    print(d)
    for l in grid:
        print(l)
    
    return d[end]

def part2(a, size, bytes):
    tot= 0
    
    def search(bytes):
        grid = [["." for i in range(size+1)] for j in range(size+1)]
        for i in range(bytes):
            j, i = [int(v) for v in a[i].split(",")]
            grid[i][j] = "#"
        
        start = (0,0)
        end = (size, size)
        N = size+1
        M = size+1
        d = {}
        heap = []
        for i in range(N):
            for j in range(M):
                d[(i,j)] = 99999999999999
        
        d[start] = 0
        heapq.heappush(heap, (d[start], start))
                
        steps = 0
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        while len(heap) != 0:
            dist, pos = heapq.heappop(heap)
            if dist > d[pos]:
                continue
            if pos == end:
                break
        
            # print(pos, steps, d[(pos,dir)], end=", ")
            for nDir in dirs:
                i = pos[0]+nDir[0]
                j = pos[1]+nDir[1]
                
                if 0 <= i < N and 0 <= j < M and grid[i][j] != "#":
                    newDist = dist + 1
                    if newDist < d[(i,j)]:
                        d[(i,j)] = newDist
                        heapq.heappush(heap, (newDist, (i,j)))
            steps+=1
        return d[end]
    
    while search(bytes) != 99999999999999:
        bytes+=1
        print(bytes)
    
    return a[bytes-1]

testInput = getInput(test+day)
input = getInput(real+day)
# print(part1(testInput, 6, 12))
# print(part1(input, 70, 1024))
print(part2(testInput, 6, 12))
print(part2(input, 70, 1024))