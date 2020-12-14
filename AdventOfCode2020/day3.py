def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line[:-1] for line in f.readlines()]


def readtest() -> list:
    input = list()
    with open("test.txt", "r") as f:
        for line in f.readlines():
            input.append(line)
    return input


def part1(file):
    counter = check(3, 1, file)
    return counter


def check(x, y, input):
    counter = 0
    xs = 0
    ys = 0
    mod = len(input[0])
    while ys < len(input) - 1:
        xs = (xs + x) % mod
        ys += y
        print(xs)
        print(ys)
        if input[ys][xs] == "#":
            counter += 1
    print("c" + str(counter))
    return counter


def part2(input):
    result = (
        check(1, 1, input)
        * check(3, 1, input)
        * check(5, 1, input)
        * check(7, 1, input)
        * check(1, 2, input)
    )
    return result


if __name__ == "__main__":
    # print(part1(readFile("in.txt")))
    print(part2(readFile("in.txt")))
