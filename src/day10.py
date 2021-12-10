import pathlib

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def read_in():
    filepath = pathlib.Path(__file__).parent / "inputs/day10.txt"
    with open(filepath, "tr") as fid:
        yield from fid

def main():
    lefters = ["(", "[", "{", "<"]
    righters = [")", "]", "}", ">"]
    couples = {closer: opener for closer, opener in zip(righters, lefters)}
    corrupters = []
    for line in read_in():
        open_chunks = []
        for char in line:
            if char in lefters:
                open_chunks.append(char)
            if char in righters:
                expected_open = couples[char]
                actual = open_chunks[-1]
                if expected_open != actual:
                    print(f"corrupt chunk, wrong closer: {char}")
                    corrupters.append(char)
                    break
                else:
                    open_chunks.pop()
    score = 0
    for char in corrupters:
        score += scores[char]
    return score
    

if __name__ == "__main__":
    print(main())
