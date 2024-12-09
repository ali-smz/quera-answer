n = int(input())
res = []
for _ in range(n):
    x,v = map(int , input().split())
    res.append(x/v)
    
print(min(res))
