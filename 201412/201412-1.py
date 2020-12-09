def get_all():
    num = int(input())
    visitor_in = input().split(' ')
    dic = {}
    ans = ''
    for i in range(num):
        visitor_in[i] = int(visitor_in[i])
    for i in range(num):
        if visitor_in[i] not in dic.keys():
            dic[visitor_in[i]] = 1
        else:
            dic[visitor_in[i]] += 1
        ans = ans + str(dic[visitor_in[i]]) + ' '
    ans.rstrip(' ')
    print(ans)


get_all()
