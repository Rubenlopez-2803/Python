def factorial(num):
    resultado = 1
    while num > 0:
        resultado = resultado * num
        num = num - 1
    return resultado

print("El factorial de", 5, "es igual a", factorial(5))
print("El factorial de", 8, "es igual a", factorial(8))
print("El factorial de", 12, "es igual a", factorial(12))
