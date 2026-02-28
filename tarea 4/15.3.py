suma = 0
for num in range(1, 101):
    if num % 3 == 0:
        continue
    suma = suma + num

print('La suma es:', suma)
