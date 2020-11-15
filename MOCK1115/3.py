import heapq
def get_all():
    frequency = int(input())
    statics = [[0, 0, j] for j in range(frequency)]
    # print(statics)
    for i in range(frequency):
        statics[i] = input()
        statics[i] = statics[i].split(' ')
        for j in range(2):
            statics[i][j] = int(statics[i][j])
    # print(statics)
    heap = []
    index = [] # 存储数字
    for static in statics:
        if static[0] == 1:
            heapq.heappush(heap, static[1])
            index.append(static[1])
        elif static[0] == 2:
            tmp = heapq.nsmallest(static[1], heap) # 最小的static[1]个元素
            for i in range(len(tmp)): # 弹出最小的static[1]个
                heapq.heappop(heap)
            key_value = tmp[-1] # 弹出元素的值
            del tmp[-1]
            for i in tmp: # 除去第static[1]个 其余都弹回去
                heapq.heappush(heap, i)
            index.remove(key_value)
            # print(index)
            enum_index = list(enumerate(index))
            # print(enum_index)
        elif static[0] == 3:
            tmp = heapq.nsmallest(static[1], heap)
            key_value = tmp[-1]
            for i in enum_index:
                if key_value in i:
                    print(i[0] + 1)


get_all()