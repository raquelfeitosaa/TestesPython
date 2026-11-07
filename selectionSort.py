from bubblesortTreino import troca
def seleciona(L: list) -> int:
    maior = 0
    for i in range(len(L)):
        if L[i] > maior:
            maior = L[i]
    return maior

def selection_sort(L: list) -> list:
    n = len(L)
    while n > 1:
        maior = seleciona(L[:n])
        i = L.index(maior)
        
        n -= 1

L = [30, 40, 20,50,10]
maior = seleciona(L)
print('Maior item da lista: ', maior)
