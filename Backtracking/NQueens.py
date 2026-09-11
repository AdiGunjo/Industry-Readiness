def solve_n_queens(n):
    solutions = []
    board = [-1] * n  # board[row] = column of queen in that row

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # undo (backtrack)

    backtrack(0)
    return solutions

results = solve_n_queens(4)
print(f"Solutions for 4-Queens: {len(results)}")
print(results[0])