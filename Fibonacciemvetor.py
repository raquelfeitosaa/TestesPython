
exibe = 0
def retorna(n: int) -> int:
    a = 0
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        i = 2
        while i <= n:
            c =  a + b
            a = b
            b = c
            i += 1
        return c

def criar_lista(limite: int) -> list:
    L = []
    for n in range(0, limite+1):
        L.append(retorna(n))
    print(L)
    return L


def main():
    L = criar_lista(60)
    n = int(input())
    for i in range(n):
        q = int(input())
        print(f'Fib({q}) = {L[q]}')
    
if __name__ == '__main__':
    main()