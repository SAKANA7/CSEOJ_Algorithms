def get_all():
    n = input()
    n = int(n)
    length = input()
    length = length.split(' ')
    for i in range(len(length)):
        length[i] = int(length[i])
    length.insert(0, '0')
    length[0] = int(length[0])
    maxx = dp(length, n)
    print(maxx)


def dp(length, n):
    f = [1 for _ in range(n)]
    f.insert(0, 0)
    g = [1 for _ in range(n)]
    g.insert(0, 0)
    for i in range(2, n + 1):
        for j in range(1, i):
            if length[i] > length[j]:
                f[i] = max(f[i], f[j] + 1)

    for i in range(n-1, 0, -1):
        for j in range(i + 1, n + 1):
            if length[i] > length[j]:
                g[i] = max(g[i], g[j] + 1)

    maxx = 0
    for i in range(1, n+1):
        tmp = f[i] + g[i] -1
        if tmp > maxx:
            maxx = tmp

    return n - maxx


get_all()