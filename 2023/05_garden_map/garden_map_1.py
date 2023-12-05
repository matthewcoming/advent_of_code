# Matthew Coming
# Advent of Code 2023

# --- Day 5: If You Give A Seed A Fertilizer ---

# You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

# "A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

# "Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.

# "I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"

# You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble making sense of it."

# The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

# For example:

# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4

# The almanac starts by listing which seeds need to be planted: seeds 79, 14, 55, and 13.

# The rest of the almanac contains a list of maps which describe how to convert numbers from a source category into numbers in a destination category. That is, the section that starts with seed-to-soil map: describes how to convert a seed number (the source) to a soil number (the destination). This lets the gardener and his team know which soil to use with which seeds, which water to use with which fertilizer, and so on.

# Rather than list every source number and its corresponding destination number one by one, the maps describe entire ranges of numbers that can be converted. Each line within a map contains three numbers: the destination range start, the source range start, and the range length.

# Consider again the example seed-to-soil map:

# 50 98 2
# 52 50 48

# The first line has a destination range start of 50, a source range start of 98, and a range length of 2. This line means that the source range starts at 98 and contains two values: 98 and 99. The destination range is the same length, but it starts at 50, so its two values are 50 and 51. With this information, you know that seed number 98 corresponds to soil number 50 and that seed number 99 corresponds to soil number 51.

# The second line means that the source range starts at 50 and contains 48 values: 50, 51, ..., 96, 97. This corresponds to a destination range starting at 52 and also containing 48 values: 52, 53, ..., 98, 99. So, seed number 53 corresponds to soil number 55.

# Any source numbers that aren't mapped correspond to the same destination number. So, seed number 10 corresponds to soil number 10.

# So, the entire list of seed numbers and their corresponding soil numbers looks like this:

# seed  soil
# 0     0
# 1     1
# ...   ...
# 48    48
# 49    49
# 50    52
# 51    53
# ...   ...
# 96    98
# 97    99
# 98    50
# 99    51

# With this map, you can look up the soil number required for each initial seed number:

#     Seed number 79 corresponds to soil number 81.
#     Seed number 14 corresponds to soil number 14.
#     Seed number 55 corresponds to soil number 57.
#     Seed number 13 corresponds to soil number 13.

# The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

#     Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
#     Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
#     Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
#     Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

# So, the lowest location number in this example is 35.

# What is the lowest location number that corresponds to any of the initial seed numbers?


def create_mapping_lookup(maps: list) -> function:
    # returns a function that takes a number and returns the mapped number
    # given a list of dest-range-start, source-range-start, and range-length maps
    # in the input argument maps

    # for example, given the following map:
    # 50 98 2
    # 52 50 48
    # the returned function would take a number and return the mapped number
    # 98 -> 50

    

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.readlines()

    seeds = lines[0].split(":")[1].split()
    
    # gitub copilot wrote like half of this repetative boilerplate 

    # get seed-to-soil map
    seed_to_soil = []
    for line in lines[1:]:
        if line == "\n":
            break
        seed_to_soil.append(list(map(int, line.split())))
        

    # get soil-to-fertilizer map
    soil_to_fertilizer = []
    for line in lines[lines.index("soil-to-fertilizer map:\n") + 1:]:
        if line == "\n":
            break
        soil_to_fertilizer.append(list(map(int, line.split())))

    # get fertilizer-to-water map
    fertilizer_to_water = []
    for line in lines[lines.index("fertilizer-to-water map:\n") + 1:]:
        if line == "\n":
            break
        fertilizer_to_water.append(list(map(int, line.split())))

    # get water-to-light map
    water_to_light = []
    for line in lines[lines.index("water-to-light map:\n") + 1:]:
        if line == "\n":
            break
        water_to_light.append(list(map(int, line.split())))

    # get light-to-temperature map
    light_to_temperature = []
    for line in lines[lines.index("light-to-temperature map:\n") + 1:]:
        if line == "\n":
            break
        light_to_temperature.append(list(map(int, line.split())))

    # get temperature-to-humidity map
    temperature_to_humidity = []
    for line in lines[lines.index("temperature-to-humidity map:\n") + 1:]:
        if line == "\n":
            break
        temperature_to_humidity.append(list(map(int, line.split())))

    # get humidity-to-location map
    humidity_to_location = []
    for line in lines[lines.index("humidity-to-location map:\n") + 1:]:
        if line == "\n":
            break
        humidity_to_location.append(list(map(int, line.split())))


    # NOW i be coding

    # get soil number
    for map in seed_to_soil:
        if seed_number in range(map[1], map[1] + map[2]):
            soil_number = 