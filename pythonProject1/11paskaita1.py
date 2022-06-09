class Namas:
    def __init__(self, vardas, amzius):
        self.plotas = plotas
        self.__verte = verte

    @property
    def verte(self):
        return self.__verte

    @verte.setter
    def verte(self, nauja):
        if type(nauja) == int or type(nauja) == float:
            self.__verte = nauja
        else:
            print("iveskite skaiciu")








