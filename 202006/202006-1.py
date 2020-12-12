# 注意输出的大小写
def get_all():
    nm = input().split(' ')
    n, m = int(nm[0]), int(nm[1])
    # infos = []
    A_infos = []
    B_infos = []
    for i in range(n):
        tmp = input().split(' ')
        tmp[0], tmp[1] = int(tmp[0]), int(tmp[1])
        # infos.append(tmp)
        if tmp[2] == 'A':
            A_infos.append(tmp)
        elif tmp[2] == 'B':
            B_infos.append(tmp)
    # ax + by + c = 0
    # print(A_infos)
    # print(B_infos)
    for i in range(m):
        flag = 0
        A_flag, B_flag = 0, 0
        tmp = input().split(' ')
        for j in range(3):
            tmp[j] = int(tmp[j])
        a, b, c = tmp[1], tmp[2], tmp[0]
        test_A_flag = a * A_infos[0][0] + b * A_infos[0][1] + c
        if test_A_flag > 0:
            A_flag, B_flag = 1, -1
        elif test_A_flag < 0:
            A_flag, B_flag = -1, 1
        for j in range(len(A_infos)):
            test_A_flag = a * A_infos[j][0] + b * A_infos[j][1] + c
            if test_A_flag * A_flag < 0:
                flag = 1
                print('No')
                break
        if flag == 0:
            for j in range(len(B_infos)):
                test_B_flag = a * B_infos[j][0] + b * B_infos[j][1] + c
                if test_B_flag * A_flag > 0:
                    flag = 1
                    print('No')
                    break
        if flag == 0:
            print('Yes')


get_all()
