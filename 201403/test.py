#窗口
#用列表来分别储存区域和点
n,m = map(int,input().split())
a = []
b = []
#利用字典来给区域窗口命名
c = {}
#判断点list2是否在区域list1中
def include(list1,list2): 
    if (list2[0] in range(list1[0],list1[2]+1)) and (list2[1] in range(list1[1],list1[3]+1)):
        return True
for i in range(n):
    a.append(list(map(int,input().split())))
    c[str(a[i])] = i
for i in range(m):
    b.append(list(map(int,input().split())))
for i in range(m):
    for j in range(n):
        #从最上层窗口开始遍历，如果在点在区域内，输出窗口编号，并将窗口提到最上方，即将列表放到末端（删除之后插入到最后）
        if include(a[-1-j],b[i]):
            print(int(c[str(a[-1-j])])+1)
            temp = a[-1-j]
            del a[-1-j]
            a.append(temp)
            break
        #遍历到最后都没有的话，输出IGNORED
        if j == n-1:
            print('IGNORED')