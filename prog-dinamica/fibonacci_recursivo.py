def fibonacci(n, sequence=None):
    if sequence is None:
        sequence = []

    if len(sequence) >= n:
        return sequence[:n]

    if len(sequence) == 0:
        sequence.append(0)
    elif len(sequence) == 1:
        sequence.append(1)
    else:
        sequence.append(sequence[-1] + sequence[-2])

    return fibonacci(n, sequence)
