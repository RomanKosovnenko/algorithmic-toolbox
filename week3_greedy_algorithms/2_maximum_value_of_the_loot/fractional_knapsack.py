from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    prices = {values[p]/weights[p]: p for p in range(len(values))}
    pl = sorted(prices.keys(), reverse=True)
    for i in pl:
        if capacity == 0:
            break
        idx = prices[i]
        w = min(capacity, weights[idx])
        capacity -= w
        value += w * i
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
