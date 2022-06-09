class Automobilis():
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        self.auto_info()

    def vaziuoti(self):
        print("vaziuoja")

    def stoveti(self):
        print("priparkuota")

    def pildyti_degalu(self):
        print("degalai ipilti")

    def auto_info(self):
        print(metai, modelis, kuro_tipas)

class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("baterija ikrauta")

    def vaziuoti_autonomiskai(self):
        print("vaziuoja autonomiskai")

audi = Automobilis()
audi.vaziuoti()
audi.stoveti()
audi.pildyti_degalu()

toyota = Elektromobilis()
toyota.vaziuoti()
toyota.stoveti()
toyota.pildyti_degalu()
toyota.vaziuoti_autonomiskai()








