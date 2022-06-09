from modules.kursas import Kursas


class PythonKursas(Kursas):
    def destyti(self):
        print("Vyksta programavimas!")

Kursas1 = Kursas("lietuviu", "Romas", 4)
Kursas2 = PythonKursas("informatika", "Rasa", 6)

Kursas1.destyti()
Kursas2.destyti()



