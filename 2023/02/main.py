from dataclasses import dataclass
import functools
from typing import List

MAXIMUM_RED_CUBES = 12
MAXIMUM_GREEN_CUBES = 13
MAXIMUM_BLUE_CUBES = 14


@dataclass
class Draw:
    red: int
    green: int
    blue: int
    sum: int


@dataclass
class Game:
    gameid: int
    draws: List[Draw]


def isGamePossible(game: Game):
    possible = True

    for draw in game.draws:
        if (
            draw.red > MAXIMUM_RED_CUBES
            or draw.blue > MAXIMUM_BLUE_CUBES
            or draw.green > MAXIMUM_GREEN_CUBES
        ):
            possible = False
            break

    return possible


def lowestNumberPossible(game: Game):
    lowestred = 0
    lowestgreen = 0
    lowestblue = 0

    for draw in game.draws:
        if draw.red > lowestred:
            lowestred = draw.red
        if draw.green > lowestgreen:
            lowestgreen = draw.green
        if draw.blue > lowestblue:
            lowestblue = draw.blue

    return lowestred * lowestgreen * lowestblue


def parseGame(gamestring: str) -> Game:
    gamestring = gamestring.split(":")
    gameid = int(gamestring[0].split(" ")[1])

    draws: List[Draw] = []

    for drawstring in gamestring[1].split(";"):
        draw = Draw(0, 0, 0, 0)

        for single_draw in drawstring.rstrip().lstrip().split(", "):
            split = single_draw.split(" ")
            count = int(split[0])
            color = split[1]

            if color == "red":
                draw.red = count
            elif color == "green":
                draw.green = count
            elif color == "blue":
                draw.blue = count

            draw.sum += count

        draws.append(draw)

    return Game(gameid, draws)


def main(inputFile="input.txt"):
    games: List[Game] = []

    # Load file
    with open(inputFile, "r") as f:
        lines = f.readlines()

        for line in lines:
            games.append(parseGame(line))

    possibleGames: List[Game] = []

    for game in games:
        if isGamePossible(game):
            possibleGames.append(game)

    part1sum = functools.reduce(
        lambda a, b: a + b, map(lambda game: game.gameid, possibleGames)
    )
    print("Part 1: " + str(part1sum))

    part2sum = functools.reduce(
        lambda a, b: a + b, map(lambda game: lowestNumberPossible(game), games)
    )

    print("Part 2: " + str(part2sum))

    return [part1sum, part2sum]


if __name__ == "__main__":
    main()
