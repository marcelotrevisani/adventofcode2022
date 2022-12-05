import re
from collections import defaultdict
from pathlib import Path
from typing import List


def solve_part_1(txt_input: List[str]) -> str:
    return solve(txt_input, False)


def solve_part_2(txt_input: List[str]) -> str:
    return solve(txt_input, True)


def solve(txt_input: List[str], maintain_order=False) -> str:
    all_crates = defaultdict(list)
    for pos, line in enumerate(txt_input):
        if line[1] == "1":
            break
        for crate_pos, val in enumerate(line[1::4], start=1):
            if val.strip():
                all_crates[crate_pos].insert(0, val)

    pos += 2
    re_move = re.compile(r"move\s+(\d+)\s+from\s+(\d+)\s+to\s+(\d+)")
    for line in txt_input[pos:]:
        n_move, move_from, move_to = (int(i) for i in re_move.match(line).groups())
        crates_to_add = all_crates[move_from][-n_move:]
        if maintain_order is False:
            crates_to_add.reverse()
        all_crates[move_to].extend(crates_to_add)
        del all_crates[move_from][-n_move:]

    return "".join(all_crates[i][-1] for i in range(1, max(all_crates.keys()) + 1) if all_crates[i])


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        txt_input = f.readlines()
    print(f"Day 5 - Part 1: {solve_part_1(txt_input)}")
    print(f"Day 5 - Part 2: {solve_part_2(txt_input)}")
