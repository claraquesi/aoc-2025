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
    return sum_invalid_ids(data, lambda num: has_pattern(num, lambda reps: reps == 2))

def solve_part2(data: str) -> int:
    return sum_invalid_ids(data, lambda num: has_pattern(num, lambda reps: reps >= 2))

def sum_invalid_ids(data: str, is_invalid) -> int:
    def invalid_numbers():
        for part in data.split(","):
            start_str, end_str = part.split("-")
            start_num, end_num = int(start_str), int(end_str)
            for num in range(start_num, end_num + 1):
                if is_invalid(num):
                    yield num
    return sum(invalid_numbers())

def has_pattern(num: int, predicate) -> bool:
    s = str(num)
    n = len(s)
    for block_size in range (1, n // 2 + 1):
        if n % block_size != 0:
            continue
        reps = n // block_size
        candidate = s[:block_size] * reps
        if candidate == s and predicate(reps):
            return True
    return False

def test():
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