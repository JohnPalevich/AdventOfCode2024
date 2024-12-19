from collections import Counter
import re

test = "testInput/"
real = "input/"
day = "3.txt"

def getInput(test):
    f = open(test, "r")
    a = f.readlines()
    f.close()
    # print(a)
    for i in range(len(a)):
        a[i] = a[i].rstrip("\n")
    return a

def part1(a):
    tot = 0
    reg = "mul\(\d+\,\d+\)"
    for line in a:
        matches = re.findall(reg,line)
        for match in matches:
            spl = match.split(",")
            n1 = int(spl[0].split("(")[1])
            n2 = int(spl[1].split(")")[0])
            tot += n1*n2
    return tot


def part2(a):
    tot = 0
    reg = "do\(\)|mul\(\d+\,\d+\)|don\'t\(\)"
    en = True
    for line in a:
        matches = re.findall(reg,line)
        for match in matches:
            if match == "do()":
                en = True
            elif match == "don't()":
                en = False
            elif en:
                spl = match.split(",")
                n1 = int(spl[0].split("(")[1])
                n2 = int(spl[1].split(")")[0])
                tot += n1*n2
    return tot


testInput = getInput(test+day)
input = getInput(real+day)
print(part1(testInput))
print(part1(input))
print(part2(["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]))
print(part2(input))