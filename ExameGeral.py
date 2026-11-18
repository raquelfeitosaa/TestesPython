# Todo ano bissexto é realizado o exame geral de matemática da Nlogônia. 
# Todos os cidadãos da nação são avaliados a fim de se estudar o desenvolvimento 
# lógico e matemático do país ao longo dos anos.
# Após as correções, os cidadãos são ordenadados de acordo com suas notas 
# (quanto maior, melhor) e recebem descontos no imposto de renda de acordo com sua qualificação.
# O Escritório Central de Estatística (ECE) é encarregado de processar os dados das 
# notas obtidas no exame. Entretanto este ano, Vasya, um dos responsáveis, está internado no 
# hospital com gripe H1N1 e você foi contratado para realizar o seu trabalho.
# Escreva um programa que dado o número de habitantes da Nlogônia e todas as notas obtidas, 
# responda as consultas para retornar a nota do cidadão que ficou em determinada posição.
#Entrada
#A entrada contém vários casos de teste. A primeira linha de cada caso contém dois 
# inteiros N (1 ≤ N ≤ 100), Q (1 ≤ Q ≤ 100), o número de habitantes do país e o 
# número de consultas, respectivamente.
#As N linhas seguintes contém, cada uma, a nota ni obtida pelo i-ésimo cidadão (0 ≤ ni ≤ 30000).
#As próximas Q linhas contém cada uma uma consulta, a posição pi (1 ≤ pi ≤ N) a qual a 
# ECE está interessada em saber a nota.
#A entrada termina com fim-de-arquivo (EOF).
#Saída
#Para cada caso de teste, imprima, para cada consulta, 
# uma linha contendo a nota do cidadão que ficou classificado na posição pi.
def troca(L: list, n: int, j: int):
    tem = L[n]
    L[n] = L[j]
    L[j] = tem

    pass
def empurra(L: list, tamanho: int):
    i = 0
    while i < tamanho-1:
        if L[i] < L[i+1]:
            troca(L, i, i+1)
        i += 1
def bubblesort(L: list) -> list:
    n = len(L) #tamanho da lista 
    while n > 1:
        empurra(L, n)
        n -= 1
    return L
def pegaHabitantes(n: int) -> list:
    notaHabitantes = []
    while n > 0:
        nota = int(input())
        notaHabitantes.append(nota)
        n -= 1
    return notaHabitantes

def pegaConsulta(c: int, lista: list):
    while c > 0:
        p = int(input())
        print(lista[p-1])
        c -= 1

def main():
    while True:
        try:
            habitantes, consultas = map(int,input().split())
            lista = pegaHabitantes(habitantes)
            listaOrdenada = bubblesort(lista)
            pegaConsulta(consultas, listaOrdenada)

        except EOFError:
            break

if __name__ == '__main__':
    main()





