while True:
    continuar = input('Deseja calcular? [S, N]: ')
    if continuar == 'N':
        break
    elif continuar != 'S':
        print('Opção inválida!')
        continue
    valor_hora = int(input('Valor da hora: '))
    horas_trabalhadas = int(input('Horas trabalhadas no mês: '))
    salario = valor_hora * horas_trabalhadas
    print(f'Total do salário: {salario}')
