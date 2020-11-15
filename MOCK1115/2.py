import heapq
def get_all():
    frequency = int(input())
    statics = [[0 for _ in range(2)] for j in range(frequency)]
    # print(statics)
    for i in range(frequency):
        statics[i] = input()
        statics[i] = statics[i].split(' ')
        for j in range(2):
            statics[i][j] = int(statics[i][j])
    # print(statics)
    heap = []
    for static in statics:
        if static[0] == 1:
            heapq.heappush(heap, static[1])
        elif static[0] == 2:
            tmp = heapq.nsmallest(static[1], heap)
            for i in range(len(tmp)):
                heapq.heappop(heap)
            del tmp[-1]
            for i in tmp:
                heapq.heappush(heap, i)
        elif static[0] == 3:
            tmp = heapq.nsmallest(static[1], heap)
            print(tmp[-1])


get_all()
