def preBmBc(x: str):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    bmBc = [m] * ASIZE
    for i in range(m - 1):
        bmBc[ord(x[i])] = m - i - 1
    return bmBc


def search(x: str, y: str):
    n, m = len(y), len(x)
    bmBc = preBmBc(x)
    firstC = x[0]
    middleC = x[m // 2]
    lastC = x[m - 1]
    
    j = 0
    while j <= n - m:
        print(f'At index {j}')
        print(f'y = {y[j : j + m]}')
        print(f'x = {x}')
        
        c = y[j + m - 1]
        if y[j + m - 1] == lastC and y[j] == firstC and y[j + m // 2] == middleC:
            if x[1 : m - 1] == y[j + 1 : j + m - 1]:
                print(f'Find x at index {j}')
            
        print(f'Shift by {bmBc[ord(c)]}\n')
        j += bmBc[ord(c)]


if __name__ == "__main__":
    x = 'GCAGAGAG'
    y = 'GCATCGCAGAGAGTATACAGTACG'
    search(x, y)
