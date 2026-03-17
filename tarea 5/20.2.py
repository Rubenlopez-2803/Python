def multiplos(divisor, tope=100):
    contador = 0
    for num in range(1, tope + 1):
        if num % divisor == 0:
            contador += 1
    print(f"Hay {contador} múltiplos de {divisor} desde el 1 hasta el {tope}")

multiplos(7)
multiplos(3, 20)
multiplos(5, 50)
