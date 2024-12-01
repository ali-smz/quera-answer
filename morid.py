def calculate_max_diameter(t, scenarios):
    results = []

    for scenario in scenarios:
        n, madrasahs = scenario
        diameters = []

        for m, _ in madrasahs:
            diameters.append(m - 1)

        diameters.sort(reverse=True)

        while len(diameters) > 1:
            largest = diameters.pop(0)
            second_largest = diameters.pop(0)

            new_diameter = largest + second_largest + 1
            diameters.append(new_diameter)
            diameters.sort(reverse=True)

        results.append(diameters[0])

    return results


t = int(input())  
scenarios = []
for _ in range(t):
    n = int(input())
    madrasahs = []
    for _ in range(n):
        m = int(input())
        if m > 1:
            _ = list(map(int, input().split()))
        madrasahs.append((m, []))
    scenarios.append((n, madrasahs))

results = calculate_max_diameter(t, scenarios)
print("\n".join(map(str, results)))
