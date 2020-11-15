sr = input().split()
n, q = int(sr[0]), int(sr[1])  # q代表q行, n代表长度为n的序列A
command = []
num = []
u = [314882150829468584, 427197303358170108, 1022292690726729920, 1698479428772363217, 2006101093849356424]


def han(x):
    return (x % 2009731336725594113) % 2019


for i in range(q):
    command.append(input().split())
for i in range(n + 1):
    num.append(i)
for item in command:
    left, right = int(item[0]), int(item[1])
    s = 0
    for i in range(left, right + 1):
        s += han(num[i])
    print(s)
    t = s % 5
    for i in range(left, right + 1):
        num[i] *= u[t]
