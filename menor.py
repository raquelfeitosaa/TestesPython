L = []
contador = 3
lista_nova = []
while contador > 0:
    valor = float(input('Digite um salário: '))
    L.append(valor)
    contador -= 1

def salario_menores (L: list[float]) -> list[float]:
    L_nova = []
    for i in L:
        if i > 1000:
            i *= 1.1
            L_nova.append(i)
    return L_nova

menor_salario = L[0]
for i in L:
    if i < menor_salario:
        menor_salario = i
print('Menor salário: ', menor_salario)
lista_nova = salario_menores(L)
for i in lista_nova:
    print(f'Salário com aumento:{i:.2f}')

maior_salario = L[0]
for i in L:
    if i > maior_salario:
        maior_salario = i
print('Maior salário: ', maior_salario)

