import heapq
from pathlib import Path


def solve(txt_input, num_largest=1):
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
    return sum(heapq.nlargest(num_largest, all_values))


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        all_input = f.readlines()
    print(f"Part 1: {solve(all_input, num_largest=1)}")
    print(f"Part 2: {solve(all_input, num_largest=3)}")
