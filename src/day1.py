import typing
import pathlib

def count_depth_increases() -> int:
    src_dir = pathlib.Path(__file__).parent
    with open(src_dir / "inputs/day1.txt", "r") as in_:
        depths: typing.Iterator[int] = (int(line) for line in in_) # use generator to not allocate memory
        increases:int = 0
        last_depth = next(depths)
        for depth in depths:
            if last_depth - depth < 0:
                increases += 1
            last_depth = depth
    return increases
    
if __name__=="__main__":
    print(count_depth_increases())
