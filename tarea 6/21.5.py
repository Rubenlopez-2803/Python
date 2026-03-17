def recuadro(texto):
    longitud = len(texto)
    print('╔' + '═' * (longitud + 2) + '╗')
    print('║ ' + texto + ' ║')
    print('╚' + '═' * (longitud + 2) + '╝')

recuadro('Hola, mundo')
recuadro('Python es genial')
recuadro('Bienvenido')
