# https://training.olinfo.it/task/ois_parentesi

import sys

# Per la sottoposizione di questo problema in piattaforma: ATTIVARE QUESTE DUE RIGHE!
sys.stdin = open('input0_parentesi.txt')
sys.stdout = open('output_parentesi.txt', 'w')

#sys.stdin = open('parentesi_input04.txt')
#sys.stdout = open('output.txt', 'w')

def controlla(N, E):
    stack = []
    coppie = {
        ')': '(', 
        ']': '[', 
        '}': '{', 
        '>': '<'
    }
    
    for parentesi in E:
        if parentesi in '([{<':
            stack.append(parentesi)
        elif parentesi in ')]}>':
            if not stack or stack[-1] != coppie[parentesi]:
                return False
            stack.pop()
    
    return len(stack) == 0
    


N = int(input().strip())
E = input().strip()

if controlla(N, E) == False:
    print("malformata")
else:
    print("corretta")

sys.exit(0)
