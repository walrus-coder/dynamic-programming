# Динамический алгоритм расстановки скобок в выражении для получения его максимального значения на выходе
def max_expression(s, op):
    l_s = len(s)
    l_op = len(op)
    operand = {'+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y}
    M = [[0 for j in range(l_s)] for i in range(l_s)]
    m = [[0 for j in range(l_s)] for i in range(l_s)]
    for i in range(l_s):
        M[i][i] = s[i]
        m[i][i] = s[i]
    for k in range(1,l_s):
        for i in range(l_s-k):
            j = k + i
            min_ = 90*l_s
            max_ = -90*l_s
            for q in range(i,j):
                a = operand[op[q]](M[i][q], M[q+1][j])
                b = operand[op[q]](M[i][q], m[q+1][j])
                c = operand[op[q]](m[i][q], M[q+1][j])
                d = operand[op[q]](m[i][q], m[q+1][j])
                min_ = min(min_, a, b, c, d)
                max_ = max(max_, a, b, c, d)
            M[i][j], m[i][j] = max_, min_
    return M[0][l_s-1]


if '__main__' == __name__:
    a =  input()
    l = len(a)
    s = []
    op = []
    for i in range(0, l, 2):
        s.append(int(a[i]))
        if i+1 != l:
            op.append(a[i+1])
    ans = max_expression(s, op)
    print(ans)
