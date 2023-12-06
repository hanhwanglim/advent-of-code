from pathlib import Path

input = Path(__file__).parent / "input.txt"
test = Path(__file__).parent / "test.txt"


def part_1(contents: str):
    lines = contents.split("\n")

    data = []
    for line in lines:
        data.append([int(x) for x in line[line.find(":") + 1 :].split()])

    product = 1
    for time, distance in zip(data[0], data[1]):
        for i in range(time):
            if ((time - i) * i) > distance:
                break
        product *= (time - i) - (i) + 1
    return product


def part_2(contents: str):
    lines = contents.split("\n")

    time_str = lines[0]
    distance_str = lines[1]
    time = int("".join(time_str[time_str.find(":") + 1 :].split()))
    distance = int("".join(distance_str[distance_str.find(":") + 1 :].split()))

    for i in range(time):
        if ((time - i) * i) > distance:
            break
    return (time - i) - (i) + 1


if __name__ == "__main__":
    with open(input) as f:
        contents = f.read()

    print(part_1(contents))
    print(part_2(contents))
