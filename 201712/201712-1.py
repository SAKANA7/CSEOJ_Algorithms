def get_all():
    num = int(input())
    values = input().split(' ')
    for i in range(num):
        values[i] = int(values[i])
    min_difference_value = float('inf')
    for i in range(num):
        for j in range(i + 1, num):
            if abs(values[i] - values[j]) < min_difference_value:
                min_difference_value = abs(values[i] - values[j])
    print(min_difference_value)


get_all()
