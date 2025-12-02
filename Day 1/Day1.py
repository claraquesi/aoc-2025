def main():
    """Main function for Advent of Code 2025 Day 1"""
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
    numPasses = 0 # Number of times the dial passes 0
    Pos_i = 50 # Initial dial position
    for line in data.splitlines():
        if line[0] == "L":
            Pos_f = (Pos_i - int(line[1:])) % 100
        elif line[0] == "R":
            Pos_f = (Pos_i + int(line[1:])) % 100
        if Pos_f == 0:
            numPasses += 1
        Pos_i = Pos_f
    return numPasses

def solve_part2(data: str) -> int:
    numPasses = 0 # Number of times the dial passes 0
    Pos_i = 50 # Initial dial position
    for line in data.splitlines():
        steps = int(line[1:])
        if line[0] == "L":
            for _ in range(steps):
                Pos_i = (Pos_i - 1) % 100
                if Pos_i == 0:
                    numPasses += 1
        elif line[0] == "R":
            for _ in range(steps):
                Pos_i = (Pos_i + 1) % 100
                if Pos_i == 0:
                    numPasses += 1
        
    return numPasses


if __name__ == "__main__":
    main()