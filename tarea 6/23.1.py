def MayusculaMinuscula(texto):
    texto_nuevo = ''
    mayuscula = True
    for letra in texto:
        if mayuscula == True:
            mayuscula = False
            texto_nuevo = texto_nuevo + letra.upper()
        else:
            mayuscula = True
            texto_nuevo = texto_nuevo + letra.lower()
    print(texto_nuevo)

MayusculaMinuscula('Este es un texto de ejemplo')
