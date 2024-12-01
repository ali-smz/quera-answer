def calculate_final_sum(n, k, cards, thresholds):
    cards = sorted([(a, b, i) for i, (a, b) in enumerate(cards)])
    thresholds.sort()

    current_values = [a for a, b, _ in cards]
    flipped = [False] * n

    card_index = 0
    for t in thresholds:
        while card_index < n and cards[card_index][0] <= t:
            a, b, i = cards[card_index]
            if not flipped[i]:
                current_values[i] = b
                flipped[i] = True
            else:
                current_values[i] = a
                flipped[i] = False
            card_index += 1

    return sum(current_values)

n, k = map(int, input().split())
cards = [tuple(map(int, input().split())) for _ in range(n)]
thresholds = [int(input()) for _ in range(k)]

result = calculate_final_sum(n, k, cards, thresholds)
print(result)
