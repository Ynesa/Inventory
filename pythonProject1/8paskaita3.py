sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
skaiciu_suma = filter(lambda x: type(x) is int or type(x) is float, sarasas)
print(sum(skaiciu_suma))

zodziai = filter(lambda x: type(x) is str, sarasas)
print(" ".join(zodziai))

bool_kiekis = filter(lambda x: type(x) is bool, sarasas)
print(bool_kiekis)


