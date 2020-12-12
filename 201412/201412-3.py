'''
输入问题已经解决，但还是错误，有些不理解，周五晚上或者周六再debug
'''
import sys


def get_all():
    orders = []
    dic_buy = {}
    dic_sell = {}
    # print(lines)
    for line in sys.stdin:
        tmp = line
        if 'buy' not in tmp and 'sell' not in tmp and 'cancel' not in tmp:
            break
        if 'cancel' not in tmp:
            orders.append(tmp)
        else:
            tmp = tmp.split(' ')
            # print(tmp)
            del orders[int(tmp[1]) - 1]
    # print(orders)
    for i in range(len(orders)):
        tmp = orders[i].split(' ')
        # print(tmp)
        if 'buy' in orders[i]:
            if float(tmp[1]) not in dic_buy.keys():
                dic_buy[float(tmp[1])] = int(tmp[2])
            else:
                dic_buy[float(tmp[1])] += int(tmp[2])

        elif 'sell' in orders[i]:
            if float(tmp[1]) not in dic_sell.keys():
                dic_sell[float(tmp[1])] = int(tmp[2])
            else:
                dic_sell[float(tmp[1])] += int(tmp[2])
    tmp = sorted(dic_sell.items(), key=lambda x: x[0])
    new_dic_sell = {i[0]: i[1] for i in tmp}
    tmp = sorted(dic_buy.items(), key=lambda x: x[0])
    new_dic_buy = {i[0]: i[1] for i in tmp}
    # print(new_dic_buy)
    # print(new_dic_sell)
    b = max(new_dic_buy.keys())
    c = max(new_dic_sell.keys())
    ans_price, ans_amount = 0.0, 0  # 成交价和成交量
    for i in range(int(c * 100), int(b * 100) + 1):
        p0 = float(i / 100)
        tmp_amount, tmp_amount_sell, tmp_amount_buy = 0, 0, 0
        for price in new_dic_sell.keys():
            if price <= p0:
                tmp_amount_sell += new_dic_sell[price]
        for price in new_dic_buy.keys():
            if price >= p0:
                tmp_amount_buy += new_dic_buy[price]
        tmp_amount = min(tmp_amount_sell, tmp_amount_buy)
        if tmp_amount >= ans_amount:
            ans_amount = tmp_amount
            ans_price = p0
    print('%.2f' % ans_price, end=' ')
    print(ans_amount)


get_all()
