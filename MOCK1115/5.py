def get_all():
    nm = input().split(' ')
    # print(nm)
    n, m = int(nm[0]), int(nm[1])
    statics = [[0, 0, 0] for _ in range(n)]
    # print(statics)
    count_by_index = [0 for _ in range(n)]
    for i in range(n):
        statics[i] = input().split(' ')
        for j in range(3):
            statics[i][j] = int(statics[i][j])
    # print(statics)
    for i in range(n):
        for j in range(n):
            if i != j:
                if statics[i][0] >= statics[j][0] and statics[i][1] >= statics[j][1] and statics[i][2] >= statics[j][2]:
                    count_by_index[i] += 1
    ans = [0 for _ in range(n)]
    for i in range(n):
        ans[count_by_index[i]] += 1
    for i in range(n):
        print(ans[i])


get_all()
