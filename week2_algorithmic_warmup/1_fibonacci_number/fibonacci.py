def fibonacci_number(n):
    if n <= 1:
        return n
    numbers = [0, 1]+[0]*(n-1)
    for i in range(2, n+1):
        numbers[i] = numbers[i-2] + numbers[i-1]
    return numbers[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

# 0 1 1 2 3 5