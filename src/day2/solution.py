import re
from pathlib import Path


def solve(txt_input):
    total_points = 0
    re_turns = re.compile(r"(\w)\s+(\w)")
    fixed_points = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    for turn in txt_input:
        turn = re_turns.match(turn).groups()
        match turn:
            case ("A", "Y") | ("B", "Z") | ("C", "X"):
                total_points += 6
            case ("A", "X") | ("B", "Y") | ("C", "Z"):
                total_points += 3
        total_points += fixed_points[turn[1]]
    return total_points


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        txt_input = f.readlines()
    print(f"Day 2, part 1: {solve(txt_input)}")