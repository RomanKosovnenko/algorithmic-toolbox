def evaluate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def maximum_value(s):
    n = len(s) // 2 + 1
    M = [[0] * n for _ in range(n)]
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        M[i][i] = int(s[2 * i])
        m[i][i] = int(s[2 * i])
    for s_len in range(2, n + 1):
        for i in range(n - s_len + 1):
            j = i + s_len - 1
            M[i][j] = float('-inf')
            m[i][j] = float('inf')
            for k in range(i, j):
                op = s[2 * k + 1]
                a = evaluate(M[i][k], op, M[k + 1][j])
                b = evaluate(M[i][k], op, m[k + 1][j])
                c = evaluate(m[i][k], op, M[k + 1][j])
                d = evaluate(m[i][k], op, m[k + 1][j])
                M[i][j] = max(M[i][j], a, b, c, d)
                m[i][j] = min(m[i][j], a, b, c, d)
    return M[0][n - 1]


if __name__ == "__main__":
    print(maximum_value(input()))
