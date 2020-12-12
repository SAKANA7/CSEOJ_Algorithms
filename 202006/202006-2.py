def get_all():
    """
    nab = input().split(' ')
    n, a, b = int(nab[0]), int(nab[1]), int(nab[2])
    """
    n, a, b = map(int, input().split())
    # vector_a, vector_b = [0 for _ in range(n)], [0 for _ in range(n)]
    # dic_a, dic_b = {}
    dic_not0_a = {}
    dic_not0_b = {}
    for i in range(a):
        tmp = input().split(' ')
        tmp[0], tmp[1] = int(tmp[0]), int(tmp[1])
        # vector_a[tmp[0] - 1] = tmp[1]
        dic_not0_a[tmp[0] - 1] = tmp[1]
    for i in range(b):
        tmp = input().split(' ')
        tmp[0], tmp[1] = int(tmp[0]), int(tmp[1])
        # vector_b[tmp[0] - 1] = tmp[1]
        dic_not0_b[tmp[0] - 1] = tmp[1]
    ans = 0
    for key in dic_not0_a.keys():
        if key in dic_not0_b.keys():
            ans += dic_not0_a[key] * dic_not0_b[key]

    print(ans)


get_all()
'''
import sys


def input2num():
    return map(int, input().split())


dim, cap_a, cap_b = input2num()
a = {}
tol = 0

for line in sys.stdin.readlines():
    i, n = map(int, line.split())
    if cap_a > 0:
        a[i] = n
        cap_a -= 1
    else:
        if i in a:
            tol += n * a[i]

print(tol)
从csdn看到一种从stdin读入的方法，在读取时即进行优化，速度更快。
'''