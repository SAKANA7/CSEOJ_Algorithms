def get_all():
    n = input()
    n = int(n)
    triangle = [[0]*n for _ in range(n)]
    for i in range(n):
        line = input()
        triangle[i] = line.split(' ')

        for j in range(len(triangle[i])):
            triangle[i][j] = int(triangle[i][j])

    r = maximumTotal(triangle)
    print (r)

def maximumTotal(triangle):
    n = len(triangle)
    f = [[0] * n for _ in range(n)]
    f[0][0] = triangle[0][0]
    for i in range(1, n):
        f[i][0] = triangle[i][0] + f[i - 1][0]
        for j in range(1, i):
            f[i][j] = max(f[i - 1][j], f[i - 1][j - 1]) + triangle[i][j]
        f[i][i] = triangle[i][i] + f[i - 1][i - 1]
    return max(f[n - 1])


get_all()
