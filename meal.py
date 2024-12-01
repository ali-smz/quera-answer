import math

def calculate_min_cost(t, shams):
    results = []    
    for i in range(t):
        k, j = shams[i][:2]
        kabab, joojeh, mix = shams[i][2:]
  
        cost1 = math.ceil((k / 2)) * kabab + math.ceil((j / 2)) * joojeh
       
        cost2 = (max(k, j)) * mix
        
        num_mixes = min(k, j)
        remaining_k = k - num_mixes
        remaining_j = j - num_mixes
        cost3 = num_mixes * mix + math.ceil((remaining_k / 2)) * kabab + math.ceil((remaining_j / 2)) * joojeh
        
        min_cost = min(cost1, cost2, cost3)
        results.append(min_cost)
    return results

t = int(input())
shams = [list(map(int, input().split())) + list(map(int, input().split())) for _ in range(t)]

results = calculate_min_cost(t, shams)
print("\n".join(map(str, results)))
