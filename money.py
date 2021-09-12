# Функция для возвращения требуемой суммы денег через минимальное количество монет

def min_change(m):
    den = [1,3,4]
    work = [i for i in range(m+1)]
    work[0] = 0
    work_1 = m+1
    work_2 = m+1
    work_3 = m+1
    for i in range(1, m+1):
        if i - 1 >= 0:
            work_1 = work[i-1] + 1
        if i - 3 >= 0:
            work_2 = work[i-3] + 1
        if i - 4 >= 0:
            work_3 = work[i-4] + 1
        work[i] = min(work_1, work_2, work_3)
    return work[-1]

if '__main__' == __name__:
    m = int(input())
    ans = min_change(m)
    print(ans)

