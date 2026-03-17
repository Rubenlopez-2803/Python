def menor(a, b, c):
    print('Número menor:', end=' ')
    if a < b and a < c:
        print(a)
    elif b < a and b < c:
        print(b)
    else:
        print(c)

menor(3, 1, 7)
menor(10, 2, 5)
menor(6, 12, 3)
