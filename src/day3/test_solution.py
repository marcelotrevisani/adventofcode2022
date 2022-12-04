from pathlib import Path

from day3.solution import solve_part_1


def test_solve_part_1():
    with open(Path(__file__).parent / "test_input.txt", "r") as f:
        txt_input = f.readlines()
    assert solve_part_1(txt_input) == 157
