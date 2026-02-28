num = input('Escribe un número: ')
num = int(num)

for i in range(1, 11):
    for j in range(1, 11):
        if i * j == num:
            print('El número', num, 'es igual a', i, 'x', j)
