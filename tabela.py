#                 0         1      2       3
produtos = [['smartphone', 100, 1199.00, True ], # 0
            ['televisão',    5, 2599.00, False], # 1
            ['notebook',    20, 4500.00, True ]] # 2

# 1) Acesse o preço do smartphone e aumente R$ 200,00.
produtos[0][2] += 200.00

# 2) Reduza em uma unidade o estoque de televisores.
produtos[1][1] -= 1

# 3) Alternar a nacionalidade do notebook.
produtos[2][3] = not produtos[2][3]

# 4) Exiba todos os produtos da tabela.

##def exibe(produtos):
##    for i in range(len(produtos)):
##        for j in range(len(produtos[i])):
##            print(produtos[i][j], end=' ')
##        print()
##    print()

##def exibe(produtos):
##    for linha in produtos:
##        print(*linha)

def exibe(produtos):
    for linha in produtos:
        nome, estoque, preco, importado = linha
        print(f'Nome.....: {nome}')
        print(f'Estoque..: {estoque}')
        print(f'Preço....: R$ {preco:.2f}')
        print(f'Importado: {"sim" if importado else "não"}')
        print('-' * 25)

exibe(produtos)
