def preprocess(s: str):
    n = len(s)
    mpNext = [0 for _ in range(n+1)]
    mpNext[0] = -1
    for i in range(1, n+1):
        window_s = s[:i]
        for j in range(i-1):
            v = window_s[:j+1]
            if window_s.endswith(v):
                mpNext[i] = j+1
    return mpNext


def search(x: str, y: str):
    mpNext = preprocess(x)
    n, m = len(x), len(y)
    index = 0
    
    while index < m-n+1:
        i = index
        j = 0
        print(f'Index {index}')
        print(f'y = {y[i:i+n]}')
        print(f'x = {x}')
        while j < n and x[j] == y[i]:
            i += 1
            j += 1
        
        if j == n:
            print(f'Found x at index {i}')
        index += j - mpNext[j]
        print(f'Shift by {j - mpNext[j]}')
        print()
        

if __name__ == "__main__":
    x = 'GCAGAGAG'
    y = 'GCATCGCAGAGAGTATACAGTACG'
    search(x, y)
        