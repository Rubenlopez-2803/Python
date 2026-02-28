frase = 'En un lugar de la Mancha, de cuyo nombre no quiero acordarme'
contador = 0
for letra in frase:
    print(letra, end='')
    contador = contador + 1
    if contador == 30:
        break

