num = input('Escribe un número: ')
num = int(num)

for divisor in range(2, num):
    if num % divisor == 0:
        print(num, 'no es un número primo')
        break
else:
    print(num, 'es un número primo')
