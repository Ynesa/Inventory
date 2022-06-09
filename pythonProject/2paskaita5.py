metai = int(input("iveskite metus"))
if metai %4 == 0 and metai %100 != 0:
    print("keliamieji metai")
elif metai % 400 == 0:
        print("keliamieji metai")
elif metai % 100 == 0:
        print("nekeliamieji metai")
else:
        print("nekeliamieji metai")


