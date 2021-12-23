import pathlib


class Line:
    def __init__(self, x0: int, y0: int, x1: int, y1: int):
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1
        self.coordinates = set()
        self._add_points()

    def _add_points(self):
        if self._x0 == self._x1:
            start = min(self._y0, self._y1)
            stop = max(self._y0, self._y1)
            self.coordinates.update(((self._x0, y) for y in range(start, stop + 1)))
        elif self._y0 == self._y1:
            start = min(self._x0, self._x1)
            stop = max(self._x0, self._x1)
            self.coordinates.update(((x, self._y0) for x in range(start, stop + 1)))
        else:
            pass


def read_inputs():
    filepath = pathlib.Path(__file__).parent / "inputs/day5.txt"
    lines = []
    with open(filepath, "tr") as fid:
        for line in fid:
            coords = line.split("->")
            x0, y0 = coords[0].strip().split(",")
            x1, y1 = coords[1].strip().split(",")
            lines.append(Line(int(x0), int(y0), int(x1), int(y1)))
    return lines


def main():
    lines = read_inputs()
    overlaps = set()
    while lines:
        l = lines.pop()
        for other in lines:
            overlaps.update(l.coordinates.intersection(other.coordinates))
    print(len(overlaps))


if __name__ == "__main__":
    main()
