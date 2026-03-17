def ordenados(a, b, c):
    if a < b and b < c:
        return True
    else:
        return False

def ordenar(a, b, c):
    print('Números ordenados:', end=' ')
    if ordenados(a, b, c):
        print(a, b, c)
    elif ordenados(a, c, b):
        print(a, c, b)
    elif ordenados(b, a, c):
        print(b, a, c)
    elif ordenados(b, c, a):
        print(b, c, a)
    elif ordenados(c, a, b):
        print(c, a, b)
    else:
        print(c, b, a)

ordenar(3, 7, 1)
ordenar(10, 2, 5)
ordenar(12, 6, 3)
