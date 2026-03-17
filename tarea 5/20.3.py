def contar_vocales(cadena):
    vocales = 'aeiouAEIOUáéíóúÁÉÍÓÚ'
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    print(f'En la cadena " {cadena} " hay {contador} vocales.')

contar_vocales("Este es un ejemplo de cadena de texto")
contar_vocales("En un lugar de la Mancha, de cuyo nombre no quiero acordarme")
