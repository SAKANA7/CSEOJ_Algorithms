def get_all():
    lineinfo = input().split(' ')
    for i in range(len(lineinfo)):
        lineinfo[i] = int(lineinfo[i])
    # print(lineinfo)
    n, k, t, xl, yd, xr, yu = lineinfo[0], lineinfo[1], lineinfo[2], lineinfo[3], lineinfo[4], lineinfo[5], lineinfo[6]
    num_guo, num_liu = 0, 0  # 经过和逗留
    for i in range(n):
        flag_guo, flag_liu = 0, 0
        tmp = input().split(' ')
        for j in range(len(tmp)):
            tmp[j] = int(tmp[j])
        # print(tmp)
        cnt = 0
        for j in range(0, 2 * t, 2):
            if xl <= tmp[j] <= xr and yd <= tmp[j + 1] <= yu:
                flag_guo = 1
                cnt += 1
                if cnt >= k:
                    flag_liu = 1
            else:
                cnt = 0
        if flag_guo == 1:
            num_guo += 1
        if flag_liu == 1:
            num_liu += 1
    print(num_guo)
    print(num_liu)


get_all()
