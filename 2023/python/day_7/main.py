from collections import Counter
from pathlib import Path

input = Path(__file__).parent / "input.txt"
test = Path(__file__).parent / "test.txt"

mapping = {"T": "B", "J": "1", "Q": "D", "K": "E", "A": "F"}


def sorter(x: str):
    s = ""
    for i in x:
        s += mapping.get(i, i)
    return s


def part_1(contents: str):
    lines = contents.split("\n")

    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for line in lines:
        card, bid = line.split()
        card_count = Counter(card).most_common()

        if card_count[0][1] == 5:
            five_of_a_kind.append((sorter(card), bid, card))
        elif card_count[0][1] == 4:
            four_of_a_kind.append((sorter(card), bid, card))
        elif card_count[0][1] == 3 and card_count[1][1] == 2:
            full_house.append((sorter(card), bid, card))
        elif card_count[0][1] == 3:
            three_of_a_kind.append((sorter(card), bid, card))
        elif card_count[0][1] == 2 and card_count[1][1] == 2:
            two_pair.append((sorter(card), bid, card))
        elif card_count[0][1] == 2:
            one_pair.append((sorter(card), bid, card))
        else:
            high_card.append((sorter(card), bid, card))

    product = 0
    i = len(lines)
    for kind in (
        five_of_a_kind,
        four_of_a_kind,
        full_house,
        three_of_a_kind,
        two_pair,
        one_pair,
        high_card,
    ):
        kind.sort(key=sorter, reverse=True)
        for k in kind:
            product += int(k[1]) * i
            i -= 1
    return product


def part_2(contents: str):
    lines = contents.split("\n")

    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for line in lines:
        card, bid = line.split()
        counter = Counter(card)
        joker_count = counter.get("J", 0)
        counter_without_joker = counter.copy()
        del counter_without_joker["J"]
        card_count = counter_without_joker.most_common()

        if joker_count == 0:
            if card_count[0][1] == 5:
                five_of_a_kind.append((sorter(card), bid, card))
            elif card_count[0][1] == 4:
                four_of_a_kind.append((sorter(card), bid, card))
            elif card_count[0][1] == 3 and card_count[1][1] == 2:
                full_house.append((sorter(card), bid, card))
            elif card_count[0][1] == 3:
                three_of_a_kind.append((sorter(card), bid, card))
            elif card_count[0][1] == 2 and card_count[1][1] == 2:
                two_pair.append((sorter(card), bid, card))
            elif card_count[0][1] == 2:
                one_pair.append((sorter(card), bid, card))
            else:
                high_card.append((sorter(card), bid, card))
            continue

        if joker_count == 5:
            five_of_a_kind.append((sorter(card), bid, card))
        elif card_count[0][1] + joker_count == 5:
            five_of_a_kind.append((sorter(card), bid, card))
        elif card_count[0][1] + joker_count == 4:
            four_of_a_kind.append((sorter(card), bid, card))
        elif (
            len(card_count) > 1
            and joker_count == 1
            and (card_count[0][1] == 2 and card_count[1][1] == 2)
        ):
            full_house.append((sorter(card), bid, card))
        elif len(card_count) > 1 and card_count[0][1] + joker_count == 3:
            three_of_a_kind.append((sorter(card), bid, card))
        elif (
            len(card_count) > 1
            and joker_count == 1
            and card_count[0][1] == 2
            and card_count[1][1] == 1
        ):
            two_pair.append((sorter(card), bid, card))
        elif card_count[0][1] + joker_count == 2:
            one_pair.append((sorter(card), bid, card))

    product = 0
    i = len(lines)
    for kind in (
        five_of_a_kind,
        four_of_a_kind,
        full_house,
        three_of_a_kind,
        two_pair,
        one_pair,
        high_card,
    ):
        kind.sort(key=sorter, reverse=True)
        for k in kind:
            product += int(k[1]) * i
            i -= 1
    return product


if __name__ == "__main__":
    with open(input) as f:
        contents = f.read()

    print(part_1(contents))
    print(part_2(contents))
