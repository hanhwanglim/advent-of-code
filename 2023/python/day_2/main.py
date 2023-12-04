import re
from collections import Counter
from pathlib import Path

input = Path(__file__).parent / "input.txt"
test = Path(__file__).parent / "test.txt"


def part_1(contents: str):
    constraint = {"red": 12, "green": 13, "blue": 14}
    total = 0

    for line in contents.split("\n"):
        game_id = int(re.match("Game (\d+)", line).groups()[0])
        round_string = line[line.find(":") + 1 :]
        impossible = False

        for round in round_string.split(";"):
            counter = Counter()

            for cube_string in round.split(","):
                s = cube_string.strip()
                count, color = re.match("(\d+) (\w+)", s).groups()
                counter[color] += int(count)

            for color, count in counter.items():
                if count > constraint[color]:
                    impossible = True
                    break

        if not impossible:
            total += game_id

    return total


def part_2(contents: str):
    total = 0

    for line in contents.split("\n"):
        round_string = line[line.find(":") + 1 :]
        game_counter = Counter()

        for round in round_string.split(";"):
            round_counter = Counter()

            for cube_string in round.split(","):
                s = cube_string.strip()
                count, color = re.match("(\d+) (\w+)", s).groups()
                round_counter[color] += int(count)

            for color, count in round_counter.items():
                game_counter[color] = max(game_counter[color], count)

        product = 1
        for count in game_counter.values():
            product *= count
        total += product

    return total


if __name__ == "__main__":
    with open(input) as f:
        contents = f.read()

    print(part_1(contents))
    print(part_2(contents))
