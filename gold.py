# Получение максимальной ценности в рюкзаке при минимальном весе

def max_weight(a, W, n):
    value = [[0 for w in range(W+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,W+1):
            value[i][w] = value[i-1][w]
            if a[i-1] <= w:
                value[i][w] = max(value[i][w], value[i-1][w-a[i-1]]+a[i-1])
    return value[n][W]


if '__main__' == __name__:
    W, n = tuple(map(int, input().split()))
    a = tuple(map(int, input().split()))
    ans = max_weight(a, W, n)
    print(ans)
