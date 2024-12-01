def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

fibs = []
res =[]
n = int(input())

for i in range(12):
    fibs.append(fibonacci(i))

for i in range(1 , n+1):
    if i in fibs : 
        res.append("+")
    else:
        res.append("-")

print(''.join(res))
