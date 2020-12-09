def get_all():
    num = int(input())
    values = input()
    values = values.split(' ')
    for i in range(num):
        values[i] = int(values[i])
    cnt = 0
    for value in values:
        if (-value) in values:
            cnt += 1
    print(int(cnt / 2))


get_all()