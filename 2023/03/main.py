import re


def main(inputFile="./input.txt"):
    # Load file
    with open(inputFile, "r") as f:
        lines = f.readlines()

        width = len(lines[0].strip())
        height = len(lines)

        print("Width: " + str(width))
        print("Height: " + str(height))
        print()

        adjacent_map = [[False for x in range(width)] for y in range(height)]

        # Step 1: Create a new boolean map which shows which locations are adjacent to a symbol
        row = 0
        for line in lines:
            for i in range(len(line.strip())):
                if line[i] not in [
                    ".",
                    "0",
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                ]:
                    adjacent_map[row][i] = True
                    if row > 0:
                        adjacent_map[row - 1][i] = True
                    if row < height - 1:
                        adjacent_map[row + 1][i] = True
                    if i > 0:
                        adjacent_map[row][i - 1] = True
                    if i < width - 1:
                        adjacent_map[row][i + 1] = True
                    if row > 0 and i > 0:
                        adjacent_map[row - 1][i - 1] = True
                    if row > 0 and i < width - 1:
                        adjacent_map[row - 1][i + 1] = True
                    if row < height - 1 and i > 0:
                        adjacent_map[row + 1][i - 1] = True
                    if row < height - 1 and i < width - 1:
                        adjacent_map[row + 1][i + 1] = True
            row += 1

        for line in lines:
            print(line.strip())

        print()

        for line in adjacent_map:
            for char in line:
                if char:
                    print("#", end="")
                else:
                    print(".", end="")
            print()

        print()

        # Step 2: Extract numbers and check if any of the digit locations are true in the boolean map
        part_map = [
            [{"id": -1, "part": -1} for x in range(width)] for y in range(height)
        ]

        numbers = []
        row = 0
        for line in lines:
            matches = re.finditer(r"\d+", line.strip())

            for match in matches:
                start = match.start()
                end = match.end()
                for i in range(start, end):
                    if adjacent_map[row][i]:
                        number = int(line[start:end])
                        numbers.append(number)

                        # NOTE: This is a part 2 only thing
                        for i in range(match.start(), match.end()):
                            part_map[row][i] = {
                                "id": str(number) + "-" + str(row) + "-" + str(start),
                                "part": number,
                            }

                        break

            row += 1

        print()
        print("Part 1: " + str(sum(numbers)))

        print()

        for line in part_map:
            for char in line:
                if char == -1:
                    print(".", end="")
                else:
                    print("#", end="")
            print()

        # Step 3: Check part number map
        gear_ratio = 0
        row = 0
        for line in lines:
            col = 0
            for char in line:
                if char == "*":
                    adjacent_part_count = 0
                    adjacent_part_numbers = []
                    adjacent_part_ids = []
                    # Search every direction in part map
                    # Left
                    if col > 0 and part_map[row][col - 1]["id"] != -1:
                        adjacent_part = part_map[row][col - 1]
                        if adjacent_part["id"] not in adjacent_part_ids:
                            adjacent_part_count += 1
                            adjacent_part_numbers.append(adjacent_part["part"])
                            adjacent_part_ids.append(adjacent_part["id"])

                    # Right
                    if col < width and part_map[row][col + 1]["id"] != -1:
                        adjacent_part = part_map[row][col + 1]
                        if adjacent_part["id"] not in adjacent_part_ids:
                            adjacent_part_count += 1
                            adjacent_part_numbers.append(adjacent_part["part"])
                            adjacent_part_ids.append(adjacent_part["id"])

                    # Up
                    if row > 0 and part_map[row - 1][col]["id"] != -1:
                        adjacent_part = part_map[row - 1][col]
                        if adjacent_part["id"] not in adjacent_part_ids:
                            adjacent_part_count += 1
                            adjacent_part_numbers.append(adjacent_part["part"])
                            adjacent_part_ids.append(adjacent_part["id"])

                    # Down
                    if row < height and part_map[row + 1][col]["id"] != -1:
                        adjacent_part = part_map[row + 1][col]
                        if adjacent_part["id"] not in adjacent_part_ids:
                            adjacent_part_count += 1
                            adjacent_part_numbers.append(adjacent_part["part"])
                            adjacent_part_ids.append(adjacent_part["id"])

                    # Diagonals
                    # Up left
                    if row > 0 and col > 0 and part_map[row - 1][col - 1]["id"] != -1:
                        adjacent_part = part_map[row - 1][col - 1]
                        if adjacent_part["id"] not in adjacent_part_ids:
                            adjacent_part_count += 1
                            adjacent_part_numbers.append(adjacent_part["part"])
                            adjacent_part_ids.append(adjacent_part["id"])

                    # Up right
                    if (
                        row > 0
                        and col < width
                        and part_map[row - 1][col + 1]["id"] != -1
                    ):
                        adjacent_part = part_map[row - 1][col + 1]
                        if adjacent_part["id"] not in adjacent_part_ids:
                            adjacent_part_count += 1
                            adjacent_part_numbers.append(adjacent_part["part"])
                            adjacent_part_ids.append(adjacent_part["id"])

                    # Down left
                    if (
                        row < height
                        and col > 0
                        and part_map[row + 1][col - 1]["id"] != -1
                    ):
                        adjacent_part = part_map[row + 1][col - 1]
                        if adjacent_part["id"] not in adjacent_part_ids:
                            adjacent_part_count += 1
                            adjacent_part_numbers.append(adjacent_part["part"])
                            adjacent_part_ids.append(adjacent_part["id"])

                    # Down right
                    if (
                        row < height
                        and col < width
                        and part_map[row + 1][col + 1]["id"] != -1
                    ):
                        adjacent_part = part_map[row + 1][col + 1]
                        if adjacent_part["id"] not in adjacent_part_ids:
                            adjacent_part_count += 1
                            adjacent_part_numbers.append(adjacent_part["part"])
                            adjacent_part_ids.append(adjacent_part["id"])

                    if adjacent_part_count == 2:
                        gear_ratio += (
                            adjacent_part_numbers[0] * adjacent_part_numbers[1]
                        )
                col += 1
            row += 1

        print()
        print("Part 2: " + str(gear_ratio))

        return [sum(numbers), gear_ratio]


if __name__ == "__main__":
    main()
