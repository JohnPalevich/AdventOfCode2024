test = "testInput/"
real = "input/"
day = "19.txt"
from functools import lru_cache

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = 0
    towels = {towel.strip() for towel in a[0].split(",")}
    
    def isPossible(remDes):
        if remDes == "":
            return True
        else:
            for towel in towels:
                if remDes.startswith(towel):
                    if isPossible(remDes[len(towel):]):
                        return True
        return False
    
    for i in range(2,len(a)):
        des = a[i]
        tot += 1 if isPossible(des) else 0        
    
    return tot

def part2(a):
    tot= 0
    towels = {towel.strip() for towel in a[0].split(",")}
    
    @lru_cache
    def isPossible(remDes):
        if remDes == "":
            return 1
        else:
            tot = 0
            for towel in towels:
                if remDes.startswith(towel):
                    tot += isPossible(remDes[len(towel):])
            return tot
                    
    for i in range(2,len(a)):
        des = a[i]
        tot += isPossible(des)
        
    return tot

testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))