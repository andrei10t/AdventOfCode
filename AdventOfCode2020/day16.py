from collections import namedtuple
from typing import List


def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line[:-1] for line in f.readlines() if len(line[:-1]) != 0]


Rule = namedtuple("Rule", ["name", "firstlow", "firsthigh", "secondlow", "secondhigh"])


def processInput(input):
    get_ticket = False
    get_nearby = False
    myticket = list()
    tickets = list()
    rules = list()
    for line in input:
        if get_ticket:
            myticket = [int(x) for x in line.split(",")]
            get_ticket = False
        elif "your ticket" in line:
            get_ticket = True
        elif "nearby tickets" in line:
            get_nearby = True
        elif get_nearby:
            tickets.append([int(x) for x in line.split(",")])
        else:
            fl = int(line.split()[-3].split("-")[0])
            fh = int(line.split()[-3].split("-")[1])
            sl = int(line.split()[-1].split("-")[0])
            sh = int(line.split()[-1].split("-")[1])
            name = line.split(":")[0]
            rules.append(Rule(name, fl, fh, sl, sh))
    return rules, myticket, tickets


def parts(input) -> int:
    rules, myticket, tickets = input
    p1 = 0
    p2 = 1
    valid_matrix = [[True for _ in range(20)] for _ in range(20)]
    assigned = [False for _ in range(20)]
    sol = [None for _ in range(20)]

    for tic in tickets:
        valid_tic = True
        for nr in tic:
            valid = False
            for rule in rules:
                if (
                    rule.firstlow <= nr <= rule.firsthigh
                    or rule.secondlow <= nr <= rule.secondhigh
                ):
                    valid = True
                    break
            if not valid:
                p1 += nr
                valid_tic = False
        if valid_tic:
            for i, nr in enumerate(tic):
                for j, rule in enumerate(rules):
                    if not (
                        rule.firstlow <= nr <= rule.firsthigh
                        or rule.secondlow <= nr <= rule.secondhigh
                    ):
                        valid_matrix[i][j] = False
    while None in sol:
        for i in range(len(rules)):
            valid_fields = [
                j
                for j in range(len(myticket))
                if valid_matrix[i][j] and not assigned[j]
            ]
            if len(valid_fields) == 1:
                sol[i] = valid_fields[0]
                assigned[valid_fields[0]] = True

    for index, field in enumerate(sol):
        if field < 6:
            p2 *= myticket[index]

    print("part1 ", p1)
    print("part2", p2)


if __name__ == "__main__":
    parts(processInput(readFile("in.txt")))
