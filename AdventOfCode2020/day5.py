def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line[:-1] for line in f.readlines()]


def processInput(input) -> list:
    return [
        int(
            line.replace("F", "0")
            .replace("B", "1")
            .replace("R", "1")
            .replace("L", "0"),
            2,
        )
        for line in input
    ]


def part1(input) -> int:
    return max(input)


def part2(input) -> int:
    for i in range(min(input), max(input)):
        if i not in input and i - 1 in input and i + 1 in input:
            return i


if __name__ == "__main__":
    print(part1(processInput(readFile("in.txt"))))
    print(part2(processInput(readFile("in.txt"))))
