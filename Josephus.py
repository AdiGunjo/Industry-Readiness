def josephus(n, k):
    """Returns the 0-indexed position of the survivor among n people,
    eliminating every k-th person in a circle."""
    result = 0
    for i in range(2, n + 1):
        result = (result + k) % i
    return result


def josephus_order(n, k):
    """Returns the full elimination order (1-indexed positions)."""
    people = list(range(1, n + 1))
    idx = 0
    order = []
    while people:
        idx = (idx + k - 1) % len(people)
        order.append(people.pop(idx))
    return order


if __name__ == "__main__":
    print("JOSEPHUS PROBLEM (n=7, k=3)")
    print("Survivor (0-indexed):", josephus(7, 3))
    print("Elimination order:", josephus_order(7, 3))
    
