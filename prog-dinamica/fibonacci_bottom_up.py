def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]

    memo = [0, 1]
    for i in range(2, n):
        memo.append(memo[i - 1] + memo[i - 2])
    return memo