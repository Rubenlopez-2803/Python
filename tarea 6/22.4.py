def letrero_inverso(texto):
    for i in range(1, len(texto) + 1):
        print(texto[-i:])

letrero_inverso('En un lugar de la Mancha')
