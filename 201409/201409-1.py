def get_all():
    num = int(input())
    values = input().split(' ')
    for i in range(num):
        values[i] = int(values[i])
    cnt = 0
    # 一开始这里写for value in values 就不行，很奇怪。
    # 以前for循环也挺经常出现问题的， 为了避免还是用range来做角标的形势吧。
    for i in range(num):
        if values[i] + 1 in values:
            cnt += 1
    print(cnt)


get_all()
