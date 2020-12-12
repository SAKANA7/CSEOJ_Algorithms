# 先不做了哈哈 但感觉考试时时间充裕的话是能混到小于50分的
# 前两题用了小于50分钟吧
# 今晚继续做做其他几届1、2题~
def get_all():
    q = int(input())
    mn = input().split(' ')
    m, n = int(mn[0]), int(mn[1])
    orders = []
    infos_in = []
    infos_out = []
    for i in range(n):
        tmp = input().split(' ')
        tmp[1] = int(tmp[1])
        orders.append(tmp)
    s = int(input())
    for i in range(s):
        tmp = input().split(' ')
        for j in range(len(tmp)):
            tmp[j] = int(tmp[j])
        infos_in.append(tmp)
    for i in range(s):
        tmp = input().split(' ')
        for j in range(len(tmp)):
            tmp[j] = int(tmp[j])
        infos_out.append(tmp)
    # print(orders)
    # print(infos_in)
    # print(infos_out)

    # 对s个输入
    for i in range(s):
        orders_out = [-1 for _ in range(n)]
        # 对n个器件
        while -1 in orders_out:
            for j in range(n):
                if orders[0] == 'NOT':
                    value1 = orders[2]

                elif orders[0] == 'AND':

                elif orders[0] == 'OR':
                elif orders[0] == 'XOR':
                elif orders[0] == 'AND':
                elif orders[0] == 'NOR':


get_all()
