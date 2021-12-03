import pathlib
from typing import Iterable, List


def binary_generator(rel_path: str) -> str:
    src_dir = pathlib.Path(__file__).parent
    with open(src_dir / rel_path, "tr") as in_:
        yield from (line.strip() for line in in_)


def get_gamma_and_epsilon(string_generator: Iterable):
    bits_count: List[int] = []
    lines_read = 0
    for binary_string in string_generator:
        lines_read += 1
        for index, char in enumerate(binary_string):
            try:
                bits_count[index] += int(char)
            except IndexError:
                bits_count.append(int(char))
    threshold = lines_read / 2
    gamma = int(
        "".join([str(1) if count >= threshold else str(0) for count in bits_count]), 2
    )
    epsilon = int(
        "".join([str(0) if count >= threshold else str(1) for count in bits_count]), 2
    )
    return gamma, epsilon


if __name__ == "__main__":
    bin_gen = binary_generator("inputs/day3.txt")
    gamma, epsilon = get_gamma_and_epsilon(bin_gen)
    print(f"{gamma=} {epsilon=}")
    print(gamma * epsilon)
