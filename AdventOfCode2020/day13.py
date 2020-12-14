def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line[:-1] for line in f.readlines()]


def processInput(input) -> tuple:
    return int(input[0]), [nr for nr in input[1].split(",")]


def part1(input) -> int:
    l = {}
    for i in input[1]:
        if i != "x":
            l[i] = (1 + int(input[0] / int(i))) * int(i) - input[0]

    h = min(l, key=l.get)

    return int(l[h]) * int(h)


def part2(input) -> int:
    rems = list()
    for i, e in enumerate(input[1]):
        rem = -i
        if e != "x":
            while rem < 0:
                rem += int(e)
            rems.append(rem)
    print(rems)
    # https://www.dcode.fr/chinese-remainder
    return 0


if __name__ == "__main__":
    print(part1(processInput(readFile("in.txt"))))
    print(part2(processInput(readFile("in.txt"))))
