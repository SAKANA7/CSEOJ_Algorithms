def get_all():
    num = int(input())  # num个block
    block_xy = [[0 for _ in range(4)] for _ in range(110)]  # x1,y1,x2,y2
    counted = set()  # 已经被记入的点
    for i in range(num):
        tmp = input().split(' ')
        for j in range(4):
            tmp[j] = int(tmp[j])
        block_xy[i] = tmp
    # 第一想法是设置counted把所有已经涂色一次的存进去，对每个矩形内的单元格遍历
    # 只得了40分，因为超时。想到python自带的set，以及set + add速度会更快的玄学经历
    # 最后得到了100分
    # 结果发现最朴素的暴力法也可以ac，好奇怪，但我最开始的代码找不到了，无法研究
    for i in range(num):
        x1, y1, x2, y2 = block_xy[i][0], block_xy[i][1], block_xy[i][2], block_xy[i][3]
        for x in range(x1, x2):
            for y in range(y1, y2):
                counted.add((x, y))
    ans = len(counted)
    print(ans)


get_all()
'''
附上最朴素的暴力法：
n=int(input())
coord=[]
#题目上约定了坐标纸的大小为0到100，所以首先建立一个101*101的数组
for i in range(101):
    y=[]
    for j in range(101):
        y+=[0]
    coord+=[y]
#读入数据：
for i in range(n):
    #读入并将坐标转换为int
    co=input().split()
    for j in range(4):
        co[j]=int(co[j])
    #将左下角到右上角每组数字都置为1，代表这里有了颜色
    for x in range(co[0],co[2]):
        for y in range(co[1],co[3]):
            coord[x][y]=1
count=0
#遍历这个101*101的数组，看有多少个1就是有多少个格子被涂了颜色
for i in range(101):
    for j in range(101):
        if coord[i][j]==1:
            count+=1
print(count)
'''