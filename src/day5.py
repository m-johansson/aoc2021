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
        x_incline = self._get_incline(self._x0, self._x1)
        y_incline = self._get_incline(self._y0, self._y1)
        if x_incline and y_incline:
            x_coords = range(self._x0, self._x1 + x_incline, x_incline)
            y_coords = range(self._y0, self._y1 + y_incline, y_incline)
            self.coordinates.update(zip(x_coords, y_coords, strict=True))
        elif x_incline and not y_incline:
            self.coordinates.update(
                (
                    (x, self._y0)
                    for x in range(self._x0, self._x1 + x_incline, x_incline)
                )
            )
        elif y_incline and not x_incline:
            self.coordinates.update(
                (
                    (self._x0, y)
                    for y in range(self._y0, self._y1 + y_incline, y_incline)
                )
            )
        elif not x_incline and not y_incline:
            # this line segment is just a point
            self.coordinates.add((self._x0, self._y0))

    def _get_incline(self, p0, p1):
        if p0 == p1:
            return 0
        if p0 > p1:
            return -1
        if p0 < p1:
            return 1


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
