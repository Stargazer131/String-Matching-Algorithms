def preBrBc(x: str):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    
    # condition 4
    brBc = [[m+2 for _ in range(ASIZE)] for _ in range(ASIZE)]
    
    # condition 3
    for i in range(ASIZE):
        brBc[i][ord(x[0])] = m + 1

    # condition 2
    for i in range(m - 1):
        brBc[ord(x[i])][ord(x[i + 1])] = m - i
        
    # condition 1
    for i in range(ASIZE):
        brBc[ord(x[m - 1])][i] = 1
        
    return brBc


def search(x: str, y: str):
    n, m = len(y), len(x)
    y += chr(0)
    y += chr(0)
    brBc = preBrBc(x)
    
    j = 0
    while j <= n - m:
        print(f'At index {j}')
        print(f'y = {y[j : j + m + 2]}')
        print(f'x = {x}')
        if x == y[j : j + m]:
            print(f'Find x at index {j}')
        
        shift = brBc[ord(y[j + m])][ord(y[j + m + 1])]
        j += shift
        print(f'Shif by {shift}')
        
        print()


if __name__ == "__main__":
    x = 'GCAGAGAG'
    y = 'GCATCGCAGAGAGTATACAGTACG'
    search(x, y)
    