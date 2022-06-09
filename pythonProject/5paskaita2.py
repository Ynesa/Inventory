import datetime
import calendar

class Sukaktis:
    def __init__(self, metai=1994, menuo=6, diena=8, valandos=6, minutes=9):
        self.metai=metai
        self.menuo=menuo
        self.diena=diena
        self.valandos=valandos
        self.minutes=minutes
        self.data=datetime.datetime(metai, menuo, diena, valandos, minutes)

    def kiek_praejo(self):
        now = datetime.datetime.now()
        skirtumas = now - self.data
        print("Praėjo metų: ", skirtumas.days // 365)
        print("Praėjo savaičių: ", skirtumas.days // 7)
        print("Praėjo dienų: ", skirtumas.days)
        print("Praėjo valandų: ", skirtumas.total_seconds() / 3600)
        print("Praėjo minučių: ", skirtumas.total_seconds() / 60)
        print("Praėjo sekundžių: ", skirtumas.total_seconds())

    def ar_sukakties_metai_keliamieji(self):
        return calendar.isleap(self.metai)
        print("ar_sukakties_metai_keliamieji")

    def atimti_dienas(self, diena):
        days = datetime.timedelta(5)
        return self.data-days

    def prideti_dienas(self, diena):
        days = datetime.timedelta(5)
        return self.data + days







