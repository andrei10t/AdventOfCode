def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line.split() for line in f.read().strip().split("\n")]


def processInput(input) -> list:
    return list(map(int, ("".join(x) for x in input)))


def isValid(input, position, preamble) -> bool:
    target = input[position]
    se = set()
    for i in range(position - preamble - 1, position):
        if target - input[i] in se:
            return True
        else:
            se.add(input[i])
    return False


def subArraySum(arr, n, sum) -> tuple:
    curr_sum = arr[0]
    start = 0
    i = 1
    while i <= n:
        while curr_sum > sum and start < i - 1:
            curr_sum = curr_sum - arr[start]
            start += 1

        if curr_sum == sum:
            return start, i - 1

        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1

    print("No subarray found")
    return 0


def part1(input, preamble) -> int:
    for i in range(preamble, len(input)):
        if not isValid(input, i, preamble):
            return input[i]
        else:
            ...


def part2(input) -> int:
    start, stop = subArraySum(input, len(input), 85848519)
    list = input[start : stop + 1]
    return min(list) + max(list)


if __name__ == "__main__":
    print(part1(processInput(readFile("in.txt")), 25))
    print(part2(processInput(readFile("in.txt"))))
