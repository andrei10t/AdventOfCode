def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line[:-1] for line in f.readlines()]


def processInput(input) -> dict:

    mainDict = {}
    for line in input:
        txt = line.split()
        mainC = txt[0] + " " + txt[1]
        dict = {}
        i = 4
        while i < len(txt):
            try:
                nr = int(txt[i])
                bag = txt[i + 1] + " " + txt[i + 2]
                dict[bag] = nr
                i += 4
            except ValueError:
                i += 4
        mainDict[mainC] = dict
    return mainDict


def part1(input) -> int:
    bags = {"shiny gold"}
    changed = True
    while changed:
        changed = False
        for rule in input:
            if rule not in bags:
                for bag in input[rule]:
                    if bag in bags:
                        bags.add(rule)
                        changed = True
    # because we count the shiny bag too, which does not contain shiny bags
    return len(bags) - 1


def ncontains(input, color):
    if not input[color]:
        return 0
    else:
        c = 0
        for bag in input[color]:
            print(bag)
            c += input[color][bag] * ncontains(input, bag) + input[color][bag]
            print(c)

    return c


def part2(input) -> int:
    return ncontains(input, "shiny gold")


if __name__ == "__main__":
    print(part1(processInput(readFile("in.txt"))))
    print(part2(processInput(readFile("in.txt"))))
