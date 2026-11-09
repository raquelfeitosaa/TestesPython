##Matriz é uma lista dentro de outra lista.
#colunas -> 0    1    2   #linhas
matriz = [[5.5, 7.0, 8.7],# 0
          [8.0, 6.0, 9.5],# 1
          [7.5, 8.5, 6.5]]# 2 

# Acrescentando 10% nas notas 
# de todos os alunos.
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] += 0.10*matriz[i][j]
        if matriz[i][j] > 10:
            matriz[i][j] = 10
# Exibindo a matriz com as notas atualizadas
for i in range(len(matriz)):
    print(*matriz[i])