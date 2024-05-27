def hash(s: str):
    MAX_INT = 2_147_483_647
    res = 0
    m = len(s)
    for index, c in enumerate(s):
        res += ord(c) * 2 ** (m-index-1)
    return res % MAX_INT


def rehash(a: int, b: int, h: int, m: int):
    MAX_INT = 2_147_483_647
    res = (h - a * 2 ** (m-1)) * 2 + b
    return res % MAX_INT


def search(x, y):
    n, m = len(x), len(y)
    hx = hash(x)
    print(f'Hash(x) = {hx}')
    prev_h = -1
    
    for i in range(m-n+1):
        window_y = y[i:i+n]
        if prev_h == -1:
            hy = hash(window_y)
        else:
            a = ord(y[i-1])
            b = ord(y[i+n-1])
            hy = rehash(a, b, prev_h, n)
            
        prev_h = hy
        print(f'Hash(y[{i} .. {i+n-1}]) = {hy}')
        if hx == hy and x == window_y:
            print(f'Found x at index {i}')
        
        
if __name__ == "__main__":
    x = 'GCAGAGAG'
    y = 'GCATCGCAGAGAGTATACAGTACG'
    search(x, y)