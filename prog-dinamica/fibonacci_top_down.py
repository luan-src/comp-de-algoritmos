def fibonacci(n, memo=None):
    if memo is None:
        memo = {}

    def fib(k):
        if k in memo:
            return memo[k]
        if k == 0:
            memo[0] = 0
        elif k == 1:
            memo[1] = 1
        else:
            memo[k] = fib(k - 1) + fib(k - 2)
        return memo[k]

    return [fib(i) for i in range(n)]