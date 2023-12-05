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

# --- Part Two ---

# The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

# You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

# Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

# The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

# This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

# Consider the same engine schematic again:

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

# In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

# What is the sum of all of the gear ratios in your engine schematic?


import re
from collections import defaultdict


special_chars = ['%', '/', '#', '-', '+', '&', '=', '$', '*', '@']

def amend_gear_ratios_from_block(lines, base_line_idx, gear_ratios):
    """
    extract the part number from a block of lines

    ......#...
    617*......
    .....+.58.

    returns [617]

    """

    middle_block = lines[1]
    # for each number in line
    for m_idx, m in enumerate(re.finditer(r'\d+', middle_block)):
        
        # setup left and right bounds inside block
        # start at zero if left side of number is at start of line        
        start = 0 if m.span()[0] == 0 else m.span()[0] - 1
        # end is the end of line if the right side of number is at end of line        
        end = m.span()[1] if m.span()[1] == len(middle_block)-1 else m.span()[1] + 1

        # check any of the surrounding characters are *
        for line_idx, line in enumerate(lines):
            for char_idx, char in enumerate(line[start:end]):
                if char is '*':
                    gear_ratios[base_line_idx + line_idx][start + char_idx].append(int(m.group(0)))

    return gear_ratios

def get_gear_ratios(schematic):
    # gear_ratio[row][column] contains the list of all ratios touching the gear at [row][column]
    gear_ratios = {i:defaultdict(list) for i in range(len(schematic))}
    # create 3 high block of lines
    for idx, _ in enumerate(schematic):
        block = []
        if idx == 0:
            block.append("." * len(schematic[idx]))
            block.extend(schematic[idx:idx+2])

        elif idx == len(schematic) - 1:
            # isn't python inuitive?
            block.extend(schematic[idx-1:idx+1])
            block.append("." * len(schematic[idx]))
        else:
            block = schematic[idx-1:idx+2]

        [print(line.strip()) for line in block]
        gear_ratios = amend_gear_ratios_from_block(block, idx, gear_ratios)
        print()
        print(gear_ratios[idx])
        # print(gear_ratios)
        print()
        print()
        print()
    
    # mapping of row number to column number to list of part numbers
    # get product of each list with length 2
    [print(v2[0], v2[1]) for _, numbers in gear_ratios.items() for _,v2 in numbers.items() if len(v2) == 2]
    gear_ratios = [v2[0]*v2[1] for _, numbers in gear_ratios.items() for _,v2 in numbers.items() if len(v2) == 2]

    return gear_ratios

if __name__ == "__main__":
    # get lines of input
    with open("input.txt") as f:
        schematic = f.readlines()
        a = set()
        for line in schematic:
            for char in line:
                a.add(char)
        gear_ratios = get_gear_ratios(schematic)
        print(sum(gear_ratios))
    