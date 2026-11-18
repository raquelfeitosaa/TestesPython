def calculo(x: float, y: float, c: float) -> float:
    somaPesos = 2 + 3 + 5
    notas = (x * 2) + (y * 3) + (c * 5)
    media = notas / somaPesos
    return media

def main():
    cont = int(input())
    while cont > 0:
        n1, n2, n3 = map(float,input().split())
        med = calculo(n1,n2,n3)
        print(f'{med:.1f}')
        cont -= 1

if __name__ == '__main__':
    main()
