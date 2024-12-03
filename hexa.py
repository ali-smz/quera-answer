directions = {
    'A': (1, -1, 0),
    'B': (0, -1, 1),
    'C': (-1, 0, 1),
    'D': (-1, 1, 0),
    'E': (0, 1, -1),
    'F': (1, 0, -1)
}

t = int(input()) 
results = []

for _ in range(t):
    path = input().strip()
    x, y, z = 0, 0, 0 
    for move in path:
        dx, dy, dz = directions[move]
        x += dx
        y += dy
        z += dz

    distance = max(abs(x), abs(y), abs(z))
    results.append(distance)

print('\n'.join(map(str, results)))
