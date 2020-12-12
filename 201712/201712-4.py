# 仅过了一个点
def get_all():
    nm = input().split(' ')
    n, m = int(nm[0]), int(nm[1])
    roads = []
    for i in range(m):
        tmp = input().split(' ')
        for j in range(4):
            tmp[j] = int(tmp[j])
        roads.append(tmp)
    # print(roads)
    '''https://blog.csdn.net/weixin_42482896/article/details/107550565'''
    roads.sort(key=lambda x: x[1])
    # print(roads)
    routes = routes_generate(roads, m)
    routes_tmp = []
    for route in routes:
        tmp = []
        for i in range(len(route)):
            tmp.append(int(route[i]))
        # print(tmp)
        routes_tmp.append(tmp)
    routes = routes_tmp
    # print(routes)
    dic = dic_generate(roads, m)
    # print(dic)
    ans = float('inf')
    for route in routes:
        length = 0
        tmp_length = 0
        for i in range(1, len(route)):
            start = route[i - 1]
            end = route[i]
            if dic[(start, end)][0] == 0:
                length += tmp_length * tmp_length
                tmp_length = 0
                length += dic[(start, end)][1]
            elif dic[(start, end)][0] == 1:
                tmp_length += dic[(start, end)][1]
            if i == len(route) - 1:
                length += tmp_length * tmp_length
        ans = min(ans, length)
    print(ans)


def dic_generate(roads, m):
    dic = {}
    for road in roads:
        if road[0] == 0:
            dic[(road[1], road[2])] = [0, road[3]]
        elif road[0] == 1:
            dic[(road[1], road[2])] = [1, road[3]]
    return dic


def routes_generate(roads, m):
    routes = ['1']
    tmp_routes = set()  # 已经生成过的子路径
    length = -1
    while True:
        for j in range(len(routes)):
            for i in range(m):
                if int(routes[j][-1]) == roads[i][1]:
                    tmp = routes[j] + str(roads[i][2])
                    tmp_routes.add(tmp)
        routes = list(tmp_routes)
        if length == len(routes):
            break
        length = len(routes)
    num_deleted = 0
    for i in range(len(routes)):
        if routes[i - num_deleted][-1] != '6':
            del routes[i - num_deleted]
            num_deleted += 1
    # print(routes)
    return routes


get_all()
