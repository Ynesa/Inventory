import os
from datetime import datetime

os.chdir('C:\\Users\\tomas\\Desktop')
os.mkdir("Naujaskatalogas")
os.chdir('C:\\Users\\tomas\\Desktop\\Naujaskatalogas')

with open("data.txt", "w") as failas:
    failas.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

os.chdir('C:\\Users\\tomas\\Desktop\\Naujaskatalogas')
print(os.stat("data.txt").st_size)
print(os.stat("data.txt").st_ctime)


