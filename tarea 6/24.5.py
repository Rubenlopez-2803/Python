char = input('Introduce un carácter: ')
num = ord(char[0])

for code in range(num + 1, num + 21):
    print(f'Código: {code:4d}  carácter: {code:c}')
