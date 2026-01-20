#!/usr/bin/env python3
# -*- coding: utf8 -*-

import sys

# se preferisci leggere e scrivere da file
# ti basta decommentare le seguenti due righe:

sys.stdin = open('pesci_input_1.txt')
sys.stdout = open('output.txt', 'w')

def solve():
    input()
    N, K = map(int, input().split())
    
    risposta = 0 # memorizza qui la risposta

    while N > 0:
        risposta += N
        N = N // K


    # aggiungi codice...

    return risposta


T = int(input())

for t in range(1, T+1):
    print("Case #" + str(t) + ":", solve())
