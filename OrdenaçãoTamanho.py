# Crie um programa para ordenar um conjunto de strings pelo seu tamanho. 
# Seu programa deve receber um conjunto de strings e retornar este mesmo
# conjunto ordenado pelo tamanho das palavras, se o tamanho das strings for 
# igual, deve-se manter a ordem original do conjunto.

#Entrada
#A primeira linha da entrada possui um único inteiro N, que indica o número
#de casos de teste. Cada caso de teste poderá conter de 1 a 50 strings inclusive,
#e cada uma das strings poderá conter entre 1 e 50 caracteres inclusive.
# Os caracteres poderão ser espaços, letras, ou números.

#Saída
#A saída deve conter o conjunto de strings da entrada ordenado pelo tamanho das
# strings. Um espaço em branco deve ser impresso entre duas palavras.

#Trocando de lugar somente elementos que eu quero
def troca(L, q, n) -> None:
    tem = L[q]
    L[q] = L[n]
    L[n] = tem


##Empurrando o menor elemento para o final da lista
def empurra(L: list, n: int) -> None:
    i = 0
    while i < n-1:
        if len(L[i]) < len(L[i+1]):
            troca(L, i, i+1)
        i += 1


##Decrecente lista
def bubble_sort(L: list) -> list:
    n = len(L) #tamanho da lista 
    while n > 1:
        empurra(L, n)
        n -= 1
    return L

def main():
    contador = int(input())
    while contador > 0:
        listinha = list(map(str, input().split()))
        bubble_sort(listinha)
        print(*listinha)
        contador -= 1


if __name__ == '__main__':
    main()