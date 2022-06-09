class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas

    # tekstas atbulai
    def grazinti_teksta_atbulai(self):
        atbulai = self.tekstas[::-1]
        return atbulai

    # tekstas mazosiomis raidemis
    def tekstas_mazosiomis_raidemis(self):
        mazosiomis = self.tekstas.lower()
        return mazosiomis

    # tekstas didziosiomis raidemis

    def tekstas_mazosiomis_raidemis(self):
        didziosiomis = self.tekstas.upper()
        return didziosiomis

    # grazinti pagal eiles numeri

    def nurodytas_eiles_numeris(self):
        return zodis = self.tekstas.count()

    # grazina kiek tekste yra nurodytu simboliu arba zodziu

    def simboliai(self):
        zodis = len(self.tekstas())
        return zodis


    # grazina teksta su pakeistu nurodytu zodziu arba simboliu

    def pakeistas_zodis (self, zodis, kitas_zodis):
        return self.tekstas.replace(zodis, kitas_zodis)

    #atspausdina kiek tekste yra nurodytu zodziu, skaiciu, didziuju ir mazuju raidziu

    def info_apie_sakini(self):
    print(f"Šiame sakinyje yra {len(stringas.split())} žodžių")
    didziosios = 0
    mazosios = 0
    skaiciai = 0
    for simbolis in stringas:
        if simbolis.isupper():
            didziosios += 1
        if simbolis.islower():
            mazosios += 1
        if simbolis.isnumeric():
            skaiciai += 1
    print(f"Didžiosios: {didziosios}, mažosios: {mazosios}, skaičiai: {skaiciai}")


info_apie_sakini("Laba diena laba diena lab 522")


