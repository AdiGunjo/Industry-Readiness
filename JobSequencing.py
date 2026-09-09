def job_sequencing(jobs):
    """jobs: list of (job_id, deadline, profit). Greedy: sort by profit desc,
    schedule each job in the latest free slot <= its deadline.
    Returns (sequence_of_job_ids, total_profit)."""
    jobs_sorted = sorted(jobs, key=lambda j: j[2], reverse=True)
    max_deadline = max(j[1] for j in jobs) if jobs else 0
    slots = [None] * (max_deadline + 1)  # 1-indexed usage
    total_profit = 0
    for job_id, deadline, profit in jobs_sorted:
        for t in range(min(deadline, max_deadline), 0, -1):
            if slots[t] is None:
                slots[t] = job_id
                total_profit += profit
                break
    sequence = [j for j in slots if j is not None]
    return sequence, total_profit

if __name__ == "__main__":
    print("JOB SEQUENCING WITH DEADLINES")
    jobs = [("a", 2, 100), ("b", 1, 19), ("c", 2, 27), ("d", 1, 25), ("e", 3, 15)]
    print(job_sequencing(jobs))
