while True:
    nota1 = int(input("Nota 1: "))
    nota2 = int(input("Nota 2: "))
    nota3 = int(input("Nota 3: "))
    nota4 = int(input("Nota 4: "))
    media = (nota1+nota2)/2

    if media >= 7:
        print(f'Aprovado com media: {media}')
    else:
        print(f'Reprovado com media: {media}')

    continuar = input('Sair [S]: ')
    if continuar.upper() == 'S':
        break
