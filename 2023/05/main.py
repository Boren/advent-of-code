seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []

location_to_humidity_map = []
humidity_to_temperature_map = []
temperature_to_light_map = []
light_to_water_map = []
water_to_fertilizer_map = []
fertilizer_to_soil_map = []
soil_to_seed_map = []


def read_map(lines):
    map = []
    reverse_map = []
    for line in lines:
        values = line.split(" ")
        value = int(values[0])
        key = int(values[1])
        rangevalue = int(values[2])

        map.append({"start": key, "end": key + rangevalue, "value": value})
        reverse_map.append({"start": value, "end": value + rangevalue, "value": key})
    return map, reverse_map


def get_value(map, key):
    for entry in map:
        if key >= entry["start"] and key <= entry["end"]:
            return entry["value"] + key - entry["start"]
    return key


def main(inputFile="./input.txt"):
    # Load file
    with open(inputFile, "r") as f:
        lines = f.readlines()

        i = 0

        # Read seeds
        seeds = [int(x) for x in lines[i].split(":")[1].strip().split(" ")]
        i += 2

        # Read seed to soil map
        start = i
        while lines[i].strip() != "":
            i += 1
        seed_to_soil_map, soil_to_seed_map = read_map(lines[start + 1 : i])

        print("Mapped " + str(len(seed_to_soil_map)) + " seeds to soil")

        i += 1

        # Read soil to fertilizer map
        start = i
        while lines[i].strip() != "":
            i += 1
        soil_to_fertilizer_map, fertilizer_to_soil_map = read_map(lines[start + 1 : i])

        print("Mapped " + str(len(soil_to_fertilizer_map)) + " soils to fertilizer")

        i += 1

        # Read fertilizer to water map
        start = i
        while lines[i].strip() != "":
            i += 1
        fertilizer_to_water_map, water_to_fertilizer_map = read_map(
            lines[start + 1 : i]
        )

        print("Mapped " + str(len(fertilizer_to_water_map)) + " fertilizers to water")

        i += 1

        # Read water to light map
        start = i
        while lines[i].strip() != "":
            i += 1
        water_to_light_map, light_to_water_map = read_map(lines[start + 1 : i])

        print("Mapped " + str(len(water_to_light_map)) + " water to light")

        i += 1

        # Read light to temperature map
        start = i
        while lines[i].strip() != "":
            i += 1
        light_to_temperature_map, temperature_to_light_map = read_map(
            lines[start + 1 : i]
        )

        print("Mapped " + str(len(light_to_temperature_map)) + " light to temperature")

        i += 1

        # Read temperature to humidity map
        start = i
        while lines[i].strip() != "":
            i += 1
        temperature_to_humidity_map, humidity_to_temperature_map = read_map(
            lines[start + 1 : i]
        )

        print(
            "Mapped "
            + str(len(temperature_to_humidity_map))
            + " temperature to humidity"
        )

        i += 1

        # Read humidity to location map
        start = i
        while i < len(lines) and lines[i].strip() != "":
            i += 1
        humidity_to_location_map, location_to_humidity_map = read_map(
            lines[start + 1 : i]
        )

        print("Mapped " + str(len(humidity_to_location_map)) + " humidity to location")

        i += 1

        # Find lowest location
        lowest_location = -1

        for seed in seeds:
            print("Seed " + str(seed) + " -> ", end="")

            soil = get_value(seed_to_soil_map, seed)
            print(" Soil " + str(soil) + " -> ", end="")

            fertilizer = get_value(soil_to_fertilizer_map, soil)
            print(" Fertilizer " + str(fertilizer) + " -> ", end="")

            water = get_value(fertilizer_to_water_map, fertilizer)
            print(" Water " + str(water) + " -> ", end="")

            light = get_value(water_to_light_map, water)
            print(" Light " + str(light) + " -> ", end="")

            temperature = get_value(light_to_temperature_map, light)
            print(" Temperature " + str(temperature) + " -> ", end="")

            humidity = get_value(temperature_to_humidity_map, temperature)
            print(" Humidity " + str(humidity) + " -> ", end="")

            location = get_value(humidity_to_location_map, humidity)
            print(" Location " + str(location))

            if lowest_location == -1 or location < lowest_location:
                lowest_location = location

        print(lowest_location)

        print()
        # Part 2 Attempt 2
        print("Part 2 Attempt 2")
        seed_map = []

        for i in range(0, len(seeds), 2):
            seed_map.append(
                {"start": seeds[i], "end": seeds[i] + seeds[i + 1], "value": i}
            )

        i = 0
        found = False

        while True:
            i += 1
            # print("Checking location " + str(i))
            humidity = get_value(location_to_humidity_map, i)
            # if humidity == i:
            #    continue

            temperature = get_value(humidity_to_temperature_map, humidity)
            # if temperature == humidity:
            #    continue

            light = get_value(temperature_to_light_map, temperature)
            # if light == temperature:
            #    continue

            water = get_value(light_to_water_map, light)
            # if water == light:
            #    continue

            fertilizer = get_value(water_to_fertilizer_map, water)
            # if fertilizer == water:
            #    continue

            soil = get_value(fertilizer_to_soil_map, fertilizer)
            # if soil == fertilizer:
            #    continue

            seed = get_value(soil_to_seed_map, soil)
            # if seed == soil:
            #    continue

            # Check if seed number is part of seed_map
            for entry in seed_map:
                if seed >= entry["start"] and seed <= entry["end"]:
                    print("Seed " + str(seed) + " -> ", end="")
                    print(" Soil " + str(soil) + " -> ", end="")
                    print(" Fertilizer " + str(fertilizer) + " -> ", end="")
                    print(" Water " + str(water) + " -> ", end="")
                    print(" Light " + str(light) + " -> ", end="")
                    print(" Temperature " + str(temperature) + " -> ", end="")
                    print(" Humidity " + str(humidity) + " -> ", end="")
                    print(" Location " + str(i))
                    found = True

            if found:
                break

        # Part 2

        print()
        print("Part 2")
        # Find lowest location
        lowest_location_part2 = -1

        for i in range(0, len(seeds), 2):
            for seed in range(seeds[i], seeds[i] + seeds[i + 1]):
                # print("Seed " + str(seed) + " -> ", end="")

                soil = get_value(seed_to_soil_map, seed)
                # print(" Soil " + str(soil) + " -> ", end="")

                fertilizer = get_value(soil_to_fertilizer_map, soil)
                # print(" Fertilizer " + str(fertilizer) + " -> ", end="")

                water = get_value(fertilizer_to_water_map, fertilizer)
                # print(" Water " + str(water) + " -> ", end="")

                light = get_value(water_to_light_map, water)
                # print(" Light " + str(light) + " -> ", end="")

                temperature = get_value(light_to_temperature_map, light)
                # print(" Temperature " + str(temperature) + " -> ", end="")

                humidity = get_value(temperature_to_humidity_map, temperature)
                # print(" Humidity " + str(humidity) + " -> ", end="")

                location = get_value(humidity_to_location_map, humidity)
                # print(" Location " + str(location))

                if lowest_location_part2 == -1 or location < lowest_location_part2:
                    lowest_location_part2 = location

        print(lowest_location_part2)

        return [lowest_location, lowest_location_part2]


if __name__ == "__main__":
    main()
