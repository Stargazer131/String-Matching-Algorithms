def preBmBc(x: str):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    bmBc = [m] * ASIZE
    for i in range(m - 1):
        bmBc[ord(x[i])] = m - i - 1
    return bmBc


def preQsBc(x: str):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    qsBc = [m+1] * ASIZE
    for i in range(m):
        qsBc[ord(x[i])] = m - i
    return qsBc


def search(x: str, y: str):
    n, m = len(y), len(x)
    bmBc = preBmBc(x)
    qsBc = preQsBc(x)
    
    j = 0
    while j <= n - m:
        print(f'At index {j}')
        print(f'y = {y[j : j + m + 1]}')
        print(f'x = {x}')
        
        if x == y[j : j + m]:
            print(f'Find x at index {j}')
            
        
        print(f'Shift by Max({bmBc[ord(y[j + m - 1])]}, {qsBc[ord(y[j + m])]})\n')
        j += max(bmBc[ord(y[j + m - 1])], qsBc[ord(y[j + m])])


if __name__ == "__main__":
    x = 'GCAGAGAG'
    y = 'GCATCGCAGAGAGTATACAGTACG'
    search(x, y)
