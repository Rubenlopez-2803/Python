suma = 0
maximo = 1000

for num in range(1, 101):
    suma = suma + num
    if suma > maximo:
        print('Se ha sumado hasta el número', num)
        print('La suma es', suma)
        break
