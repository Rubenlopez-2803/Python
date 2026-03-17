def letrero_corto(texto):
    # Añadir espacios al inicio y al final
    texto = '    ' + texto + '    '
    
    for i in range(len(texto) - 4):
        print(texto[i:i+5])

letrero_corto('En un lugar de la Mancha')
