# Crie um programa que solicite ao usuário uma quantidade n
# positiva de números e, em seguida, os n números.
# o programa deverá, ao final, exibir duas listas, uma
# com os primos digitados e a outra com os não-primos.


def eh_primo(x: int) -> bool:
    qtd_divisores = 0
    for pd in range(1, x+1):
        if x % pd == 0:
            qtd_divisores +=1 
    return qtd_divisores

def main():
    n = int(input())
    for i in range(n):
        x = int(input())
        if eh_primo(x):
            print(f'{x} eh primo')
        else:
            print(f'{x} nao eh primo')

if __name__ == '__main__':
    main()
