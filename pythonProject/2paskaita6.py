for keliamieji_metai in range(1900, 2100):
    if keliamieji_metai % 4 == 0 and keliamieji_metai % 100 != 0:
        print(keliamieji_metai)
    elif keliamieji_metai % 400 == 0:
        print(keliamieji_metai)
    elif keliamieji_metai % 100 == 0:
        continue
    else:
        continue

