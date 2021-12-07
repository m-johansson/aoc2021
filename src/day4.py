from typing import Iterator, Tuple, List
import pathlib


class BingoBoard:
    def __init__(self, id_: int, row_generator):
        self.id = id_
        self.rows: List[List[int]] = []
        self.columns: List[List[int]] = []
        self.populate_board(row_generator)

    def populate_board(self, row_generator: Iterator[Tuple[int, int, int, int, int]]):
        for row in row_generator:
            self.rows.append(list(row))
        for i in range(len(self.rows)):
            self.columns.append([])
        for el in self.rows:
            for in_, i in enumerate(el):
                self.columns[in_].append(i)

    def draw(self, nbr):
        for row in self.rows:
            self._try_pop_item(row, nbr)
        for column in self.columns:
            self._try_pop_item(column, nbr)

    def check_bingo(
        self,
    ):
        for row in self.rows:
            if len(row) == 0:
                return True
        for column in self.columns:
            if len(column) == 0:
                return True
        return False

    @staticmethod
    def _try_pop_item(row, nbr):
        try:
            row.remove(nbr)
        except ValueError:
            pass
            # not present, do nothing

    def score(self, draw):
        sum_ = 0
        for row in self.rows:
            sum_ += sum(row)
        return draw * sum_

    def __eq__(self, __o: object) -> bool:
        return __o.id == self.id


class InputReader:
    def __init__(self, filepath):
        self.filepath = filepath
        self._basepath = pathlib.Path(__file__).parent

    def yield_draw(
        self,
    ):
        with open(self._basepath / self.filepath, "tr") as fid:
            draw_sequence = fid.readline()
        yield from map(lambda x: int(x), draw_sequence.split(","))

    def yield_bingo_board(
        self,
    ):
        with open(self._basepath / self.filepath, "tr") as fid:
            for _ in range(2):
                fid.readline()  # throw away sequence and empty line
            while True:
                board = []
                while (line := fid.readline()) not in ("\n", ""):
                    board.append(list(map(lambda x: int(x), line.split())))
                yield board
                if line == "":
                    return


def play(input_boards: list[BingoBoard], draws):
    bingo = []
    for draw in draws:
        print(draw)
        for board in input_boards:
            board.draw(draw)
            if board.check_bingo():
                bingo.append(board)
        for board in bingo:
            if len(input_boards) == 1:
                print(f"{board.id=}:{board.score(draw)=}")
                return
            input_boards.remove(board)
        bingo = []


if __name__ == "__main__":
    reader = InputReader("inputs/day4.txt")
    boards = [
        BingoBoard(id_, board_input)
        for id_, board_input in enumerate(reader.yield_bingo_board())
    ]
    play(boards, draws=reader.yield_draw())
