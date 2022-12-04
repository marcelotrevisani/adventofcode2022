from pathlib import Path


def calc_letter_val(letter: str) -> int:
    if letter.isupper():
        return ord(letter) - ord("A") + 27
    return ord(letter) - ord("a") + 1


def solve_part_1(txt_input: str) -> int:
    total_val = 0
    for line in txt_input:
        line = line.strip()
        duplicated_letter = set(line[: len(line) // 2]) & set(line[len(line) // 2 :])
        total_val += calc_letter_val(list(duplicated_letter)[0])
    return total_val


def solve_part_2(txt_input: str) -> int:
    total_val = 0
    for i in range(len(txt_input) // 3):
        sacks = [set(line.strip()) for line in txt_input[i * 3 : (i * 3) + 3]]
        letter = list(sacks[0] & sacks[1] & sacks[2])[0]
        total_val += calc_letter_val(letter)
    return total_val


if __name__ == "__main__":
    with open(Path(__file__).parent / "input.txt", "r") as f:
        txt_input = f.readlines()
    print(f"Day 3 - Part 1: {solve_part_1(txt_input)}")
    print(f"Day 3 - Part 2: {solve_part_2(txt_input)}")
