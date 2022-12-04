import re
from pathlib import Path


def solve_part_1(txt_input):
    total = 0
    re_elf = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")
    for line in txt_input:
        start_1, end_1, start_2, end_2 = [int(i) for i in re_elf.match(line).groups()]
        if (start_1 <= start_2 and end_1 >= end_2) or (
            start_1 >= start_2 and end_1 <= end_2
        ):
            total += 1
    return total


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        txt_input = f.readlines()
    print(f"Day 4 - Part 1: {solve_part_1(txt_input)}")
