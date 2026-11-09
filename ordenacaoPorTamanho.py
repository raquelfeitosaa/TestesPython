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


def troca(Lista: list, Lugar1: str, Lugar2: str) -> None:
    lugarNovo = Lista[Lugar1] #Lugar1 é o lugar que eu quero trocar e a posição dele na lista
    Lista[Lugar1] = Lista[Lugar2]
    Lista[Lugar2] = lugarNovo

def empurra_decrescente(lista: list, tamanhoLista: int) -> None:
    i = 0
    while i < tamanhoLista-1:
        if lista[i] < lista[i+1]: 
            troca(lista, i, i+1)
        i += 1

def main():
    tamanho = int(input("")) #Numero de repetição
    while tamanho > 0:
        item = list(map(str, input('').split()))
        n = len(item)
        empurra_decrescente(item, n)
        print(*item)
        tamanho -= 1
        item = []

if __name__ == '__main__':
    main()