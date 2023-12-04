# Matthew Coming
# Advent of Code 2023

# --- Part Two ---

# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

import re

int_to_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


if __name__ == "__main__":
    # get lines of input
    with open("input.txt") as f:
        content = f.readlines() 
    
    # setup 2d array
    numbers = [[] for _ in range(len(content))]
    calibrations = []

    # for each line
    for idx, line in enumerate(content):
        # filter its integers
        matches = [m for m in re.finditer(
            # search whole numbers
            # ?= lookaheads, e.g. find oneight as one and eight
            '(?=one)|'
            '(?=two)|'
            '(?=three)|'
            '(?=four)|'
            '(?=five)|'
            '(?=six)|'
            '(?=seven)|'
            '(?=eight)|'
            '(?=nine)|'
            # # searches digits
            '([0-9])', line)]

        # For each match
        for integer in [matches[0], matches[-1]]:
            start = integer.start()
            end = integer.end()
            # collcet the  "word" number matches ... end === start because of lookahead
            if end == start:
                for word, val in int_to_num.items():
                    # if the word matches, add the value to numbers
                    if word[0:3] == line[start:start+3]:
                        numbers[idx].append(val)
            
            # collect the digits
            if end - start == 1:
                numbers[idx].append(int(line[start]))
            print(numbers[idx][-1])
            
        # store first and last as a 2 digit base 10 number
        calibrations.append(10*numbers[idx][0] + numbers[idx][-1])

    print(sum(calibrations)) 