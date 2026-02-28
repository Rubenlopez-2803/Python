for i in range(10):
    for j in range(10):
        if (i + j) % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()
