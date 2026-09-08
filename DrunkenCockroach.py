def cockroach_walk(n=5, start=(0, 0)):
    board = [[-1] * n for _ in range(n)]
    moves = [(1,0),(-1,0),(0,1),(0,-1)]  

    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < n and board[r][c] == -1

    def backtrack(r, c, step):
        if step == n * n:
            return True
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if is_valid(nr, nc):
                board[nr][nc] = step
                if backtrack(nr, nc, step + 1):
                    return True
                board[nr][nc] = -1  # stumble back, try another direction
        return False

    sr, sc = start
    board[sr][sc] = 0
    if backtrack(sr, sc, 1):
        for row in board:
            print(' '.join(f'{x:2}' for x in row))
    else:
        print("The cockroach got stuck — no full-coverage walk from this start")

cockroach_walk(5, start=(0, 0))