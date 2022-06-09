import random

min=1
max=6

print("sugeneruoti 3 skaiciai")
print("jei vienas is skaiciu 5 - pralaimėjai")

for x in range(3):
    skaicius = random.randint(min, max)
    print(skaicius)
    if skaicius == 5:
        print("pralaimejai")
        break
else:
    print("laimejai!")



