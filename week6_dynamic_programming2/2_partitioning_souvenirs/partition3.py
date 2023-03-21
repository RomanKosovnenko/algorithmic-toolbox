from sys import stdin


def partition3(values):
    capacity = sum(values)
    if capacity % 3 != 0:
        return 0
    capacity //= 3
    subset_sums = [0] * 3
    indices = [[] for _ in range(3)]

    def helper(curr_index):
        if curr_index == len(values):
            return subset_sums[0] == subset_sums[1] == subset_sums[2]

        for i in range(3):
            if subset_sums[i] + values[curr_index] <= capacity:
                subset_sums[i] += values[curr_index]
                indices[i].append(curr_index)
                if helper(curr_index + 1):
                    return 1
                subset_sums[i] -= values[curr_index]
                indices[i].pop()

        return 0

    return helper(0)


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
