from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    max_product = 0
    for _ in range(len(first_sequence)):
        m1 = max(first_sequence)
        m2 = max(second_sequence)
        max_product += max(first_sequence)*max(second_sequence)
        first_sequence.remove(m1)
        second_sequence.remove(m2)

    return max_product


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
