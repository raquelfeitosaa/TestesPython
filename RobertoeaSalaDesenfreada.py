def relatorio(epr : int, ehd: int, intu: int) -> None:
  print(f'EPR: {epr}')
  print(f'EHD: {ehd}')
  print(f'INTRUSOS: {intu}')
def contabilizacao(qtd_alunos: int) -> list:
  EPR = 0
  EHD = 0
  intrusos = 0
  while qtd_alunos > 0:
    n, curso = input().split()
    n = int(n)
    match curso:
      case 'EPR': EPR += 1
      case 'EHD': EHD += 1
      case _: intrusos += 1
    qtd_alunos -= 1
  return [EPR, EHD, intrusos]
def main():
  while True:
    try:
      qtd_alunos = int(input())
      EPR, EHD, intrusos = contabilizacao(qtd_alunos)
      relatorio(EPR, EHD, intrusos)
    except (EOFError, KeyboardInterrupt):
        break

if __name__ == '__main__':
  main()