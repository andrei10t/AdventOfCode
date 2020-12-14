import re


def readFile(filename) -> list:
    result = list()
    with open(filename, "r") as f:
        for line in f.read()[:-1].split("\n\n"):
            result.append(dict(d.split(":") for d in line.replace("\n", " ").split()))
    return result


def assert_fields(data: dict) -> bool:
    return all((k in data for k in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")))


def part1(input) -> int:
    return len(input)


def part2(input) -> int:
    c = 0
    rules = {
        "byr": "19[2-9][0-9]|200[0-2]",
        "iyr": "20(1[0-9]|20)",
        "eyr": "20(2[0-9]|30)",
        "hgt": "1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in",
        "hcl": "#[0-9a-f]{6}",
        "ecl": "amb|blu|brn|gry|grn|hzl|oth",
        "pid": "[0-9]{9}",
        "cid": ".*",
    }
    for elem in input:
        if all(re.fullmatch(rules[ch], elem[ch]) for ch in elem):
            c += 1
    return c


if __name__ == "__main__":
    vals = readFile("in.txt")
    valid_passes = [val for val in vals if assert_fields(val)]
    print(part2(valid_passes))
    # print(part1(processInput(readFile("in.txt")),25))
    # print(part2(processInput(readFile("in.txt"))))
