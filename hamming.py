def hamming_code(t, test_cases):
    results = []
    for n, encoded in test_cases:
        r = 0
        while (1 << r) <= n:
            r += 1

        error_pos = 0
        for i in range(r):
            parity_index = (1 << i)
            parity_xor = 0
            for j in range(1, n + 1):
                if j & parity_index:
                    parity_xor ^= int(encoded[j - 1])
            if parity_xor != 0:
                error_pos += parity_index

        if error_pos > n:
            results.append("INVALID")
        else:
            if error_pos > 0:
                results.append("YES")
                corrected = list(encoded)
                corrected[error_pos - 1] = '1' if corrected[error_pos - 1] == '0' else '0'
                results.append("".join(corrected))
            else:
                results.append("NO")
    
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    encoded = input()
    test_cases.append((n, encoded))

results = hamming_code(t, test_cases)
for res in results:
    print(res)
