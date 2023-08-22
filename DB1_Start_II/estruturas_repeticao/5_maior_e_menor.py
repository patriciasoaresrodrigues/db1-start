while True:
    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))
    n3 = int(input("Informe o terceiro número: "))
    n4 = int(input("Informe o quarto número: "))

    if n1 > n2 and n1 > n3 and n1 > n4:
        print(f'O maior número é: {n1}')
    elif n2 > n1 and n2 > n3 and n2 > n4:
        print(f'O maior número é: {n2}')
    elif n3 > n1 and n3 > n2 and n3 > n4:
        print(f'O maior número é: {n3}')
    else:
        print(f'O maior número é: {n4}')

    if n1 < n2 and n1 < n3 and n1 < n4:
        print(f'O menor número é: {n1}')
    elif n2 < n1 and n2 < n3 and n2 < n4:
        print(f'O menor número é: {n2}')
    elif n3 < n1 and n3 < n2 and n3 < n4:
        print(f'O menor número é: {n3}')
    else:
        print(f'O menor número é: {n4}')

    continuar = input('Sair [S]: ')
    if continuar.upper() == 'S':
        break
