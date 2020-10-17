def get_all():
    tmp = input()
    tmp = tmp.split(' ')
    n = len(tmp)
    for i in range(n):
        tmp[i] = int(tmp[i])  # tmp代表n m x y
    ans = dp(tmp)
    print(ans)


def dp(tmp):
    a = [[0] * 21 for _ in range(21)]  # 记录路径数
    b = [[0] * 21 for _ in range(21)]  # 记录是否为控制区域
    n, m = tmp[0], tmp[1]
    x, y = tmp[2], tmp[3]
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    b[x][y] = 1
    for i in range(8):
        if 0 <= x + dx[i] <= n and 0 <= y + dy[i] <= m:
            b[x + dx[i]][y + dy[i]] = 1
            a[x + dx[i]][y + dy[i]] = 0
    '''
    for i in range(n + 1):
        if not b[i][0]:
            a[i][0] = 1
    for i in range(m + 1):
        if not b[0][i]:
            a[0][i] = 1
    '''
    k = 0
    while k <= n and not b[k][0]:
        a[k][0] = 1
        k += 1

    l = 0
    while l <= m and not b[0][l]:
        a[0][l] = 1
        l += 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if not b[i][j]:
                a[i][j] = a[i][j - 1] + a[i - 1][j]
    return a[n][m]


get_all()
