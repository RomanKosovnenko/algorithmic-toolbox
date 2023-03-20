from itertools import combinations

def merge_sort1(a):
    if len(a) == 1:
        return a, 0
    #divide
    m = len(a)//2
    left, count_l = merge_sort1(a[:m])
    right, count_r = merge_sort1(a[m:])
    #merge

    sorted_list, count_m = merge(left, right)
    
    return sorted_list,count_l + count_r + count_m

    
def merge(left, right):
    merged = []
    inv = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv += len(left) - i
    
    merged += left[i:]
    merged += right[j:]
    
    return merged, inv

def inversions_not_naive(a):
    _, count = merge_sort1(a)
    return count


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_not_naive(elements))
