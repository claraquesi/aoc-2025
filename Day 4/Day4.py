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
    roll_sum = sum_accessible_rolls(rows)
    return roll_sum

def solve_part2(data: str) -> int:
    total = 0
    rows = data.splitlines()
    while True:
        roll_sum = sum_accessible_rolls(rows)
        if roll_sum == 0:
            break
        total += roll_sum
        rows = [row.replace("X",".") for row in rows]
    return total

def sum_accessible_rolls(rows: list[str]) -> tuple[int, list[str]]:
    count = 0
    for idy, row in enumerate(rows):
        for idx, ch in enumerate(row):
            if ch in "@X" and num_neighboring_rolls(rows, idx, idy) < 4:
                count += 1
                left_of_me = rows[idy][:idx]
                right_of_me = rows[idy][idx+1:]
                rows[idy] = left_of_me + "X" + right_of_me

    return count

def num_neighboring_rolls(rows: list[str], x: int, y: int) -> int:
    height = len(rows)
    width = len(rows[0])
    count = 0

    return sum(
        1
        for dy in (-1, 0, 1)
        for dx in (-1, 0, 1)
        if not (dx == 0 and dy ==0)
        and 0 <= y + dy < height
        and 0 <= x + dx < width
        and rows[y + dy][x + dx] in "@X"
    )


if __name__ == "__main__":
    main()