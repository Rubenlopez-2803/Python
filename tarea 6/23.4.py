def reemplaza_vocales(texto, vocal='e'):
  
    texto = texto.lower()
    
    texto = texto.replace('a', vocal)
    texto = texto.replace('e', vocal)
    texto = texto.replace('i', vocal)
    texto = texto.replace('o', vocal)
    texto = texto.replace('u', vocal)
    texto = texto.replace('á', vocal)
    texto = texto.replace('é', vocal)
    texto = texto.replace('í', vocal)
    texto = texto.replace('ó', vocal)
    texto = texto.replace('ú', vocal)
    
    print(texto)

reemplaza_vocales('En un lugar de la mancha')
reemplaza_vocales('Hola mundo', 'a')
reemplaza_vocales('Python es genial', 'o')
