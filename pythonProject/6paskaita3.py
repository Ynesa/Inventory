class Irasas:
    def __init__(self, suma):
        self.suma = suma

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

class Biudzetas:
        def __init__(self):
            self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        pajamos = Irasas("Pajamos", suma)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma):
        islaidos = Irasas("Išlaidos", suma)
        self.zurnalas.append(islaidos)

    def gauti_balansą(self):
        suma = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                suma += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                suma -= irasas.suma
        print(suma)

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            if isinstance(irasas, pajamu_irasas):
            print(f"{irasas.tipas}: {irasas.suma}")
biudzetas = Biudzetas()

while True:
    pasirinkimas = int(input("1 - įvesti pajamas, \n2 - įvesti išlaidas, \n3 - gauti balansą, \n4 - parodyti ataskaitą, \n9 - išeiti iš programos"))
    if pasirinkimas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        biudzetas.prideti_pajamu_irasa(suma)
    if pasirinkimas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        biudzetas.prideti_islaidu_irasa(suma)
    if pasirinkimas == 3:
        biudzetas.gauti_balansą()
    if pasirinkimas == 4:
        biudzetas.parodyti_ataskaita()
    if pasirinkimas == 9:
        print("Viso gero")
        break