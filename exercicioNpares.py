def lista_pares(numero: int) -> list:
    L = []
    for i in range(0, numero+1, 2):
        L.append(i)
    return L

def main():
    numeros = int(input('Quais são seus números?'))
    lista = lista_pares(numeros)
    print(lista)
if __name__ == '__main__':
    main()