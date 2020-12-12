def get_all():
    nk = input().split(' ')
    n, k = int(nk[0]), int(nk[1])
    children_in_game = [i + 1 for i in range(n)]
    flag = 0
    while k == 1 and n > 1:
        print(children_in_game[-1])
        return 0
    while len(children_in_game) > 1:
        deleted_num = 0  # 已经删除的数目
        for i in range(len(children_in_game)):
            flag += 1
            unit_digit = int(str(flag)[-1])  # 个位
            if unit_digit == k or flag % k == 0:
                children_in_game.remove(children_in_game[i - deleted_num])
                deleted_num += 1
    print(children_in_game[0])


get_all()
