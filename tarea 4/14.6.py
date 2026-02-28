num = input('Introduce cuántos impares sumaremos: ')
num = int(num)

suma = 0
for i in range(1, num*2, 2):
    suma = suma + i

print('La suma de los', num, 'primeros impares es igual a', suma)
print('El cuadrado de', num, 'es igual a', num*num)
