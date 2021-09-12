# Динамический алгоритм выравнивания строк
def edit_distance(str_1, str_2, str_3, n, m, l):
    d = [[[0 for k in range(l+1)] for i in range(n+1)] for j in range(m+1)]
    for k in range(1,l+1):
        for i in range(1,n+1):
            for j in range(1,m+1):
                ins_ = d[j-1][i][k]
                del_ = d[j][i-1][k]
                new_ = d[j][i][k-1]
                mis_ = d[j-1][i-1][k-1] + 0
                match_ = d[j-1][i-1][k-1] + 1
                if str_1[i-1] == str_2[j-1] == str_3[k-1]:
                    d[j][i][k] = max(ins_, del_, new_, match_)
                else:
                    d[j][i][k] = max(ins_, del_, new_, mis_)
    return d[m][n][l]

if '__main__' == __name__:
    n = int(input())
    str_1 = list(input().split())
    m = int(input())
    str_2 = list(input().split())
    l = int(input())
    str_3 = list(input().split())
    ans = edit_distance(str_1, str_2, str_3, n, m, l)
    print(ans)
