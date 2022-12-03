from pathlib import Path


def solve(txt_input):
    max_val = 0
    single_accumulator = 0
    for line in txt_input:
        try:
            single_accumulator += int(line)
        except ValueError:
            max_val = max(max_val, single_accumulator)
            single_accumulator = 0
    return max_val


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        print(solve(f.readlines()))
