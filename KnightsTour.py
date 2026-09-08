def knight_tour(n=8):
    board = [[-1] * n for _ in range(n)]
    moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < n and board[r][c] == -1

    def backtrack(r, c, move_count):
        if move_count == n * n:
            return True
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc):
                board[nr][nc] = move_count
                if backtrack(nr, nc, move_count + 1):
                    return True
                board[nr][nc] = -1  # undo
        return False

    board[0][0] = 0
    if backtrack(0, 0, 1):
        for row in board:
            print(' '.join(f'{x:2}' for x in row))
    else:
        print("No solution exists")

knight_tour(8)