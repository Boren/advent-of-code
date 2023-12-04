from functools import reduce


def main(inputFile="./input.txt"):
    # Load file
    with open(inputFile, "r") as f:
        lines = f.readlines()

        total_score = 0

        for line in lines:
            score = 0

            numbers = line.split(":")[1].split("|")
            winning_numbers = set(
                map(lambda x: int(x), numbers[0].strip().replace("  ", " ").split(" "))
            )
            numbers_you_have = map(
                lambda x: int(x), numbers[1].strip().replace("  ", " ").split(" ")
            )

            for number in numbers_you_have:
                if number in winning_numbers:
                    if score == 0:
                        score = 1
                    else:
                        score *= 2

            total_score += score

        print(total_score)

        # Part 2
        cards = {x: 1 for x in range(1, len(lines) + 1)}

        for index, line in enumerate(lines):
            print(
                "Card " + str(index + 1) + " has " + str(cards[index + 1]) + " copies"
            )

            matches = 0

            numbers = line.split(":")[1].split("|")
            winning_numbers = set(
                map(lambda x: int(x), numbers[0].strip().replace("  ", " ").split(" "))
            )
            numbers_you_have = map(
                lambda x: int(x), numbers[1].strip().replace("  ", " ").split(" ")
            )

            for number in numbers_you_have:
                if number in winning_numbers:
                    matches += 1

            print("Card " + str(index + 1) + " has " + str(matches) + " matches")

            for i in range(cards[index + 1]):
                for j in range(1, matches + 1):
                    cards[index + j + 1] += 1

            print()

        total_cards = reduce(lambda a, b: a + b, cards.values())

        print(total_cards)

        return [total_score, total_cards]


if __name__ == "__main__":
    main()
