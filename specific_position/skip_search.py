def build_z_table(x: str):
    ASIZE = 256  # Assuming ASCII characters
    m = len(x)
    z = [[] for _ in range(ASIZE)]
    for i in range(m-1, -1, -1):
        z[ord(x[i])].append(i)
    
    return z
        
        
def search(x: str, y: str):
    n, m = len(y), len(x)
    z = build_z_table(x)
    
    for j in range(m-1, n, m):
        print(f'At index {j}')
        print(f'y = {y[j - m + 1 : j + 1]}')
        print(f'x = {x}')
        for node in z[ord(y[j])]:
            print(f'+ p = {j} - {node} = {j - node}')
            print(f'y = {y[j - node : j - node + m]}')
            print(f'x = {x}')
            if x == y[j - node : j - node + m]:
                print(f'Found x at index {j - node}')
        print()


if __name__ == "__main__":
    x = 'GCAGAGAG'
    y = 'GCATCGCAGAGAGTATACAGTACG'
    search(x, y)
