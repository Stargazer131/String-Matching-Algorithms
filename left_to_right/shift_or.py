def build_Sc_table(x: str, y: str):
    alphabet = set(x+y)    
    Sc = {}
    for c in alphabet:
        binary_string = ''
        for char in x:
            if char == c:
                binary_string += '0'
            else:
                binary_string += '1'     
                     
        # convert from binary string to int -> only int can use bitwise operation
        Sc[c] = int(binary_string, 2)
    
    return Sc


def search(x: str, y: str):
    Sc = build_Sc_table(x, y)
    n, m = len(x), len(y)
    prev_rj = int('1' * n, 2)
    format_str = f'0{n}b'
    
    print(f'Init R = {format(prev_rj, format_str)}')
    for index, char in enumerate(y):
        # shift
        new_rj = prev_rj >> 1
        print(f'Shift R({index-1}) = {format(new_rj, format_str)}')
        
        # or
        new_rj = new_rj | Sc[char]
        print(f'Or S({char}) = R({index}) = {format(new_rj, format_str)}')
        print()
        
        prev_rj = new_rj


if __name__ == "__main__":
    x = 'GCAGAGAG'
    y = 'GCATCGCAGAGAGTATACAGTACG'
    search(x, y)
    