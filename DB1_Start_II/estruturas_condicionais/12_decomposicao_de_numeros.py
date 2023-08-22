numero = int(input('Digite um numero positivo menor que 1000: '))

if numero < 0 or numero > 1000:
    print('Número inválido')
else:
    unidade = int(numero % 10)
    numero = int((numero - unidade) / 10)
    dezena = int(numero % 10)
    numero = int((numero - dezena) / 10)
    centena = int(numero)
    print(f'Centena: {centena}, dezena: {dezena}, unidade: {unidade}')
