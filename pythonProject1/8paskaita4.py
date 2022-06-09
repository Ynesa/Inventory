from operator import attrgetter

class Zmogus:
    def __init__(self, vardas, amzius):
        self.vardas = vardas
        self.amzius = amzius

    def __repr__(self):
        return (f"({self.vardas}, {self.amzius})")

z1 = Zmogus ("Romas", 30)
z2 = Zmogus ("Emilija", 20)
z3 = Zmogus ("Rokas", 25)
sarasas = [z1, z2, z3]

surusiuotas = sorted(sarasas, key=attrgetter("vardas"))
print(surusiuotas)

surusiuotas = sorted(sarasas, key=attrgetter("amzius"))
print(surusiuotas)

surusiuotas = sorted(sarasas, key=attrgetter("vardas"), reverse=True)
print(surusiuotas)
surusiuotas = sorted(sarasas, key=attrgetter("amzius"), reverse=True)
print(surusiuotas)



