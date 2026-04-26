def calculate_average(scores):
    if not scores:
        raise ValueError("Scores list cannot be empty.")

    return sum(scores) / len(scores)