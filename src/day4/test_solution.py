from pathlib import Path

from day4.solution import solve_part_1, solve_part_2


def test_solution():
    with open(Path(__file__).parent / "test_input.txt", "r") as f:
        txt_input = f.readlines()
    assert solve_part_1(txt_input) == 2
    assert solve_part_2(txt_input) == 4
