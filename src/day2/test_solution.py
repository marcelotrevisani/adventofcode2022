from pathlib import Path

from day2.solution import solve


def test_solve():
    with open(Path(__file__).parent / "test_input.txt", "r") as f:
        txt_input = f.readlines()
    assert solve(txt_input) == 15
