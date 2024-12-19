test = "testInput/"
real = "input/"
day = "2.txt"
from collections import Counter

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = 0
    for line in a:
        p = ""
        inc, dec, safe = True, True, True
        for c in line.split():
            c = int(c)
            if p == "":
                p = c
            else:
                if p > c:
                    dec = False
                elif p < c: 
                    inc = False
                elif p == c:
                    inc, dec = False, False
                if not (1 <= abs(p - c) <=3):
                    # print(p, c, abs(p-c))
                    safe = False  
            p = c 
        # print(inc, dec, safe,  (inc or dec) and safe)
        tot += 1 if (inc or dec) and safe else 0                
    return tot


def helper(line):
    p = ""
    inc, dec, safe = True, True, True
    for c in line:
        c = int(c)
        if p == "":
            p = c
        else:
            if p > c:
                dec = False
            elif p < c: 
                inc = False
            elif p == c:
                inc, dec = False, False
            if not (1 <= abs(p - c) <=3):
                # print(p, c, abs(p-c))
                safe = False  
        p = c 
    return (inc or dec) and safe

def part2(a):
    tot = 0
    for line in a:
        line = line.split()
        if helper(line):
            tot += 1
        else:
            for i in range(len(line)):
                if helper(line[:i]+line[i+1:]):
                    tot+=1
                    break
    return tot


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))