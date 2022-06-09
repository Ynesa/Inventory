while True:
    try:
        skaicius = int(input("Įveskite norima datą ir laika"))
        break
    except ValueError:
        print("ivedete neteisinga formata. iveskite YYYY-MM-DD HH:MM:SS")