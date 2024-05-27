def preZtBc(x: str):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    
    # condition 3
    ztBc = [[m for _ in range(ASIZE)] for _ in range(ASIZE)]
    
    # condition 2
    for i in range(ASIZE):
        ztBc[i][ord(x[0])] = m - 1

    # condition 1
    for i in range(1, m - 1):
        ztBc[ord(x[i - 1])][ord(x[i])] = m - 1 - i
        
    return ztBc


def preBmGs(x: str):
    m = len(x)
    period_of_x = ''
    bmGs = [0] * (m + 1)
    
    # first element is the length of the period of x and will be removed when we returning the bmGs table
    bmGs[0] = len(period_of_x)
    
    # Helper function to check Cs condition
    def Cs(i, s):
        for k in range(i + 1, m):
            if s >= k or x[k - s] == x[k]:
                continue
            else:
                return False
        return True
    
    # Helper function to check Co condition
    def Co(i, s):
        if s >= i:
            return True
            
        if x[i - s] != x[i]:
            return True
        return False
    
    # Main loop to calculate bmGs
    for i in range(m):
        for s in range(1, m + 1):
            if Cs(i, s) and Co(i, s):
                bmGs[i + 1] = s
                break
    
    return bmGs[1:]


def search(x: str, y: str):
    n, m = len(y), len(x)
    bmGs = preBmGs(x)
    ztBc = preZtBc(x)
    
    j = 0
    while j <= n - m:
        print(f'At index {j}')
        i = m - 1
        print(f'x = {x}')
        print(f'y = {y[j : j + m]}')
        
        while i >= 0 and x[i] == y[i + j]:
            i -= 1
        if i < 0:
            print(f'Shift by {bmGs[0]}')
            print(f'Found x at index {j}')
            j += bmGs[0]
        else:
            print(f'Shift by Max({bmGs[i]}, {ztBc[ord(y[j + m - 2])][ord(y[j + m - 1])]})')
            j += max(bmGs[i], ztBc[ord(y[j + m - 2])][ord(y[j + m - 1])])
        print()


if __name__ == "__main__":
    x = 'GCAGAGAG'
    y = 'GCATCGCAGAGAGTATACAGTACG'
    search(x, y)
