l1 = int(input('Lado 1: '))
l2 = int(input('Lado 2: '))
l3 = int(input('Lado 3: '))

if l1 == l2 and l2 == l3:
    print('Equilátero')
elif l1 != l2 and l2 != l3:
    print('Escaleno')
else:
    print('Isósceles')
