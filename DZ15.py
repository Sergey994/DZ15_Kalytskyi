def is_simple(n: int):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
