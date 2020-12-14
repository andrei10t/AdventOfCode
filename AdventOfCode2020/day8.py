def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line.split() for line in f.read().strip().split("\n")]


def run(input) -> tuple:
    visited = [0] * len(input)
    acc, i = 0, 0
    visited[0] = 1
    while visited[i] != 2:
        if input[i][0] == "acc":
            acc += int(input[i][1])
            i += 1
        elif input[i][0] == "jmp":
            i += int(input[i][1])
        else:
            i += 1
        try:
            visited[i] += 1
        except IndexError:
            return i, acc
    return i, acc


def part1(input) -> int:
    return run(input)[1]


def part2(input) -> int:
    for i, line in enumerate(input):
        if line[0] == "nop":
            input[i][0] = "jmp"
            pointer, acc = run(input)
            input[i][0] = "nop"

        elif line[0] == "jmp":
            input[i][0] = "nop"
            pointer, acc = run(input)
            input[i][0] = "jmp"
        else:
            continue
        if pointer == len(input):
            return acc


if __name__ == "__main__":
    # print(part1(readFile("test.txt")))
    # print(part1(readFile("in.txt")))
    print(part2(readFile("in.txt")))
    # part2()
