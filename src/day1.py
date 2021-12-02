import itertools
import pathlib
import typing

from src.utils import iterations


def count_depth_increases() -> int:
    src_dir = pathlib.Path(__file__).parent
    with open(src_dir / "inputs/day1.txt", "tr") as in_:
        depths: typing.Iterator[int] = (int(line) for line in in_)
        sums = (sum(window) for window in iterations.sliding_window(depths, 3))
        increases = sum((1 for x, y in itertools.pairwise(sums) if x < y))
    return increases


if __name__ == "__main__":
    print(count_depth_increases())
