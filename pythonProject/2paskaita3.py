zodziai = []
for zodis in range(5):
    zodziai.append(input("Įveskite žodį: "))
for zodis in zodziai:
    print(zodis, len(zodis), zodziai.index(zodis))