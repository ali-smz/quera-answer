def solve():
    t = int(input(""))
    results = []
    
    for _ in range(t):
        s = input("")  
        q_index = s.index('?') 
        valid_codes = []
        
        for digit in range(10):
            candidate = s[:q_index] + str(digit) + s[q_index+1:]
            weights = list(range(10, 1, -1))
            c = sum(int(candidate[j]) * weights[j] for j in range(9)) % 11
            control_digit = int(candidate[9])
            if (c in {0, 1} and control_digit == c) or (c > 1 and control_digit == 11 - c):
                valid_codes.append(candidate)
        
        if len(valid_codes) == 1:
            results.append(valid_codes[0])
        elif len(valid_codes) == 0:
            results.append("cannot be recovered!")
        else:
            results.append("it's not unique!")
    
    print("\n".join(results))

solve()