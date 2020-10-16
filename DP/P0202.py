def get_all():
    n = input()
    n = int(n)
    dp = init_route_num()
    for i in range(n):
        tmp = input()
        tmp = tmp.split(' ')
        distance = int(tmp[1]) - int(tmp[0])
        print(dp[distance])


def init_route_num():
    dp = [0 for _ in range(50)]
    dp[0], dp[1] = 1, 1
    for i in range(1, 50):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp


get_all()
