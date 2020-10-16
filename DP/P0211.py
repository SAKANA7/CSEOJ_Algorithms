def get_all():
    n = input()
    n = int(n)
    prices = input()
    prices = prices.split(' ')
    for i in range(len(prices)):
        prices[i] = int(prices[i])
    prices.insert(0, '0')
    maxx, num = dp(prices, n)
    print(str(maxx)+' '+str(num))

def dp(prices, n):
    f = [1 for _ in range(n + 1)]
    t = [0 for _ in range(n + 1)]
    maxx = 0
    summ = 0
    for i in range(1, n + 1):
        for j in range(1, i):
            if prices[i] < prices[j]:
                f[i] = max(f[i], f[j]+1)
        if f[i] > maxx:   maxx = f[i]
        for j in range(1, i):
            if f[i] == f[j] and prices[i] == prices[j]:
                t[j] = 0
            elif f[i] == f[j] + 1 and prices[i] < prices[j]:
                t[i] += t[j]
        if not t[i]:
            t[i] = 1
    for i in range(1, n+1):
        if f[i] == maxx:
            summ += t[i]

    return maxx, summ


get_all()