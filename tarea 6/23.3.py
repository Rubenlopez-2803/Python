print('Describe a Lionel Messi sin escribir ninguna palabra tabú.')
print('Las palabras tabú son: Argentina, Barcelona, futbol, PSG')
descripcion = input('Descripción: ')
descripcion_lower = descripcion.lower()

if descripcion_lower.find('argentina') >= 0:
    print('Error, he encontrado la palabra tabú "Argentina" en la descripción')
elif descripcion_lower.find('barcelona') >= 0:
    print('Error, he encontrado la palabra tabú "Barcelona" en la descripción')
elif descripcion_lower.find('futbol') >= 0:
    print('Error, he encontrado la palabra tabú "futbol" en la descripción')
elif descripcion_lower.find('psg') >= 0:
    print('Error, he encontrado la palabra tabú "PSG" en la descripción')
else:
    print('¡Descripción aceptada! No contiene palabras tabú.')
