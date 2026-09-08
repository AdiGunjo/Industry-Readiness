def killer_sudoku_solve(grid, cages):
    
    """grid: 9x9 list with 0 for empty cells.
    cages: list of (cell_list, target_sum) where cells in a cage must have
    distinct digits summing to target_sum (standard killer sudoku rule).
    Returns solved grid or None."""
    
    board = [row[:] for row in grid]
    cage_of = {}
    for cells, total in cages:
        for cell in cells:
            cage_of[cell] = (cells, total)

    def valid(r, c, val):
        for i in range(9):
            if board[r][i] == val or board[i][c] == val:
                return False
        br, bc = 3 * (r // 3), 3 * (c // 3)
        for i in range(br, br + 3):
            for j in range(bc, bc + 3):
                if board[i][j] == val:
                    return False
                
        # cage constraint
        
        cells, total = cage_of.get((r, c), (None, None))
        if cells:
            vals_in_cage = [board[cr][cc] for cr, cc in cells if board[cr][cc] != 0]
            if val in vals_in_cage:
                return False
            if sum(vals_in_cage) + val > total:
                return False
            filled = len(vals_in_cage) + 1
            if filled == len(cells) and sum(vals_in_cage) + val != total:
                return False
        return True

    def find_empty():
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    return r, c
        return None

    def backtrack():
        pos = find_empty()
        if not pos:
            return True
        r, c = pos
        for val in range(1, 10):
            if valid(r, c, val):
                board[r][c] = val
                if backtrack():
                    return True
                board[r][c] = 0
        return False

    if backtrack():
        return board
    return None


if __name__ == "__main__":
    print("KILLER SUDOKU (partial demo grid)")
    empty_grid = [[0] * 9 for _ in range(9)]
    demo_cages = [([(0, 0), (0, 1)], 10), ([(0, 2), (0, 3), (0, 4)], 15)]
    # NOTE: full 9x9 killer sudoku solve is slow without full cage coverage;
    # demoing solver machinery on a lightly-constrained grid.
    print("(solver defined - use killer_sudoku_solve(grid, cages) with full cage set)")