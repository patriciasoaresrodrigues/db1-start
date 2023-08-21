p1 = float(input("Valor do primeiro produto: "))
p2 = float(input("Valor do segundo produto: "))
p3 = float(input("Valor do terceiro produto: "))

if p1 < p2 and p1 < p3:
    print(f'Você deve comprar o primeiro produto, de valor: {p1}')
elif p2 < p1 and p2 < p3:
    print(f'Você deve comprar o segundo produto, de valor: {p2}')
else:
    print(f'Você deve comprar o terceiro produto, de valor: {p3}')
