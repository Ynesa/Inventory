while True:
    try:
        skaicius = int(input("iveskite sveika skaiciu"))
        break
    except ValueError:
        print("ivedete ne sveikaji skaiciu. Bandykite dar karta")


