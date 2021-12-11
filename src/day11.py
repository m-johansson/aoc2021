import pathlib
from pprint import pprint


class Cave:
    def __init__(self, board: list[list[int]]):
        self.flashed = []
        self.board = board
        self.element_count = len(self.board) * len(self.board[0])

    def flash(self, y_0: int, x_0: int):
        self.flashed.append((x_0, y_0))
        for y in range(max(y_0 - 1, 0, 0), min(y_0 + 1, len(self.board) - 1) + 1):
            for x in range(max(x_0 - 1, 0), min(x_0 + 1, len(self.board[y]) - 1) + 1):
                if (x, y) in self.flashed:
                    # don't increase and check for flash
                    continue
                self.board[y][x] = self.board[y][x] + 1
                if self.board[y][x] > 9:
                    self.flash(x_0=x, y_0=y)
        self.board[y_0][x_0] = 0

    def step(self):
        self.flashed = []
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                self.board[y][x] = self.board[y][x] + 1
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x] > 9:
                    self.flash(x_0=x, y_0=y)

    def all_flashed(self):
        return len(self.flashed) == self.element_count


def read_inputs():
    matrix = []
    with open(pathlib.Path(__file__).parent / "inputs/day11.txt") as fid:
        for l in fid:
            matrix.append([int(_) for _ in l.strip()])
    return matrix


def main():
    matrix = read_inputs()
    cave = Cave(matrix)
    i = 0
    while True:
        i += 1
        print(i)
        cave.step()
        if cave.all_flashed():
            break
    pprint(cave.board)
    print(i)


if __name__ == "__main__":
    main()
