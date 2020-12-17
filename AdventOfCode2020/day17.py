def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line[:-1] for line in f.readlines()]


def solve(input) -> list:
    ...


def part1(input) -> int:
    active = set()
    for i, line in enumerate(input):
        for j, ch in enumerate(line):
            if ch == "#":
                active.add((i, j, 0, 0))

    neigh = [(x, y, z) for x in [-1, 0, 1] for y in [-1, 0, 1] for z in [-1, 0, 1]]
    neigh.remove((0, 0, 0))

    for _ in range(6):
        new_active = set()
        for x in range(-14, 14):
            for y in range(-14, 14):
                for z in range(-10, 10):
                    numneig = 0
                    for n in neigh:
                        if (x + n[0], y + n[1], z + n[2]) in active:
                            numneig += 1
                    if numneig in [2, 3] and (x, y, z) in active:
                        new_active.add((x, y, z))
                    elif numneig == 3 and (x, y, z) not in active:
                        new_active.add((x, y, z))
        active = new_active
    return len(active)


def part2(input) -> int:
    active = set()
    for i, line in enumerate(input):
        for j, ch in enumerate(line):
            if ch == "#":
                active.add((i, j, 0, 0))

    neigh = [
        (x, y, z, w)
        for x in [-1, 0, 1]
        for y in [-1, 0, 1]
        for z in [-1, 0, 1]
        for w in [-1, 0, 1]
    ]
    neigh.remove((0, 0, 0, 0))

    for _ in range(6):
        new_active = set()
        for x in range(-14, 14):
            for y in range(-14, 14):
                for z in range(-10, 10):
                    for w in range(-10, 10):
                        numneig = 0
                        for n in neigh:
                            if (x + n[0], y + n[1], z + n[2], w + n[3]) in active:
                                numneig += 1
                        if numneig in [2, 3] and (x, y, z, w) in active:
                            new_active.add((x, y, z, w))
                        elif numneig == 3 and (x, y, z, w) not in active:
                            new_active.add((x, y, z, w))
        active = new_active
    return len(active)


if __name__ == "__main__":
    print(part1(readFile("in.txt")))
    print(part2(readFile("in.txt")))
