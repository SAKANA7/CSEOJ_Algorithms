def get_all():
    rnd = input('')
    rnd = int(rnd)
    for i in range(rnd):
        temp = input('')
        temp = int(temp)
        x = climb(temp)
    print(x)


def climb(n):
    x1 = 1
    x2 = 1
    x = 1
    for i in range(2, n):
        x = x1 + x2
        x2 = x1
        x1 = x
    return x


get_all()
