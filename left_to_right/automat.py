def build_automat(x: str, y: str):
    NODES_LIMIT = 10
    automat = [[] for x in range(NODES_LIMIT)]
    n, m = len(x), len(y)

    alphabet = set(x+y) # tat ca chu cai trong 2 xau
    Q = [x[:i] for i in range(n+1)]
    T = x
    current_node = 0
    for q in Q:
        for a in alphabet:
            qa = q+a 
            if qa in Q:
                automat[current_node].append((current_node + 1, a)) # ex: (1, G), (2, C), ...
            else:
                # duyet qua tung hau to cua qa
                for i in range(len(qa)):
                    p = qa[i:]
                    if p in Q:
                        node_num = len(p)
                        automat[current_node].append((node_num, a))
                        break
        current_node += 1
    
    return automat


def search(x: str, y: str):
    n, m = len(x), len(y)
    automat = build_automat(x, y)
    
    state = 0
    for index, c in enumerate(y):
        if state == n:
            print(f'Found x at index {index}')
        
        go_next = False
        for node in automat[state]:
            node_num, character = node    
            if character == c: # can go to this state
                state = node_num
                go_next = True
                break
        if not go_next:
            state = 0
        print(f'Index {index}, State {state}, Character {c}')


if __name__ == "__main__":
    x = 'GCAGAGAG'
    y = 'GCATCGCAGAGAGTATACAGTACG'
    search(x, y)