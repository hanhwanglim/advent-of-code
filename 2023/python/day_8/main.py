import math
from pathlib import Path

input = Path(__file__).parent / "input.txt"
test = Path(__file__).parent / "test.txt"


def part_1(contents: str):
    lines = contents.split("\n")
    instructions = lines[0]

    mapping = {}

    for line in lines[2:]:
        start, end = line.split(" = ")
        mapping[start] = tuple(end[1:-1].split(", "))

    element = "AAA"
    idx = 0
    count = 0
    while element != "ZZZ":
        instruction = 0 if instructions[idx % len(instructions)] == "L" else 1
        element = mapping[element][instruction]
        idx += 1
        count += 1

    return count


def part_2(contents: str):
    lines = contents.split("\n")
    instructions = lines[0]

    mapping = {}
    elements = []

    for line in lines[2:]:
        start, end = line.split(" = ")
        mapping[start] = tuple(end[1:-1].split(", "))

        if "A" == start[-1]:
            elements.append(start)

    for i, element in enumerate(elements):
        idx, count = 0, 0
        while element[-1] != "Z":
            instruction = 0 if instructions[idx % len(instructions)] == "L" else 1
            element = mapping[element][instruction]
            idx += 1
            count += 1
        elements[i] = count

    return math.lcm(*elements)


if __name__ == "__main__":
    with open(input) as f:
        contents = f.read()

    print(part_1(contents))
    print(part_2(contents))
