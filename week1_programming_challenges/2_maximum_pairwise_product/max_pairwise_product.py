def max_pairwise_product(numbers):
    max1 = max(numbers)
    numbers.remove(max1)

    return max1 * max(numbers)


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
