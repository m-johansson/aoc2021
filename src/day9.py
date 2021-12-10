import pathlib
from src.utils.iterations import sliding_window


def read_inputs():
    input_path = pathlib.Path(__file__).parent / "inputs/day9.txt"
    with open(input_path, "tr") as fid:
        return fid.read().split()


def number_row(row: str):
    return [int(char) for char in row]


def main(): 
    lines = [number_row(row) for row in read_inputs()]
    sum_ = 0
    first = True
    for l1, l2, l3 in sliding_window(lines, 3):
        if first:
            first = False
            for index, number in enumerate(l1):
                if number < l2[index]:
                    sum_ += get_low_or_0(index, number, l1)
        for index, number in enumerate(l2):
            if l1[index] > number < l3[index]:
                sum_ += get_low_or_0(index, number, l2)
    else:
        for index, number in enumerate(lines[-1]):  # fully un-indented => l3 last line in file
            if number < lines[-2][index]:
                sum_ += get_low_or_0(index, number, lines[-1])
    print(sum_)


def get_low_or_0(index, number, row):
    if index == 0:
        return number+1 if number < row[1] else 0
    elif index == len(row)-1:
        return number+1 if number < row[index-1] else 0
    else:
        return number+1 if row[index - 1] > number < row[index + 1] else 0


if __name__ == "__main__":
    main()
