from dataclasses import dataclass
from typing import List


@dataclass
class Hand:
    cards: str
    bid: int
    score: 0
    scorepart2: 0


ranks = {
    "A": "14",
    "K": "13",
    "Q": "12",
    "J": "11",
    "T": "10",
    "9": "09",
    "8": "08",
    "7": "07",
    "6": "06",
    "5": "05",
    "4": "04",
    "3": "03",
    "2": "02",
}

ranks2 = {
    "A": "14",
    "K": "13",
    "Q": "12",
    "J": "01",
    "T": "10",
    "9": "09",
    "8": "08",
    "7": "07",
    "6": "06",
    "5": "05",
    "4": "04",
    "3": "03",
    "2": "02",
}


def parse_hands(lines):
    hands: List[Hand] = []

    for line in lines:
        cards, bid = line.strip().split()
        hands.append(Hand(cards.strip(), int(bid.strip()), 0, 0))

    return hands


def get_score(hand):
    score = ""

    card_count = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "J": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
    }

    for card in hand.cards:
        card_count[card] += 1

    card_count_list = sorted(card_count.items(), key=lambda item: item[1], reverse=True)

    if card_count_list[0][1] == 5:
        score += "7"
    elif card_count_list[0][1] == 4:
        score += "6"
    elif card_count_list[0][1] == 3 and card_count_list[1][1] == 2:
        score += "5"
    elif card_count_list[0][1] == 3:
        score += "4"
    elif card_count_list[0][1] == 2 and card_count_list[1][1] == 2:
        score += "3"
    elif card_count_list[0][1] == 2:
        score += "2"
    else:
        score += "1"

    for card in hand.cards:
        score += str(ranks[card])

    return int(score)


def get_score2(hand):
    score = ""

    card_count = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
    }

    jokers = 0

    for card in hand.cards:
        if card == "J":
            jokers += 1
        else:
            card_count[card] += 1

    card_count_list = sorted(card_count.items(), key=lambda item: item[1], reverse=True)

    print(card_count_list)

    if card_count_list[0][1] >= (5 - jokers):
        score += "7"
    elif card_count_list[0][1] >= (4 - jokers):
        score += "6"
    elif card_count_list[0][1] >= 3 and card_count_list[1][1] >= 2:
        score += "5"
    elif card_count_list[0][1] >= (3 - jokers) and card_count_list[1][1] >= 2:
        score += "5"
    elif card_count_list[0][1] >= 3 and card_count_list[1][1] >= (2 - jokers):
        score += "5"
    elif card_count_list[0][1] >= (3 - jokers):
        score += "4"
    elif card_count_list[0][1] >= 2 and card_count_list[1][1] >= 2:
        score += "3"
    elif card_count_list[0][1] >= (2 - jokers) and card_count_list[1][1] >= 2:
        score += "3"
    elif card_count_list[0][1] >= 2 and card_count_list[1][1] >= (2 - jokers):
        score += "3"
    elif card_count_list[0][1] >= (2 - jokers):
        score += "2"
    else:
        score += "1"

    for card in hand.cards:
        score += str(ranks2[card])

    return int(score)


def main(inputFile="./input.txt"):
    # Load file
    with open(inputFile, "r") as f:
        lines = f.readlines()

        hands = parse_hands(lines)

        # Part 1
        part1 = 0

        for hand in hands:
            hand.score = get_score(hand)
            hand.scorepart2 = get_score2(hand)

        hands.sort(key=lambda x: x.score)

        for idx, hand in enumerate(hands):
            print(
                "Rank idx: "
                + str(idx + 1)
                + " Bid: "
                + str(hand.bid)
                + " Score: "
                + str(hand.score)
                + " Hand: "
                + str(hand.cards)
            )
            part1 += hand.bid * (idx + 1)

        print(hands)

        print("Part 1 answer: " + str(part1))
        print()

        # Part 2
        part2 = 0

        hands.sort(key=lambda x: x.scorepart2)

        for idx, hand in enumerate(hands):
            print(
                "Rank idx: "
                + str(idx + 1)
                + " Bid: "
                + str(hand.bid)
                + " Score: "
                + str(hand.scorepart2)
                + " Hand: "
                + str(hand.cards)
            )
            part2 += hand.bid * (idx + 1)

        # print(hands)

        print("Part 2 answer: " + str(part2))

        return [part1, part2]


if __name__ == "__main__":
    main()
