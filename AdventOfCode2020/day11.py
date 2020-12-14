def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line[:-1] for line in f.readlines()]


def getN1(input, x, y):
    neigh = list()
    ns = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for my, mx in ns:
        if 0 <= (y + my) < len(input) and 0 <= (x + mx) < len(input[0]):
            neigh.append(input[y + my][x + mx])
    return neigh


def do_step(input, getN):
    changed = False
    matrix = [[0 for i in range(len(input))] for j in range(len(input[0]))]
    print(len(matrix), len(matrix[0]))
    for y, line in enumerate(input):
        for x, index in enumerate(line):
            if (
                index == "L"
                and len(list(filter(lambda x: x == "#", getN(input, x, y)))) == 0
            ):
                matrix[x][y] = "#"
                changed = True
            elif (
                index == "#"
                and len(list(filter(lambda x: x == "#", getN(input, x, y)))) >= 5
            ):
                matrix[x][y] = "L"
                changed = True
            else:
                print(x, y)
                matrix[x][y] = index
    return matrix, changed


def getN2(input, x, y):
    neigh = list()
    ns = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for ny, nx in ns:
        c = "."
        cx, cy = (x + nx), (y + ny)
        while 0 <= cy < len(input) and 0 <= cx < len(input[0]) and c == ".":
            c = input[cy][cx]
            cx, cy = (cx + nx), (cy + ny)
        neigh.append(c)
    return neigh


def part1(input) -> int:
    changed = True
    while changed:
        input, changed = do_step(input, getN1)
    return len([x for y in input for x in y if x == "#"])


def part2(input) -> int:
    changed = True
    while changed:
        input, changed = do_step(input, getN2)
    return len([x for y in input for x in y if x == "#"])


if __name__ == "__main__":
    # print(part1(readFile("test.txt")))
    print(part2(readFile("in.txt")))
