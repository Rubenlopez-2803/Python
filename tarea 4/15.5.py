for anio in range(1600, 2401):
    if (anio % 4 == 0) and (anio % 100 != 0 or anio % 400 == 0):
        continue
    print(anio)
