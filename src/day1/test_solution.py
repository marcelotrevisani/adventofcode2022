from pathlib import Path

from day1.solution import solve


def test_solution_part1():
    test_input_file = Path(__file__).parent / "test_input.txt"
    with open(test_input_file, "r") as f:
        test_input_file = f.readlines()
    assert solve(test_input_file) == 24000

def test_solution_part2():
    test_input_file = Path(__file__).parent / "test_input.txt"
    with open(test_input_file, "r") as f:
        test_input_file = f.readlines()
    assert solve(test_input_file, num_largest=3) == 45000
