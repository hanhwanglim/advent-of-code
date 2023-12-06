from pathlib import Path

input = Path(__file__).parent / "input.txt"
test = Path(__file__).parent / "test.txt"


def part_1(contents: str):
    lines = contents.split("\n")
    seed_str = lines[0]
    seeds = [int(x.strip()) for x in seed_str[seed_str.find(":") + 1 :].split()]

    i = 1
    while i <= len(lines):
        if lines[i] and lines[i][0].isalpha():
            mapping = []
            i += 1
            while i < len(lines) and lines[i]:
                mapping.append([int(x) for x in lines[i].split()])
                i += 1

            for j, seed in enumerate(seeds):
                for dest_start, src_start, range_len in mapping:
                    if src_start <= seed <= (src_start + range_len):
                        seeds[j] = dest_start + (seed - src_start)
                        break

        i += 1
    return min(seeds)


def part_2(contents: str):
    lines = contents.split("\n")
    seed_str = lines[0]
    seeds = [int(x.strip()) for x in seed_str[seed_str.find(":") + 1 :].split()]

    seeds_range = []
    for i in range(0, len(seeds), 2):
        seeds_range.append((seeds[i], seeds[i] + seeds[i + 1] - 1, ""))
    seeds_range.sort()

    i = 1
    while i <= len(lines):
        if lines[i] and lines[i][0].isalpha():
            mapping = []
            i += 1
            while i < len(lines) and lines[i]:
                mapping.append([int(x) for x in lines[i].split()])
                i += 1
            mapping.sort(key=lambda x: x[1])

            survived_seeds = []
            for seed_start, seed_end, _ in seeds_range:
                for dest_start, src_start, range_len in mapping:
                    if seed_start > seed_end:
                        continue
                    bound_start, bound_end = src_start, src_start + range_len - 1
                    offset = src_start - dest_start
                    if seed_end < bound_start:
                        survived_seeds.append(
                            (seed_start, seed_end, f"s{seed_end} < b{bound_start}")
                        )
                        seed_start = seed_end + 1
                    elif bound_start <= seed_start <= bound_end:
                        survived_seeds.append(
                            (
                                seed_start - offset,
                                min(seed_end - offset, bound_end - offset),
                                f"b{bound_start} < s{seed_start} < b{bound_end}",
                            )
                        )
                        seed_start = min(seed_end, bound_end) + 1
                    elif seed_start <= bound_start <= seed_end:
                        survived_seeds.append(
                            (
                                bound_start - offset,
                                min(bound_end - offset, seed_end - offset),
                                f"s{seed_start} < b{bound_start} < s{seed_end}",
                            )
                        )
                        if seed_start < bound_start:
                            survived_seeds.append(
                                (
                                    seed_start,
                                    bound_start - 1,
                                    f"s{seed_start} < b{bound_start}",
                                )
                            )

                        seed_start = bound_end + 1
                if seed_start <= seed_end and bound_end < seed_start:
                    survived_seeds.append(
                        (seed_start, seed_end, f"b{bound_end} < s{seed_start}")
                    )
            seeds_range = sorted(survived_seeds)

        i += 1

    res = []
    for x, y, _ in seeds_range:
        res.extend([x, y])

    return min(res)


if __name__ == "__main__":
    with open(input) as f:
        contents = f.read()

    print(part_1(contents))
    print(part_2(contents))
