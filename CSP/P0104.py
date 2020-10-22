# 没有AC就很奇怪？
"""
20/10/22 update:这和LC011还是不一样的，LC011移动指针的原因是：对应的数字较小的那个指针不可能再作为容器的边界了。
即：如果不移动对应数字较小的指针，就不可能有新解。
这道题并不是，如果min在切片中间，那么不管怎么移动，除非通过移动排除了当前最小值，否则不会有新解。
这么想这样的思路似乎是不够完整合理的。（暂时没想好怎么证明）
所以：逐个矩形遍历，向两边无限延伸。
"""
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
