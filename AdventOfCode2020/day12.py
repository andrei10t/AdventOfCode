def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line[:-1] for line in f.readlines()]


def processInput(input) -> list:
    list = [(a[0], int(a[1:])) for a in input]
    return list


def move1(ins, steps, ox, oy, ds):
    if ins == "N":
        oy += steps
    elif ins == "S":
        oy -= steps
    elif ins == "E":
        ox += steps
    elif ins == "W":
        ox -= steps
    elif ins == "L":
        d = steps / 90
        ds -= d
    elif ins == "R":
        d = steps / 90
        ds += d
    print(ox, oy, ds)
    return ox, oy, ds


def move2(ins, steps, ox, oy):
    dir = ["E", "S", "W", "N"]
    if ins == "N":
        oy += steps
    elif ins == "S":
        oy -= steps
    elif ins == "E":
        ox += steps
    elif ins == "W":
        ox -= steps
    elif ins == "L":
        d = int(steps / 90) % 4
        if d == 0:
            ...
        elif d == 1:
            ox, oy = -1 * oy, ox
        elif d == 2:
            ox, oy = -1 * ox, -1 * oy
        elif d == 3:
            ox, oy = oy, -1 * ox
    elif ins == "R":
        d = int(steps / 90) % 4
        if d == 0:
            ...
        elif d == 1:
            ox, oy = oy, -1 * ox
        elif d == 2:
            ox, oy = -1 * ox, -1 * oy
        elif d == 3:
            ox, oy = -1 * oy, ox
    return ox, oy


def part1(input) -> int:
    dir = ["E", "S", "W", "N"]
    ds = 0
    ox = 0
    oy = 0
    for ins in input:
        if ins[0] == "F":
            ox, oy, ds = move1(dir[int(ds) % 4], ins[1], ox, oy, ds)
        else:
            ox, oy, ds = move1(ins[0], ins[1], ox, oy, ds)
    return abs(ox) + abs(oy)


def part2(input):
    wox = 10
    woy = 1
    sox = 0
    soy = 0
    for ins in input:
        if ins[0] == "F":
            sox += wox * ins[1]
            soy += woy * ins[1]
        else:
            wox, woy = move2(ins[0], ins[1], wox, woy)
    return abs(sox) + abs(soy)


if __name__ == "__main__":
    print(part1(processInput(readFile("in.txt"))))
    print(part2(processInput(readFile("in.txt"))))
