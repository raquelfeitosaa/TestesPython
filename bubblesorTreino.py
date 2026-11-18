#Trocando de lugar somente elementos que eu quero
def troca(L, lugarQqueroTrocar, NumeroQqueroTrocar) -> None:
    tem = L[lugarQqueroTrocar]
    L[lugarQqueroTrocar] = L[NumeroQqueroTrocar]
    L[NumeroQqueroTrocar] = tem


##Empurrando o menor elemento para o final da lista
def empurra_decrescente(L: list, n: int) -> None:
    i = 0
    while i < n-1:
        if len(L[i]) < len(L[i+1]):
            troca(L, i, i+1)
        i += 1


##Decrecente lista
def bubble_sort_decrescente(L: list) -> list:
    n = len(L) #tamanho da lista 
    while n > 1:
        empurra_decrescente(L, n)
        n -= 1
    return L

Lista = ['meu', 'nome', 'oi', 'i']
print(*Lista)
bubble_sort_decrescente(Lista)
print(*Lista)
 