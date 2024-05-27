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
    shift = bmBc[ord(x[m - 1])]
    bmBc[ord(x[m - 1])] = 0
    y += x[m - 1] * m
    
    j = 0
    while j <= n-m:
        print(f'At index {j}, start with y = {y[j : j + m]}')
        k = bmBc[ord(y[j + m -1])]
        if k == 0:
            print(f'Shift by 0, y = {y[j : j + m]}')
        while k !=  0:
            j += k
            print(f'Shift by {k}, y = {y[j : j + m]}')
            k = bmBc[ord(y[j + m -1])]
            
            j += k
            print(f'Shift by {k}, y = {y[j : j + m]}')
            k = bmBc[ord(y[j + m -1])]
            
            j += k
            print(f'Shift by {k}, y = {y[j : j + m]}')
            k = bmBc[ord(y[j + m -1])]
            
        if x[ : m - 1] == y[j : j + m - 1]:
            print(f'Find x at index {j}')
        j += shift
        print(f'Final shift by {shift}')
        print()


if __name__ == "__main__":
    x = 'GCAGAGAG'
    y = 'GCATCGCAGAGAGTATACAGTACG'
    search(x, y)
