MOD = 10**9 + 7

def solve(n, edges):
    dist = [float('inf')] * n
    dist[0] = 0
    for u, v, t in edges:
        dist[v] = min(dist[v], dist[u] + t)
    return dist[n-1] if dist[n-1] != float('inf') else -1


n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u-1, v-1, t))

result = solve(n, edges)
print(result)
