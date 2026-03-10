#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# sys.stdin = open('input0_isogram.txt', 'r')
# sys.stdout = open('output0_isogram.txt', 'w')

# input data
N = int(input().strip())

soglia = 2
count = 0

for i in range(N):
    S = input().strip()

    conteggio = {}

    for parola in S.lower():
        if parola.isalpha():
            conteggio[parola] = conteggio.get(parola, 0) + 1

    if all(count <= soglia for count in conteggio.values()):
        count += 1
    
    


print(count)  # print the result
