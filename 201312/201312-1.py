def get_all():
    num = int(input(''))
    array1 = input('')
    array1 = array1.split(' ')
    for i in range(num):
        array1[i] = int(array1[i])
    dic = {}
    flag, times = 0, 0  # 出现次数最多的数字，出现的次数。
    for i in range(num):
        if array1[i] not in dic.keys():
            dic[array1[i]] = 1
        else:
            dic[array1[i]] += 1
        if dic[array1[i]] > times:
            times = dic[array1[i]]
            flag = array1[i]
        elif dic[array1[i]] == times:
            if array1[i] < flag:
                flag = array1[i]
    print(flag)


get_all()
