contador = 0
for num in range(1, 101):
    if (num % 3 == 0) or (num % 7 == 0):
        continue
    contador = contador + 1

print('Hay', contador, 'números')
