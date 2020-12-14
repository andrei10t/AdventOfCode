def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line[:-1] for line in f.readlines()]


def listStringToListInt(input) -> list:
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


def part1(input) -> int:
    input.sort()
    sol = [0, 0, 1]
    cur = 0
    for num in input:
        sol[num - cur - 1] += 1
        cur = num
    return sol[0] * sol[2]


def part2(input) -> int:
    input.append(0)
    input.append(max(input) + 3)
    input.sort()
    dp = [0] * (max(input) + 1)
    dp[0] = 1
    for elem in input:
        for step in range(1, 4):
            if (elem - step) in input:
                dp[elem] += dp[elem - step]
    return dp[-1]


if __name__ == "__main__":
    # print(part1(listStringToListInt(readFile("in.txt"))))
    print(part2(listStringToListInt(readFile("in.txt"))))
