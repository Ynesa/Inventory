class Darbuotojas():

    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo
        self.darbuotojo_info()

    def kiek_nudirbo_dienu(self):
        dabar = datetime.datetime.now()
        ivesta_diena = datetime.datetime.strptime(self.dirba_nuo, "%Y-%m-%d %H:%M:%S")
        skirtumas = dabar - ivesta_diena
        return skirumas.days * 7

    def paskaiciuoti_atlyginima(self):
        bendras_atlyginimas = self.valandos_ikainis * 8
        return bendras_atlyginimas * self.kiek_nudirbo_dienu()

class Normalus_darbuotojas(Darbuotojas):
    def kiek_nudirbo_dienu(self):
        dabar = datetime.datetime.now()
        ivesta_diena = datetime.datetime.strptime(self.dirba_nuo, "%Y-%m-%d %H:%M:%S")
        skirtumas = dabar - ivesta_diena
        return skirumas.days * 5

    def paskaiciuoti_atlyginima(self):
        bendras_atlyginimas = self.valandos_ikainis * 8
        return bendras_atlyginimas * self.kiek_nudirbo_dienu()

    Tadas = Darbuotojas("Tadas", 11, "2020, 12, 01, 08, 00, 00")
    Romas = Normalus_darbuotojas("Romas", 15, "2019, 12, 01, 08, 00, 00")
    Tadas.paskaiciuoti_atlyginima()
    Romas.paskaiciuoti_atlyginima()








