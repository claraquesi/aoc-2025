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
    rows = data.splitlines()
    roll_sum,rows = sum_accessible_rolls(rows)
    return roll_sum

def solve_part2(data: str) -> int:
    total = 0
    rows = data.splitlines()
    while True:
        roll_sum,rows = sum_accessible_rolls(rows)
        if roll_sum == 0:
            break
        total += roll_sum
        for i in range(len(rows)):
            rows[i] = rows[i].replace("X",".")

    return total

def sum_accessible_rolls(rows: str) -> tuple[int, str]:

    def accessible_rolls():
        for idy, y in enumerate(rows):
            for idx, x in enumerate(rows[idy]):
                if (x == "@" or x == "X") and num_neighboring_rolls(rows, idx, idy) < 4:
                    yield 1
                    left_of_me = rows[idy][:idx]
                    right_of_me = rows[idy][idx+1:]
                    rows[idy] = left_of_me + "X" + right_of_me
                else:
                    yield 0

    return sum(accessible_rolls()), rows

def num_neighboring_rolls(s: str, x: int, y: int) -> int:
    neighbors = find_all_neighbors(s, x, y)
    def count_neighboring_rolls():
        for neighbor in enumerate(neighbors):
            if neighbor[1] == "@" or neighbor[1] == "X":
                yield 1
    return sum(count_neighboring_rolls())

def find_all_neighbors(s: str, x: int, y: int) -> str:
    neighbors = ""
    row_len = len(s[y])
    num_rows = len(s)
    if (x > 0): neighbors = neighbors + s[y][x-1]
    if (x < row_len - 1): neighbors = neighbors + s[y][x+1]
    if (x > 0 and y > 0): neighbors = neighbors + s[y-1][x-1]
    if (y > 0): neighbors = neighbors + s[y-1][x]
    if (y > 0) and (x < row_len - 1): neighbors = neighbors + s[y-1][x+1]
    if (y < num_rows - 1) and (x > 0): neighbors = neighbors + s[y+1][x-1]
    if (y < num_rows - 1): neighbors = neighbors + s[y+1][x]
    if (y < num_rows - 1) and (x < row_len - 1): neighbors = neighbors + s[y+1][x+1]
    return neighbors


if __name__ == "__main__":
    main()