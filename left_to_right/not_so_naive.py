def search(x: str, y: str):
    n, m = len(y), len(x)

    j = 0
    if x[0] == x[1]:        
        while j <= n - m:
            print(f'At index {j}')
            print(f'y = {y[j : j + m]}')
            print(f'x = {x}')
                
            if x[1] != y[j + 1]:
                shift = 2
            else:
                shift = 1
                
            if x[2 : m] == y[j + 2 : j + m] and x[0] == y[j]:
                print(f'Find x at index {j}')            
            
            print(f'Shift by {shift}\n')
            j += shift
    else:
        while j <= n - m:
            print(f'At index {j}')
            print(f'y = {y[j : j + m]}')
            print(f'x = {x}')
                
            if x[1] == y[j + 1]:
                shift = 2
            else:
                shift = 1
                
            if x[2 : m] == y[j + 2 : j + m] and x[0] == y[j]:
                print(f'Find x at index {j}')            
            
            print(f'Shift by {shift}\n')
            j += shift
    

if __name__ == "__main__":
    x = 'GCAGAGAG'
    y = 'GCATCGCAGAGAGTATACAGTACG'
    search(x, y)
