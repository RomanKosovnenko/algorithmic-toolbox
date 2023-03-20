from random import randint


def partition3(array, left, right):
    pivot_value = array[left]
    p_l = i = left
    p_e = right

    while i <= p_e:
        if array[i] < pivot_value:
            array[p_l], array[i] = array[i], array[p_l]
            p_l += 1
            i += 1
        elif array[i] > pivot_value:
            array[p_e], array[i] = array[i], array[p_e]
            p_e -= 1
        else:
            i += 1

    return p_l, p_e


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
