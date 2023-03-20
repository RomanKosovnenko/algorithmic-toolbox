def optimal_summands(n):
    summands = []
    s = n
    i = 1
    while s > 0:
        if s - i <= i:
            summands.append(s)
            s=0
        else:
            summands.append(i)
            s -= i
            i += 1
            
    # write your code here
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
