
def solve_part1(i_ranges: list[str], ingredients: list[str]) -> int:
    count = 0
    for i in ingredients:
        for r in i_ranges:
            if is_in_range(r, i):
                count +=1
                break
    return count

def solve_part2(i_ranges: list[str]) -> int:
    i_ranges = remove_overlap(i_ranges)

    def range_counts():
        for r in i_ranges:
            low = int(r.split("-")[0])
            high = int(r.split("-")[1])
            yield len(range(low, high)) + 1

    return sum(range_counts())
        
def is_in_range(i_range: str, ingredient: str) -> bool:
    low, high = i_range.split("-")
    if int(low) <= int(ingredient) <= int(high):
        return True
    
def remove_overlap(i_ranges: list[str]) -> list[str]:

    for idr, r in enumerate(i_ranges):
        low = int(r.split("-")[0])
        high = int(r.split("-")[1])
        for offset, r_comp in enumerate(i_ranges[idr+1:]):
            idr_comp = idr + 1 + offset
            low_comp = int(r_comp.split("-")[0])
            high_comp = int(r_comp.split("-")[1])
            if ranges_overlap(low, high, low_comp, high_comp):
                i_ranges[idr] = ""
                i_ranges[idr_comp] = str(min(low, low_comp)) + "-" + str(max(high, high_comp))
                break

    return list(filter(None,i_ranges))

def ranges_overlap(l: int, h: int, lc: int, hc: int) -> bool:    
    return max(l, lc) < min(h, hc)

def main():
    """Main function for Advent of Code 2025 Day 4"""
    # Read input
    with open("input.txt", "r") as f:
        data = f.read()

    chunks = data.split("\n\n")
    fresh_ranges = chunks[0].splitlines()
    ingredients = chunks[1].splitlines()

    # Part 1
    result_part1 = solve_part1(fresh_ranges, ingredients)
    print(f"Part 1: {result_part1}")
    
    # Part 2
    result_part2 = solve_part2(fresh_ranges)
    print(f"Part 2: {result_part2}")

def test():
    i_ranges = "3-5\n10-14\n16-20\n12-18".splitlines()
    ingredients = "1\n5\n8\n11\n17\n32".splitlines()
    assert solve_part1(i_ranges, ingredients) == 3

    assert solve_part2(i_ranges) == 14


if __name__ == "__main__":
    test()
    main()