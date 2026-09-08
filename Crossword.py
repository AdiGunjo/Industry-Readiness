def crossword_fill(grid, words):

    rows = len(grid)
    cols = len(grid[0])
    board = [list(row) for row in grid]

    slots = []  # each: (cells list, length)
    # horizontal slots
    for r in range(rows):
        c = 0
        while c < cols:
            if board[r][c] != '#':
                start = c
                cells = []
                while c < cols and board[r][c] != '#':
                    cells.append((r, c))
                    c += 1
                if len(cells) > 1:
                    slots.append(cells)
            else:
                c += 1
    # vertical slots
    for c in range(cols):
        r = 0
        while r < rows:
            if board[r][c] != '#':
                cells = []
                while r < rows and board[r][c] != '#':
                    cells.append((r, c))
                    r += 1
                if len(cells) > 1:
                    slots.append(cells)
            else:
                r += 1

    words_by_len = {}
    for w in words:
        words_by_len.setdefault(len(w), []).append(w)

    used = set()

    def fits(cells, word):
        for (r, c), ch in zip(cells, word):
            if board[r][c] != '-' and board[r][c] != ch:
                return False
        return True

    def place(cells, word):
        old = [board[r][c] for r, c in cells]
        for (r, c), ch in zip(cells, word):
            board[r][c] = ch
        return old

    def unplace(cells, old):
        for (r, c), ch in zip(cells, old):
            board[r][c] = ch

    def backtrack(i):
        if i == len(slots):
            return True
        cells = slots[i]
        candidates = words_by_len.get(len(cells), [])
        for word in candidates:
            if word in used:
                continue
            if fits(cells, word):
                old = place(cells, word)
                used.add(word)
                if backtrack(i + 1):
                    return True
                used.remove(word)
                unplace(cells, old)
        return False

    if backtrack(0):
        return ["".join(row) for row in board]
    return None


if __name__ == "__main__":
    print("CROSSWORD PUZZLE FILLING")
    grid = ["---", "-#-", "---"]
    result = crossword_fill(grid, ["CAT", "COW", "TIE", "WOE"])
    print(result)