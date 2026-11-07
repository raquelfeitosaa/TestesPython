from random import randint, shuffle 
from math import factorial 
## shuffle bagunça a lista
##radint gera um número aleatório 
## factorial calcula o fatorial de um número
def ordenada(L: list, n: int) -> bool:
    i = 0
    while i < n-1:
        if L[i] > L[i+1]:
            return False
        i += 1
    return True


def bogo_sort(L: list) -> list:
    print(f'Lista inicial: {L}')
    i = 0
    while not ordenada(L, len(L)):
        shuffle(L)
        i += 1
        print(f'Lista embaralhada {i}: {L}')
    return L

def bubble_sort(L: list) -> list:
    pass 

def lista (n: int, vmin = 10, vmax = 99) -> list:
    L = []
    for i in range(n):
        x = randint(vmin, vmax)
        L.append(x)
    return L

