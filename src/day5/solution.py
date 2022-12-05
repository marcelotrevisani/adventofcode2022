import re
from collections import deque, defaultdict
from pathlib import Path
from typing import List


def solve_part_1(txt_input: List[str]) -> str:
    all_crates = defaultdict(deque)
    for pos, line in enumerate(txt_input):
        if line[1] == "1":
            break
        for crate_pos, val in enumerate(line[1::4], start=1):
            if val.strip():
                all_crates[crate_pos].appendleft(val)

    pos += 2
    re_move = re.compile(r"move\s+(\d+)\s+from\s+(\d+)\s+to\s+(\d+)")
    for line in txt_input[pos:]:
        n_move, move_from, move_to = (int(i) for i in re_move.match(line).groups())
        for _ in range(n_move):
            all_crates[move_to].append(all_crates[move_from].pop())

    return "".join(all_crates[i][-1] for i in range(1, max(all_crates.keys()) + 1) if all_crates[i])


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        txt_input = f.readlines()
    print(f"Day 6 - Part 1: {solve_part_1(txt_input)}")
