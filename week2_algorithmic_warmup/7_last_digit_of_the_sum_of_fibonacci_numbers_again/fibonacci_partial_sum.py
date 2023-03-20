# Uses python3
import sys

def fibonacci_partial_sum_naive(m, n):
    a = [0, 1]
    for i in range(2, 60):
        a.append(a[i - 1] + a[i - 2])
    m = m % 60
    n = n % 60
    if n < m:
        n += 60
    su = 0
    for j in range(m, n + 1):
        su += a[j % 60]

    return su % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))
