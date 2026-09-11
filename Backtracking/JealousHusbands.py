from itertools import combinations
from collections import deque


def jealous_husbands(n=3, boat_cap=2):
    """N couples must cross a river; a woman may never be in the company of
    another man (bank or boat) unless her own husband is also present.
    State: tuple of 0/1 for each husband/wife position + boat side.
    We encode as (husbands_side_tuple, wives_side_tuple, boat_side)."""
    
    start = (tuple([0] * n), tuple([0] * n), 0)
    goal = (tuple([1] * n), tuple([1] * n), 1)

    def valid(state):
        husbands, wives, _ = state
        for side in (0, 1):
            men_here = [i for i in range(n) if husbands[i] == side]
            for i in range(n):
                if wives[i] == side and husbands[i] != side:
                    # wife i is on this side without her husband
                    other_men = [j for j in men_here if j != i]
                    if other_men:
                        return False
        return True

    def neighbors(state):
        husbands, wives, side = state
        people = [('H', i) for i in range(n) if husbands[i] == side] + \
                 [('W', i) for i in range(n) if wives[i] == side]
        results = []
        for r in range(1, boat_cap + 1):
            for group in combinations(people, r):
                nh, nw = list(husbands), list(wives)
                for typ, idx in group:
                    if typ == 'H':
                        nh[idx] = 1 - side
                    else:
                        nw[idx] = 1 - side
                new_state = (tuple(nh), tuple(nw), 1 - side)
                if valid(new_state):
                    results.append(new_state)
        return results

    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for nxt in neighbors(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path + [nxt]))
    return None


if __name__ == "__main__":
    print("JEALOUS HUSBANDS (n=3)")
    sol = jealous_husbands(3)
    print(f"Solved in {len(sol) - 1} crossings" if sol else "No solution")