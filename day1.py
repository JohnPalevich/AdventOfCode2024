test = "testInput/"
real = "input/"
day = "1.txt"
from collections import Counter

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    l = []
    r = []
    for line in a:
        s = line.split("   ")
        l.append(int(s[0]))
        r.append(int(s[1]))
    l = sorted(l)
    r = sorted(r)
    tot = 0
    for i in range(len(l)):
    
        # print(abs(l[i]-r[i]))
        tot += abs(l[i]-r[i])
    return tot

def part2(a):
    l = []
    r = []
    for line in a:
        s = line.split("   ")
        l.append(int(s[0]))
        r.append(int(s[1]))
    r = Counter(r)
    tot = 0
    for v in l:
        tot += v * r[v]
    return tot


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(testInput))
print(part2(input))