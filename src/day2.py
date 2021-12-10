import pathlib


def command_generator(filepath: str):
    """Take relative path, and yield command and distance"""
    src_dir = pathlib.Path(__file__).parent
    with open(src_dir / filepath, "tr") as in_:
        yield from (
            (cmd, int(distance))
            for cmd, distance in (str(row).strip().lower().split(" ") for row in in_)
        )


def where_are_we(command_generator):
    forward = 0
    aim = 0
    depth = 0
    for command, distance in command_generator:
        match command:
            case "forward":
                forward += distance
                depth = depth + distance * aim
            case "down":
                aim += distance
            case "up":
                aim -= distance
    return forward, depth


if __name__ == "__main__":
    in_ = command_generator("inputs/day2.txt")
    x, z = where_are_we(in_)
    print(f"horizontal {x}, depth {z}, product {x*z}")
