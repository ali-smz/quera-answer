import itertools
MOD = 10**9 + 7

# محاسبه فاکتوریل و معکوس پیمانه‌ای
def precompute_factorials(max_n, mod):
    fact = [1] * (max_n + 1)
    inv_fact = [1] * (max_n + 1)
    for i in range(2, max_n + 1):
        fact[i] = fact[i - 1] * i % mod
    inv_fact[max_n] = pow(fact[max_n], mod - 2, mod)
    for i in range(max_n - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % mod
    return fact, inv_fact

# تابع شبیه‌سازی نمایش
def simulate_beauty(n, positions):
    steps = 0
    while any(pos != 0 for pos in positions):
        next_positions = positions[:]
        for i in range(n):
            if positions[i] > 0:
                if positions[i] > i:
                    next_positions[i] -= 1
                elif positions[i] < i:
                    next_positions[i] += 1
        positions = next_positions
        steps += 1
    return steps

# حل مسئله
def solve(n, k, a):
    fact, inv_fact = precompute_factorials(n, MOD)
    
    # جایگاه‌های مشخص‌شده و نامشخص
    fixed_positions = []
    unknown_indices = []
    for i in range(n):
        if a[i] != -1:
            fixed_positions.append(a[i] - 1)
        else:
            unknown_indices.append(i)
    
    if k == 0:
        # همه جایگاه‌ها مشخص است
        return simulate_beauty(n, fixed_positions)
    
    # مجموع زیبایی
    total_beauty = 0
    
    # بررسی همه جایگشت‌های ممکن
    for perm in itertools.permutations(range(k)):
        positions = fixed_positions[:]
        for i, idx in enumerate(unknown_indices):
            positions[idx] = perm[i]
        total_beauty += simulate_beauty(n, positions)
        total_beauty %= MOD
    
    # بازگشت باقی‌مانده به پیمانه MOD
    return total_beauty * fact[k] % MOD

# ورودی
n, k = map(int, input().split())
a = list(map(int, input().split()))

# خروجی
print(solve(n, k, a))
