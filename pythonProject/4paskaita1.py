# 1

def skaiciu_suma(skaicius1, skaicius2, skaicius3):
    return skaicius1 + skaicius2 + skaicius3

print(skaiciu_suma(5, 8, 2))

# 2
def saraso_suma(sarasas):
    suma = 0
    for skaicius in sarasas:
        suma += skaicius
    return suma
sarasas = [2,8,1]
print(saraso_suma(sarasas))

# 3
def didziausias_skaicius(*args):
    return max(args)
print(didziausias_skaicius(2,4,8))

# 4
def zodis_atbulai(zodis):
    return zodis[::-1]
print(zodis_atbulai("zodis"))

# 6
def unikalus_sarasas(elementas):
    naujas_sarasas = []
    for skaicius in elementas:
        if skaicius not in naujas_sarasas:
            naujas_sarasas.append(elementas)
    return naujas_sarasas

print(unikalus_sarasas([6, "Vienas", 5, "zodis", 10]))



