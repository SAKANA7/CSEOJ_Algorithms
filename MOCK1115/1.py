def get_all():
    tmp = input()
    tmp = tmp.split(' ')
    length = int(tmp[0])  # 序列长度
    frequency = int(tmp[1])  # 操作次数
    tmp = input()
    nums = tmp.split(' ')
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    # print(nums)
    statics = [[0 for _ in range(3)] for j in range(length)]
    # print(statics)
    # statics[i][0], statics[i][1], statics[i][2] = op, l, r
    for i in range(length):
        statics[i] = input()
        statics[i] = statics[i].split(' ')
        for j in range(3):
            statics[i][j] = int(statics[i][j])
    for i in statics:
        l, r = i[1], i[2]
        if i[0] == 1:
            for j in range(l - 1, r):
                nums[j] = -nums[j]
            '''
            for num in nums[l: r + 1]:
                num = -num
            '''
        elif i[0] == 2:
            print(min(nums[l - 1: r]))


get_all()
