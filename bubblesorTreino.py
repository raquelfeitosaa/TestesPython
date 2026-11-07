#Ordena a lista de forma crescente
def bubble_sort(L: list) -> list:
    n = len(L) #tamanho da lista 
    while n > 1:
        empurra(L, n)
        n -= 1

    return L
#Trocando de lugar somente elementos que eu quero
def troca(L, i, j) -> None:
    tem = L[i]
    L[i] = L[j]
    L[j] = tem



##Empurrando o maior elemento para o final da lista
def empurra(L: list, n: int) -> None:
    i = 0
    while i < n-1:
        if L[i] > L[i+1]:
            troca(L, i, i+1)
        i += 1

## 
##Empurrando o menor elemento para o final da lista
def empurra_decrescente(L: list, n: int) -> None:
    i = 0
    while i < n-1:
        if L[i] < L[i+1]:
            troca(L, i, i+1)
        i += 1


##Decrecente lista
def bubble_sort_decrescente(L: list) -> list:
    n = len(L) #tamanho da lista 
    while n > 1:
        empurra_decrescente(L, n)
        n -= 1
    return L

Lista = [70, 50, 20, 90, 80, 60, 90, 10]
print(Lista)
bubble_sort_decrescente(Lista)
print(Lista)
 