from pathlib import Path

input = Path(__file__).parent / "input.txt"
test = Path(__file__).parent / "test.txt"


def part_1(contents: str):
    symbols = "+*-#@/&%=$"
    data = [list(line) for line in contents.split("\n")]

    def dfs(i, j):
        count = 0

        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if (x, y) == (i, j):
                    continue
                while y > 0 and data[x][y].isnumeric() and data[x][y - 1].isnumeric():
                    y -= 1
                number = ""
                while y < len(data[0]) and data[x][y].isnumeric():
                    number += data[x][y]
                    data[x][y] = "."
                    y += 1

                if number != "":
                    count += int(number)

        return count

    total = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] in symbols:
                total += dfs(i, j)

    return total


def part_2(contents: str):
    data = [list(line) for line in contents.split("\n")]

    def dfs(i, j):
        count = 0
        product = 1

        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if (x, y) == (i, j):
                    continue
                while y > 0 and data[x][y].isnumeric() and data[x][y - 1].isnumeric():
                    y -= 1
                number = ""
                while y < len(data[0]) and data[x][y].isnumeric():
                    number += data[x][y]
                    data[x][y] = "."
                    y += 1

                if number != "":
                    count += 1
                    product *= int(number)

        return product if count > 1 else 0

    total = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "*":
                total += dfs(i, j)

    return total


if __name__ == "__main__":
    with open(input) as f:
        contents = f.read()

    print(part_1(contents))
    print(part_2(contents))
