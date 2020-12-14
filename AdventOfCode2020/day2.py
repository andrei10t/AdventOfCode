from utils import sub, get_input


def readFile() -> list:
    input = list()
    with open("in.txt", "r") as f:
        for line in f.readlines():
            txt = line.split()
            nums = txt[0].split("-")
            input.append((int(nums[0]), int(nums[1]), txt[1][:1], txt[2]))
    return input


def part1(list) -> int:
    valid = 0
    for item in list:
        count = 0
        c = item[2]
        for char in item[3]:
            if char == c:
                count += 1
        if count >= item[0] and count <= item[1]:
            valid += 1
    return valid


def part2(list) -> int:
    valid = 0
    for item in list:
        pos1 = item[0]
        pos2 = item[1]
        c = item[2]
        w = item[3]

        if (
            w[pos1 - 1] == c
            and w[pos2 - 1] != c
            or w[pos1 - 1] != c
            and w[pos2 - 1] == c
        ):
            valid += 1
    return valid


if __name__ == "__main__":
    get_input()
    sub(part1(readFile()), "a")
    sub(part2(readFile()), "b")
