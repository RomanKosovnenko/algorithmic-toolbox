def majority_element_naive(elements):
    def majority(elements):
        n = len(elements)
        # base case
        if n == 1:
            return elements[0]

        # divide
        left = majority(elements[:n//2])
        right = majority(elements[n//2:])

        # conquer
        if left == right:
            return left

        # combine
        left_count = elements.count(left)
        right_count = elements.count(right)
        if left_count > n//2:
            return left
        elif right_count > n//2:
            return right
        else:
            return None

    ans = majority(elements)
    return 0 if ans is None else 1

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
