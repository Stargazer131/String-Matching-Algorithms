def preprocess(w: str):
    m = len(w)
    kmpNext = [0 for _ in range(m+1)]
    kmpNext[0] = -1
    pos = 1 # (the current position we are computing)
    cnd = 0 # (the zero-based index in W of the next character of the current candidate substring)

    # Loop through the string
    while pos < m:
        if w[pos] == w[cnd]:
            kmpNext[pos] = kmpNext[cnd]
        else:
            kmpNext[pos] = cnd
            while cnd >= 0 and w[pos] != w[cnd]:
                cnd = kmpNext[cnd]
        pos += 1
        cnd += 1
        
    kmpNext[pos] = cnd
    return kmpNext


def search(x: str, y: str):
    kmpNext = preprocess(x)
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
        index += j - kmpNext[j]
        print(f'Shift by {j - kmpNext[j]}')
        print()


if __name__ == "__main__":
    x = 'GCAGAGAG'
    y = 'GCATCGCAGAGAGTATACAGTACG'
    search(x, y)
        