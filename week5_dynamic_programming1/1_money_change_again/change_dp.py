def change(money):
    MinNumCoins = [float('inf')] * (money+1)
    MinNumCoins[0] = 0
    for i in range(1, money+1):
        for coin in [1, 3, 4]:
            if i >= coin:
                num_coins = MinNumCoins[i-coin] + 1
                MinNumCoins[i] = min(MinNumCoins[i], num_coins)
    return MinNumCoins[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
