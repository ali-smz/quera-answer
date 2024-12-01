import heapq

def find_minimum_time(n, m, k, flights):
    INF = float('inf')
    dp = [[INF] * k for _ in range(n + 1)]
    dp[1][0] = 0  
    
    graph = [[] for _ in range(n + 1)]
    for u, v, t in flights:
        graph[u].append((v, t))

    pq = [(0, 1, 0)]  
    while pq:
        current_time, current_city, current_mod = heapq.heappop(pq)
        
        if current_time > dp[current_city][current_mod]:
            continue
        
        for neighbor, travel_time in graph[current_city]:
            next_time = current_time + travel_time
            next_mod = (current_mod + 1) % k     
            
            if next_time < dp[neighbor][next_mod]:
                dp[neighbor][next_mod] = next_time
                heapq.heappush(pq, (next_time, neighbor, next_mod))
    

    result = dp[n][0]
    return result if result != INF else -1

n, m, k = map(int, input().split())
flights = []
for _ in range(m):
    u, v, t = map(int, input().split())
    flights.append((u, v, t))

result = find_minimum_time(n, m, k, flights)
print(result)
