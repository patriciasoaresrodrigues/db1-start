while True:
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite outro número inteiro: '))
    n3 = float(input('Digite um número real: '))
    soma = n1 + n2 + n3
    print(f'A soma de {n1} + {n2} + {n3} = {soma}')

    continuar = input('Sair [S]: ')
    if continuar.upper() == 'S':
        break
