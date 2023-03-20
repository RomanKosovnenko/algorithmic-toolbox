def fibonacci_sum_squares(n):
    a = [0, 1]
    for i in range(2, 60):
        a.append(a[i - 1] + a[i - 2])
    n = n % 60
    if n < 0:
        n += 60
    su = 0
    for j in range(n + 1):
        su += a[j % 60]**2

    return su % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
