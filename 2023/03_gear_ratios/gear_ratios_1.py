# Matthew Coming
# Advent of Code 2023


# --- Day 3: Gear Ratios ---

# You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

# It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

# "Aaah!"

# You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

# The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

# The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

# Here is an example engine schematic:

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

# In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

import re

special_chars = ['%', '/', '#', '-', '+', '&', '=', '$', '*', '@']

def extract_part_number_from_block(lines):
    """
    extract the part number from a block of lines

    ......#...
    617*......
    .....+.58.

    returns [617]

    """

    middle_block = lines[1]
    part_numbers = []
    # for each number in line
    for m in re.finditer(r'\d+', middle_block):
        start = 0
        end = 0
        
        # set bounds on searching around number
        if m.span()[0] == 0:
            start = 0
        else:
            start = m.span()[0] - 1
            
        if m.span()[1] == len(middle_block) - 1:
            end = m.span()[1]
        else:
            end = m.span()[1]
        found = False
        for line in lines:
            for special_char in special_chars:
                if special_char in line[start:end+1]:
                    part_numbers.append(int(m.group(0)))
                    found = True
                    break
            if found:
                break

    return part_numbers

def get_part_numbers(schematic):
    part_numbers = []
    for idx, _ in enumerate(schematic):
        lines = []
        if idx == 0:
            lines.append("." * len(schematic[idx]))
            lines.append(schematic[idx])
            lines.append(schematic[idx+1])

        elif idx == len(schematic) - 1:
            lines.append(schematic[idx-1])
            lines.append(schematic[idx])
            lines.append("." * len(schematic[idx]))
        else:
            lines = schematic[idx-1:idx+2]

        part_numbers.extend(extract_part_number_from_block(lines))

    return part_numbers

if __name__ == "__main__":
    # get lines of input
    with open("input.txt") as f:
        schematic = f.readlines()
        a = set()
        for line in schematic:
            for char in line:
                a.add(char)
        part_numbers = get_part_numbers(schematic)
        print(sum(part_numbers))
    