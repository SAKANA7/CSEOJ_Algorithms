def get_all():
    nm = input().split(' ')
    n, m = int(nm[0]), int(nm[1])  # n个窗口, m次click
    window_xy = [[0 for _ in range(4)] for _ in range(20)]
    click_xy = [[0 for _ in range(2)] for _ in range(20)]
    # 一开始runtime error就是因为这个数组开小了，做前两题的时候尽可能开大一点，因为一般不会超过空间的

    for i in range(n):
        tmp = input().split(' ')
        for j in range(4):
            tmp[j] = int(tmp[j])
        window_xy[i] = tmp
    for i in range(m):
        tmp = input().split(' ')
        for j in range(2):
            tmp[j] = int(tmp[j])
        click_xy[i] = tmp

    window_dic = window_xy[:]  # window_dic为存储序号用

    # print(window_xy)
    # print(window_dic)
    # print(click_xy)
    for i in range(m):
        click_x, click_y = click_xy[i][0], click_xy[i][1]
        for j in range(n - 1, -1, -1):
            if window_xy[j][0] <= click_x <= window_xy[j][2] and window_xy[j][1] <= click_y <= window_xy[j][3]:
                for k in range(n):  # 打印出窗口序号
                    if window_xy[j] == window_dic[k]:
                        print(k + 1)
                tmp = window_xy[j]
                del window_xy[j]
                window_xy[n - 1] = tmp
                # print(window_xy)
                break
            if j == 0:
                print('IGNORED')


get_all()
