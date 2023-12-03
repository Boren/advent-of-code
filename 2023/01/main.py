# NOTE: This is a bit cheaty, but it works and I'm tired.
string_to_number = {
    "zero": "ze0o",
    "one": "o1e",
    "two": "t2o",
    "three": "th3ee",
    "four": "f4ur",
    "five": "f5ve",
    "six": "s6x",
    "seven": "s7ven",
    "eight": "e8ght",
    "nine": "n9ne",
}


def replace_text_numbers(line):
    for key, value in string_to_number.items():
        if line.startswith(key):
            line = line.replace(key, str(value), 1)
            return line, True
    return line, False


def main(inputFile="input.txt"):
    sum = 0

    # Load file
    with open(inputFile, "r") as f:
        lines = f.readlines()

        for line in lines:
            i = 0
            while i < len(line):
                for i in range(len(line)):
                    replaced_line, replaced = replace_text_numbers(line[i:])
                    line = line[:i] + replaced_line
                    if replaced:
                        i = 0
                        break
                    i += 1

            for char in line:
                try:
                    first = int(char)
                    break
                except ValueError:
                    pass

            for char in reversed(line):
                try:
                    last = int(char)
                    break
                except ValueError:
                    pass

            combined = int(str(first) + str(last))
            sum += combined

    print(sum)
    return sum


if __name__ == "__main__":
    main()
