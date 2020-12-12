"""
一开始TLE 因为自己想的是用字符串加完再输出一整行，实际上可以用print(matrix[x][y] end=' '的方法)
减少了遍历时的加法所消耗的时间。
"""

# 这道题还是得画图找规律然后一点点做出来，画图是必要的，找到奇数偶数的分类讨论很重要
# 奇数偶数的分类 主要还是看到了x + y是奇数的时候才会左下，否则会有右上。


def get_all():
    num = int(input())
    matrix = [[0 for _ in range(num + 5)] for _ in range(num + 5)]  # 5无实际含义，仅防越界
    # ans = ''
    for i in range(num):
        tmp = input().split(' ')
        for j in range(num):
            matrix[i + 1][j + 1] = int(tmp[j])
    # print(matrix)
    x, y = 1, 1
    while x != num or y != num:
        print(matrix[x][y], end=' ')
        if (x + y) % 2 == 0:
            if y == num:
                # ans = ans + str(matrix[x][y]) + ' '
                x += 1
            elif x == 1:
                # ans = ans + str(matrix[x][y]) + ' '
                y += 1
            else:
                # ans = ans + str(matrix[x][y]) + ' '
                x -= 1
                y += 1
        elif (x + y) % 2 == 1:
            if x == num:
                # ans = ans + str(matrix[x][y]) + ' '
                y += 1
            elif y == 1:
                # ans = ans + str(matrix[x][y]) + ' '
                x += 1
            else:
                # ans = ans + str(matrix[x][y]) + ' '
                x += 1
                y -= 1
    # ans += str(matrix[num][num])
    print(matrix[num][num])


get_all()
