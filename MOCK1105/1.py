def get_all():
    n = input()
    n = int(n)
    pass_num = input()
    pass_num = pass_num.split(' ')
    for i in range(len(pass_num)):
        pass_num[i] = int(pass_num[i])
    pass_num.insert(0, 0)
    ans = func(n, pass_num)
    print(ans)


def func(n, pass_num):
    known = [[i] for i in range(n + 1)]
    cnt = [1 for i in range(n + 1)]
    while True:
        tmp = []
        for i in range(1, n + 1):
            for j in known[i]:
                known[pass_num[i]].append(j)
                tmp.append(j)
            if pass_num[i] in known[i]:
                return max(cnt)
        tmp = list(set(tmp))
        for i in range(n + 1):
            if i in tmp:
                cnt[i] += 1
        print(known)



get_all()