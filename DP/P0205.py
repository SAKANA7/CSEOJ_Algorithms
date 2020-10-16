#  不知道为什么不能AC
def get_all():
    mn = input()
    mn = mn.split(" ")
    n, m = int(mn[0]), int(mn[1])
    calories = [[0] * m for _ in range(n)]
    for i in range(m):
        tmp = input()
        tmp = tmp.split(" ")
        for j in range(len(tmp)):
            calories[i][j] = int(tmp[j])
    x = max_distance(n, m, calories)
    print(x)


# 两人在网格中只能相遇一次的意思是 两个人只能有重复的一个网格，就是碰面的，而不是说，只能碰面一次，但可以走重复网格。
def max_distance(n, m, calories):
    dp1 = [[0] * (m + 2) for _ in range(n + 2)]
    dp2 = [[0] * (m + 2) for _ in range(n + 2)]
    dp3 = [[0] * (m + 2) for _ in range(n + 2)]
    dp4 = [[0] * (m + 2) for _ in range(n + 2)]
    # 左上
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp1[i][j] = calories[i - 1][j - 1] + max(dp1[i - 1][j], dp1[i][j - 1])
    # 左下
    for i in range(n, 0, -1):
        for j in range(1, m + 1):
            dp2[i][j] = calories[i - 1][j - 1] + max(dp2[i + 1][j], dp2[i][j - 1])
    # 右上
    for i in range(1, n + 1):
        for j in range(m, 0, -1):
            dp3[i][j] = calories[i - 1][j - 1] + max(dp3[i - 1][j], dp3[i][j + 1])
    # 右下
    for i in range(n, 0, -1):
        for j in range(m, 0, -1):
            dp4[i][j] = calories[i - 1][j - 1] + max(dp4[i + 1][j], dp4[i][j + 1])

    x = 0
    for i in range(2, n):
        for j in range(2, m):
            x = max(x, dp1[i][j - 1] + dp4[i][j + 1] + dp2[i + 1][j] + dp3[i - 1][j])
            x = max(x, dp1[i - 1][j] + dp4[i + 1][j] + dp2[i][j - 1] + dp4[i][j + 1])
    return x


get_all()
