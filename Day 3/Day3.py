def main():
    """Main function for Advent of Code 2025 Day 3"""
    # Read input
    with open("input.txt", "r") as f:
        data = f.read().strip()
    
    # Part 1
    result_part1 = solve_part1(data)
    print(f"Part 1: {result_part1}")
    
    # Part 2
    result_part2 = solve_part2(data)
    print(f"Part 2: {result_part2}")

def solve_part1(data: str) -> int:
    return sum_joltages(data, 2)

def solve_part2(data: str) -> int:
    return sum_joltages(data, 12)

# Helper Functions

# Sum all joltages from the input data for a given joltage length (number of batteries selected from each pack)
def sum_joltages(data: str, j_len: int) -> int:

    # Generator to yield joltages from each pack in the input data
    def joltages():
        for line in data.splitlines():
            yield find_joltage(line, j_len)

    return sum(joltages()) # sum all joltages generated from the input data

# Find the largest joltage by selecting j_len batteries from the given pack line
def find_joltage(line: str, j_len: int) -> int:
    joltage = [0 for _ in range(j_len)] # initialize list to hold selected batteries as strings (for easier concatenation later)
    loc = 0 # initialize starting location for search
    L = len(line) # length of the battery pack line
    for i in range(j_len):
        # for each battery left to select, find the largest battery in the remaining range of the line.
        # This range shrinks as we select more batteries, since we need to leave enough batteries at the end to fill the remaining slots.
        # The next battery is chosen from the range (loc + 1) to (L + 1 - j_len + i) of the pack, where loc is the position of the last found battery.
        joltage[i], loc = find_largest_in_range(line, loc, L + 1 - j_len + i)

    return int("".join(joltage)) # concatenate selected batteries and convert to int

# For each given search range, find the largest battery and return it along with its position for the next search
def find_largest_in_range(line: str, start: int, end: int) -> int:
    largest = "0" # initialize largest found battery
    delta = 0 # this will track the offset from start to the position of the found largest battery to be used in the next search
    # search for the largest battery in the specified range of the pack line
    for idx, x in enumerate(line[start:end]):
        if int(x) > int(largest):
            largest = x # update largest found battery
            delta = idx # delta from start to the position of the found largest battery
    return largest, start + delta + 1 # search started at 'start', so we need to offset start by delta + 1 for the starting location of the next search.

def test():
    # Test cases for find_joltage
    assert find_joltage("9876543210", 2) == 98
    assert find_joltage("818181911112111", 2) == 92
    assert find_joltage("234234234234278", 2) == 78
    assert not find_joltage("811111111111119", 2) == 98
    assert find_joltage("987654321111111", 12) == 987654321111
    assert find_joltage("811111111111119", 12) == 811111111119
    assert find_joltage("234234234234278", 12) == 434234234278
    assert find_joltage("818181911112111", 12) == 888911112111


if __name__ == "__main__":
    test()
    main()