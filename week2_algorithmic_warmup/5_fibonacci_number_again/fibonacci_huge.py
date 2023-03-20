def fibonacci_huge_naive(n, m):
    prev, curr = 0, 1
    for i in range(m*m):
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            period_length = i + 1
            break
    k = n % period_length
    prev, curr = 0, 1
    for _ in range(k):
        prev, curr = curr, (prev + curr) % m

    return prev % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
