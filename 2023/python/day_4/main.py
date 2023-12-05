from pathlib import Path

input = Path(__file__).parent / "input.txt"
test = Path(__file__).parent / "test.txt"


def part_1(contents: str):
    total = 0

    for line in contents.split("\n"):
        s = line[line.find(":") + 1 :]
        group_1, group_2 = s.split("|")
        set_1 = {x.strip() for x in group_1.split()}
        set_2 = {x.strip() for x in group_2.split()}

        intersection = set_1 & set_2

        points = 1
        for _ in range(1, len(intersection)):
            points *= 2
        total += points if intersection else 0

    return total


def part_2(contents: str):
    lines = contents.split("\n")
    total = [1] * len(lines)

    for i in range(len(total)):
        line = lines[i]
        s = line[line.find(":") + 1 :]
        group_1, group_2 = s.split("|")
        set_1 = {x.strip() for x in group_1.split()}
        set_2 = {x.strip() for x in group_2.split()}

        intersection = set_1 & set_2

        for _ in range(total[i]):
            for j in range(i + 1, i + 1 + len(intersection)):
                total[j] += 1

    return sum(total)


if __name__ == "__main__":
    with open(input) as f:
        contents = f.read()

    print(part_1(contents))
    print(part_2(contents))
