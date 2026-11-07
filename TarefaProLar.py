# Crie um programa que solicite ao usuário
# diversos salários, ao final, some todos
# eles, exiba o menor salário, o maior salário
# e acrescente 10% em cada salário que estiver
# abaixo da média salarial.
# Obs.: Considere "diversos" como todos os
#       salários informados até o EOF (simulado
#       com KeyboardInterrupt).

def cria_lista() -> list[float]:
    L = []
    x = float(input('Digite um salário: '))
    L.append(x)

def soma_salarios(salarios: list[float]) -> float:
    soma = sum(salarios)
    media = soma / len(salarios)
    return media

def menor_salario(salarios: list[float]) -> float:
    menor_salario = salarios[0]
    for i in salarios:
        if i < menor_salario:
            menor_salario = i
    return menor_salario

def maior_salario(salarios: list[float]) -> float:
    maior_salario = salarios[0]
    for i in salarios:
        if i > maior_salario:
            maior_salario = i
    return maior_salario

def aumento(salarios: list[float], aumento: float) -> list[float]:
    mediaa = soma_salarios(salarios)
    nova_lista = []
    for i in salarios:
        if i < mediaa:
            i *= aumento
            nova_lista.append(i)
    return nova_lista

def main():
    while True:
        try:
            salarios = cria_lista()
        except KeyboardInterrupt:
            print(salarios)
            print('Media dos salários: ', soma_salarios(salarios))
            print('Menor salário: ', menor_salario(salarios))
            print('Maior salário: ', maior_salario(salarios))    
            print('Salários com aumento: ', aumento(salarios, 1.1))
            break


if __name__ == '__main__':
    main()