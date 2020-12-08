def get_all():
    max_area = 0
    length = 0  # length = i - j + 1
    num = int(input(''))
    heights = input('').split(' ')
    # print(heights)
    for i in range(num):
        heights[i] = int(heights[i])
    # print(heights)
    for i in range(num):
        min_tmp = float('inf')  # [i,j]之间的最小height
        for j in range(i, -1, -1):
            min_tmp = min(min_tmp, heights[j])
            length = i - j + 1
            area_tmp = length * min_tmp
            max_area = max(max_area, area_tmp)
    print(max_area)


get_all()
'''
也有更正确的解法，通过限制条件减少了时间复杂度，属于完成本代码后的优化行为：
在oj上测试结果是接近两倍的时间差。
def get_all():
    num = input()
    num = int(num)
    heights = input()
    heights = heights.split(' ')
    n = len(heights)
    ans = 0
    for i in range(num):
        heights[i] = int(heights[i])
    for i in range(num):
        weight = 1
        for j in range(i + 1, num):
            if heights[j] >= heights[i]:
                weight += 1
            else:
                break
        if i > 0:
            for j in range(i - 1, -1, -1):
                if heights[j] >= heights[i]:
                    weight += 1
                else:
                    break
        ans = max(ans, heights[i] * weight)
    print(ans)


get_all()

'''


