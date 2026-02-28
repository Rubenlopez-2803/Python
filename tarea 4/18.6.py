import random
numero_secreto = random.randint(1, 100)

while True:
    intento = input('Adivina el número (1-100): ')
    intento = int(intento)
    
    if intento > numero_secreto:
        print('Demasiado alto')
    elif intento < numero_secreto:
        print('Demasiado bajo')
    else:
        print('¡Acertaste!')
        break
