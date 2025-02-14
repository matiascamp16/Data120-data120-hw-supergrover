# Problem 1: GCD
def gcd(a, b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    return gcd(b, a % b)

# Problem 2: Direction simplification
def remove_pairs(pathstring):
    if len(pathstring) < 2:
        return pathstring
    first_two = pathstring[:2]
    if first_two in {'NS', 'SN', 'EW', 'WE'}:
        return remove_pairs(pathstring[2:])
    else:
        return pathstring[0] + remove_pairs(pathstring[1:])

def simplify_pairs(pathstring):
    simplified = remove_pairs(pathstring)
    return simplified if simplified == pathstring else simplify_pairs(simplified)

# Problem 3: Bisection Method
def bisection_root(f, x0, x1):
    f_x0, f_x1 = f(x0), f(x1)
    if f_x0 * f_x1 > 0:
        raise ValueError("No root in interval")
    tolerance = 0.001
    
    while True:
        if abs(f_x0) <= tolerance:
            return x0
        if abs(f_x1) <= tolerance:
            return x1
        
        x_mid = (x0 + x1) / 2
        f_mid = f(x_mid)
        
        if abs(f_mid) <= tolerance:
            return x_mid
        
        if f_x0 * f_mid < 0:
            x1, f_x1 = x_mid, f_mid
        else:
            x0, f_x0 = x_mid, f_mid

# Problem 4: Coin Change
COINS = [100, 25, 10, 5, 1]

def make_change(total):
    def helper(remaining, index):
        if remaining == 0:
            return [[]]
        if index >= len(COINS) or remaining < 0:
            return []
        
        coin = COINS[index]
        max_count = remaining // coin
        combinations = []
        
        for count in range(max_count + 1):
            new_remaining = remaining - count * coin
            for combo in helper(new_remaining, index + 1):
                combinations.append([coin] * count + combo)
        
        return combinations
    
    return helper(total, 0)

# Problem 5: Dollar Change Analysis
def foundollarschange():
    combinations = make_change(400)
    num_ways = len(combinations)
    freq = {}
    for combo in combinations:
        length = len(combo)
        if length in freq:
            freq[length] += 1
        else:
            freq[length] = 1
    if not freq:
        max_count = 0
        mode_length = 0
    else:
        max_count = max(freq.values())
        candidates = [k for k, v in freq.items() if v == max_count]
        mode_length = max(candidates) if candidates else 0
    return (400, num_ways, mode_length, max_count)

foundollarschange = foundollarschange()