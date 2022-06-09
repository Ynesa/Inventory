import this
import os
from datetime import datetime

# sukurti faila su tekstu

with open("failas.txt", 'w') as failas:
    failas.write("Zen of Python")

# atspausdintu teksta is sukurto failo

with open("failas.txt", 'r+') as failas:
    print(failas.read())

# paskutineje eiluteje pridetu siandienos data ir laika

with open("failas.txt", 'a') as failas:
    failas.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# sunumeruotu teksto eilutes

# Beautiful is better than ugly pakeisti į "Gražu yra geriau nei bjauru

with open("failas.txt", 'r') as failas:
    replace = zodis.replace("Beautiful is better than ugly", "Gražu yra geriau nei bjauru")
with open("failas.txt", 'w', encoding="UTF-8") as failas:
    failas.write(replace)

