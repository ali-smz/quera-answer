import sys

sys.setrecursionlimit(1000 * 100 + 10)

def dfs(s):
    mark[s] = True
    for i in range(0, n):
        if x[s] == x[i] or y[s] == y[i]:
            if not mark[i]:
                dfs(i)
    return

n = int(input())



mark = [False] * n

x = [None] * n
y = [None] * n

adj = [[False for i in range(0, n)] for i in range(0, n)]

for i in range(0, n):
    x[i], y[i] = map(int, input().split())

ans = 0
for i in range(0, n):
    if not mark[i]:
        ans += 1
        dfs(i)
print(int(ans - 1))