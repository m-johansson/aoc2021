import pathlib

scores_1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

scores_2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

lefters = ("(", "[", "{", "<")
righters = (")", "]", "}", ">")
couples = {closer: opener for closer, opener in zip(righters, lefters)}
class Line:

    def __init__(self, chars:str):
        self.corrupt = False
        self._chars:str = chars.strip()
        self._score = 0
        self._open_delims = []

    def process(self,):
        for char in self._chars:
            if char in lefters:
                self._open_delims.append(char)
            elif char in righters:
                expected_open = couples[char]
                actual = self._open_delims[-1]
                if expected_open != actual:
                    self._set_corrupt()
                    return
                else:
                    self._open_delims.pop()

    def _set_corrupt(self,):
        self.corrupt = True

    def set_score(self,):
        if self.corrupt:
            raise ValueError("Corrupt lines have no score")
        s = 0
        for deliminator in reversed(self._open_delims):
            char_score = scores_2[deliminator]
            s = 5*s + char_score
        self._score = s
    
    def get_score(self,):
        if self.corrupt:
            raise ValueError("Corrupt lines have no scores!")
        return self._score

    def __lt__(self, __ob:object):
        return self.get_score() < __ob.get_score()

def read_in():
    filepath = pathlib.Path(__file__).parent / "inputs/day10.txt"
    with open(filepath, "tr") as fid:
        yield from fid


def main():
    lines = []
    for line in map(lambda x: x.strip(), read_in()):
        l = Line(line)
        l.process()
        if not l.corrupt:
            l.set_score()
            lines.append(l)
    uncorrupt_lines = sorted([l for l in lines if not l.corrupt])
    selected = uncorrupt_lines[int(len(uncorrupt_lines)/2)]
    print(f"{selected.get_score()}, {selected._chars}")


if __name__ == "__main__":
    main()
