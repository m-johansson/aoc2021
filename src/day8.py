import pathlib
from typing import Dict

input_wires = ["a", "b", "c", "d", "e", "f", "g"]


class Row:
    def __init__(self):
        self.solved_digits: Dict[int, set] = {}
        self.unsolved_digits = {
            1: is_one,
            2: is_two,
            3: is_three,
            4: is_four,
            5: is_five,
            7: is_seven,
            8: is_eight,
            9: is_nine,
        }

    def solve_digit(self, solution: str, digit: int):
        self.solved_digits[digit] = set(solution)
        try:
            self.unsolved_digits.pop(digit)
        except KeyError:
            pass  # this happens dependent solvers


def is_zero(input_str: str, wire_counts, row: Row):
    if not len(input_str) == 6:
        return False
    wire_set = set(input_wires)
    input_set = set(input_str)
    unlit_seg = (
        wire_set - input_set
    )  # if this segment is in the 1 solution, this is a six or nine
    return not unlit_seg.issubset(row.solved_digits[1])


def is_one(input_str: str, wire_counts):
    return len(input_str) == 2


def is_two(input_str: str, wire_counts: dict):
    for letter, count in wire_counts.items():
        if count == 9:
            return letter not in input_str
    return False


def is_three(input_str, wire_counts):
    reverse_lookup = {
        b: a for a, b in wire_counts.items()
    }  # only intersted in the unique counts in any case
    if len(input_str) == 5:
        epsilon = reverse_lookup[4]
        delta = reverse_lookup[6]
        return epsilon not in input_str and delta not in input_str
    return False


def is_four(input_str: str, wire_counts):
    return len(input_str) == 4


def is_five(input_str: str, wire_counts):
    return (
        len(input_str) == 5
        and not is_three(input_str, wire_counts)
        and not is_two(input_str, wire_counts)
    )


def is_six(input_str: str, wire_counts, row: Row):
    return (
        len(input_str) == 6
        and not is_zero(input_str, wire_counts, row)
        and not is_nine(input_str, wire_counts)
    )


def is_seven(input_str: str, wire_counts):
    return len(input_str) == 3


def is_eight(input_str: str, wire_counts):
    return len(input_str) == 7


def is_nine(input_str, wire_counts):
    if len(input_str) == 6:
        for letter, count in wire_counts.items():
            if count == 4:
                return letter not in input_str
    return False


def independent_solve(in_str: str, row: Row, wire_counts: dict):
    for digit, solver in row.unsolved_digits.copy().items():
        if solver(in_str, wire_counts):
            row.solve_digit(in_str, digit)


def main():
    filepath = "inputs/day8.txt"
    sum_ = 0
    for inputs, outputs in read_input(filepath):
        row = Row()
        wire_counts = count_wires(inputs)
        solution_list = []
        for in_str in inputs:
            independent_solve(in_str, row, wire_counts)
        unsolved_ins = [x for x in inputs if set(x) not in row.solved_digits.values()]
        for in_str in unsolved_ins:
            # this is either zero or six
            if is_zero(in_str, wire_counts, row):
                row.solve_digit(in_str, 0)
            elif is_six(in_str, wire_counts, row):
                row.solve_digit(in_str, 6)
            else:
                raise ValueError(in_str)
        for output in outputs:
            for digit, solution in row.solved_digits.items():
                if set(output) == solution:
                    solution_list.append(str(digit))
                    break
        row_solution = int("".join(solution_list))
        sum_ += row_solution
    return sum_


def count_wires(input_strings) -> Dict[str, int]:
    counts = {}
    for wire in input_wires:
        count = 0
        for input_ in input_strings:
            if wire in input_:
                count += 1
        counts[wire] = count
    return counts


def read_input(filepath):
    input_path = pathlib.Path(__file__).parent / filepath
    with open(input_path, "tr") as fid:
        for line in fid:
            inputs = line.split("|")[0].split()
            outputs = line.split("|")[-1].split()
            yield inputs, outputs


if __name__ == "__main__":
    print(main())
