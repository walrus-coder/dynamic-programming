# Алгоритм определяет возможность рвзделения множества на 3 подмножества одинаковой ценности (здесь вес равен ценности)

def max_weight(a, W_1, W_2, n):
    value = [[[0 for w_2 in range(W_2+1)] for w_1 in range(W_1+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for w_1 in range(0,W_1+1):
            for w_2 in range(0,W_2+1):
                value[i][w_1][w_2] = value[i-1][w_1][w_2]
                if a[i-1] <= w_1:
                    value[i][w_1][w_2] = max(value[i][w_1][w_2], value[i-1][w_1-a[i-1]][w_2] + a[i-1])
                if a[i-1] <= w_2:
                    value[i][w_1][w_2] = max(value[i][w_1][w_2], value[i-1][w_1][w_2-a[i-1]] + a[i-1])
    return value[n][W_1][W_2]

def able_to_split(n,v):
    s = sum(v)
    if s % 3 == 0:
        W = s // 3
    else:
        return 0
    sum_weight = max_weight(v, W, W, n)
    if sum_weight == 2*W:
        return 1
    else:
        return 0

if '__main__' == __name__:
    n = int(input())
    v = list(map(int, input().split()))
    ans = able_to_split(n,v)
    print(ans)
