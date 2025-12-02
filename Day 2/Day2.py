def main():
    """Main function for Advent of Code 2025 Day 2"""
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
    # find and sum all numbers from input with exactly 2 repeating blocks
    return sum_invalid_ids(data, lambda num: has_pattern(num, lambda reps: reps == 2))

def solve_part2(data: str) -> int:
    # find and sum all numbers from input with 2 or more repeating blocks
    return sum_invalid_ids(data, lambda num: has_pattern(num, lambda reps: reps >= 2))

# Helper functions

# Sum all invalid IDs from the input data based on the is_invalid predicate; is_valid will be different for part 1 and part 2
def sum_invalid_ids(data: str, is_invalid) -> int:

    # Generator to yield invalid numbers from the input data
    def invalid_numbers():
        for part in data.split(","):
            start_str, end_str = part.split("-")
            start_num, end_num = int(start_str), int(end_str)
            for num in range(start_num, end_num + 1):
                if is_invalid(num):
                    yield num

    return sum(invalid_numbers())

# Check if the given number from the input has a repeating pattern according to the given predicate (e.g., exactly 2 repetitions for part 1, or 2 or more for part 2)
def has_pattern(num: int, predicate) -> bool:
    s = str(num)
    n = len(s)

    # find a number that divides the length of our number string, this will be our block_size.
    # then check if repeating the string block s[:block_size] a number of times equal to n // block_size gives us back our original string
    # if there is a match, check if the number of repetitions satisfies the predicate (i.e., equals 2 for part 1, or is >= 2 for part 2)
    # if so, return True. If no such block_size is found, return False.
    # Only need to check block sizes up to n // 2, since a block size larger than that cannot repeat at least twice and still form the original string.
    for block_size in range (1, n // 2 + 1):
        if n % block_size != 0:
            continue
        reps = n // block_size
        candidate = s[:block_size] * reps
        if candidate == s and predicate(reps):
            return True
    return False

def test():
    # some basic tests for has_pattern
    assert has_pattern(11, lambda r: r == 2)
    assert not has_pattern(11, lambda r: r >= 3)
    assert has_pattern(111111, lambda r: r >= 2)
    assert has_pattern(111111, lambda r: r == 2)  # via "111" * 2
    assert not has_pattern(12345, lambda r: r >= 2)
    assert has_pattern(12121212, lambda r: r == 4)
    assert has_pattern(12121212, lambda r: r == 2)

if __name__ == "__main__":
    test()
    main()