frase = 'Hola, mundo! Me llamo Python y sé como hablar con la a.'
for letra in frase:
    if letra in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
        print('a', sep='', end='')
        continue
    print(letra, sep='', end='')
