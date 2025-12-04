def main():
    """Main function for Advent of Code 2025 Day 4"""
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
    rows = data.splitlines() # parse data into a list of rows
    return sum_accessible_rolls(rows) # return the sum of all accessible rows in the input data

def solve_part2(data: str) -> int:
    total = 0 # initialize counter for total rolls removed in all trials
    rows = data.splitlines() # parse data into list of rows
    while True: # keep looping until no more rolls are accessible
        roll_sum = sum_accessible_rolls(rows) # for each trial, find how many rolls are accessible given the current state of the input data
        if roll_sum == 0: 
            break # finish when no more rolls are accessible
        total += roll_sum # count up total number of rolls removed over all trials
        rows = [row.replace("X",".") for row in rows] # remove rolls from our list that were already picked
    return total

def sum_accessible_rolls(rows: list[str]) -> tuple[int, list[str]]:
    count = 0 # initialize counter for number of accessible rows in the current state of the input data
    for idy, row in enumerate(rows): # loop through each row
        for idx, ch in enumerate(row): # loop through each entry in each row
            if ch in "@" and num_neighboring_rolls(rows, idx, idy) < 4: # if the current entry is a roll, if it has fewer than 4 roll neighbors, it is accessible
                count += 1 # keep count of accessible rolls
                left_of_me = rows[idy][:idx] # the row to the left of the current entry
                right_of_me = rows[idy][idx+1:] # the row to the right of the current entry
                rows[idy] = left_of_me + "X" + right_of_me # mark entry for removal in next trial. It will remain marked for now since it can still prevent other rolls from being accessible.

    return count

def num_neighboring_rolls(rows: list[str], x: int, y: int) -> int:
    height = len(rows)
    width = len(rows[0])
    count = 0 # initialize counter for number of neighbors that are rolls (either unmarked, @, or marked, X)

    return sum(
        1
        for dy in (-1, 0, 1)
        for dx in (-1, 0, 1)
        if not (dx == 0 and dy ==0)
        and 0 <= y + dy < height
        and 0 <= x + dx < width
        and rows[y + dy][x + dx] in "@X" # Sum up all neighbors relative to position (x,y) that are rolls (either marked or unmarked)
    )


if __name__ == "__main__":
    main()