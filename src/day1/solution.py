import heapq
from pathlib import Path


def solve(txt_input):
    max_val = 0
    single_accumulator = 0
    for line in txt_input:
        try:
            single_accumulator += int(line)
        except ValueError:
            max_val = max(max_val, single_accumulator)
            single_accumulator = 0
    return max(max_val, single_accumulator)


def solve_part2(txt_input):
    accumulator = 0
    all_values = []
    for line in txt_input:
        try:
            accumulator += int(line)
        except ValueError:
            all_values.append(accumulator)
            accumulator = 0
    if accumulator > 0:
        all_values.append(accumulator)
    return sum(heapq.nlargest(3, all_values))


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        all_input = f.readlines()
    print(f"Part 1: {solve(all_input)}")
    print(f"Part 2: {solve_part2(all_input)}")
