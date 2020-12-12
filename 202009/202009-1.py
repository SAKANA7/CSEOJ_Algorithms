def get_all():
    nxy = input().split(' ')
    n, x, y = int(nxy[0]), int(nxy[1]), int(nxy[2])
    cur_3mins = []
    for i in range(3):
        tmp = input().split(' ')
        distance2 = (x - int(tmp[0])) ** 2 + (y - int(tmp[1])) ** 2
        cur_3mins.append([i, distance2])  # [序号，距离]
    for i in range(3, n):
        cur_3mins.sort(key=lambda a: a[1])
        tmp = input().split(' ')
        distance2 = (x - int(tmp[0])) ** 2 + (y - int(tmp[1])) ** 2
        tmp_array = [i, distance2]
        if tmp_array[1] < cur_3mins[2][1] or tmp_array[1] < cur_3mins[1][1] or tmp_array[1] < cur_3mins[0][1]:
            del cur_3mins[2]
            cur_3mins.append(tmp_array)

    for i in range(3):
        print(cur_3mins[i][0] + 1)


get_all()
