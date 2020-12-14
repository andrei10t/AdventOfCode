from functools import reduce


def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line[:-1] for line in f.readlines()]


def processInput1(input) -> list:
    l = list()
    se = set()
    for line in input:
        if not line:
            l.append(se)
            se = set()
        else:
            for ch in line:
                se.add(ch)

    return l


def processInput2(input) -> list:
    result = list()
    biglist = list()
    l = list()
    for line in input:
        if not line:
            biglist.append(l)
            l = list()
        else:
            l.append(line)

    for l in biglist:
        s = set()
        for char in l[0]:
            allyes = True
            for string in l:
                if char not in string:
                    allyes = False
            if allyes:
                s.add(char)
        result.append(s)
    return result


def part(input) -> int:
    return reduce(lambda x, y: x + y, list(map(lambda x: len(x), input)))


if __name__ == "__main__":
    print(part(processInput1(readFile("in.txt"))))
    print(part(processInput2(readFile("in.txt"))))
