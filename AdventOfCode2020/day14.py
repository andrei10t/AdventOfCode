def readFile(filename) -> list:
    with open(filename, "r") as f:
        return [line[:-1] for line in f.readlines()]


def processInput(input) -> list:
    ...


def dec_to_sbin(dec):
    bits = []
    while dec != 0:
        bits.append(str(dec % 2))
        dec = dec // 2

    bits.reverse()
    s = ""
    s = s.join(bits)

    while len(s) != 36:
        s = "0" + s
    return s


def sbin_to_dec(b):
    while b[0] == "0":
        b = b[1:]

    dec = 0
    for i in range(len(b)):
        j = len(b) - i - 1
        dec += int(b[j]) * (2 ** i)

    return dec


def part1(input) -> int:
    d = dict()
    mask = ""
    for line in input:
        txt = line.split()
        if txt[0] == "mask":
            mask = txt[2]
        else:
            res = ""
            bits = dec_to_sbin(int(txt[2]))
            for i, m in zip(bits, mask):
                if m == "X":
                    res += i
                else:
                    res += m
            d[txt[0][4:-1]] = sbin_to_dec(res)
    s = 0
    for key in d:
        s += d[key]
    return s


def gen_addr(sbin, l: list) -> list:
    if "X" not in sbin:
        return sbin

    xi = sbin.index("X")
    s0 = sbin[:xi] + "0" + sbin[xi + 1 :]
    s1 = sbin[:xi] + "1" + sbin[xi + 1 :]

    l.append(gen_addr(s0, l))
    l.append(gen_addr(s1, l))

    return l


def part2(input):
    d = dict()
    mask = ""
    for line in input:
        txt = line.split()
        if txt[0] == "mask":
            mask = txt[2]
        else:
            res = ""
            bits = dec_to_sbin(int(txt[0][4:-1]))
            for i, m in zip(bits, mask):
                if m == "X":
                    res += "X"
                elif m == "1":
                    res += "1"
                else:
                    res += i
            l = gen_addr(res, list())
            addrlist = [elem for elem in l if isinstance(elem, str)]
            for bitadd in addrlist:
                d[sbin_to_dec(bitadd)] = int(txt[2])
    s = 0
    for key in d:
        s += d[key]
    return s


if __name__ == "__main__":
    print(part1(readFile("in.txt")))
    print(part2(readFile("in.txt")))
