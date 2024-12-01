n = int(input())
names = []
for _ in range(n) :
    names.append(input().split()[0])
    
unique={name:names.count(name) for name in set(names)}
print(max(unique.values()))
    

