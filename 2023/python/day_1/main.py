from pathlib import Path

input = Path(__file__).parent / "input.txt"
test = Path(__file__).parent / "test.txt"

NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def part_1(contents: str) -> int:
    total = 0

    for line in contents.split("\n"):
        l, r = 0, len(line) - 1
        while not line[l].isnumeric():
            l += 1
        while not line[r].isnumeric():
            r -= 1
        total += int(line[l] + line[r])

    return total


def part_2(contents: str) -> int:
    total = 0

    for line in contents.split("\n"):
        l, r = None, None

        for i, c in enumerate(line):
            if c.isnumeric():
                l = c if l is None else l
                r = c
                continue

            for j, number in enumerate(NUMBERS):
                if number.startswith(c) and line[i : i + len(number)] == number:
                    l = str(j + 1) if l is None else l
                    r = str(j + 1)
                    break

        total += int(l + r)

    return total


if __name__ == "__main__":
    with open(input) as f:
        contents = f.read()

    print(part_1(contents))
    print(part_2(contents))
