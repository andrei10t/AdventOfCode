def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [int(number) for number in f.read().split(",")]


def solve(input, pos) -> list:
    d = dict()
    for i, nr in enumerate(input):
        d[nr] = [i + 1]
    last = input[-1]

    for i in range(len(input), pos + 2):
        if len(d[last]) == 1:
            d[0].append(i + 1)
            last = 0

        else:
            last = d[last][-1] - d[last][-2]
            try:
                d[last].append(i + 1)
            except KeyError:
                l = [i + 1]
                d[last] = l

    for key in d:
        if pos in d[key]:
            return key


def part1(input) -> int:
    return solve(input, 2020)


def part2(input) -> int:
    return solve(input, 30000000)


if __name__ == "__main__":
    print(part1(readFile("in.txt")))
    print(part2(readFile("in.txt")))
