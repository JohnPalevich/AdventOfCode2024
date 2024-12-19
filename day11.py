from collections import defaultdict
import re
from functools import cmp_to_key, lru_cache

test = "testInput/"
real = "input/"
day = "11.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = 0
    stones = [int(v) for v in a[0].split()]
    def blink(stones):
        nStones = []
        for i in range(len(stones)):
            stone = stones[i]
            if stones[i] == 0:
                nStones.append(1)
            elif len(str(stones[i])) % 2 == 0:
                # print(stone)
                lStone = int(str(stones[i])[:len(str(stones[i]))//2])
                rStone = int(str(stones[i])[len(str(stones[i]))//2:])
                nStones.append(lStone)
                nStones.append(rStone)
            else:
                nStones.append(stone*2024)
        # print(nStones)
        return nStones
    
    for i in range(25):
        stones = blink(stones)
    
    return len(stones)

def part2(a):
    tot = 0
    stones = [int(v) for v in a[0].split()]
    target = 75
    @lru_cache(10000000)
    def blink(stone, blinks):
        if blinks == target:
            return 1
        t = 0
        if stone == 0:
            t += blink(1, blinks + 1)   
        elif len(str(stone)) % 2 == 0:
            # print(stone)
            lStone = int(str(stone)[:len(str(stone))//2])
            rStone = int(str(stone)[len(str(stone))//2:])
            t += blink(lStone, blinks+1) + blink(rStone, blinks+1)
        else:
            t+= blink(stone*2024, blinks + 1)
        return t
    
    for stone in stones:
        v = blink(stone, 0)
        tot += v
    
    return tot

testInput = getInput(test+day)
input = getInput(real+day)
# print(part1(testInput))
# print(part1(input))
print(part2(testInput))
print(part2(input))