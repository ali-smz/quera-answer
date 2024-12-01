import heapq
from collections import defaultdict

def solve():
    n, m, k = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))

    dist = {}
    dist[(1, 0)] = 0 

    pq = [(0, 1, 0)]

    while pq:
        curr_time, u, r = heapq.heappop(pq)

        if (u, r) in dist and curr_time > dist[(u, r)]:
            continue


        for v, t in graph[u]:
            new_time = curr_time + t
            new_r = (r + 1) % k 

            if (v, new_r) not in dist or new_time < dist[(v, new_r)]:
                dist[(v, new_r)] = new_time
                heapq.heappush(pq, (new_time, v, new_r))

    result = dist.get((n, 0), float('inf'))
    print(result if result < float('inf') else -1)

solve()
