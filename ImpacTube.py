# A ImpacTube, uma famosa empresa de compartilhamento de vídeos, quer premiar 
# alguns de seus mais notáveis criadores de conteúdo. Para isso, a ImpacTube 
# montará uma tabela com alguns dos canais que possuem grande quantidade de usuários inscritos.
# No site da ImpacTube, os canais geram renda para seus criadores de conteúdo por meio de 
# diversos mecanismos, a conhecida "monetização", o que geralmente é influenciado pela quantidade 
# de inscritos no canal e que acessam aos vídeos postados.
# Para possibilitar a premiação, cada registro da tabela (vide exemplo na Figura 1) 
# terá quatro campos dispostos em colunas na seguinte ordem:
# O nome do canal;
# A quantidade atual de inscritos; 
# A monetização do último mês do canal e;
# Um valor indicando se o canal produz conteúdo premium, que são vídeos exclusivos 
# para usuários que pagam uma mensalidade à ImpacTube.
# Com esses dados será possível definir a bonificação de cada canal, 
# que será composta pelo valor "monetização" da tabela acrescido de um valor 
# fixo para cada mil inscritos. O valor fixo será definido pela ImpacTube, sendo
# X para canais com conteúdo premium e Y para os que não possuem conteúdo premium.
# 
# Figura 1 - Exemplo de tabela com canais selecionados para receberem bonificação.
# Você foi escolhido para desenvolver um programa que receberá como entrada os dados 
# de cada canal, gerando internamente a tabela modelo, e que mostrará os nomes dos canais, 
# na ordem em que foram dados na entrada, acompanhados do valor que receberão como bonificação. 
# Observe cuidadosamente o formato de entrada e o formato de saída especificados.

# Entrada
# A entrada pode ser separada em três partes:
# Na primeira linha será informado um número inteiro que representa 
# a quantidade N (1 <= N <= 200) de canais da tabela;
# Em cada uma das N linhas seguintes serão informados os registros que compõem a 
# tabela, com os valores das colunas separados por um ponto e vírgula, nesta ordem: 
# (1) uma string com o nome do canal que será bonificado; (2) um número natural que é 
# a quantidade de inscritos no canal; (3) um número real simbolizando a monetização do 
# canal no mês anterior (dado em reais R$) e; (4) uma string 'sim' ou 'não', sem apóstrofos 
# e completamente em minúsculo, que indica se o canal produz conteúdo premium;
# Por fim, serão informados dois números reais X e Y, um em cada linha, que indicam o valor 
# fixo (em reais R$) que os canais receberão a mais para cada mil inscritos no canal. 
# O primeiro valor é X e refere-se aos canais que possuem conteúdo premium. O segundo valor 
# é Y e refere-se aos canais que não possuem conteúdo premium.

# Saída
# O cabeçalho contém três linhas, sendo a primeira e a terceira compostas por apenas 
# cinco hifens, e a segunda composta unicamente pela palavra 'BÔNUS', sem apóstrofos e 
# completamente em maiúsculo. Nas próximas N linhas, estão os nomes dos canais, na mesma 
# ordem em que foram dados na entrada, acompanhados à direita pelo valor que receberão como 
# bonificação, em reais e com duas casas decimais, exatamente como consta nos exemplos.

def exibiLista(listaM: list):
     print('-'*5)
     print('BÔNUS')
     print('-'*5)
     for atual in listaM:
          nomecanal,bonus = atual
          print(f'{nomecanal}: R$ {bonus:.2f}')
     
def MontarValores(listinha: list, p: float, np: float) -> list:
    novalista = []
    for linha in listinha:
        nomeC = linha[0]
        inscritos = linha[1] // 1000
        if linha[3] == 'sim':
            calc = inscritos * p
            bonus = calc + linha[2]
            novalista.append([nomeC,bonus])
        else:
            calc = inscritos * np
            bonus = calc + linha[2]
            novalista.append([nomeC,bonus])
    return novalista
def pegarValores() -> list:
    contador = int(input())
    lista = []
    while contador > 0:
        dados = input()
        canal, inscritos, monetizacao, premiun = dados.split(';')
        inscritos = int(inscritos)
        monetizacao = float(monetizacao)
        lista.append([canal, inscritos, monetizacao, premiun])
        contador -= 1
    return lista

def main():
    l1 = pegarValores()
    x = float(input())
    y = float(input())
    l2 = MontarValores(l1, x, y)
    exibiLista(l2)

if __name__ == '__main__':
    main()