import re
from pathlib import Path


def solve_part_1(txt_input):
    re_turns = re.compile(r"(\w)\s+(\w)")
    turns = [re_turns.match(turn).groups() for turn in txt_input]
    return calculate_points(turns)


def calculate_points(all_turns):
    fixed_points = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    total_points = 0
    for turn in all_turns:
        match turn:
            case ("A", "Y") | ("B", "Z") | ("C", "X"):
                total_points += 6
            case ("A", "X") | ("B", "Y") | ("C", "Z"):
                total_points += 3
        total_points += fixed_points[turn[1]]
    return total_points


def solve_part_2(txt_input):
    re_turns = re.compile(r"(\w)\s+(\w)")
    all_turns = []
    seq_pos = ("X", "Y", "Z")
    seq_val = {j: i for i, j in enumerate(seq_pos)}
    mapping = {"A": "X", "B": "Y", "C": "Z"}
    for turn in txt_input:
        turn = re_turns.match(turn).groups()
        result = turn[1]
        match result:
            case "X":
                all_turns.append((turn[0], seq_pos[seq_val[mapping[turn[0]]] - 1]))
            case "Y":
                all_turns.append((turn[0], mapping[turn[0]]))
            case "Z":
                all_turns.append((turn[0], seq_pos[(seq_val[mapping[turn[0]]] + 1) % len(seq_pos)]))
    return calculate_points(all_turns)


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        txt_input = f.readlines()
    print(f"Day 2, part 1: {solve_part_1(txt_input)}")
    print(f"Day 2, part 2: {solve_part_2(txt_input)}")
