from dataclasses import dataclass
from typing import List


@dataclass
class Race:
    duration: int
    record: int


def parse_races(lines):
    races: List[Race] = []

    durations = [
        int(x.strip())
        for x in " ".join(lines.pop(0).split()).split(":")[1].strip().split(" ")
    ]
    records = [
        int(x.strip())
        for x in " ".join(lines.pop(0).split()).split(":")[1].strip().split(" ")
    ]

    for duration, record in zip(durations, records):
        races.append(Race(duration, record))

    print(races)

    return races


def main(inputFile="./input.txt"):
    # Load file
    with open(inputFile, "r") as f:
        lines = f.readlines()

        races = parse_races(lines)

        # Part 1
        part1 = 1

        for race in races:
            # Distance defined as distance = speed * (duration - speed)
            # Find lowest limit
            # TODO: Fix brute force solution
            lower_limit = 0
            upper_limit = 0
            for s in range(0, race.duration):
                if s * (race.duration - s) > race.record:
                    lower_limit = s
                    break

            # Find upper limit
            for s in range(race.duration, 0, -1):
                if s * (race.duration - s) > race.record:
                    upper_limit = s
                    break

            part1 *= (upper_limit - lower_limit) + 1

        print("Part 1 answer: " + str(part1))

        # Part 2
        part2 = 0

        # Combine races
        duration = int("".join(str(x.duration) for x in races))
        record = int("".join(str(x.record) for x in races))

        lower_limit = 0
        upper_limit = 0
        for s in range(0, duration):
            if s * (duration - s) > record:
                lower_limit = s
                break

        # Find upper limit
        for s in range(duration, 0, -1):
            if s * (duration - s) > record:
                upper_limit = s
                break

        part2 = (upper_limit - lower_limit) + 1

        print("Part 2 answer: " + str(part2))

        return [part1, part2]


if __name__ == "__main__":
    main()
