import pathlib
from typing import Iterable, List


def binary_str_generator(rel_path: str) -> str:
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


def search_with_bit_condition(input_list: List[str], bit_index:int=0, least:bool=False):
    if len(input_list) == 1:
        return input_list[0]
    leading_ones = [1 if x[bit_index] == "1" else 0 for x in input_list]
    most_common = 1 if len(leading_ones)/sum(leading_ones) <= 2 else 0
    if (most_common == 1 and not least) or (most_common == 0 and least):
        filtered_list = [binary for binary, leading_one in zip(input_list,leading_ones) if leading_one]
    else:
        filtered_list = [binary for binary, leading_one in zip(input_list,leading_ones) if not leading_one]
    return search_with_bit_condition(filtered_list, bit_index=bit_index+1, least=least)


if __name__ == "__main__":
    in_ = list(binary_str_generator("inputs/day3.txt"))
    oxygen = int(search_with_bit_condition(in_, bit_index=0, least=False),2)
    co2_scrubber = int(search_with_bit_condition(in_, bit_index=0, least=True),2)
    print(f"{oxygen=}, {co2_scrubber=}, {oxygen*co2_scrubber=}")
